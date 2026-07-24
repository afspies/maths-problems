import unittest
from fractions import Fraction as F

from grain_union_ledger import (
    assigned_catalog_required_carrier_exponent,
    dyadic_harmonic_bound,
    distributed_catalog_load_exponent,
    hausdorff_cover_cost_lower_bound,
    harmonic_number,
    high_multiplicity_incidence_fraction,
    inverse_tangency_mass_lower_bound,
    normalized_union_lower_bound,
    normalized_weighted_union_lower_bound,
    rank_two_parabolic_stack_union_lower_bound,
    transverse_parent_ancestry_error,
    quadratic_catalog_evasion_exponent,
    quadric_thinning_can_be_sticky_and_extremal,
    quadric_direction_capacity_exponents,
    sticky_quadric_persistence_margin,
)


class GrainUnionLedgerTests(unittest.TestCase):
    def test_dyadic_bound_dominates_harmonic_number_exactly(self) -> None:
        for m in range(0, 257):
            self.assertLessEqual(harmonic_number(m), dyadic_harmonic_bound(m))

    def test_delta_inverse_carriers_leave_only_a_harmonic_loss(self) -> None:
        for m in (2, 4, 16, 64):
            lower = normalized_union_lower_bound(
                carriers=m, delta=F(1, m), shading_density=F(1)
            )
            expected = F(1, 1 + 2 * harmonic_number(m - 1))
            self.assertEqual(lower, expected)
            self.assertGreaterEqual(
                lower, F(1, 1 + 2 * dyadic_harmonic_bound(m - 1))
            )

    def test_shading_cost_is_exactly_quadratic_in_the_ledger(self) -> None:
        m = 32
        full = normalized_union_lower_bound(
            carriers=m, delta=F(1, m), shading_density=F(1)
        )
        half = normalized_union_lower_bound(
            carriers=m, delta=F(1, m), shading_density=F(1, 2)
        )
        self.assertEqual(half, full / 4)

    def test_weighted_sparse_ledger_recovers_uniform_case(self) -> None:
        m = 16
        density = F(3, 5)
        uniform = normalized_union_lower_bound(
            carriers=m, delta=F(1, m), shading_density=density
        )
        weighted = normalized_weighted_union_lower_bound(
            carrier_masses=[density] * m, delta=F(1, m)
        )
        self.assertEqual(weighted, uniform)

    def test_quadric_direction_capacity_and_carrier_count(self) -> None:
        self.assertEqual(
            quadric_direction_capacity_exponents(F(0)), (F(2), F(1))
        )
        self.assertEqual(
            quadric_direction_capacity_exponents(F(1, 4)),
            (F(5, 2), F(1, 2)),
        )
        self.assertEqual(
            quadric_direction_capacity_exponents(F(1, 2)), (F(3), F(0))
        )

    def test_quadratic_catalog_evasion_budget(self) -> None:
        self.assertEqual(
            quadratic_catalog_evasion_exponent(
                catalog_exponent=F(1, 4),
                tube_deficit_exponent=F(1, 10),
                overlap_exponent=F(1, 20),
                qw2_loss_exponent=F(1, 20),
            ),
            F(2, 5),
        )
        self.assertLess(
            quadratic_catalog_evasion_exponent(
                catalog_exponent=F(3, 4),
                tube_deficit_exponent=F(1, 10),
                overlap_exponent=F(1, 20),
                qw2_loss_exponent=F(0),
            ),
            0,
        )

    def test_low_entropy_sticky_quadric_output_can_be_impossible(self) -> None:
        rejected = sticky_quadric_persistence_margin(
            mass_exponent=F(1, 20),
            catalog_exponent=F(1, 20),
            overlap_exponent=F(0),
            scale_exponent=F(1, 2),
            sticky_loss=F(1, 100),
        )
        self.assertLess(rejected, 0)
        boundary = sticky_quadric_persistence_margin(
            mass_exponent=F(49, 200),
            catalog_exponent=F(49, 200),
            overlap_exponent=F(0),
            scale_exponent=F(1, 2),
            sticky_loss=F(1, 100),
        )
        self.assertEqual(boundary, 0)

    def test_distributed_catalog_load_has_fourth_power_entropy_cost(self) -> None:
        self.assertEqual(
            distributed_catalog_load_exponent(
                tube_deficit_exponent=F(1, 10),
                catalog_exponent=F(1, 20),
                distributed_overlap_exponent=F(1, 40),
            ),
            F(3, 5),
        )

    def test_quadric_thinning_cannot_repair_small_eta_stickiness(self) -> None:
        eta = F(1, 10)
        for beta in (F(0), F(1, 10), F(1, 2), F(9, 10), F(1)):
            self.assertFalse(
                quadric_thinning_can_be_sticky_and_extremal(
                    extremality_loss=eta, thinning_exponent=beta
                )
            )
        self.assertTrue(
            quadric_thinning_can_be_sticky_and_extremal(
                extremality_loss=F(1, 2), thinning_exponent=F(1, 2)
            )
        )

    def test_small_union_extracts_high_incidence_mass_only(self) -> None:
        threshold, retained = high_multiplicity_incidence_fraction(
            total_incidence=F(3, 5), union_volume=F(1, 10)
        )
        self.assertEqual(threshold, F(3))
        self.assertEqual(retained, F(3, 10))

    def test_assigned_catalog_pays_linear_not_fourth_power_entropy(self) -> None:
        self.assertEqual(
            assigned_catalog_required_carrier_exponent(
                tube_deficit_exponent=F(1, 20),
                retained_fraction_exponent=F(1, 20),
                overlap_exponent=F(1, 40),
                qw2_loss_exponent=F(1, 20),
            ),
            F(3, 4),
        )

    def test_small_stack_union_forces_low_jacobian_pair_mass(self) -> None:
        lower = inverse_tangency_mass_lower_bound(
            carriers=16,
            delta=F(1, 16),
            shading_density=F(1),
            union_volume=F(1, 8),
            jacobian_threshold=F(1),
        )
        self.assertEqual(lower, F(97, 16))
        self.assertGreater(lower, 0)

    def test_fixed_stack_cover_cost_diverges_at_subcritical_dimension(self) -> None:
        # s=3 makes 4-s=1.  For dyadic r<=2^-k0 and logarithmic
        # L(r)=k+1, the scale sum tends to zero as k0 grows.
        def bound(k0: int) -> F:
            radii = [F(1, 2**k) for k in range(k0, k0 + 20)]
            losses = [F(k + 1) for k in range(k0, k0 + 20)]
            return hausdorff_cover_cost_lower_bound(
                total_line_incidence=F(1),
                radii=radii,
                losses=losses,
                dimension=F(3),
            )

        self.assertGreater(bound(20), bound(10))

    def test_rank_two_parabolic_stack_pays_only_two_harmonic_factors(self) -> None:
        lower = rank_two_parabolic_stack_union_lower_bound(
            carriers=8,
            delta=F(1, 8),
            shading_density=F(1, 2),
        )
        self.assertEqual(lower, F(1, 4) / (1 + harmonic_number(8) ** 2))
        self.assertGreater(lower, 0)
        with self.assertRaisesRegex(ValueError, "critical spacing"):
            rank_two_parabolic_stack_union_lower_bound(
                carriers=8,
                delta=F(1, 16),
                shading_density=F(1, 2),
            )

    def test_parent_ancestry_prevents_descendant_baseline_multiplication(self) -> None:
        self.assertEqual(
            transverse_parent_ancestry_error(
                parent_labels_per_line=2,
                polynomial_degree=3,
                scale=F(1, 1024),
                derivative_threshold=F(1, 8),
            ),
            F(3, 64),
        )


if __name__ == "__main__":
    unittest.main()
