import unittest
from fractions import Fraction as F

from grain_union_ledger import (
    dyadic_harmonic_bound,
    distributed_catalog_load_exponent,
    harmonic_number,
    normalized_union_lower_bound,
    normalized_weighted_union_lower_bound,
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


if __name__ == "__main__":
    unittest.main()
