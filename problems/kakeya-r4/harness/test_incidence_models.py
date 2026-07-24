import unittest
from fractions import Fraction as F

from incidence_models import (
    normalized_wedge_squared,
    plany_model,
    quadric_line_coefficients,
    quadric_value,
    rank,
    ruled_quadric_lines,
    split_quadric_direction_derivatives,
    split_quadric_sweep,
    split_quadric_sweep_derivatives,
    trilinear_model,
    transverse_pencil_seed_derivatives,
    wedge_squared,
)


class IncidenceModelTests(unittest.TestCase):
    def test_plany_model_has_direction_rank_two(self) -> None:
        lines = plany_model()
        directions = [line.direction for line in lines]
        self.assertEqual(rank(directions), 2)
        self.assertEqual(wedge_squared(*directions), 0)

    def test_trilinear_model_has_nonzero_wedge(self) -> None:
        directions = [line.direction for line in trilinear_model()]
        self.assertEqual(rank(directions), 3)
        self.assertEqual(wedge_squared(*directions), 1)

    def test_ruled_quadric_lines_are_exact(self) -> None:
        lines = ruled_quadric_lines()
        for line in lines:
            self.assertEqual(
                quadric_line_coefficients(line), (F(1), F(0), F(0))
            )
            for t in (F(-3, 2), F(0), F(2, 3), F(5)):
                self.assertEqual(quadric_value(line.point(t)), 1)

    def test_ruled_quadric_can_be_pointwise_trilinear(self) -> None:
        directions = [line.direction for line in ruled_quadric_lines()]
        self.assertEqual(rank(directions), 3)
        self.assertEqual(wedge_squared(*directions), 4)
        self.assertEqual(normalized_wedge_squared(*directions), F(1, 50))

    def test_split_quadric_has_an_exact_two_parameter_line_sweep(self) -> None:
        for p, q in ((F(0), F(0)), (F(1, 3), F(-2, 5)), (F(2), F(3))):
            for t in (F(1), F(3, 2), F(2)):
                self.assertEqual(quadric_value(split_quadric_sweep(p, q, t)), 1)

    def test_split_quadric_sweep_and_direction_maps_have_full_rank(self) -> None:
        p, q, t = F(1, 3), F(-2, 5), F(3, 2)
        self.assertEqual(rank(list(split_quadric_sweep_derivatives(p, q, t))), 3)
        self.assertEqual(rank(list(split_quadric_direction_derivatives(p, q))), 3)

    def test_explicit_transverse_pencil_sweep_has_rank_four(self) -> None:
        self.assertEqual(rank(transverse_pencil_seed_derivatives()), 4)


if __name__ == "__main__":
    unittest.main()
