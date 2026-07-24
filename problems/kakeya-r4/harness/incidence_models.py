#!/usr/bin/env python3
"""Small exact incidence models for plany, trilinear, and ruled cases."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


Vector = tuple[F, F, F, F]


def vec(values: tuple[int, int, int, int]) -> Vector:
    return tuple(F(x) for x in values)  # type: ignore[return-value]


def rank(vectors: list[Vector]) -> int:
    matrix = [list(row) for row in vectors]
    r = 0
    for col in range(4):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        scale = matrix[r][col]
        matrix[r] = [x / scale for x in matrix[r]]
        for i in range(len(matrix)):
            if i != r and matrix[i][col]:
                scale = matrix[i][col]
                matrix[i] = [
                    matrix[i][j] - scale * matrix[r][j] for j in range(4)
                ]
        r += 1
    return r


def wedge_squared(a: Vector, b: Vector, c: Vector) -> F:
    """Squared norm of a∧b∧c, as the sum of squared 3x3 minors."""
    total = F(0)
    rows = (a, b, c)
    for cols in combinations(range(4), 3):
        matrix = [[row[j] for j in cols] for row in rows]
        det = (
            matrix[0][0]
            * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1]
            * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2]
            * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
        total += det * det
    return total


def norm_squared(a: Vector) -> F:
    return sum(x * x for x in a)


def normalized_wedge_squared(a: Vector, b: Vector, c: Vector) -> F:
    """Squared wedge after Euclidean normalization, still exactly rational."""
    return wedge_squared(a, b, c) / (
        norm_squared(a) * norm_squared(b) * norm_squared(c)
    )


@dataclass(frozen=True)
class Line:
    base: Vector
    direction: Vector

    def point(self, t: F) -> Vector:
        return tuple(
            self.base[i] + t * self.direction[i] for i in range(4)
        )  # type: ignore[return-value]


def quadric_value(x: Vector) -> F:
    return x[0] ** 2 + x[1] ** 2 - x[2] ** 2 - x[3] ** 2


def quadric_line_coefficients(line: Line) -> tuple[F, F, F]:
    """Coefficients (constant, linear, quadratic) of Q(base+t*direction)."""
    b = line.base
    d = line.direction
    linear = 2 * (
        b[0] * d[0] + b[1] * d[1] - b[2] * d[2] - b[3] * d[3]
    )
    return quadric_value(b), linear, quadric_value(d)


def plany_model() -> list[Line]:
    zero = vec((0, 0, 0, 0))
    return [
        Line(zero, vec((1, 0, 0, 0))),
        Line(zero, vec((0, 1, 0, 0))),
        Line(zero, vec((1, 1, 0, 0))),
    ]


def trilinear_model() -> list[Line]:
    zero = vec((0, 0, 0, 0))
    return [
        Line(zero, vec((1, 0, 0, 0))),
        Line(zero, vec((0, 1, 0, 0))),
        Line(zero, vec((0, 0, 1, 0))),
    ]


def ruled_quadric_lines() -> list[Line]:
    """Three rational lines on x1^2+x2^2-x3^2-x4^2=1.

    Identify the quadric with SL_2 via
      M=[[x1+x3, x2+x4], [x4-x2, x1-x3]].
    At M=I, M(I+t p q^T) stays in SL_2 whenever q^T p=0.
    """
    base = vec((1, 0, 0, 0))
    return [
        Line(base, vec((0, 1, 1, 0))),
        Line(base, vec((0, 1, 0, 1))),
        Line(base, vec((0, 5, 3, 4))),
    ]
