"""Numerically locate the bi-centred representative of a projective class.

This is a discovery aid only.  It deliberately reuses exact face
triangulations, but evaluates the centroid equations in binary floating point.
Any theorem or certificate suggested here must be reconstructed exactly.
"""

from fractions import Fraction
from math import factorial

from polytope import paffenholz_24_cell


def solve_linear(matrix, right):
    work = [list(row) + [value] for row, value in zip(matrix, right)]
    size = len(work)
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        if abs(scale) < 1e-14:
            raise ValueError("singular numerical Jacobian")
        work[column] = [value / scale for value in work[column]]
        for row in range(size):
            if row == column:
                continue
            scale = work[row][column]
            work[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(work[row], work[column])
            ]
    return [work[row][-1] for row in range(size)]


def simplex_volume_float(vertices):
    dimension = len(vertices) - 1
    base = vertices[0]
    matrix = [
        [vertices[column + 1][row] - base[row] for column in range(dimension)]
        for row in range(dimension)
    ]
    return abs(determinant_float(matrix)) / factorial(dimension)


def determinant_float(matrix):
    work = [list(row) for row in matrix]
    result = 1.0
    for column in range(len(work)):
        pivot = max(
            range(column, len(work)),
            key=lambda row: abs(work[row][column]),
        )
        if abs(work[pivot][column]) < 1e-15:
            return 0.0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            scale = work[row][column] / pivot_value
            for inner in range(column + 1, len(work)):
                work[row][inner] -= scale * work[column][inner]
    return result


def centroid_from_fixed_triangulation(vertices, simplices):
    return moments_from_fixed_triangulation(vertices, simplices)[1]


def moments_from_fixed_triangulation(vertices, simplices):
    dimension = len(vertices[0])
    volume = 0.0
    moment = [0.0] * dimension
    second = [[0.0] * dimension for _ in range(dimension)]
    for simplex in simplices:
        simplex_vertices = [vertices[index] for index in simplex]
        weight = simplex_volume_float(simplex_vertices)
        volume += weight
        sums = [
            sum(vertex[coordinate] for vertex in simplex_vertices)
            for coordinate in range(dimension)
        ]
        for coordinate in range(dimension):
            moment[coordinate] += weight * sums[coordinate] / (dimension + 1)
            for other in range(dimension):
                diagonal = sum(
                    vertex[coordinate] * vertex[other]
                    for vertex in simplex_vertices
                )
                second[coordinate][other] += weight * (
                    sums[coordinate] * sums[other] + diagonal
                ) / ((dimension + 1) * (dimension + 2))
    centroid = tuple(value / volume for value in moment)
    covariance = tuple(
        tuple(
            second[row][column] / volume
            - centroid[row] * centroid[column]
            for column in range(dimension)
        )
        for row in range(dimension)
    )
    return volume, centroid, covariance


def bicenter_data(parameters, initial=None, verbose=False):
    polytope = paffenholz_24_cell(parameters)
    primal_simplices = polytope.pulling_triangulation()
    polar = polytope.polar()
    polar_simplices = polar.pulling_triangulation()
    facet_data = [
        (tuple(map(float, normal)), float(offset))
        for _, normal, offset in polytope.facets
    ]
    vertices = [tuple(map(float, vertex)) for vertex in polytope.vertices]

    def transformed_data(z):
        translated_polar_vertices = [
            tuple(
                coordinate / (offset - sum(a * b for a, b in zip(normal, z)))
                for coordinate in normal
            )
            for normal, offset in facet_data
        ]
        polar_centroid = centroid_from_fixed_triangulation(
            translated_polar_vertices, polar_simplices
        )
        projective_parameter = tuple(-value for value in polar_centroid)
        transformed_vertices = []
        for vertex in vertices:
            shifted = tuple(a - b for a, b in zip(vertex, z))
            denominator = 1 + sum(
                a * b for a, b in zip(projective_parameter, shifted)
            )
            transformed_vertices.append(
                tuple(value / denominator for value in shifted)
            )
        return (
            centroid_from_fixed_triangulation(
                transformed_vertices, primal_simplices
            ),
            transformed_vertices,
            translated_polar_vertices,
        )

    def residual(z):
        return transformed_data(z)[0]

    z = [0.0] * 4 if initial is None else list(initial)
    for iteration in range(20):
        value = residual(z)
        norm = max(abs(entry) for entry in value)
        if verbose:
            print(iteration, "z", z, "residual", value, "norm", norm)
        if norm < 1e-12:
            break
        step = 1e-6
        jacobian = []
        for row in range(4):
            jacobian.append([])
            for column in range(4):
                perturbed = list(z)
                perturbed[column] += step
                changed = residual(perturbed)
                jacobian[row].append((changed[row] - value[row]) / step)
        delta = solve_linear(jacobian, [-entry for entry in value])
        z = [entry + change for entry, change in zip(z, delta)]
    centroid, transformed, translated_polar = transformed_data(z)
    return {
        "translation": tuple(z),
        "residual": centroid,
        "vertices": tuple(transformed),
        "polar_vertices_before_centering": tuple(translated_polar),
        "primal_simplices": primal_simplices,
        "polar_simplices": polar_simplices,
    }


def inverse_float(matrix):
    size = len(matrix)
    columns = []
    for column in range(size):
        right = [float(row == column) for row in range(size)]
        columns.append(solve_linear(matrix, right))
    return tuple(
        tuple(columns[column][row] for column in range(size))
        for row in range(size)
    )


def covariance_gap(data):
    _, _, primal_covariance = moments_from_fixed_triangulation(
        data["vertices"], data["primal_simplices"]
    )
    _, polar_centroid, polar_covariance = moments_from_fixed_triangulation(
        data["polar_vertices_before_centering"], data["polar_simplices"]
    )
    inverse_primal = inverse_float(primal_covariance)
    gap = tuple(
        tuple(
            polar_covariance[row][column] - inverse_primal[row][column] / 36
            for column in range(4)
        )
        for row in range(4)
    )
    return polar_centroid, primal_covariance, polar_covariance, gap


def main():
    parameters = (
        Fraction(1, 5),
        Fraction(2, 5),
        Fraction(3, 5),
        Fraction(4, 5),
    )
    data = bicenter_data(parameters, verbose=True)
    _, _, _, gap = covariance_gap(data)
    print("gap-diagonal", tuple(gap[index][index] for index in range(4)))


if __name__ == "__main__":
    main()
