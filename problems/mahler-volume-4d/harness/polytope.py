"""Exact rational polytope and admissible-shadow-speed calculations.

These routines are for falsifying terminal-polytope lemmas, not for
enumerating large face lattices.
"""

from fractions import Fraction
from itertools import combinations, product
from math import factorial


def Q(value):
    return value if isinstance(value, Fraction) else Fraction(value)


def dot(left, right):
    return sum((Q(a) * Q(b) for a, b in zip(left, right)), Fraction())


def rref(matrix):
    """Return (reduced_matrix, pivot_columns) over the rationals."""
    work = [[Q(value) for value in row] for row in matrix]
    if not work:
        return work, []
    rows, columns = len(work), len(work[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(work[row], work[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivot_columns


def rank(matrix):
    return len(rref(matrix)[1])


def nullspace(matrix):
    """Return a basis for the right nullspace of a rational matrix."""
    if not matrix:
        return []
    reduced, pivots = rref(matrix)
    columns = len(reduced[0])
    free_columns = [column for column in range(columns) if column not in pivots]
    basis = []
    for free in free_columns:
        vector = [Fraction() for _ in range(columns)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(tuple(vector))
    return basis


def determinant(matrix):
    square = [[Q(value) for value in row] for row in matrix]
    size = len(square)
    if any(len(row) != size for row in square):
        raise ValueError("determinant requires a square matrix")
    sign = 1
    result = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if square[row][column]),
            None,
        )
        if pivot is None:
            return Fraction()
        if pivot != column:
            square[column], square[pivot] = square[pivot], square[column]
            sign *= -1
        pivot_value = square[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            scale = square[row][column] / pivot_value
            for inner in range(column + 1, size):
                square[row][inner] -= scale * square[column][inner]
    return sign * result


def affine_rank(points):
    return rank([[Fraction(1), *map(Q, point)] for point in points]) - 1


def simplex_volume(vertices):
    dimension = len(vertices) - 1
    if any(len(vertex) != dimension for vertex in vertices):
        raise ValueError("expected d+1 vertices in dimension d")
    base = vertices[0]
    columns = [
        [Q(vertex[row]) - Q(base[row]) for row in range(dimension)]
        for vertex in vertices[1:]
    ]
    matrix = [
        [columns[column][row] for column in range(dimension)]
        for row in range(dimension)
    ]
    return abs(determinant(matrix)) / factorial(dimension)


def pyramid_mahler_factor(dimension):
    """Exact factor P(pyr_d K) / P(K) from the polar-section integral."""
    if dimension < 2:
        raise ValueError("a pyramid dimension must be at least two")
    return Fraction(
        (dimension + 1) ** (dimension + 1),
        dimension ** (dimension + 2),
    )


class RationalPolytope:
    """A small full-dimensional rational polytope containing the origin."""

    def __init__(self, vertices):
        self.vertices = tuple(tuple(map(Q, vertex)) for vertex in vertices)
        if not self.vertices:
            raise ValueError("a polytope needs vertices")
        self.dimension = len(self.vertices[0])
        if any(len(vertex) != self.dimension for vertex in self.vertices):
            raise ValueError("inconsistent vertex dimensions")
        if affine_rank(self.vertices) != self.dimension:
            raise ValueError("vertices are not full-dimensional")
        self.facets = self._enumerate_facets()

    def _enumerate_facets(self):
        facets = {}
        d = self.dimension
        for chosen in combinations(range(len(self.vertices)), d):
            points = [self.vertices[index] for index in chosen]
            differences = [
                [
                    points[row][column] - points[0][column]
                    for column in range(d)
                ]
                for row in range(1, d)
            ]
            normal_basis = nullspace(differences)
            if len(normal_basis) != 1:
                continue
            normal = normal_basis[0]
            offset = dot(normal, points[0])
            signed = [dot(normal, vertex) - offset for vertex in self.vertices]
            if any(value > 0 for value in signed) and any(value < 0 for value in signed):
                continue
            if all(value >= 0 for value in signed):
                normal = tuple(-value for value in normal)
                offset = -offset
                signed = [-value for value in signed]
            incident = tuple(index for index, value in enumerate(signed) if value == 0)
            if affine_rank([self.vertices[index] for index in incident]) != d - 1:
                continue
            if offset <= 0:
                raise ValueError("the origin is not strictly inside the polytope")
            facets[incident] = (normal, offset)
        return tuple(
            (incident, facets[incident][0], facets[incident][1])
            for incident in sorted(facets)
        )

    def polar(self):
        """Return P° from supporting inequalities n·x <= h."""
        return RationalPolytope(
            [tuple(value / offset for value in normal) for _, normal, offset in self.facets]
        )

    def incidence_summary(self):
        degrees = [0] * len(self.vertices)
        for incident, _, _ in self.facets:
            for vertex in incident:
                degrees[vertex] += 1
        sizes = [len(incident) for incident, _, _ in self.facets]
        return {
            "f0": len(self.vertices),
            "f3": len(self.facets),
            "f03": sum(sizes),
            "Delta": max(sizes),
            "delta": max(degrees),
            "facet_sizes": tuple(sorted(sizes)),
            "vertex_facet_degrees": tuple(sorted(degrees)),
        }

    def admissible_matrix(self, direction):
        """Rows lambda encode sum_{v in F} lambda_v alpha_v = 0."""
        theta = tuple(map(Q, direction))
        if len(theta) != self.dimension or not any(theta):
            raise ValueError("direction must be a nonzero d-vector")
        rows = []
        vertex_count = len(self.vertices)
        for incident, normal, _ in self.facets:
            if dot(normal, theta) == 0:
                continue
            evaluation_transpose = [
                [Fraction(1) for _ in incident],
                *[
                    [self.vertices[index][coordinate] for index in incident]
                    for coordinate in range(self.dimension)
                ],
            ]
            for relation in nullspace(evaluation_transpose):
                row = [Fraction() for _ in range(vertex_count)]
                for index, coefficient in zip(incident, relation):
                    row[index] = coefficient
                rows.append(tuple(row))
        return tuple(rows)

    def admissible_dimension(self, direction):
        return len(self.vertices) - rank(self.admissible_matrix(direction))

    def trivial_dimension(self):
        return rank([[Fraction(1), *vertex] for vertex in self.vertices])


def centered_simplex_4():
    return RationalPolytope(
        [
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
            (-1, -1, -1, -1),
        ]
    )


def cube_4():
    return RationalPolytope(list(product((-1, 1), repeat=4)))


def cross_polytope_4():
    vertices = []
    for coordinate in range(4):
        for sign in (-1, 1):
            vertex = [0, 0, 0, 0]
            vertex[coordinate] = sign
            vertices.append(tuple(vertex))
    return RationalPolytope(vertices)


def pyramid_over_cube_3():
    base = [(*vertex, -1) for vertex in product((-1, 1), repeat=3)]
    return RationalPolytope([*base, (0, 0, 0, 3)])
