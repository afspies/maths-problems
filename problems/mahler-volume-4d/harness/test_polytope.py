import unittest
from fractions import Fraction

from polytope import (
    cell_24,
    centered_simplex_4,
    cross_polytope_4,
    cube_4,
    inverse,
    paffenholz_24_cell,
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

    def test_direction_flat_enumeration_matches_known_examples(self):
        simplex = centered_simplex_4()
        self.assertEqual(
            {case["dimension"] for case in simplex.direction_flat_dimensions()},
            {5},
        )
        cube = cube_4()
        self.assertEqual(
            min(case["dimension"] for case in cube.direction_flat_dimensions()),
            5,
        )
        self.assertGreater(
            max(case["dimension"] for case in cube.direction_flat_dimensions()),
            5,
        )

    def test_24_cell_incidence_and_polar(self):
        polytope = cell_24()
        expected = {
            "f0": 24,
            "f3": 24,
            "f03": 144,
            "Delta": 6,
            "delta": 6,
            "facet_sizes": (6,) * 24,
            "vertex_facet_degrees": (6,) * 24,
        }
        self.assertEqual(polytope.incidence_summary(), expected)
        self.assertEqual(polytope.polar().incidence_summary(), expected)

    def test_exact_pulling_volumes_and_centroids(self):
        simplex = centered_simplex_4()
        self.assertEqual(simplex.volume_and_centroid()[0], simplex_volume(simplex.vertices))
        self.assertEqual(simplex.volume_and_centroid()[1], (0, 0, 0, 0))
        self.assertEqual(cube_4().volume_and_centroid(), (16, (0, 0, 0, 0)))
        self.assertEqual(
            cross_polytope_4().volume_and_centroid(),
            (Fraction(2, 3), (0, 0, 0, 0)),
        )
        cube_volume, cube_centroid, cube_covariance = (
            cube_4().volume_centroid_covariance()
        )
        self.assertEqual((cube_volume, cube_centroid), (16, (0, 0, 0, 0)))
        self.assertEqual(
            cube_covariance,
            tuple(
                tuple(Fraction(int(row == column), 3) for column in range(4))
                for row in range(4)
            ),
        )
        self.assertEqual(
            inverse(((2, 1), (1, 1))),
            ((1, -1), (-1, 2)),
        )

    def test_paffenholz_realization_has_24_cell_incidence(self):
        polytope = paffenholz_24_cell()
        self.assertEqual(polytope.incidence_summary()["facet_sizes"], (6,) * 24)
        self.assertEqual(polytope.incidence_summary()["vertex_facet_degrees"], (6,) * 24)
        regular_family_member = paffenholz_24_cell((0, 0, 0, 0))
        self.assertEqual(
            tuple(incident for incident, _, _ in polytope.facets),
            tuple(incident for incident, _, _ in regular_family_member.facets),
        )
        self.assertEqual(
            polytope.volume_and_centroid(),
            polytope.facet_cone_volume_and_centroid(),
        )


if __name__ == "__main__":
    unittest.main()
