#!/usr/bin/env python3
"""Exact second-moment ledger for a one-parameter family of grains."""

from __future__ import annotations

from fractions import Fraction


def harmonic_number(m: int) -> Fraction:
    if m < 0:
        raise ValueError("m must be nonnegative")
    return sum((Fraction(1, k) for k in range(1, m + 1)), Fraction(0))


def dyadic_harmonic_bound(m: int) -> int:
    """An exact integer B with H_m <= B, proved by dyadic blocks."""
    if m < 0:
        raise ValueError("m must be nonnegative")
    if m == 0:
        return 0
    return 1 + (m.bit_length() - 1)


def normalized_union_lower_bound(
    *, carriers: int, delta: Fraction, shading_density: Fraction
) -> Fraction:
    """Second-moment lower bound under the normalized overlap ledger.

    Each carrier contributes at least lambda*delta.  Diagonal mass is at
    most delta per carrier.  For carriers i,j at index distance k, the
    overlap is at most delta^2*carriers/k.  Constants are normalized to one.
    """
    if carriers < 1:
        raise ValueError("carriers must be positive")
    if not 0 < delta <= 1:
        raise ValueError("expected 0 < delta <= 1")
    if not 0 < shading_density <= 1:
        raise ValueError("expected 0 < shading_density <= 1")

    total_mass_lower = carriers * shading_density * delta
    diagonal_upper = carriers * delta
    off_diagonal_upper = 2 * carriers * carriers * delta * delta * harmonic_number(
        carriers - 1
    )
    return total_mass_lower * total_mass_lower / (
        diagonal_upper + off_diagonal_upper
    )


def normalized_weighted_union_lower_bound(
    *, carrier_masses: list[Fraction], delta: Fraction
) -> Fraction:
    """Sparse-stack version with m_i in [0,1] and inner mass delta*m_i."""
    if not carrier_masses:
        raise ValueError("carrier_masses must be nonempty")
    if not 0 < delta <= 1:
        raise ValueError("expected 0 < delta <= 1")
    if any(not 0 <= mass <= 1 for mass in carrier_masses):
        raise ValueError("expected every carrier mass in [0,1]")
    carriers = len(carrier_masses)
    total_mass_lower = delta * sum(carrier_masses, Fraction(0))
    diagonal_upper = carriers * delta
    off_diagonal_upper = 2 * carriers * carriers * delta * delta * harmonic_number(
        carriers - 1
    )
    return total_mass_lower * total_mass_lower / (
        diagonal_upper + off_diagonal_upper
    )


def quadric_direction_capacity_exponents(
    shading_exponent: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return tube-capacity and required-carrier exponents.

    With lambda=delta^beta, one quadratic carrier holds at most
    delta^(-min(3,2+2 beta)) directions.  Covering delta^-3 directions
    therefore needs delta^(-max(0,1-2 beta)) carriers.
    """
    if not 0 <= shading_exponent:
        raise ValueError("shading exponent must be nonnegative")
    capacity = min(Fraction(3), Fraction(2) + 2 * shading_exponent)
    required_carriers = max(Fraction(0), Fraction(3) - capacity)
    return capacity, required_carriers


def quadratic_catalog_evasion_exponent(
    *,
    catalog_exponent: Fraction,
    tube_deficit_exponent: Fraction,
    overlap_exponent: Fraction,
    qw2_loss_exponent: Fraction,
) -> Fraction:
    """Power saving in the QW2 catalog-capacity lemma.

    M<=delta^-h, #T>=delta^(-3+tau), lambda=delta^a, and QW2 constant
    A<=delta^-b give carried fraction O(delta^(1-h-tau-4a-b)).
    """
    values = (
        catalog_exponent,
        tube_deficit_exponent,
        overlap_exponent,
        qw2_loss_exponent,
    )
    if any(value < 0 for value in values):
        raise ValueError("all loss exponents must be nonnegative")
    return (
        1
        - catalog_exponent
        - tube_deficit_exponent
        - 4 * overlap_exponent
        - qw2_loss_exponent
    )


def sticky_quadric_persistence_margin(
    *,
    mass_exponent: Fraction,
    catalog_exponent: Fraction,
    overlap_exponent: Fraction,
    scale_exponent: Fraction,
    sticky_loss: Fraction,
) -> Fraction:
    """LHS minus RHS in tau+zeta+2ell >= a(1-2epsilon)."""
    values = (
        mass_exponent,
        catalog_exponent,
        overlap_exponent,
        scale_exponent,
        sticky_loss,
    )
    if any(value < 0 for value in values):
        raise ValueError("all exponents must be nonnegative")
    return (
        mass_exponent
        + catalog_exponent
        + 2 * overlap_exponent
        - scale_exponent * (1 - 2 * sticky_loss)
    )


def distributed_catalog_load_exponent(
    *,
    tube_deficit_exponent: Fraction,
    catalog_exponent: Fraction,
    distributed_overlap_exponent: Fraction,
) -> Fraction:
    """Power of the QW2 load forced by distributed catalog coverage.

    N>=delta^(-3+tau), M<=delta^-h, q>=delta^s force
    Delta >= delta^(-(1-tau-4h-4s)), up to constants.
    """
    values = (
        tube_deficit_exponent,
        catalog_exponent,
        distributed_overlap_exponent,
    )
    if any(value < 0 for value in values):
        raise ValueError("all exponents must be nonnegative")
    return (
        1
        - tube_deficit_exponent
        - 4 * catalog_exponent
        - 4 * distributed_overlap_exponent
    )


def quadric_thinning_can_be_sticky_and_extremal(
    *, extremality_loss: Fraction, thinning_exponent: Fraction
) -> bool:
    """Check beta<=eta (mass) and beta>=1-eta (direction multiplicity)."""
    if not 0 <= extremality_loss or not 0 <= thinning_exponent:
        raise ValueError("exponents must be nonnegative")
    return (
        thinning_exponent <= extremality_loss
        and thinning_exponent >= 1 - extremality_loss
    )
