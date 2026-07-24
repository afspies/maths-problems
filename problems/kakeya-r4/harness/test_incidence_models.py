import unittest
from fractions import Fraction as F

from incidence_models import (
    bivector_squared,
    determinant,
    normalized_wedge_squared,
    plany_model,
    quadric_line_coefficients,
    quadric_value,
    rank_three_parabolic_gradient,
    rank_three_parabolic_line_directions,
    rank_three_parabolic_line_point,
    rank_three_parabolic_value,
    rank_two_separated_coefficient_difference,
    rank_two_separated_direction_chart_seed,
    rank_two_separated_line_direction,
    rank_two_separated_null_direction,
    rank_two_separated_parabolic_line,
    rank_two_separated_parabolic_value,
    rank_two_separated_sweep_seed_derivatives,
    rank,
    ruled_quadric_lines,
    rotating_rank_one_moment_matrix,
    split_quadric_direction_derivatives,
    split_quadric_sweep,
    split_quadric_sweep_derivatives,
    trilinear_model,
    transverse_pencil_seed_derivatives,
    vec,
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

    def test_rank_three_parabolic_pencil_is_pointwise_trilinear(self) -> None:
        for s in (F(1), F(3, 2), F(2)):
            directions = rank_three_parabolic_line_directions(s)
            self.assertEqual(rank(directions), 3)
            for direction in directions:
                for t in (F(-1), F(0), F(2, 3)):
                    point = rank_three_parabolic_line_point(direction, t)
                    self.assertEqual(rank_three_parabolic_value(point, s), 0)

    def test_rank_three_pencil_normal_wedge_has_exact_degeneracy_factor(self) -> None:
        x = vec((F(1, 3), F(-2, 5), F(3, 7), F(0)))
        s, t = F(1), F(7, 4)
        left = bivector_squared(
            rank_three_parabolic_gradient(x, s),
            rank_three_parabolic_gradient(x, t),
        )
        # |grad P_s wedge grad P_t|^2 =
        # 4(s-t)^2*x3^2*|grad P_s wedge e3|^2.
        e_3 = vec((0, 0, 1, 0))
        right = (
            4
            * (s - t) ** 2
            * x[2] ** 2
            * bivector_squared(rank_three_parabolic_gradient(x, s), e_3)
        )
        self.assertEqual(left, right)

    def test_rank_two_separated_parabolic_lines_are_exact(self) -> None:
        for s in (F(0), F(1, 3), F(1)):
            for q, r in ((F(0), F(1, 2)), (F(2, 3), F(-1, 4))):
                u = rank_two_separated_null_direction(s, q)
                a = (1 + s) ** 2
                self.assertEqual(a * (u[0] ** 2 + u[2] ** 2) - u[1] ** 2, 0)
                for t in (F(-1), F(0), F(3, 5)):
                    point = rank_two_separated_parabolic_line(s, q, r, t)
                    self.assertEqual(rank_two_separated_parabolic_value(point, s), 0)
                point_0 = rank_two_separated_parabolic_line(s, q, r, F(0))
                point_1 = rank_two_separated_parabolic_line(s, q, r, F(1))
                self.assertEqual(
                    tuple(
                        b - a
                        for a, b in zip(point_0, point_1, strict=True)
                    ),
                    rank_two_separated_line_direction(s, q, r),
                )

    def test_rank_two_separated_family_has_full_direction_chart(self) -> None:
        direction_seed = rank_two_separated_direction_chart_seed()
        sweep_seed = rank_two_separated_sweep_seed_derivatives()
        self.assertEqual(rank(direction_seed), 4)
        self.assertEqual(rank(sweep_seed), 4)
        self.assertEqual(abs(determinant(direction_seed)), 4)
        self.assertEqual(abs(determinant(sweep_seed)), 4)

    def test_parabolic_coefficient_path_has_rank_two_separation(self) -> None:
        self.assertEqual(
            rank(rank_two_separated_coefficient_difference(F(1, 4), F(3, 4))),
            2,
        )

    def test_rotating_rank_one_tangent_acquires_rank_two_only_cubically(self) -> None:
        h = F(2, 5)
        matrix = rotating_rank_one_moment_matrix(h)
        self.assertEqual(rank(matrix), 2)
        principal_determinant = (
            matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        )
        self.assertEqual(principal_determinant, h**4 / 12)


if __name__ == "__main__":
    unittest.main()
