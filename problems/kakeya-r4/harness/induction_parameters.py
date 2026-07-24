#!/usr/bin/env python3
"""Exact checks for the scale parameters in Rai Choudhuri, Section 6.

The arXiv v1 proof chooses N minimally with 4/N < epsilon_0 and then states
epsilon_0 < 2/N.  That implication is false.  The exact useful bounds are

    epsilon_0/(4+epsilon_0) <= 1/N < epsilon_0/4.

For 0 < epsilon_0 < 1 this gives the convenient 1/N >= epsilon_0/5.
"""

from __future__ import annotations

from fractions import Fraction


def minimal_scale_count(epsilon_0: Fraction) -> int:
    if not 0 < epsilon_0 < 1:
        raise ValueError("expected 0 < epsilon_0 < 1")
    n = 1
    while Fraction(4, n) >= epsilon_0:
        n += 1
    return n


def exact_scale_bounds(epsilon_0: Fraction, n: int) -> bool:
    return (
        Fraction(4, n) < epsilon_0
        and (n == 1 or Fraction(4, n - 1) >= epsilon_0)
        and epsilon_0 / (4 + epsilon_0) <= Fraction(1, n)
        and Fraction(1, n) < epsilon_0 / 4
        and epsilon_0 / 5 < Fraction(1, n)
    )


def trilinear_budget_holds(
    epsilon_0: Fraction,
    epsilon_1: Fraction,
    eta_0: Fraction,
    n: int,
) -> bool:
    """Check the two losses assigned one factor delta^(1/N) each."""
    return 14 * eta_0 <= Fraction(1, n) and epsilon_1 <= Fraction(1, n)


def balanced_scale_is_admissible(eta_j: Fraction, j: int) -> bool:
    """Check rho is in [delta_tilde^(1-eta_j), delta_tilde^eta_j].

    Here rho=delta^(1/N), delta_tilde=delta^((j+1)/N), and 0<delta<1.
    The two endpoint comparisons reduce to eta_j <= j/(j+1) and
    eta_j <= 1/(j+1).
    """
    if j < 1:
        raise ValueError("j must be positive")
    return 0 < eta_j <= Fraction(1, j + 1)


def planebrush_parameters_are_strict(
    robust_exponent: Fraction, weakened_two_ends_exponent: Fraction
) -> bool:
    """Theorem 5.5 requires 0<epsilon_2<epsilon_1<1."""
    return 0 < robust_exponent < weakened_two_ends_exponent < 1


def plany_bracket_exponent(
    *,
    sigma: Fraction,
    epsilon_2: Fraction,
    eta_j_minus_1: Fraction,
    eta_j: Fraction,
    eta_j_plus_1: Fraction,
    n: int,
) -> Fraction:
    """Exact delta exponent of the bracket in equation (6.??)/brackineq."""
    rho_exponent = (
        -Fraction(1, 12)
        + 23 * (eta_j + eta_j_minus_1) / sigma
        + epsilon_2
    )
    delta_exponent = 24 * eta_j_plus_1 + 3 * eta_j
    return rho_exponent / n + delta_exponent
