import unittest
from fractions import Fraction

from induction_parameters import (
    balanced_scale_is_admissible,
    exact_scale_bounds,
    minimal_scale_count,
    planebrush_parameters_are_strict,
    plany_bracket_exponent,
    trilinear_budget_holds,
)


class InductionParameterTests(unittest.TestCase):
    def test_published_minimal_n_implication_is_false(self) -> None:
        epsilon_0 = Fraction(1, 10)
        n = minimal_scale_count(epsilon_0)
        self.assertEqual(n, 41)
        self.assertFalse(epsilon_0 < Fraction(2, n))
        self.assertTrue(exact_scale_bounds(epsilon_0, n))

    def test_epsilon_over_four_is_not_a_safe_trilinear_choice(self) -> None:
        epsilon_0 = Fraction(1, 10)
        n = minimal_scale_count(epsilon_0)
        epsilon_1 = Fraction(249, 10_000)  # < epsilon_0/4, but > 1/N
        self.assertLess(epsilon_1, epsilon_0 / 4)
        self.assertFalse(
            trilinear_budget_holds(epsilon_0, epsilon_1, Fraction(1, 100_000), n)
        )

    def test_epsilon_over_five_repairs_trilinear_budget(self) -> None:
        epsilon_0 = Fraction(1, 10)
        n = minimal_scale_count(epsilon_0)
        epsilon_1 = Fraction(19, 1_000)  # < epsilon_0/5 < 1/N
        eta_0 = Fraction(1, 100_000)
        self.assertTrue(trilinear_budget_holds(epsilon_0, epsilon_1, eta_0, n))

    def test_one_exact_repaired_plany_budget(self) -> None:
        epsilon_0 = Fraction(1, 10)
        n = minimal_scale_count(epsilon_0)
        sigma = Fraction(3, 4)
        epsilon_2 = Fraction(1, 10_000)
        eta_0 = Fraction(1, 2_000_000)
        exponent = plany_bracket_exponent(
            sigma=sigma,
            epsilon_2=epsilon_2,
            eta_j_minus_1=eta_0,
            eta_j=eta_0,
            eta_j_plus_1=eta_0,
            n=n,
        )
        self.assertLess(exponent, 0)

    def test_balanced_scale_interval_has_an_implicit_eta_constraint(self) -> None:
        self.assertTrue(balanced_scale_is_admissible(Fraction(1, 41), 40))
        self.assertFalse(balanced_scale_is_admissible(Fraction(1, 40), 40))

    def test_planebrush_parameters_must_be_strict(self) -> None:
        sigma_4 = Fraction(3, 4)
        self.assertFalse(planebrush_parameters_are_strict(sigma_4, Fraction(1)))
        self.assertTrue(
            planebrush_parameters_are_strict(sigma_4, Fraction(7, 8))
        )


if __name__ == "__main__":
    unittest.main()
