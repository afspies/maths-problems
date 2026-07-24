"""Numerically locate the bi-centred representative of a projective class.

This is a discovery aid only.  It deliberately reuses exact face
triangulations, but evaluates the centroid equations in binary floating point.
Any theorem or certificate suggested here must be reconstructed exactly.
"""

from fractions import Fraction
from math import factorial

from polytope import determinant, paffenholz_24_cell


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
    return abs(float(determinant(matrix))) / factorial(dimension)


def centroid_from_fixed_triangulation(vertices, simplices):
    dimension = len(vertices[0])
    volume = 0.0
    moment = [0.0] * dimension
    for simplex in simplices:
        simplex_vertices = [vertices[index] for index in simplex]
        weight = simplex_volume_float(simplex_vertices)
        volume += weight
        for coordinate in range(dimension):
            moment[coordinate] += weight * sum(
                vertex[coordinate] for vertex in simplex_vertices
            ) / (dimension + 1)
    return tuple(value / volume for value in moment)


def main():
    polytope = paffenholz_24_cell(
        (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5))
    )
    primal_simplices = polytope.pulling_triangulation()
    polar = polytope.polar()
    polar_simplices = polar.pulling_triangulation()
    facet_data = [
        (tuple(map(float, normal)), float(offset))
        for _, normal, offset in polytope.facets
    ]
    vertices = [tuple(map(float, vertex)) for vertex in polytope.vertices]

    def residual(z):
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
        return centroid_from_fixed_triangulation(
            transformed_vertices, primal_simplices
        )

    z = [0.0] * 4
    for iteration in range(20):
        value = residual(z)
        norm = max(abs(entry) for entry in value)
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


if __name__ == "__main__":
    main()
