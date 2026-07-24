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


def inverse(matrix):
    """Return the exact inverse of a nonsingular rational square matrix."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("inverse requires a square matrix")
    augmented = [
        [*map(Q, row), *[Fraction(int(index == column)) for column in range(size)]]
        for index, row in enumerate(matrix)
    ]
    reduced, pivots = rref(augmented)
    if pivots[:size] != list(range(size)):
        raise ValueError("matrix is singular")
    return tuple(tuple(row[size:]) for row in reduced)


def affine_rank(points):
    return rank([[Fraction(1), *map(Q, point)] for point in points]) - 1


def rowspace_key(matrix):
    """Canonical tuple of nonzero RREF rows spanning the same row space."""
    reduced, _ = rref(matrix)
    return tuple(tuple(row) for row in reduced if any(row))


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


def product_free_sum_mahler_factor(left_dimension, right_dimension):
    """Mahler factor for products and free sums in complementary subspaces."""
    if left_dimension < 1 or right_dimension < 1:
        raise ValueError("product/free-sum factors must have positive dimensions")
    dimension = left_dimension + right_dimension
    return Fraction(
        factorial(left_dimension) * factorial(right_dimension),
        factorial(dimension),
    )


def join_mahler_factor(left_dimension, right_dimension):
    """Mahler factor for the affine join of two convex bodies."""
    if left_dimension < 0 or right_dimension < 0:
        raise ValueError("join factors cannot have negative dimension")
    dimension = left_dimension + right_dimension + 1
    beta = Fraction(
        factorial(left_dimension) * factorial(right_dimension),
        factorial(dimension),
    )
    santalo_height = Fraction(
        (dimension + 1) ** (dimension + 1),
        (left_dimension + 1) ** (left_dimension + 1)
        * (right_dimension + 1) ** (right_dimension + 1),
    )
    return beta**2 * santalo_height


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

    def pulling_triangulation(self):
        """Return an exact pulling triangulation as vertex-index simplices."""
        cache = {}

        def face_facets(face):
            face_set = frozenset(face)
            face_dimension = affine_rank([self.vertices[index] for index in face])
            facets = set()
            for incident, _, _ in self.facets:
                intersection = face_set.intersection(incident)
                if not intersection or intersection == face_set:
                    continue
                ordered = tuple(sorted(intersection))
                if (
                    affine_rank([self.vertices[index] for index in ordered])
                    == face_dimension - 1
                ):
                    facets.add(ordered)
            return tuple(sorted(facets))

        def triangulate(face):
            face = tuple(sorted(face))
            if face in cache:
                return cache[face]
            dimension = affine_rank([self.vertices[index] for index in face])
            if len(face) == dimension + 1:
                cache[face] = (face,)
                return cache[face]
            apex = face[0]
            simplices = []
            for subfacet in face_facets(face):
                if apex in subfacet:
                    continue
                for simplex in triangulate(subfacet):
                    simplices.append(tuple(sorted((apex, *simplex))))
            cache[face] = tuple(sorted(set(simplices)))
            return cache[face]

        return triangulate(tuple(range(len(self.vertices))))

    def volume_and_centroid(self):
        """Compute volume and centroid exactly from a pulling triangulation."""
        volume, centroid, _ = self.volume_centroid_covariance()
        return volume, centroid

    def volume_centroid_covariance(self):
        """Compute volume, centroid, and covariance exactly.

        The simplex second-moment formula follows by integrating barycentric
        coordinates, so the whole calculation remains rational.
        """
        total_volume = Fraction()
        first_moment = [Fraction() for _ in range(self.dimension)]
        second_moment = [
            [Fraction() for _ in range(self.dimension)]
            for _ in range(self.dimension)
        ]
        for simplex in self.pulling_triangulation():
            simplex_vertices = [self.vertices[index] for index in simplex]
            volume = simplex_volume(simplex_vertices)
            total_volume += volume
            vertex_sum = [
                sum(
                    (vertex[coordinate] for vertex in simplex_vertices),
                    Fraction(),
                )
                for coordinate in range(self.dimension)
            ]
            for coordinate in range(self.dimension):
                simplex_centroid_coordinate = vertex_sum[coordinate] / (
                    self.dimension + 1
                )
                first_moment[coordinate] += volume * simplex_centroid_coordinate
                for other in range(self.dimension):
                    diagonal_sum = sum(
                        (
                            vertex[coordinate] * vertex[other]
                            for vertex in simplex_vertices
                        ),
                        Fraction(),
                    )
                    simplex_second_moment = (
                        vertex_sum[coordinate] * vertex_sum[other] + diagonal_sum
                    ) / ((self.dimension + 1) * (self.dimension + 2))
                    second_moment[coordinate][other] += (
                        volume * simplex_second_moment
                    )
        if not total_volume:
            raise ValueError("triangulation has zero volume")
        centroid = tuple(value / total_volume for value in first_moment)
        covariance = tuple(
            tuple(
                second_moment[row][column] / total_volume
                - centroid[row] * centroid[column]
                for column in range(self.dimension)
            )
            for row in range(self.dimension)
        )
        return total_volume, centroid, covariance

    def facet_cone_volume_and_centroid(self):
        """Independently integrate when every ridge is a simplex.

        Each facet is pulled from its least-labelled vertex using its
        triangular ridges, then every boundary tetrahedron is coned to the
        origin.  This does not call ``pulling_triangulation`` and is used to
        cross-check the 24-cell Santaló certificate.
        """
        if self.dimension != 4:
            raise ValueError("facet-cone cross-check is implemented in dimension four")
        origin = (Fraction(),) * self.dimension
        total_volume = Fraction()
        first_moment = [Fraction() for _ in range(self.dimension)]
        facet_sets = [frozenset(incident) for incident, _, _ in self.facets]
        for facet_index, facet in enumerate(facet_sets):
            apex = min(facet)
            ridges = set()
            for other_index, other in enumerate(facet_sets):
                if other_index == facet_index:
                    continue
                intersection = tuple(sorted(facet.intersection(other)))
                if not intersection:
                    continue
                if affine_rank([self.vertices[index] for index in intersection]) == 2:
                    ridges.add(intersection)
            for ridge in sorted(ridges):
                if len(ridge) != 3:
                    raise ValueError("facet-cone cross-check requires triangular ridges")
                if apex in ridge:
                    continue
                simplex_vertices = [
                    origin,
                    self.vertices[apex],
                    *[self.vertices[index] for index in ridge],
                ]
                volume = simplex_volume(simplex_vertices)
                total_volume += volume
                for coordinate in range(self.dimension):
                    first_moment[coordinate] += volume * sum(
                        (vertex[coordinate] for vertex in simplex_vertices),
                        Fraction(),
                    ) / (self.dimension + 1)
        if not total_volume:
            raise ValueError("facet-cone triangulation has zero volume")
        return total_volume, tuple(value / total_volume for value in first_moment)

    def santalo_projective_normalization(self):
        """Return T(P), where T(x)=x/(1-g·x) and s(T(P))=0.

        Here g is the centroid of P°.  The transformed polar is P°-g.
        """
        polar = self.polar()
        _, centroid = polar.volume_and_centroid()
        transformed = []
        for vertex in self.vertices:
            denominator = 1 - dot(centroid, vertex)
            if denominator <= 0:
                raise ValueError("projective denominator is not positive")
            transformed.append(tuple(value / denominator for value in vertex))
        return RationalPolytope(transformed)

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
        waived = {
            facet_index
            for facet_index, (_, normal, _) in enumerate(self.facets)
            if dot(normal, theta) == 0
        }
        return self.admissible_matrix_waiving(waived)

    def admissible_matrix_waiving(self, waived_facets):
        """Build the speed matrix after waiving the indexed parallel facets."""
        waived = set(waived_facets)
        rows = []
        vertex_count = len(self.vertices)
        for facet_index, (incident, _, _) in enumerate(self.facets):
            if facet_index in waived:
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

    def direction_flat_dimensions(self):
        """Enumerate every facet-normal arrangement flat exactly.

        A direction theta waives precisely those facets whose normals lie in
        theta-perp, a subspace of rank at most d-1.  Every possible closure is
        generated by at most d-1 facet normals, so this finite enumeration
        checks all direction types without sampling directions.
        """
        normals = [normal for _, normal, _ in self.facets]
        span_keys = {()}
        for size in range(1, self.dimension):
            for chosen in combinations(range(len(normals)), size):
                key = rowspace_key([normals[index] for index in chosen])
                if len(key) < self.dimension:
                    span_keys.add(key)
        results = []
        for key in sorted(span_keys):
            span_rank = len(key)
            waived = tuple(
                index
                for index, normal in enumerate(normals)
                if rank([*key, normal]) == span_rank
            )
            results.append(
                {
                    "normal_span_rank": span_rank,
                    "waived_facets": waived,
                    "dimension": len(self.vertices)
                    - rank(self.admissible_matrix_waiving(waived)),
                }
            )
        return tuple(results)


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


def join_segment_square_4():
    """Santaló-centered join of [-1,1] and [-1,1]^2."""
    segment = [
        (-1, 0, 0, Fraction(-3, 5)),
        (1, 0, 0, Fraction(-3, 5)),
    ]
    square = [
        (0, first, second, Fraction(2, 5))
        for first, second in product((-1, 1), repeat=2)
    ]
    return RationalPolytope([*segment, *square])


def cell_24():
    vertices = []
    for first, second in combinations(range(4), 2):
        for first_sign, second_sign in product((-1, 1), repeat=2):
            vertex = [0, 0, 0, 0]
            vertex[first] = first_sign
            vertex[second] = second_sign
            vertices.append(tuple(vertex))
    return RationalPolytope(vertices)


def paffenholz_24_cell(
    parameters=(
        Fraction(1, 5),
        Fraction(2, 5),
        Fraction(3, 5),
        Fraction(4, 5),
    )
):
    """A rational non-regular 24-cell realization from Paffenholz's family."""
    parameters = tuple(map(Q, parameters))
    if len(parameters) != 4 or any(abs(value) >= 1 for value in parameters):
        raise ValueError("expected four parameters strictly between -1 and 1")
    vertices = list(product((-1, 1), repeat=4))
    for coordinate in range(4):
        for side in (-1, 1):
            vertex = list(parameters)
            vertex[coordinate] = 2 * side - parameters[coordinate]
            vertices.append(tuple(vertex))
    return RationalPolytope(vertices)


def full_rank_24_cell(parameter=Fraction(1, 2), signs=(1, 1, 1)):
    """Rastanawi--Sinn--Ziegler's smooth one-parameter 24-cell family."""
    parameter = Q(parameter)
    signs = tuple(signs)
    if not 0 <= parameter < 1:
        raise ValueError("expected a parameter in [0, 1)")
    if len(signs) != 3 or any(sign not in (-1, 1) for sign in signs):
        raise ValueError("expected three signs in {-1, 1}")
    denominator = 1 + parameter**2
    axial = Fraction(2) / denominator
    first, second, third = (
        Fraction(2 * sign) * parameter / denominator for sign in signs
    )
    extra = [
        (-axial, -first, -second, -third),
        (axial, first, second, third),
        (first, -axial, third, -second),
        (-first, axial, -third, second),
        (second, -third, -axial, first),
        (-second, third, axial, -first),
        (third, second, -first, -axial),
        (-third, -second, first, axial),
    ]
    return RationalPolytope([*product((-1, 1), repeat=4), *extra])


def full_rank_24_cell_invariants(parameter):
    """Closed exact invariants for the centrally symmetric smooth family."""
    parameter = Q(parameter)
    if not 0 <= parameter < 1:
        raise ValueError("expected a parameter in [0, 1)")
    squared = parameter**2
    primal_volume = Fraction(32) / (1 + squared)
    polar_volume = (3 + squared) / 6
    primal_covariance_scalar = (
        13 + 22 * squared + 5 * squared**2
    ) / (30 * (1 + squared) ** 2)
    polar_covariance_scalar = (
        39 + 27 * squared - 3 * squared**2 + squared**3
    ) / (240 * (3 + squared))
    return {
        "primal_volume": primal_volume,
        "polar_volume": polar_volume,
        "mahler": primal_volume * polar_volume,
        "primal_covariance_scalar": primal_covariance_scalar,
        "polar_covariance_scalar": polar_covariance_scalar,
    }
