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


def high_multiplicity_incidence_fraction(
    *, total_incidence: Fraction, union_volume: Fraction
) -> tuple[Fraction, Fraction]:
    """Threshold and guaranteed incidence mass in the high-multiplicity set.

    If m is supported on a set of volume V and integral m=A, then
    {m >= A/(2V)} carries at least A/2 incidence mass.
    """
    if total_incidence <= 0 or union_volume <= 0:
        raise ValueError("incidence and volume must be positive")
    return (
        total_incidence / (2 * union_volume),
        total_incidence / 2,
    )


def assigned_catalog_required_carrier_exponent(
    *,
    tube_deficit_exponent: Fraction,
    overlap_exponent: Fraction,
    qw2_loss_exponent: Fraction,
    retained_fraction_exponent: Fraction = Fraction(0),
) -> Fraction:
    """Exponent h forced in M >= delta^-h for assigned carrier incidences.

    With N>=delta^(-3+tau), retained fraction f>=delta^g,
    overlap lambda>=delta^a, and QW2 loss A<=delta^-b:

        M >= delta^(-1+tau+g+4a+b)
          = delta^(-(1-tau-g-4a-b)).
    """
    values = (
        tube_deficit_exponent,
        overlap_exponent,
        qw2_loss_exponent,
        retained_fraction_exponent,
    )
    if any(value < 0 for value in values):
        raise ValueError("all loss exponents must be nonnegative")
    return max(
        Fraction(0),
        1
        - tube_deficit_exponent
        - retained_fraction_exponent
        - 4 * overlap_exponent
        - qw2_loss_exponent,
    )


def inverse_tangency_mass_lower_bound(
    *,
    carriers: int,
    delta: Fraction,
    shading_density: Fraction,
    union_volume: Fraction,
    jacobian_threshold: Fraction,
) -> Fraction:
    """Normalized lower bound for low-Jacobian ordered pair mass.

    Normalizations:
      |U_i| >= lambda*delta and |U_i| <= delta;
      each ordered pair's region with two-Jacobian >= theta has volume
      at most delta^2/theta.
    """
    if carriers < 1:
        raise ValueError("carriers must be positive")
    values = (delta, shading_density, union_volume, jacobian_threshold)
    if any(value <= 0 for value in values):
        raise ValueError("all scale parameters must be positive")
    total_mass = carriers * shading_density * delta
    second_moment_lower = total_mass * total_mass / union_volume
    diagonal_upper = carriers * delta
    transverse_pair_upper = (
        carriers * (carriers - 1) * delta * delta / jacobian_threshold
    )
    return max(
        Fraction(0),
        second_moment_lower - diagonal_upper - transverse_pair_upper,
    )


def hausdorff_cover_cost_lower_bound(
    *,
    total_line_incidence: Fraction,
    radii: list[Fraction],
    losses: list[Fraction],
    dimension: Fraction,
) -> Fraction:
    """Cauchy lower bound for the fixed-stack Hausdorff covering lemma.

    If the scale-r sublevel estimate is |N_r(V)| >= A(V)^2/L(r), then
    every cover has s-cost at least

        total_line_incidence^2 / sum_r r^(4-s)L(r).

    Fractional powers are deliberately unsupported: the exact harness uses
    integer 4-s, while the proof note handles arbitrary real s<4.
    """
    if total_line_incidence <= 0:
        raise ValueError("total incidence must be positive")
    if len(radii) != len(losses) or not radii:
        raise ValueError("radii and losses must be nonempty and equally sized")
    exponent = Fraction(4) - dimension
    if exponent.denominator != 1 or exponent < 0:
        raise ValueError("exact harness requires nonnegative integer 4-s")
    power = exponent.numerator
    if any(not 0 < radius <= 1 for radius in radii):
        raise ValueError("radii must lie in (0,1]")
    if any(loss <= 0 for loss in losses):
        raise ValueError("losses must be positive")
    scale_sum = sum(
        (radius**power) * loss
        for radius, loss in zip(radii, losses, strict=True)
    )
    return total_line_incidence * total_line_incidence / scale_sum


def rank_two_parabolic_stack_union_lower_bound(
    *,
    carriers: int,
    delta: Fraction,
    shading_density: Fraction,
) -> Fraction:
    """Exact ledger for a rank-two-separated parabolic stack.

    A quadratic sublevel estimate costs one harmonic factor and summing over
    carrier separation costs a second.  At the critical spacing
    M*delta = 1, the normalized second-moment conclusion is

        |union U_i| >= lambda^2 (M*delta) / (1 + H_M^2).

    The analytic theorem absorbs absolute geometric constants.
    """
    if carriers < 1:
        raise ValueError("carriers must be positive")
    if not 0 < delta <= 1:
        raise ValueError("delta must lie in (0,1]")
    if not 0 < shading_density <= 1:
        raise ValueError("shading density must lie in (0,1]")
    if carriers * delta != 1:
        raise ValueError("ledger certifies the critical spacing M*delta = 1")
    harmonic = harmonic_number(carriers)
    return (
        shading_density
        * shading_density
        * carriers
        * delta
        / (1 + harmonic * harmonic)
    )


def transverse_parent_ancestry_error(
    *,
    parent_labels_per_line: int,
    polynomial_degree: int,
    scale: Fraction,
    derivative_threshold: Fraction,
) -> Fraction:
    """Longitudinal error from transverse crossings of parent wall sublevels.

    A degree-D restriction to a line spends O(D*r/alpha) parameter length in
    {|P|<=r, |dP/dt|>=alpha}.  If a line meets descendants from at most K
    distinct parent polynomials, descendant multiplicity does not change the
    union-length bound:

        error <= K*D*r/alpha.

    Absolute geometric constants are omitted from this exact ledger.
    """
    if parent_labels_per_line < 1 or polynomial_degree < 1:
        raise ValueError("parent count and degree must be positive")
    if not 0 < scale <= 1 or derivative_threshold <= 0:
        raise ValueError("scale and derivative threshold must be positive")
    return (
        parent_labels_per_line
        * polynomial_degree
        * scale
        / derivative_threshold
    )


def cubic_ssi_cover_cost_lower_bound(
    *,
    total_line_incidence: Fraction,
    radii: list[Fraction],
    square_root_losses: list[Fraction],
    dimension: Fraction,
) -> Fraction:
    """Exact Hausdorff ledger for |N_r(V)| >= A(V)^3/L(r).

    Holder with exponents 3 and 3/2 gives

      cost >= A_total^3 /
        (sum_r r^((4-s)/2) sqrt(L(r)))^2.

    The exact harness accepts only integer (4-s)/2 and takes sqrt(L) as an
    explicit rational input.  The analytic proof treats every real s<4.
    """
    if total_line_incidence <= 0:
        raise ValueError("total incidence must be positive")
    if (
        len(radii) != len(square_root_losses)
        or not radii
    ):
        raise ValueError(
            "radii and square-root losses must be nonempty and equally sized"
        )
    exponent = (Fraction(4) - dimension) / 2
    if exponent.denominator != 1 or exponent < 0:
        raise ValueError("exact harness requires nonnegative integer (4-s)/2")
    power = exponent.numerator
    if any(not 0 < radius <= 1 for radius in radii):
        raise ValueError("radii must lie in (0,1]")
    if any(loss <= 0 for loss in square_root_losses):
        raise ValueError("square-root losses must be positive")
    scale_sum = sum(
        (radius**power) * loss
        for radius, loss in zip(radii, square_root_losses, strict=True)
    )
    return total_line_incidence**3 / (scale_sum**2)


def dyadic_partition_parent_walls(depth: int) -> int:
    """Distinct internal dyadic walls through depth L on the unit interval."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return 2**depth - 1


def one_shot_transverse_tail_margin(
    *, dimension: Fraction, derivative_threshold_exponent: Fraction
) -> Fraction:
    """Numerator of the one-shot dyadic tail exponent.

    With alpha=r^epsilon, Holder produces the scale weight

      r^((4-s-4 epsilon)/3).

    The tail is summable exactly when this returned numerator is positive.
    """
    if not 0 <= dimension < 4:
        raise ValueError("dimension must lie in [0,4)")
    if derivative_threshold_exponent < 0:
        raise ValueError("threshold exponent must be nonnegative")
    return 4 - dimension - 4 * derivative_threshold_exponent
