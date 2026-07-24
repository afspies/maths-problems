"""Exact second variations of Santaló Mahler volume in a fixed chamber."""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb

from polytope import (
    affine_rank,
    determinant,
    dot,
    inverse,
    nullspace,
    rank,
    rref,
    simplex_volume,
)


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


@lru_cache(maxsize=None)
def paired_geometry(polytope):
    """Cache the expensive polar/fixed-triangulation data for one realization."""
    polar = polytope.polar()
    return (
        polar,
        polytope.pulling_triangulation(),
        polar.pulling_triangulation(),
        polar.volume_centroid_covariance()[2],
    )


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


def log_volume_gradient(vertices, simplices):
    """Exact gradient of log volume in flattened vertex coordinates."""
    dimension = len(vertices[0])
    gradient = []
    for vertex_index in range(len(vertices)):
        for coordinate in range(dimension):
            jets = tuple(
                tuple(
                    Jet2(
                        entry,
                        int(
                            index == vertex_index
                            and inner == coordinate
                        ),
                    )
                    for inner, entry in enumerate(vertex)
                )
                for index, vertex in enumerate(vertices)
            )
            volume, _ = volume_centroid_jets(jets, simplices)
            gradient.append(log_first(volume))
    return tuple(gradient)


def paired_log_volume_gradient(polytope):
    """Gradient of log|conv X|+log|conv Y| in paired incidence coordinates."""
    polar, primal_simplices, polar_simplices, _ = paired_geometry(polytope)
    return (
        *log_volume_gradient(
            polytope.vertices, primal_simplices
        ),
        *log_volume_gradient(
            polar.vertices, polar_simplices
        ),
    )


def solve_consistent_linear_system(matrix, right):
    """Return one exact solution, setting all free variables to zero."""
    augmented = tuple(
        tuple((*row, value)) for row, value in zip(matrix, right)
    )
    reduced, pivots = rref(augmented)
    variable_count = len(matrix[0])
    if any(
        not any(row[:variable_count]) and row[variable_count]
        for row in reduced
    ):
        raise ValueError("linear system is inconsistent")
    solution = [Fraction() for _ in range(variable_count)]
    for row_index, pivot in enumerate(pivots):
        if pivot < variable_count:
            solution[pivot] = reduced[row_index][variable_count]
    return tuple(solution)


def incidence_kkt_multiplier(polytope):
    """Solve grad(log|X|+log|Y|)=J^T lambda exactly."""
    tangent_matrix = incidence_tangent_matrix(polytope)
    transpose = tuple(
        tuple(
            tangent_matrix[row][column]
            for row in range(len(tangent_matrix))
        )
        for column in range(len(tangent_matrix[0]))
    )
    gradient = paired_log_volume_gradient(polytope)
    multiplier = solve_consistent_linear_system(transpose, gradient)
    if any(
        sum(
            coefficient * value
            for coefficient, value in zip(row, multiplier)
        )
        != target
        for row, target in zip(transpose, gradient)
    ):
        raise AssertionError("the returned KKT multiplier is not exact")
    return multiplier


@lru_cache(maxsize=None)
def paired_straight_reduced_log_second(polytope, velocity):
    """Ambient Santaló-envelope Hessian on a paired straight velocity.

    This does not impose second-order incidence preservation.  The missing
    Lagrange-stress term is added by ``constrained_reduced_log_second``.
    """
    polar, primal_simplices, polar_simplices, polar_covariance = (
        paired_geometry(polytope)
    )
    dimension = polytope.dimension
    vertex_count = len(polytope.vertices)
    expected = dimension * (vertex_count + len(polar.vertices))
    if len(velocity) != expected:
        raise ValueError("paired velocity has the wrong length")
    primal_velocity = tuple(
        velocity[
            dimension * index : dimension * (index + 1)
        ]
        for index in range(vertex_count)
    )
    polar_offset = dimension * vertex_count
    polar_velocity = tuple(
        velocity[
            polar_offset
            + dimension * index : polar_offset
            + dimension * (index + 1)
        ]
        for index in range(len(polar.vertices))
    )

    def straight_jets(vertices, velocities):
        return tuple(
            tuple(
                Jet2(entry, velocities[index][coordinate])
                for coordinate, entry in enumerate(vertex)
            )
            for index, vertex in enumerate(vertices)
        )

    primal_volume, _ = volume_centroid_jets(
        straight_jets(polytope.vertices, primal_velocity),
        primal_simplices,
    )
    polar_volume, polar_centroid = volume_centroid_jets(
        straight_jets(polar.vertices, polar_velocity),
        polar_simplices,
    )
    if any(entry.value for entry in polar_centroid):
        raise ValueError("the paired base is not bi-centered")
    santalo_hessian = tuple(
        tuple(
            (dimension + 1)
            * (dimension + 2)
            * polar_covariance[row][column]
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    cross = tuple(
        (dimension + 1) * entry.first for entry in polar_centroid
    )
    correction = quadratic_form(inverse(santalo_hessian), cross)
    return (
        log_second(primal_volume)
        + log_second(polar_volume)
        - correction
    )


@lru_cache(maxsize=None)
def constrained_reduced_log_second(polytope, velocity, multiplier):
    """Lagrangian Hessian on an incidence tangent at a critical pair."""
    ambient = paired_straight_reduced_log_second(polytope, velocity)
    stress = incidence_stress_quadratic(
        polytope, multiplier, velocity
    )
    return ambient - 2 * stress


def constrained_reduced_log_bilinear(
    polytope, multiplier, left, right
):
    """Polarization of the exact constrained Santaló Hessian."""
    summed = tuple(a + b for a, b in zip(left, right))
    return (
        constrained_reduced_log_second(
            polytope, summed, multiplier
        )
        - constrained_reduced_log_second(
            polytope, left, multiplier
        )
        - constrained_reduced_log_second(
            polytope, right, multiplier
        )
    ) / 2


@lru_cache(maxsize=None)
def triangulation_vertex_mass_matrix(polytope):
    """Global barycentric second-moment mass matrix for a triangulation.

    If R_S selects a pulling simplex and G=I+11^T, this returns
    sum_S (|S|/|P|) R_S G R_S^T.
    """
    simplices = polytope.pulling_triangulation()
    weights = tuple(
        simplex_volume(
            [polytope.vertices[index] for index in simplex]
        )
        for simplex in simplices
    )
    total = sum(weights, Fraction())
    size = len(polytope.vertices)
    matrix = [
        [Fraction() for _ in range(size)] for _ in range(size)
    ]
    for simplex, weight in zip(simplices, weights):
        normalized = weight / total
        for left in simplex:
            for right in simplex:
                matrix[left][right] += normalized * (
                    2 if left == right else 1
                )
    return tuple(tuple(row) for row in matrix)


def simplex_pair_energy(primal_vertices, polar_vertices):
    """The exact 900-scaled second moment for a pair of 4-simplices."""
    pairing = tuple(
        tuple(dot(left, right) for right in polar_vertices)
        for left in primal_vertices
    )
    row_sums = tuple(sum(row, Fraction()) for row in pairing)
    column_sums = tuple(
        sum((pairing[row][column] for row in range(5)), Fraction())
        for column in range(5)
    )
    total = sum(row_sums, Fraction())
    return (
        total**2
        + sum((value**2 for value in row_sums), Fraction())
        + sum((value**2 for value in column_sums), Fraction())
        + sum(
            (value**2 for row in pairing for value in row),
            Fraction(),
        )
    )


def triangulation_slack_mass_trace(polytope):
    """Return tr(M_P N M_Q N^T) for the primal-polar vertex pairing."""
    polar, _, _, _ = paired_geometry(polytope)
    primal_mass = triangulation_vertex_mass_matrix(polytope)
    polar_mass = triangulation_vertex_mass_matrix(polar)
    pairing = tuple(
        tuple(dot(left, right) for right in polar.vertices)
        for left in polytope.vertices
    )
    return sum(
        (
            primal_mass[left][right]
            * pairing[right][facet]
            * polar_mass[facet][other_facet]
            * pairing[left][other_facet]
            for left in range(len(polytope.vertices))
            for right in range(len(polytope.vertices))
            for facet in range(len(polar.vertices))
            for other_facet in range(len(polar.vertices))
        ),
        Fraction(),
    )


def facet_cone_moment_data(polytope):
    """Cone weights, centroids, and second moments of 4-polytope facets.

    This exact helper currently requires triangular ridges, as in the
    24-cell. Four-dimensional cone volumes are proportional to intrinsic
    facet volumes within each supporting hyperplane, so no square roots
    enter the normalized facet moments.
    """
    if polytope.dimension != 4:
        raise ValueError("facet moment helper is specialized to dimension four")
    origin = (Fraction(),) * 4
    facet_sets = [frozenset(incident) for incident, _, _ in polytope.facets]
    raw = []
    for facet_index, facet in enumerate(facet_sets):
        apex = min(facet)
        ridges = set()
        for other_index, other in enumerate(facet_sets):
            if other_index == facet_index:
                continue
            intersection = tuple(sorted(facet.intersection(other)))
            if (
                intersection
                and affine_rank(
                    [polytope.vertices[index] for index in intersection]
                )
                == 2
            ):
                ridges.add(intersection)
        tetrahedra = tuple(
            tuple((apex, *ridge))
            for ridge in sorted(ridges)
            if apex not in ridge
        )
        if not tetrahedra or any(len(tetrahedron) != 4 for tetrahedron in tetrahedra):
            raise ValueError("facet moment helper requires triangular ridges")
        volume = Fraction()
        first = [Fraction() for _ in range(4)]
        second = [[Fraction() for _ in range(4)] for _ in range(4)]
        for tetrahedron in tetrahedra:
            vertices = [
                polytope.vertices[index] for index in tetrahedron
            ]
            weight = simplex_volume([origin, *vertices])
            volume += weight
            sums = [
                sum(
                    (vertex[coordinate] for vertex in vertices),
                    Fraction(),
                )
                for coordinate in range(4)
            ]
            for row in range(4):
                first[row] += weight * sums[row] / 4
                for column in range(4):
                    diagonal = sum(
                        (
                            vertex[row] * vertex[column]
                            for vertex in vertices
                        ),
                        Fraction(),
                    )
                    second[row][column] += weight * (
                        sums[row] * sums[column] + diagonal
                    ) / 20
        raw.append(
            (
                volume,
                tuple(value / volume for value in first),
                tuple(
                    tuple(value / volume for value in row)
                    for row in second
                ),
            )
        )
    total = sum((entry[0] for entry in raw), Fraction())
    return tuple(
        (volume / total, centroid, second)
        for volume, centroid, second in raw
    )


def boundary_trace_deficit(polytope):
    """Facet-pair divergence decomposition of 1/4-(9/4)tr(CovP CovP°)."""
    polar, _, _, _ = paired_geometry(polytope)
    primal_data = facet_cone_moment_data(polytope)
    polar_data = facet_cone_moment_data(polar)
    polar_facet_for_vertex = []
    for vertex in polytope.vertices:
        matches = [
            index
            for index, (_, normal, offset) in enumerate(polar.facets)
            if tuple(value / offset for value in normal) == vertex
        ]
        if len(matches) != 1:
            raise ValueError("could not match a primal vertex to its dual facet")
        polar_facet_for_vertex.append(matches[0])

    local = []
    for facet_index, (_, normal, offset) in enumerate(polytope.facets):
        polar_vertex = tuple(value / offset for value in normal)
        primal_weight, primal_centroid, primal_second = primal_data[facet_index]
        for vertex_index, vertex in enumerate(polytope.vertices):
            polar_facet_index = polar_facet_for_vertex[vertex_index]
            polar_weight, polar_centroid, polar_second = polar_data[
                polar_facet_index
            ]
            moment_pairing = sum(
                (
                    primal_second[row][column]
                    * polar_second[column][row]
                    for row in range(4)
                    for column in range(4)
                ),
                Fraction(),
            )
            bracket = (
                dot(vertex, polar_vertex)
                * dot(primal_centroid, polar_centroid)
                - moment_pairing
            )
            local.append(
                {
                    "facet": facet_index,
                    "vertex": vertex_index,
                    "incident": vertex_index
                    in polytope.facets[facet_index][0],
                    "bracket": bracket,
                    "weighted": primal_weight * polar_weight * bracket,
                }
            )
    return sum((entry["weighted"] for entry in local), Fraction()), tuple(local)


def terminal_excess_data(polytope):
    """Exact weighted row-capacity data behind robust terminality.

    A facet with ``m`` vertices contributes ``m-4`` independent affine
    relations.  ``beta3`` is the largest total excess on three
    nonsimplicial facets with independent normals.
    """
    nonsimplicial = tuple(
        (
            index,
            len(incident) - 4,
            tuple(value / offset for value in normal),
        )
        for index, (incident, normal, offset) in enumerate(polytope.facets)
        if len(incident) > 4
    )
    beta3 = max(
        (
            sum(entry[1] for entry in triple)
            for triple in combinations(nonsimplicial, 3)
            if rank([entry[2] for entry in triple]) == 3
        ),
        default=0,
    )
    return {
        "vertex_count": len(polytope.vertices),
        "facet_count": len(polytope.facets),
        "incidence_count": sum(
            len(incident) for incident, _, _ in polytope.facets
        ),
        "nonsimplicial_facet_count": len(nonsimplicial),
        "excess": sum(entry[1] for entry in nonsimplicial),
        "beta3": beta3,
    }


def quadratic_circuit_coupling(polytope):
    """Ranks of the intrinsic primal/dual degree-two circuit data.

    Circuit relations, rather than shadow-speed residuals, index the
    intrinsic second-moment tensors.  The mixed matrix has entries

        gamma^T (N o N) delta = tr(Q_gamma Q_delta^polar).

    Its rank is basis-independent even though the displayed circuit rows
    may be redundant.
    """
    polar, _, _, _ = paired_geometry(polytope)
    primal_circuits = polytope.admissible_matrix_waiving(())
    polar_circuits = polar.admissible_matrix_waiving(())

    def quadratic_rows(vertices, circuits):
        return tuple(
            tuple(
                sum(
                    (
                        coefficient * vertex[row] * vertex[column]
                        for coefficient, vertex in zip(circuit, vertices)
                    ),
                    Fraction(),
                )
                for row in range(4)
                for column in range(4)
            )
            for circuit in circuits
        )

    pairing_squared = tuple(
        tuple(dot(vertex, dual) ** 2 for dual in polar.vertices)
        for vertex in polytope.vertices
    )
    mixed = tuple(
        tuple(
            sum(
                (
                    primal_circuit[vertex]
                    * pairing_squared[vertex][facet]
                    * polar_circuit[facet]
                    for vertex in range(len(polytope.vertices))
                    for facet in range(len(polar.vertices))
                ),
                Fraction(),
            )
            for polar_circuit in polar_circuits
        )
        for primal_circuit in primal_circuits
    )
    return {
        "primal_circuit_rank": rank(primal_circuits),
        "polar_circuit_rank": rank(polar_circuits),
        "primal_quadratic_rank": rank(
            quadratic_rows(polytope.vertices, primal_circuits)
        ),
        "polar_quadratic_rank": rank(
            quadratic_rows(polar.vertices, polar_circuits)
        ),
        "mixed_rank": rank(mixed),
    }


def quadratic_slack_flex_data(polytope):
    """Global obstruction to the Hadamard-square slack tangent.

    If ``S`` is the normalized vertex--facet slack matrix, then

        S o S in T_S {matrices of rank at most 5}

    exactly when the returned obstruction has rank zero.  Unlike
    ``quadratic_circuit_coupling``, this uses bases of the complete affine
    dependency spaces; the two agree when facet circuits span globally.
    """
    polar, _, _, _ = paired_geometry(polytope)
    primal_relations = tuple(
        nullspace(
            [
                [Fraction(1) for _ in polytope.vertices],
                *[
                    [vertex[coordinate] for vertex in polytope.vertices]
                    for coordinate in range(4)
                ],
            ]
        )
    )
    polar_relations = tuple(
        nullspace(
            [
                [Fraction(1) for _ in polar.vertices],
                *[
                    [vertex[coordinate] for vertex in polar.vertices]
                    for coordinate in range(4)
                ],
            ]
        )
    )
    slack_squared = tuple(
        tuple((1 - dot(vertex, dual)) ** 2 for dual in polar.vertices)
        for vertex in polytope.vertices
    )
    obstruction = tuple(
        tuple(
            sum(
                (
                    primal[vertex]
                    * slack_squared[vertex][facet]
                    * dual[facet]
                    for vertex in range(len(polytope.vertices))
                    for facet in range(len(polar.vertices))
                ),
                Fraction(),
            )
            for dual in polar_relations
        )
        for primal in primal_relations
    )
    obstruction_rank = rank(obstruction)
    return {
        "primal_relation_dimension": len(primal_relations),
        "polar_relation_dimension": len(polar_relations),
        "obstruction_rank": obstruction_rank,
        "is_hadamard_square_tangent": obstruction_rank == 0,
    }


def speed_affinity_data(polytope, speeds):
    """Return the exact facets on which a vertex speed is nonaffine."""
    speeds = tuple(map(Q, speeds))
    if len(speeds) != len(polytope.vertices):
        raise ValueError("one speed is required per vertex")

    def is_affine(indices):
        evaluation_rows = [
            [Fraction(1) for _ in indices],
            *[
                [
                    polytope.vertices[index][coordinate]
                    for index in indices
                ]
                for coordinate in range(polytope.dimension)
            ],
        ]
        return rank([*evaluation_rows, [speeds[index] for index in indices]]) == (
            rank(evaluation_rows)
        )

    violated = tuple(
        facet_index
        for facet_index, (incident, _, _) in enumerate(polytope.facets)
        if not is_affine(incident)
    )
    return {
        "is_globally_affine": is_affine(tuple(range(len(polytope.vertices)))),
        "violated_facets": violated,
        "violated_normal_rank": rank(
            [polytope.facets[index][1] for index in violated]
        ),
    }


def cone_volume_green_data(polytope):
    """Intrinsic double-nonaffine energy of the squared slack matrix.

    Vertex weights are the normalized cone volumes of the corresponding
    dual facets.  The returned Green energy is the squared weighted norm of
    the double affine-regression residual of ``S o S``.
    """
    polar, _, _, _ = paired_geometry(polytope)
    primal_facet_weights = polytope.facet_cone_weights()
    polar_facet_weights = polar.facet_cone_weights()

    primal_vertex_weights = []
    for vertex in polytope.vertices:
        matches = [
            facet_index
            for facet_index, (_, normal, offset) in enumerate(polar.facets)
            if tuple(value / offset for value in normal) == vertex
        ]
        if len(matches) != 1:
            raise ValueError("could not match a primal vertex to its dual facet")
        primal_vertex_weights.append(polar_facet_weights[matches[0]])

    primal_relations = tuple(
        nullspace(
            [
                [Fraction(1) for _ in polytope.vertices],
                *[
                    [vertex[coordinate] for vertex in polytope.vertices]
                    for coordinate in range(polytope.dimension)
                ],
            ]
        )
    )
    polar_relations = tuple(
        nullspace(
            [
                [Fraction(1) for _ in polar.vertices],
                *[
                    [vertex[coordinate] for vertex in polar.vertices]
                    for coordinate in range(polytope.dimension)
                ],
            ]
        )
    )
    if not primal_relations or not polar_relations:
        return {
            "green_energy": Fraction(),
            "boundary_deficit": Fraction(),
            "deficit_to_energy_ratio": None,
        }

    def transpose(matrix):
        return tuple(zip(*matrix))

    def multiply(left, right):
        return tuple(
            tuple(
                sum(
                    (
                        left[row][inner] * right[inner][column]
                        for inner in range(len(right))
                    ),
                    Fraction(),
                )
                for column in range(len(right[0]))
            )
            for row in range(len(left))
        )

    slack_squared = tuple(
        tuple((1 - dot(vertex, dual)) ** 2 for dual in polar.vertices)
        for vertex in polytope.vertices
    )
    coupling = multiply(
        multiply(primal_relations, slack_squared),
        transpose(polar_relations),
    )
    primal_gram = tuple(
        tuple(
            sum(
                (
                    primal_relations[left][vertex]
                    * primal_relations[right][vertex]
                    / primal_vertex_weights[vertex]
                    for vertex in range(len(polytope.vertices))
                ),
                Fraction(),
            )
            for right in range(len(primal_relations))
        )
        for left in range(len(primal_relations))
    )
    polar_gram = tuple(
        tuple(
            sum(
                (
                    polar_relations[left][facet]
                    * polar_relations[right][facet]
                    / primal_facet_weights[facet]
                    for facet in range(len(polar.vertices))
                ),
                Fraction(),
            )
            for right in range(len(polar_relations))
        )
        for left in range(len(polar_relations))
    )
    energy_matrix = multiply(
        multiply(
            multiply(inverse(primal_gram), coupling),
            inverse(polar_gram),
        ),
        transpose(coupling),
    )
    green_energy = sum(
        (energy_matrix[index][index] for index in range(len(energy_matrix))),
        Fraction(),
    )

    _, primal_centroid, primal_covariance = (
        polytope.volume_centroid_covariance()
    )
    _, polar_centroid, polar_covariance = polar.volume_centroid_covariance()
    if any(primal_centroid) or any(polar_centroid):
        boundary_deficit = None
        ratio = None
    else:
        covariance_trace = sum(
            (
                primal_covariance[row][column]
                * polar_covariance[column][row]
                for row in range(polytope.dimension)
                for column in range(polytope.dimension)
            ),
            Fraction(),
        )
        boundary_deficit = Fraction(1, 4) - Fraction(9, 4) * covariance_trace
        ratio = (
            boundary_deficit / green_energy
            if green_energy
            else None
        )
    return {
        "green_energy": green_energy,
        "boundary_deficit": boundary_deficit,
        "deficit_to_energy_ratio": ratio,
    }


def circuit_cofactor_response(
        polytope,
        primal_indices,
        polar_indices,
):
    """Exact oriented response on two six-point affine circuits.

    The first derivative of ``det(S + t (N o N))`` equals the mixed
    quadratic-circuit contraction.  The four barycentric simplex-energy
    components have residues ``(C, -C, -C, C)`` and therefore cancel.
    """
    polar, _, _, _ = paired_geometry(polytope)
    if len(primal_indices) != 6 or len(polar_indices) != 6:
        raise ValueError("expected two six-point affine circuits")
    primal_rows = tuple(
        (Fraction(1), *polytope.vertices[index])
        for index in primal_indices
    )
    polar_rows = tuple(
        (Fraction(1), *polar.vertices[index])
        for index in polar_indices
    )
    primal_circuit = tuple(
        Fraction((-1) ** omitted)
        * determinant(
            [
                row
                for index, row in enumerate(primal_rows)
                if index != omitted
            ]
        )
        for omitted in range(6)
    )
    polar_circuit = tuple(
        Fraction((-1) ** omitted)
        * determinant(
            [
                row
                for index, row in enumerate(polar_rows)
                if index != omitted
            ]
        )
        for omitted in range(6)
    )
    if not all(primal_circuit) or not all(polar_circuit):
        raise ValueError("each five-point deletion must be an affine basis")

    pairing = tuple(
        tuple(
            dot(
                polytope.vertices[primal_index],
                polar.vertices[polar_index],
            )
            for polar_index in polar_indices
        )
        for primal_index in primal_indices
    )
    slack = tuple(
        tuple(1 - value for value in row)
        for row in pairing
    )
    coupling = sum(
        (
            primal_circuit[row]
            * pairing[row][column] ** 2
            * polar_circuit[column]
            for row in range(6)
            for column in range(6)
        ),
        Fraction(),
    )
    determinant_derivative = sum(
        (
            Fraction((-1) ** (row + column))
            * determinant(
                [
                    [
                        slack[inner_row][inner_column]
                        for inner_column in range(6)
                        if inner_column != column
                    ]
                    for inner_row in range(6)
                    if inner_row != row
                ]
            )
            * pairing[row][column] ** 2
            for row in range(6)
            for column in range(6)
        ),
        Fraction(),
    )

    component_residues = [Fraction() for _ in range(4)]
    energy_residue = Fraction()
    for omitted_row in range(6):
        for omitted_column in range(6):
            minor = tuple(
                tuple(
                    pairing[row][column]
                    for column in range(6)
                    if column != omitted_column
                )
                for row in range(6)
                if row != omitted_row
            )
            row_sums = tuple(sum(row, Fraction()) for row in minor)
            column_sums = tuple(
                sum((minor[row][column] for row in range(5)), Fraction())
                for column in range(5)
            )
            components = (
                sum(row_sums, Fraction()) ** 2,
                sum((value**2 for value in row_sums), Fraction()),
                sum((value**2 for value in column_sums), Fraction()),
                sum(
                    (value**2 for row in minor for value in row),
                    Fraction(),
                ),
            )
            weight = (
                primal_circuit[omitted_row]
                * polar_circuit[omitted_column]
            )
            for index, component in enumerate(components):
                component_residues[index] += weight * component
            energy_residue += weight * (
                sum(components, Fraction()) - 100
            )
    return {
        "primal_circuit": primal_circuit,
        "polar_circuit": polar_circuit,
        "coupling": coupling,
        "determinant_derivative": determinant_derivative,
        "component_residues": tuple(component_residues),
        "energy_residue": energy_residue,
    }


def low_rank_terminal_quadratic_countermodel(quadratic_rank):
    """Abstract robust-terminal tensor data for ranks three through five.

    These exact Vandermonde models satisfy normal-flat erasure, positive
    normal spanning, the facet-kernel condition, and the local
    triangular-bipyramid inertia.  They are not asserted to glue to a
    polytope.
    """
    if quadratic_rank not in (3, 4, 5):
        raise ValueError("the model is defined for ranks three, four, and five")
    degree = quadratic_rank - 3
    count = quadratic_rank + 3

    def polynomial_sum(value):
        return sum(
            (value**power for power in range(degree + 1)),
            Fraction(),
        )

    normals = []
    matrices = []
    for index in range(count):
        value = Fraction(index)
        sign = -1 if index % 2 else 1
        normals.append(
            tuple(
                Fraction(sign) * value**power
                for power in range(4)
            )
        )
        polynomial = polynomial_sum(value)
        matrices.append(
            (
                (value**2, -value, 0, 0),
                (-value, 1 - value**2, value, 0),
                (
                    0,
                    value,
                    -1 - polynomial * value**2,
                    polynomial * value,
                ),
                (0, 0, polynomial * value, -polynomial),
            )
        )
    positive_weights = tuple(
        Fraction(comb(count - 1, index))
        for index in range(count)
    )
    return {
        "normals": tuple(normals),
        "matrices": tuple(matrices),
        "positive_weights": positive_weights,
        "normal_rank": rank(normals),
        "matrix_rank": rank(
            [
                tuple(value for row in matrix for value in row)
                for matrix in matrices
            ]
        ),
    }


def boundary_regression_data(polytope):
    """Exact regression/Pythagorean invariants for the boundary normals.

    The covariance-deficit interpretation assumes that the primal and polar
    centroids are both zero; callers are responsible for this hypothesis.
    This helper is currently restricted by ``facet_cone_moment_data`` to
    four-polytopes with triangular ridges.
    """
    polar, _, _, _ = paired_geometry(polytope)
    primal_data = facet_cone_moment_data(polytope)
    polar_data = facet_cone_moment_data(polar)

    dimension = 4
    primal_second = tuple(
        tuple(
            sum(
                (
                    weight * second[row][column]
                    for weight, _, second in primal_data
                ),
                Fraction(),
            )
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    polar_second = tuple(
        tuple(
            sum(
                (
                    weight * second[row][column]
                    for weight, _, second in polar_data
                ),
                Fraction(),
            )
            for column in range(dimension)
        )
        for row in range(dimension)
    )

    polar_facet_weights = {}
    for facet_index, (incident, normal, offset) in enumerate(polar.facets):
        primal_vertex = tuple(value / offset for value in normal)
        polar_facet_weights[primal_vertex] = polar_data[facet_index][0]
    if len(polar_facet_weights) != len(polytope.vertices):
        raise ValueError("could not match every primal vertex to a polar facet")

    normal_squared_moment = sum(
        (
            primal_data[facet_index][0]
            * polar_facet_weights[vertex]
            * dot(vertex, tuple(value / offset for value in normal)) ** 2
            for facet_index, (incident, normal, offset)
            in enumerate(polytope.facets)
            for vertex in polytope.vertices
        ),
        Fraction(),
    )
    covariance_pairing = sum(
        (
            primal_second[row][column] * polar_second[column][row]
            for row in range(dimension)
            for column in range(dimension)
        ),
        Fraction(),
    )
    inverse_primal = inverse(primal_second)
    inverse_polar = inverse(polar_second)
    inverse_trace = sum(
        (
            inverse_primal[row][column] * inverse_polar[column][row]
            for row in range(dimension)
            for column in range(dimension)
        ),
        Fraction(),
    )
    linear_baseline = inverse_trace / 256
    return {
        "boundary_covariance_trace": covariance_pairing,
        "deficit": Fraction(1, 4) - covariance_pairing,
        "normal_squared_moment": normal_squared_moment,
        "inverse_trace": inverse_trace,
        "linear_baseline": linear_baseline,
        "regression_residual": normal_squared_moment - linear_baseline,
    }


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
    polar, _, _, _ = paired_geometry(polytope)
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


def incidence_pairs(polytope):
    """Incidence labels in exactly the row order of incidence_tangent_matrix."""
    return tuple(
        (vertex_index, facet_index)
        for facet_index, (incident, _, _) in enumerate(polytope.facets)
        for vertex_index in incident
    )


def incidence_tangent_and_stress_bases(polytope):
    """Return exact bases for ker J and ker J^T."""
    matrix = incidence_tangent_matrix(polytope)
    transpose = tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )
    return tuple(nullspace(matrix)), tuple(nullspace(transpose))


def split_paired_velocity(polytope, velocity, vertex_index, facet_index):
    dimension = polytope.dimension
    vertex_count = len(polytope.vertices)
    primal_start = dimension * vertex_index
    polar_start = dimension * vertex_count + dimension * facet_index
    return (
        velocity[primal_start : primal_start + dimension],
        velocity[polar_start : polar_start + dimension],
    )


def incidence_stress_bilinear(polytope, stress, left, right):
    """Polarization of sum stress[v,F] * left_v dot left_F."""
    result = Fraction()
    for coefficient, (vertex_index, facet_index) in zip(
        stress, incidence_pairs(polytope)
    ):
        left_vertex, left_facet = split_paired_velocity(
            polytope, left, vertex_index, facet_index
        )
        right_vertex, right_facet = split_paired_velocity(
            polytope, right, vertex_index, facet_index
        )
        result += coefficient * (
            dot(left_vertex, right_facet)
            + dot(right_vertex, left_facet)
        ) / 2
    return result


def incidence_stress_quadratic(polytope, stress, velocity):
    return incidence_stress_bilinear(
        polytope, stress, velocity, velocity
    )


def second_order_incidence_rhs(polytope, velocity):
    """Right side J*w=-c(u,u) for z(t)=z+t*u+t^2*w+... ."""
    result = []
    for vertex_index, facet_index in incidence_pairs(polytope):
        vertex_velocity, facet_velocity = split_paired_velocity(
            polytope, velocity, vertex_index, facet_index
        )
        result.append(-dot(vertex_velocity, facet_velocity))
    return tuple(result)


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
    polar, _, _, _ = paired_geometry(polytope)
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
