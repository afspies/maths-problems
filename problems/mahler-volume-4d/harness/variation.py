"""Exact second variations of Santaló Mahler volume in a fixed chamber."""

from fractions import Fraction
from itertools import permutations

from polytope import affine_rank, dot, inverse, rank


def Q(value):
    return value if isinstance(value, Fraction) else Fraction(value)


class Jet2:
    """The value, first derivative, and second derivative of a scalar path."""

    def __init__(self, value, first=0, second=0):
        self.value = Q(value)
        self.first = Q(first)
        self.second = Q(second)

    def __add__(self, other):
        other = as_jet(other)
        return Jet2(
            self.value + other.value,
            self.first + other.first,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self):
        return Jet2(-self.value, -self.first, -self.second)

    def __sub__(self, other):
        return self + (-as_jet(other))

    def __rsub__(self, other):
        return as_jet(other) - self

    def __mul__(self, other):
        other = as_jet(other)
        return Jet2(
            self.value * other.value,
            self.first * other.value + self.value * other.first,
            self.second * other.value
            + 2 * self.first * other.first
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def reciprocal(self):
        if not self.value:
            raise ZeroDivisionError
        return Jet2(
            1 / self.value,
            -self.first / self.value**2,
            2 * self.first**2 / self.value**3
            - self.second / self.value**2,
        )

    def __truediv__(self, other):
        return self * as_jet(other).reciprocal()

    def __rtruediv__(self, other):
        return as_jet(other) / self


def as_jet(value):
    return value if isinstance(value, Jet2) else Jet2(value)


def determinant_jet(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    result = Jet2(0)
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(size)
            for right in range(left + 1, size)
        )
        term = Jet2(1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        result += term if inversions % 2 == 0 else -term
    return result


def signed_simplex_weight(vertices):
    """Return |det| as a jet, using the fixed nonzero base orientation."""
    dimension = len(vertices) - 1
    base = vertices[0]
    matrix = [
        [
            vertices[column + 1][row] - base[row]
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]
    determinant = determinant_jet(matrix)
    if determinant.value > 0:
        return determinant
    if determinant.value < 0:
        return -determinant
    raise ValueError("the base simplex is degenerate")


def volume_centroid_jets(vertices, simplices):
    """Return volume up to a harmless d! factor and the centroid jet."""
    dimension = len(vertices[0])
    volume = Jet2(0)
    moment = [Jet2(0) for _ in range(dimension)]
    for simplex in simplices:
        points = [vertices[index] for index in simplex]
        weight = signed_simplex_weight(points)
        volume += weight
        for coordinate in range(dimension):
            moment[coordinate] += weight * sum(
                (point[coordinate] for point in points),
                Jet2(0),
            ) / (dimension + 1)
    return volume, tuple(entry / volume for entry in moment)


def polar_vertex_jets(polytope, vertex_jets):
    """Solve n(t)·x_v(t)=1 for one affine basis in every fixed facet."""
    result = []
    for incident, _, _ in polytope.facets:
        basis = next(
            chosen
            for chosen in __import__("itertools").combinations(incident, 4)
            if affine_rank([polytope.vertices[index] for index in chosen]) == 3
        )
        matrix = [
            [vertex_jets[index][coordinate] for coordinate in range(4)]
            for index in basis
        ]
        denominator = determinant_jet(matrix)
        normal = []
        for coordinate in range(4):
            replaced = [
                [
                    Jet2(1) if column == coordinate else matrix[row][column]
                    for column in range(4)
                ]
                for row in range(4)
            ]
            normal.append(determinant_jet(replaced) / denominator)
        normal = tuple(normal)
        for index in incident:
            residual = sum(
                (
                    normal[coordinate] * vertex_jets[index][coordinate]
                    for coordinate in range(4)
                ),
                Jet2(0),
            ) - 1
            if residual.value or residual.first or residual.second:
                raise ValueError("the supplied path does not preserve facet coplanarity")
        result.append(normal)
    return tuple(result)


def log_second(jet):
    if jet.value <= 0:
        raise ValueError("logarithm requires a positive base value")
    return jet.second / jet.value - (jet.first / jet.value) ** 2


def log_first(jet):
    if jet.value <= 0:
        raise ValueError("logarithm requires a positive base value")
    return jet.first / jet.value


def quadratic_form(matrix, vector):
    return sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(len(vector))
            for column in range(len(vector))
        ),
        Fraction(),
    )


def reduced_log_mahler_second(polytope, first_velocities, second_velocities=None):
    """Exact second derivative after minimizing over the Santaló point.

    The input is a twice differentiable vertex path through ``polytope`` in
    a fixed face-lattice chamber.  The base body must be in Santaló position.
    """
    if second_velocities is None:
        second_velocities = [(0,) * polytope.dimension] * len(polytope.vertices)
    if len(first_velocities) != len(polytope.vertices) or len(
        second_velocities
    ) != len(polytope.vertices):
        raise ValueError("one velocity and acceleration are required per vertex")
    vertex_jets = tuple(
        tuple(
            Jet2(
                vertex[coordinate],
                first_velocities[index][coordinate],
                second_velocities[index][coordinate],
            )
            for coordinate in range(polytope.dimension)
        )
        for index, vertex in enumerate(polytope.vertices)
    )
    primal_volume, _ = volume_centroid_jets(
        vertex_jets, polytope.pulling_triangulation()
    )
    polar_jets = polar_vertex_jets(polytope, vertex_jets)
    polar = polytope.polar()
    polar_volume, polar_centroid = volume_centroid_jets(
        polar_jets, polar.pulling_triangulation()
    )
    if any(entry.value for entry in polar_centroid):
        raise ValueError("the base polytope is not in Santaló position")

    _, _, polar_covariance = polar.volume_centroid_covariance()
    dimension = polytope.dimension
    santalo_hessian = tuple(
        tuple(
            (dimension + 1)
            * (dimension + 2)
            * polar_covariance[row][column]
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    cross = tuple((dimension + 1) * entry.first for entry in polar_centroid)
    correction = quadratic_form(inverse(santalo_hessian), cross)
    first = log_first(primal_volume) + log_first(polar_volume)
    unreduced = log_second(primal_volume) + log_second(polar_volume)
    return {
        "first": first,
        "unreduced": unreduced,
        "santalo_correction": correction,
        "reduced": unreduced - correction,
        "polar_centroid_first": tuple(entry.first for entry in polar_centroid),
    }


def projective_vertex_path(polytope, direction):
    """Jets of x/(1+t direction·x)."""
    direction = tuple(map(Q, direction))
    first = []
    second = []
    for vertex in polytope.vertices:
        evaluation = dot(direction, vertex)
        first.append(tuple(-evaluation * coordinate for coordinate in vertex))
        second.append(
            tuple(2 * evaluation**2 * coordinate for coordinate in vertex)
        )
    return tuple(first), tuple(second)


def paffenholz_parameter_path(direction):
    """Vertex jets induced by a -> a+t*direction in Paffenholz's family."""
    direction = tuple(map(Q, direction))
    if len(direction) != 4:
        raise ValueError("expected four parameter velocities")
    first = [(Fraction(),) * 4 for _ in range(16)]
    for reflected_coordinate in range(4):
        for _side in (-1, 1):
            first.append(
                tuple(
                    -direction[coordinate]
                    if coordinate == reflected_coordinate
                    else direction[coordinate]
                    for coordinate in range(4)
                )
            )
    return tuple(first), tuple((Fraction(),) * 4 for _ in range(24))


def paired_tangent_from_vertex_path(polytope, first_velocities):
    """Lift a fixed-facet vertex velocity to paired primal/polar coordinates."""
    vertex_jets = tuple(
        tuple(
            Jet2(
                vertex[coordinate],
                first_velocities[index][coordinate],
            )
            for coordinate in range(polytope.dimension)
        )
        for index, vertex in enumerate(polytope.vertices)
    )
    polar_jets = polar_vertex_jets(polytope, vertex_jets)
    return tuple(
        [
            coordinate
            for velocity in first_velocities
            for coordinate in velocity
        ]
        + [
            entry.first
            for vertex in polar_jets
            for entry in vertex
        ]
    )


def incidence_tangent_matrix(polytope):
    """Linearization of x_v·y_F=1 in paired primal/polar coordinates."""
    polar = polytope.polar()
    vertex_count = len(polytope.vertices)
    facet_count = len(polytope.facets)
    dimension = polytope.dimension
    rows = []
    for facet_index, (incident, _, _) in enumerate(polytope.facets):
        polar_vertex = polar.vertices[facet_index]
        for vertex_index in incident:
            row = [
                Fraction()
                for _ in range(dimension * (vertex_count + facet_count))
            ]
            for coordinate in range(dimension):
                row[dimension * vertex_index + coordinate] = polar_vertex[
                    coordinate
                ]
                row[
                    dimension * vertex_count
                    + dimension * facet_index
                    + coordinate
                ] = polytope.vertices[vertex_index][coordinate]
            rows.append(tuple(row))
    return tuple(rows)


def incidence_tangent_dimension(polytope):
    matrix = incidence_tangent_matrix(polytope)
    variables = polytope.dimension * (
        len(polytope.vertices) + len(polytope.facets)
    )
    return variables - rank(matrix)


def projective_orbit_tangent_vectors(polytope):
    """Return the 24 standard infinitesimal PGL(5) directions in dimension 4."""
    if polytope.dimension != 4:
        raise ValueError("the standard basis below is specialized to dimension four")
    polar = polytope.polar()
    vectors = []

    def pack(primal_velocities, polar_velocities):
        return tuple(
            coordinate
            for velocity in (*primal_velocities, *polar_velocities)
            for coordinate in velocity
        )

    for coordinate in range(4):
        translation = tuple(Fraction(int(index == coordinate)) for index in range(4))
        primal = [translation for _ in polytope.vertices]
        dual = [
            tuple(
                -dot(translation, vertex) * entry for entry in vertex
            )
            for vertex in polar.vertices
        ]
        vectors.append(pack(primal, dual))

    for row in range(4):
        for column in range(4):
            primal = [
                tuple(
                    vertex[column] if coordinate == row else Fraction()
                    for coordinate in range(4)
                )
                for vertex in polytope.vertices
            ]
            dual = [
                tuple(
                    -vertex[row] if coordinate == column else Fraction()
                    for coordinate in range(4)
                )
                for vertex in polar.vertices
            ]
            vectors.append(pack(primal, dual))

    for coordinate in range(4):
        projective = tuple(
            Fraction(int(index == coordinate)) for index in range(4)
        )
        primal = [
            tuple(-dot(projective, vertex) * entry for entry in vertex)
            for vertex in polytope.vertices
        ]
        dual = [
            tuple(
                projective[index]
                for index in range(4)
            )
            for _ in polar.vertices
        ]
        vectors.append(pack(primal, dual))
    return tuple(vectors)
