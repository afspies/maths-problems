"""Exact checks for the normalized four-parameter optimization in Steiner."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Surd73:
    """An exact number ``rational + coefficient*sqrt(73)``."""

    rational: Fraction
    coefficient: Fraction = Fraction(0)

    def __add__(self, other: "Surd73") -> "Surd73":
        return Surd73(
            self.rational + other.rational,
            self.coefficient + other.coefficient,
        )

    def __sub__(self, other: "Surd73") -> "Surd73":
        return Surd73(
            self.rational - other.rational,
            self.coefficient - other.coefficient,
        )

    def __mul__(self, other: "Surd73") -> "Surd73":
        return Surd73(
            self.rational * other.rational + 73 * self.coefficient * other.coefficient,
            self.rational * other.coefficient + self.coefficient * other.rational,
        )

    def scale(self, scalar: Fraction | int) -> "Surd73":
        return Surd73(self.rational * scalar, self.coefficient * scalar)


def steiner_terms(
    x1: Fraction, x2: Fraction, y1: Fraction, y2: Fraction
) -> tuple[Fraction, ...]:
    """The six normalized lower bounds in Steiner's Theorem 1.3 proof."""
    if not (0 <= x1 <= x2 <= 1 and 0 <= y1 <= y2 <= 1):
        raise ValueError("need 0 <= x1 <= x2 <= 1 and 0 <= y1 <= y2 <= 1")
    return (
        (2 - x1) / 3,
        (2 - y1) / 3,
        Fraction(3, 4) - x2 / 2,
        Fraction(3, 4) - y2 / 2,
        x1 + y2 * (1 - x1),
        y1 + x2 * (1 - y1),
    )


def steiner_lower_envelope(
    x1: Fraction, x2: Fraction, y1: Fraction, y2: Fraction
) -> Fraction:
    return max(steiner_terms(x1, x2, y1, y2))


def withdrawn_cps_term(A: int, B: int, x: int, y: int) -> int:
    """Correct expansion of A(B-y) + (A-x)y from the withdrawn paper."""
    return A * B - x * y


def withdrawn_claimed_term(A: int, B: int, x: int, y: int) -> int:
    """The false replacement used in equation (2.2) of arXiv:2607.01109v1."""
    return 3 * A * B - 2 * A * y - 2 * x * B + x * y


def steiner_exact_constants() -> tuple[Surd73, Surd73, Surd73]:
    """Return ``(c,a,b)`` used in the exact threshold proof."""
    c = Surd73(Fraction(5, 24), Fraction(1, 24))
    a = Surd73(Fraction(11, 8), Fraction(-1, 8))
    b = Surd73(Fraction(13, 12), Fraction(-1, 12))
    return c, a, b
