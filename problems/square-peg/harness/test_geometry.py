from fractions import Fraction
import unittest

from geometry import (
    is_simple_polygon,
    liouville_primitive,
    point,
    signed_double_area,
    subdivide,
    verify_inscribed_square,
)


class GeometryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.unit_square = [
            point(0, 0),
            point(1, 0),
            point(1, 1),
            point(0, 1),
        ]

    def test_known_simple_polygon_and_square(self) -> None:
        self.assertTrue(is_simple_polygon(self.unit_square))
        self.assertTrue(verify_inscribed_square(self.unit_square, self.unit_square))

    def test_crossing_and_degenerate_polygons_rejected(self) -> None:
        bow_tie = [point(0, 0), point(1, 1), point(0, 1), point(1, 0)]
        self.assertFalse(is_simple_polygon(bow_tie))
        self.assertFalse(
            is_simple_polygon([point(0, 0), point(1, 0), point(1, 0)])
        )

    def test_shoelace_and_liouville_sign(self) -> None:
        primitive = liouville_primitive(self.unit_square)
        self.assertEqual(signed_double_area(self.unit_square), 2)
        # For counterclockwise orientation, integral y dx = -area.
        self.assertEqual(primitive[-1], -1)

    def test_subdivision_preserves_total_primitive_and_old_values(self) -> None:
        refined = subdivide(
            self.unit_square, cuts=(Fraction(1, 3), Fraction(2, 3))
        )
        self.assertTrue(is_simple_polygon(refined))
        coarse_f = liouville_primitive(self.unit_square)
        refined_f = liouville_primitive(refined)
        self.assertEqual(refined_f[-1], coarse_f[-1])
        self.assertEqual([refined_f[3 * i] for i in range(4)], coarse_f[:4])

    def test_non_square_boundary_quad_rejected(self) -> None:
        rectangle = [point(0, 0), point(1, 0), point(1, 1), point(0, 1)]
        bad = [
            point(0, 0),
            point(1, 0),
            point(1, Fraction(1, 2)),
            point(0, Fraction(1, 2)),
        ]
        self.assertFalse(verify_inscribed_square(rectangle, bad))


if __name__ == "__main__":
    unittest.main()
