"""Exact rational checks for polygonal Square Peg data.

Nothing in this module searches for squares or proves a universal statement.
It exists to keep finite examples and area-primitive calculations honest.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

Point = tuple[Fraction, Fraction]


def point(x: int | str | Fraction, y: int | str | Fraction) -> Point:
    return Fraction(x), Fraction(y)


def sub(a: Point, b: Point) -> Point:
    return a[0] - b[0], a[1] - b[1]


def cross(a: Point, b: Point) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def dot(a: Point, b: Point) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return cross(sub(b, a), sub(c, a))


def _on_segment(a: Point, b: Point, p: Point) -> bool:
    return (
        orient(a, b, p) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    """Return whether the two closed segments have any point in common."""

    o1, o2 = orient(a, b, c), orient(a, b, d)
    o3, o4 = orient(c, d, a), orient(c, d, b)
    if ((o1 > 0 > o2) or (o2 > 0 > o1)) and (
        (o3 > 0 > o4) or (o4 > 0 > o3)
    ):
        return True
    return (
        (o1 == 0 and _on_segment(a, b, c))
        or (o2 == 0 and _on_segment(a, b, d))
        or (o3 == 0 and _on_segment(c, d, a))
        or (o4 == 0 and _on_segment(c, d, b))
    )


def is_simple_polygon(vertices: Sequence[Point]) -> bool:
    """Check that the cyclic polygon is an embedded closed polygonal curve."""

    n = len(vertices)
    if n < 3 or len(set(vertices)) != n:
        return False
    for i in range(n):
        if vertices[i] == vertices[(i + 1) % n]:
            return False
    for i in range(n):
        a, b = vertices[i], vertices[(i + 1) % n]
        for j in range(i + 1, n):
            c, d = vertices[j], vertices[(j + 1) % n]
            adjacent = j == i + 1 or (i == 0 and j == n - 1)
            if not adjacent and segments_intersect(a, b, c, d):
                return False
    return True


def edge_liouville(a: Point, b: Point) -> Fraction:
    """Exactly integrate y dx along the affine segment from a to b."""

    return (a[1] + b[1]) * (b[0] - a[0]) / 2


def liouville_primitive(vertices: Sequence[Point]) -> list[Fraction]:
    """Primitive values at cyclic vertices, including the final period value."""

    if len(vertices) < 2:
        raise ValueError("need at least two vertices")
    values = [Fraction(0)]
    for i, a in enumerate(vertices):
        b = vertices[(i + 1) % len(vertices)]
        values.append(values[-1] + edge_liouville(a, b))
    return values


def signed_double_area(vertices: Sequence[Point]) -> Fraction:
    """Twice the oriented shoelace area."""

    return sum(
        cross(vertices[i], vertices[(i + 1) % len(vertices)])
        for i in range(len(vertices))
    )


def subdivide(
    vertices: Sequence[Point], cuts: Iterable[Fraction] = (Fraction(1, 2),)
) -> list[Point]:
    """Subdivide every edge at the same strictly interior rational parameters."""

    ordered = sorted(set(Fraction(t) for t in cuts))
    if any(t <= 0 or t >= 1 for t in ordered):
        raise ValueError("cuts must lie strictly between 0 and 1")
    out: list[Point] = []
    for i, a in enumerate(vertices):
        b = vertices[(i + 1) % len(vertices)]
        out.append(a)
        delta = sub(b, a)
        out.extend((a[0] + t * delta[0], a[1] + t * delta[1]) for t in ordered)
    return out


def point_on_polygon_boundary(p: Point, vertices: Sequence[Point]) -> bool:
    return any(
        _on_segment(vertices[i], vertices[(i + 1) % len(vertices)], p)
        for i in range(len(vertices))
    )


def verify_inscribed_square(
    vertices: Sequence[Point], square: Sequence[Point]
) -> bool:
    """Verify four cyclically ordered boundary points form a nondegenerate square."""

    if not is_simple_polygon(vertices) or len(square) != 4:
        return False
    if len(set(square)) != 4 or not all(
        point_on_polygon_boundary(p, vertices) for p in square
    ):
        return False
    sides = [sub(square[(i + 1) % 4], square[i]) for i in range(4)]
    side_lengths = [dot(v, v) for v in sides]
    return (
        side_lengths[0] > 0
        and len(set(side_lengths)) == 1
        and all(dot(sides[i], sides[(i + 1) % 4]) == 0 for i in range(4))
        and (
            square[0][0] + square[2][0],
            square[0][1] + square[2][1],
        )
        == (
            square[1][0] + square[3][0],
            square[1][1] + square[3][1],
        )
    )
