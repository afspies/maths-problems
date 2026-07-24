"""Rational interval certificate for a projectively critical 24-cell.

The certificate proves that the Paffenholz realization has a unique
bi-centering translation in a displayed rational box and that the
projective covariance Hessian there has a negative direction.  It uses no
floating-point arithmetic or external interval package.
"""

from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, lcm

from polytope import (
    affine_rank,
    determinant,
    inverse,
    paffenholz_24_cell,
    rank,
    rowspace_key,
)


def Q(value):
    return value if isinstance(value, Fraction) else Fraction(value)


class Interval:
    # Outward dyadic rounding keeps exact rational interval expressions from
    # suffering denominator explosion.  The enclosure remains rigorous.
    SCALE = 1 << 160

    def __init__(self, low, high=None):
        exact_low = Q(low)
        exact_high = exact_low if high is None else Q(high)
        self.low = Fraction(
            (exact_low.numerator * self.SCALE) // exact_low.denominator,
            self.SCALE,
        )
        self.high = Fraction(
            -((-exact_high.numerator * self.SCALE) // exact_high.denominator),
            self.SCALE,
        )
        if self.low > self.high:
            raise ValueError("reversed interval")

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.low + other.low, self.high + other.high)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        products = (
            self.low * other.low,
            self.low * other.high,
            self.high * other.low,
            self.high * other.high,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.low <= 0 <= self.high:
            raise ZeroDivisionError("interval contains zero")
        return Interval(1 / self.high, 1 / self.low)

    def __truediv__(self, other):
        return self * as_interval(other).reciprocal()

    def __rtruediv__(self, other):
        return as_interval(other) / self

    def midpoint(self):
        return (self.low + self.high) / 2

    def width(self):
        return self.high - self.low


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


class AD:
    """Interval value with interval first derivatives."""

    def __init__(self, value, gradient):
        self.value = as_interval(value)
        self.gradient = tuple(as_interval(entry) for entry in gradient)

    @classmethod
    def constant(cls, value, dimension=4):
        return cls(value, (0,) * dimension)

    def __add__(self, other):
        other = as_ad(other, len(self.gradient))
        return AD(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.gradient, other.gradient)),
        )

    __radd__ = __add__

    def __neg__(self):
        return AD(-self.value, tuple(-entry for entry in self.gradient))

    def __sub__(self, other):
        return self + (-as_ad(other, len(self.gradient)))

    def __rsub__(self, other):
        return as_ad(other, len(self.gradient)) - self

    def __mul__(self, other):
        other = as_ad(other, len(self.gradient))
        return AD(
            self.value * other.value,
            tuple(
                self.value * right + other.value * left
                for left, right in zip(self.gradient, other.gradient)
            ),
        )

    __rmul__ = __mul__

    def reciprocal(self):
        reciprocal = self.value.reciprocal()
        return AD(
            reciprocal,
            tuple(-entry * reciprocal * reciprocal for entry in self.gradient),
        )

    def __truediv__(self, other):
        return self * as_ad(other, len(self.gradient)).reciprocal()

    def __rtruediv__(self, other):
        return as_ad(other, len(self.gradient)) / self


def as_ad(value, dimension=4):
    return value if isinstance(value, AD) else AD.constant(value, dimension)


def determinant_generic(matrix):
    size = len(matrix)
    result = 0
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(size)
            for right in range(left + 1, size)
        )
        term = 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        result += term if inversions % 2 == 0 else -term
    return result


def positive_simplex_weight(vertices):
    base = vertices[0]
    matrix = [
        [
            vertices[column + 1][row] - base[row]
            for column in range(len(vertices) - 1)
        ]
        for row in range(len(vertices) - 1)
    ]
    determinant = determinant_generic(matrix)
    value = determinant.value if isinstance(determinant, AD) else determinant
    if isinstance(value, Interval):
        if value.low > 0:
            return determinant
        if value.high < 0:
            return -determinant
    else:
        if value > 0:
            return determinant
        if value < 0:
            return -determinant
    raise ValueError("simplex orientation is not certified in the box")


def moments(vertices, simplices, with_covariance=True):
    """Return unnormalised volume, first moment, and second moment.

    The common factor 4! cancels from every normalized moment, so simplex
    determinant magnitudes are used directly as weights.
    """
    dimension = len(vertices[0])
    volume = 0
    first = [0 for _ in range(dimension)]
    second = (
        [[0 for _ in range(dimension)] for _ in range(dimension)]
        if with_covariance
        else None
    )
    for simplex in simplices:
        points = [vertices[index] for index in simplex]
        weight = positive_simplex_weight(points)
        sums = [
            sum((point[coordinate] for point in points), 0)
            for coordinate in range(dimension)
        ]
        volume += weight
        for row in range(dimension):
            first[row] += weight * sums[row] / (dimension + 1)
            if with_covariance:
                for column in range(dimension):
                    diagonal = sum(
                        (point[row] * point[column] for point in points), 0
                    )
                    second[row][column] += weight * (
                        sums[row] * sums[column] + diagonal
                    ) / ((dimension + 1) * (dimension + 2))
    centroid = tuple(entry / volume for entry in first)
    if not with_covariance:
        return centroid, None
    covariance = tuple(
        tuple(
            second[row][column] / volume - centroid[row] * centroid[column]
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    return centroid, covariance


def projective_pair_data(variables):
    """Vertices of the polar-centered projective image and its polar."""
    polytope = paffenholz_24_cell()
    polar_simplices = polytope.polar().pulling_triangulation()
    polar_vertices = []
    facet_denominators = []
    for _, normal, offset in polytope.facets:
        denominator = offset - sum(
            (normal[index] * variables[index] for index in range(4)), 0
        )
        facet_denominators.append(denominator)
        polar_vertices.append(
            tuple(normal[index] / denominator for index in range(4))
        )
    polar_centroid, _ = moments(
        polar_vertices, polar_simplices, with_covariance=False
    )

    transformed_vertices = []
    projective_denominators = []
    for vertex in polytope.vertices:
        shifted = tuple(vertex[index] - variables[index] for index in range(4))
        denominator = 1 - sum(
            (polar_centroid[index] * shifted[index] for index in range(4)), 0
        )
        projective_denominators.append(denominator)
        transformed_vertices.append(
            tuple(shifted[index] / denominator for index in range(4))
        )
    centered_polar_vertices = tuple(
        tuple(
            polar_vertex[index] - polar_centroid[index]
            for index in range(4)
        )
        for polar_vertex in polar_vertices
    )
    return (
        tuple(transformed_vertices),
        centered_polar_vertices,
        tuple(facet_denominators),
        tuple(projective_denominators),
        tuple(polar_vertices),
    )


def centroid_system(box, derivatives=True, with_covariance=False):
    polytope = paffenholz_24_cell()
    primal_simplices = polytope.pulling_triangulation()
    polar_simplices = polytope.polar().pulling_triangulation()
    if derivatives:
        variables = []
        for index, interval in enumerate(box):
            gradient = [Interval(0) for _ in range(4)]
            gradient[index] = Interval(1)
            variables.append(AD(interval, gradient))
    else:
        variables = list(box)

    (
        transformed_vertices,
        centered_polar_vertices,
        _,
        _,
        translated_polar_vertices,
    ) = projective_pair_data(variables)
    _, polar_covariance = moments(
        translated_polar_vertices, polar_simplices, with_covariance
    )
    centroid, covariance = moments(
        transformed_vertices, primal_simplices, with_covariance
    )
    return centroid, covariance, polar_covariance


def normal_flat_waived_sets(normals):
    """Enumerate every hyperplane-waivable normal flat from exact normals."""
    def primitive(row):
        denominator = 1
        for value in row:
            denominator = lcm(denominator, value.denominator)
        integers = [
            value.numerator * (denominator // value.denominator)
            for value in row
        ]
        divisor = 0
        for value in integers:
            divisor = gcd(divisor, abs(value))
        integers = [value // divisor for value in integers]
        first = next(value for value in integers if value)
        if first < 0:
            integers = [-value for value in integers]
        return tuple(Fraction(value) for value in integers)

    normals = tuple(primitive(normal) for normal in normals)
    span_keys = {()}
    for size in range(1, 4):
        for chosen in combinations(range(len(normals)), size):
            key = rowspace_key([normals[index] for index in chosen])
            if len(key) < 4:
                span_keys.add(key)
    result = set()
    for key in sorted(span_keys):
        span_rank = len(key)
        result.add(
            tuple(
                index
                for index, normal in enumerate(normals)
                if rank([*key, normal]) == span_rank
            )
        )
    return tuple(sorted(result))


def terminal_dimensions_from_reference(reference, normals):
    """Use projective circuit-rank transport with a new normal arrangement."""
    return tuple(
        len(reference.vertices)
        - rank(reference.admissible_matrix_waiving(waived))
        for waived in normal_flat_waived_sets(normals)
    )


def polar_normals_in_facet_order(reference, transformed_vertices):
    """Order transformed primal vertices as normals of reference° facets."""
    polar = reference.polar()
    vertex_index = {vertex: index for index, vertex in enumerate(reference.vertices)}
    result = []
    for _, normal, offset in polar.facets:
        original_vertex = tuple(value / offset for value in normal)
        result.append(transformed_vertices[vertex_index[original_vertex]])
    return tuple(result)


def certify_nonzero_four_normal_determinants(center_normals, box_normals):
    exact_nonzero = 0
    exact_zero = 0
    unresolved = 0
    for chosen in combinations(range(len(center_normals)), 4):
        exact = determinant([center_normals[index] for index in chosen])
        if not exact:
            exact_zero += 1
            continue
        exact_nonzero += 1
        enclosure = determinant_generic(
            [box_normals[index] for index in chosen]
        )
        if enclosure.low <= 0 <= enclosure.high:
            unresolved += 1
    if unresolved:
        raise AssertionError("a nonzero normal determinant may vanish in the box")
    return exact_nonzero, exact_zero, unresolved


def minimal_facet_circuit_supports(polytope):
    supports = set()
    for incident, _, _ in polytope.facets:
        for size in range(2, min(5, len(incident)) + 1):
            for chosen in combinations(incident, size):
                points = [polytope.vertices[index] for index in chosen]
                if affine_rank(points) == size - 1:
                    continue
                if all(
                    affine_rank(
                        [
                            polytope.vertices[index]
                            for index in chosen
                            if index != removed
                        ]
                    )
                    == size - 2
                    for removed in chosen
                ):
                    supports.add(tuple(chosen))
    return tuple(sorted(supports))


def circuit_support_connected(vertex_count, supports):
    adjacency = [set() for _ in range(vertex_count)]
    for support in supports:
        for left in support:
            adjacency[left].update(index for index in support if index != left)
    seen = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for neighbor in adjacency[current] - seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    return len(seen) == vertex_count


def interval_matrix_product(left, right):
    return tuple(
        tuple(
            sum(
                (
                    as_interval(left[row][inner])
                    * as_interval(right[inner][column])
                    for inner in range(len(right))
                ),
                Interval(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def certify():
    center = tuple(
        map(
            Fraction,
            (
                "0.065348617243",
                "0.127816191744",
                "0.153467113574",
                "0.022269205148",
            ),
        )
    )
    radius = Fraction(1, 10**10)
    box = tuple(Interval(value - radius, value + radius) for value in center)
    centroid, _, _ = centroid_system(box)

    point_box = tuple(Interval(value) for value in center)
    point_centroid, _, _ = centroid_system(
        point_box, derivatives=False
    )
    jacobian = tuple(
        tuple(centroid[row].gradient[column].midpoint() for column in range(4))
        for row in range(4)
    )
    preconditioner = inverse(jacobian)
    interval_jacobian = tuple(
        tuple(centroid[row].gradient[column] for column in range(4))
        for row in range(4)
    )
    product = interval_matrix_product(preconditioner, interval_jacobian)
    defect = tuple(
        tuple(
            Interval(int(row == column)) - product[row][column]
            for column in range(4)
        )
        for row in range(4)
    )
    correction = tuple(
        Interval(center[row])
        - sum(
            (
                preconditioner[row][column] * point_centroid[column]
                for column in range(4)
            ),
            Interval(0),
        )
        for row in range(4)
    )
    centered_box = tuple(Interval(-radius, radius) for _ in range(4))
    remainder = interval_matrix_product(defect, tuple((entry,) for entry in centered_box))
    krawczyk = tuple(
        correction[row] + remainder[row][0] for row in range(4)
    )
    if not all(
        box[index].low < krawczyk[index].low
        and krawczyk[index].high < box[index].high
        for index in range(4)
    ):
        raise AssertionError("Krawczyk image is not strictly inside the box")

    _, covariance_values, polar_covariance_values = centroid_system(
        box, derivatives=False, with_covariance=True
    )
    minor = determinant_generic(
        [list(row[1:]) for row in covariance_values[1:]]
    )
    full_determinant = determinant_generic([list(row) for row in covariance_values])
    inverse_00 = minor / full_determinant
    gap_00 = polar_covariance_values[0][0] - inverse_00 / 36
    if gap_00.high >= 0:
        raise AssertionError("the covariance-Hessian violation is not certified")
    covariance_trace = sum(
        (
            covariance_values[row][column]
            * polar_covariance_values[column][row]
            for row in range(4)
            for column in range(4)
        ),
        Interval(0),
    )
    if covariance_trace.high >= Fraction(1, 9):
        raise AssertionError("the strict covariance-trace gap is not certified")

    reference = paffenholz_24_cell()
    (
        center_primal_vertices,
        center_polar_vertices,
        _,
        _,
        _,
    ) = projective_pair_data(center)
    center_primal_normals = center_polar_vertices
    center_polar_normals = polar_normals_in_facet_order(
        reference, center_primal_vertices
    )
    primal_dimensions = terminal_dimensions_from_reference(
        reference, center_primal_normals
    )
    polar_reference = reference.polar()
    polar_dimensions = terminal_dimensions_from_reference(
        polar_reference, center_polar_normals
    )
    if set(primal_dimensions) != {5} or set(polar_dimensions) != {5}:
        raise AssertionError("the rational box center is not pair-terminal")

    primal_supports = minimal_facet_circuit_supports(reference)
    polar_supports = minimal_facet_circuit_supports(polar_reference)
    if not circuit_support_connected(len(reference.vertices), primal_supports):
        raise AssertionError("the primal circuit support is disconnected")
    if not circuit_support_connected(
        len(polar_reference.vertices), polar_supports
    ):
        raise AssertionError("the polar circuit support is disconnected")

    (
        box_primal_vertices,
        box_polar_vertices,
        facet_denominators,
        projective_denominators,
        _,
    ) = projective_pair_data(box)
    box_primal_normals = box_polar_vertices
    box_polar_normals = polar_normals_in_facet_order(
        reference, box_primal_vertices
    )
    primal_determinants = certify_nonzero_four_normal_determinants(
        center_primal_normals, box_primal_normals
    )
    polar_determinants = certify_nonzero_four_normal_determinants(
        center_polar_normals, box_polar_normals
    )
    facet_denominator_lower = min(
        denominator.low for denominator in facet_denominators
    )
    projective_denominator_lower = min(
        denominator.low for denominator in projective_denominators
    )
    if facet_denominator_lower <= 0 or projective_denominator_lower <= 0:
        raise AssertionError("a projective denominator may vanish in the box")

    print("box-radius", radius)
    print(
        "krawczyk-widths",
        tuple(interval.width() for interval in krawczyk),
    )
    print("unique-bicenter-root", True)
    print("covariance-gap-e1-upper", gap_00.high)
    print(
        "covariance-trace-enclosure",
        (covariance_trace.low, covariance_trace.high),
    )
    print("covariance-trace-below-one-ninth", True)
    print(
        "rational-center-normal-flats",
        (len(primal_dimensions), len(polar_dimensions)),
    )
    print("rational-center-pair-terminal", True)
    print(
        "circuit-supports",
        (
            len(primal_supports),
            tuple(sorted({len(support) for support in primal_supports})),
            len(polar_supports),
            tuple(sorted({len(support) for support in polar_supports})),
        ),
    )
    print("circuit-support-connected", True)
    print("primal-four-normal-determinants", primal_determinants)
    print("polar-four-normal-determinants", polar_determinants)
    print(
        "projective-denominator-lower-bounds",
        (facet_denominator_lower, projective_denominator_lower),
    )
    print("bi-centered-root-pair-terminal", True)
    print("projective-local-minimum", False)


if __name__ == "__main__":
    certify()
