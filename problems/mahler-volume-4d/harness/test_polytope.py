import unittest
from fractions import Fraction

from polytope import (
    centered_simplex_4,
    cross_polytope_4,
    cube_4,
    pyramid_mahler_factor,
    pyramid_over_cube_3,
    simplex_volume,
)


class ExactPolytopeHarnessTests(unittest.TestCase):
    def test_simplex_polar_and_mahler_product(self):
        simplex = centered_simplex_4()
        polar = simplex.polar()
        self.assertEqual(
            simplex.incidence_summary(),
            {
                "f0": 5,
                "f3": 5,
                "f03": 20,
                "Delta": 4,
                "delta": 4,
                "facet_sizes": (4, 4, 4, 4, 4),
                "vertex_facet_degrees": (4, 4, 4, 4, 4),
            },
        )
        self.assertEqual(polar.incidence_summary(), simplex.incidence_summary())
        product = simplex_volume(simplex.vertices) * simplex_volume(polar.vertices)
        self.assertEqual(product, Fraction(3125, 576))
        for direction in ((1, 2, 3, 5), (1, 0, 0, 0)):
            self.assertEqual(simplex.admissible_dimension(direction), 5)
            self.assertEqual(simplex.trivial_dimension(), 5)

    def test_cube_cross_polar_incidence(self):
        cube = cube_4()
        polar = cube.polar()
        cross = cross_polytope_4()
        self.assertEqual(cube.incidence_summary()["facet_sizes"], (8,) * 8)
        self.assertEqual(cube.incidence_summary()["vertex_facet_degrees"], (4,) * 16)
        self.assertEqual(polar.incidence_summary(), cross.incidence_summary())
        self.assertEqual(polar.polar().incidence_summary(), cube.incidence_summary())

    def test_simplicial_cross_polytope_has_no_speed_constraints(self):
        cross = cross_polytope_4()
        self.assertEqual(cross.trivial_dimension(), 5)
        for direction in ((1, 2, 3, 5), (1, 0, 0, 0)):
            self.assertEqual(cross.admissible_matrix(direction), ())
            self.assertEqual(cross.admissible_dimension(direction), 8)

    def test_cube_is_rigid_generically_but_not_terminal(self):
        cube = cube_4()
        self.assertEqual(cube.admissible_dimension((1, 2, 3, 5)), 5)
        self.assertGreater(cube.admissible_dimension((1, 0, 0, 0)), 5)

    def test_pyramid_tangent_speed_dimension_matches_base_pattern(self):
        pyramid = pyramid_over_cube_3()
        summary = pyramid.incidence_summary()
        self.assertEqual(summary["f0"], 9)
        self.assertEqual(summary["facet_sizes"], (5, 5, 5, 5, 5, 5, 8))
        self.assertEqual(pyramid.admissible_dimension((1, 2, 3, 0)), 5)
        self.assertGreater(pyramid.admissible_dimension((1, 0, 0, 0)), 5)

    def test_pyramid_factor_transports_the_3d_sharp_constant(self):
        self.assertEqual(
            pyramid_mahler_factor(4) * Fraction(64, 9),
            Fraction(3125, 576),
        )


if __name__ == "__main__":
    unittest.main()
