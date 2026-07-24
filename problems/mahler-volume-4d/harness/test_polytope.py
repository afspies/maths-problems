import unittest
from fractions import Fraction

from polytope import (
    cell_24,
    centered_hypersimplex_2_5,
    centered_simplex_4,
    cone_duality_defect_laplacian,
    cross_polytope_4,
    cube_4,
    full_rank_24_cell,
    full_rank_24_cell_invariants,
    hypersimplex_2_m_covariance_trace,
    inverse,
    join_covariance_trace,
    join_mahler_factor,
    join_segment_square_4,
    nullspace,
    paffenholz_24_cell,
    product_free_sum_mahler_factor,
    product_free_sum_covariance_trace,
    pyramid_mahler_factor,
    pyramid_over_cube_3,
    rank,
    simplex_volume,
)
from variation import (
    boundary_trace_deficit,
    constrained_reduced_log_bilinear,
    incidence_kkt_multiplier,
    incidence_stress_bilinear,
    incidence_stress_quadratic,
    incidence_tangent_and_stress_bases,
    incidence_tangent_dimension,
    incidence_tangent_matrix,
    paffenholz_parameter_path,
    paired_tangent_from_vertex_path,
    projective_orbit_tangent_vectors,
    projective_vertex_path,
    reduced_log_mahler_second,
    second_order_incidence_rhs,
    simplex_pair_energy,
    triangulation_slack_mass_trace,
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

    def test_product_free_sum_and_join_factors(self):
        triangle_product = Fraction(27, 4)
        segment_product = Fraction(4)
        tetrahedron_product = Fraction(64, 9)
        self.assertEqual(
            product_free_sum_mahler_factor(2, 2) * triangle_product**2,
            Fraction(243, 32),
        )
        self.assertEqual(
            product_free_sum_mahler_factor(1, 3)
            * segment_product
            * tetrahedron_product,
            Fraction(64, 9),
        )
        self.assertEqual(
            join_mahler_factor(1, 2)
            * segment_product
            * triangle_product,
            Fraction(3125, 576),
        )
        self.assertEqual(
            join_mahler_factor(0, 3) * tetrahedron_product,
            Fraction(3125, 576),
        )
        joined = join_segment_square_4()
        self.assertEqual(joined.volume_and_centroid()[1], (0, 0, 0, 0))
        self.assertEqual(joined.polar().volume_and_centroid()[1], (0, 0, 0, 0))
        self.assertEqual(
            joined.volume_and_centroid()[0]
            * joined.polar().volume_and_centroid()[0],
            join_mahler_factor(1, 2) * segment_product * Fraction(8),
        )

    def test_product_free_sum_and_join_covariance_trace_factors(self):
        segment_trace = Fraction(1, 9)
        triangle_trace = Fraction(1, 8)
        square_trace = Fraction(1, 9)
        self.assertEqual(
            join_covariance_trace(
                1, 2, segment_trace, triangle_trace
            ),
            Fraction(1, 9),
        )
        self.assertEqual(
            join_covariance_trace(
                1, 2, segment_trace, square_trace
            ),
            Fraction(17, 162),
        )
        joined = join_segment_square_4()
        _, _, joined_covariance = joined.volume_centroid_covariance()
        _, _, joined_polar_covariance = (
            joined.polar().volume_centroid_covariance()
        )
        self.assertEqual(
            sum(
                joined_covariance[row][column]
                * joined_polar_covariance[column][row]
                for row in range(4)
                for column in range(4)
            ),
            Fraction(17, 162),
        )
        self.assertEqual(
            product_free_sum_covariance_trace(
                1, 2, segment_trace, square_trace
            ),
            Fraction(1, 10),
        )

    def test_cone_duality_defect_laplacian(self):
        self.assertEqual(cone_duality_defect_laplacian(4, Fraction(1, 9)), 0)
        self.assertEqual(
            cone_duality_defect_laplacian(4, Fraction(169, 1800)),
            Fraction(-31, 50),
        )
        boundary_deficit = Fraction(1, 4) - Fraction(9, 4) * Fraction(
            169, 1800
        )
        self.assertEqual(
            cone_duality_defect_laplacian(4, Fraction(169, 1800)),
            -16 * boundary_deficit,
        )

    def test_hypersimplex_trace_formula_and_concentration_no_go(self):
        hypersimplex = centered_hypersimplex_2_5()
        polar = hypersimplex.polar()
        _, primal_center, primal_covariance = (
            hypersimplex.volume_centroid_covariance()
        )
        _, polar_center, polar_covariance = polar.volume_centroid_covariance()
        geometric_trace = sum(
            primal_covariance[row][column]
            * polar_covariance[column][row]
            for row in range(4)
            for column in range(4)
        )
        self.assertEqual(primal_center, (0, 0, 0, 0))
        self.assertEqual(polar_center, (0, 0, 0, 0))
        self.assertEqual(geometric_trace, Fraction(667, 7128))
        self.assertEqual(hypersimplex_2_m_covariance_trace(5), geometric_trace)
        self.assertEqual(
            cone_duality_defect_laplacian(4, geometric_trace),
            Fraction(-125, 198),
        )
        self.assertEqual(
            {case["dimension"] for case in hypersimplex.direction_flat_dimensions()},
            {5, 6},
        )
        self.assertEqual(
            {case["dimension"] for case in polar.direction_flat_dimensions()},
            {5, 6},
        )

        ten_dimensional_trace = hypersimplex_2_m_covariance_trace(11)
        self.assertEqual(ten_dimensional_trace, Fraction(51389, 738477))
        self.assertEqual(
            ten_dimensional_trace - Fraction(5, 72),
            Fraction(847, 5907816),
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

    def test_santalo_reduced_second_variation_sanity_checks(self):
        polytope = paffenholz_24_cell((0, 0, 0, 0))
        scaling = reduced_log_mahler_second(
            polytope,
            polytope.vertices,
        )
        self.assertEqual(scaling["reduced"], 0)
        self.assertEqual(scaling["santalo_correction"], 0)

        first, second = projective_vertex_path(polytope, (1, 0, 0, 0))
        projective = reduced_log_mahler_second(polytope, first, second)
        self.assertEqual(projective["unreduced"], 13)
        self.assertEqual(projective["santalo_correction"], Fraction(200, 13))
        self.assertEqual(projective["reduced"], Fraction(-31, 13))
        self.assertEqual(projective["polar_centroid_first"], (1, 0, 0, 0))

        parameter_first, parameter_second = paffenholz_parameter_path(
            (1, 0, 0, 0)
        )
        parameter = reduced_log_mahler_second(
            polytope, parameter_first, parameter_second
        )
        self.assertEqual(parameter["first"], 0)
        self.assertEqual(parameter["unreduced"], Fraction(-5, 24))
        self.assertEqual(
            parameter["santalo_correction"], Fraction(49, 936)
        )
        self.assertEqual(parameter["reduced"], Fraction(-61, 234))
        for coordinate in range(1, 4):
            direction = [0, 0, 0, 0]
            direction[coordinate] = 1
            unit_first, unit_second = paffenholz_parameter_path(direction)
            unit = reduced_log_mahler_second(
                polytope, unit_first, unit_second
            )
            self.assertEqual(unit["first"], 0)
            self.assertEqual(unit["reduced"], Fraction(-61, 234))
        for first_coordinate in range(4):
            for second_coordinate in range(first_coordinate + 1, 4):
                direction = [0, 0, 0, 0]
                direction[first_coordinate] = direction[second_coordinate] = 1
                sum_first, sum_second = paffenholz_parameter_path(direction)
                summed = reduced_log_mahler_second(
                    polytope, sum_first, sum_second
                )
                self.assertEqual(summed["first"], 0)
                self.assertEqual(summed["reduced"], Fraction(-61, 117))

    def test_24_cell_incidence_tangent_space_contains_projective_orbit(self):
        regular = paffenholz_24_cell((0, 0, 0, 0))
        nonregular = paffenholz_24_cell()
        self.assertEqual(incidence_tangent_dimension(regular), 52)
        self.assertEqual(incidence_tangent_dimension(nonregular), 50)
        tangent_matrix = incidence_tangent_matrix(nonregular)
        projective_vectors = projective_orbit_tangent_vectors(nonregular)
        self.assertEqual(len(projective_vectors), 24)
        self.assertEqual(rank(projective_vectors), 24)
        for vector in projective_vectors:
            self.assertTrue(
                all(
                    sum(
                        coefficient * entry
                        for coefficient, entry in zip(row, vector)
                    )
                    == 0
                    for row in tangent_matrix
                )
            )

        regular_projective = projective_orbit_tangent_vectors(regular)
        parameter_first, _ = paffenholz_parameter_path((1, 0, 0, 0))
        parameter_tangent = paired_tangent_from_vertex_path(
            regular, parameter_first
        )
        self.assertEqual(rank((*regular_projective, parameter_tangent)), 25)

    def test_regular_24_cell_constrained_hessian_and_stress_radical(self):
        polytope = paffenholz_24_cell((0, 0, 0, 0))
        multiplier = incidence_kkt_multiplier(polytope)
        self.assertEqual(len(multiplier), 144)
        self.assertEqual(sum(value != 0 for value in multiplier), 120)
        self.assertEqual((min(multiplier), max(multiplier)), (
            Fraction(-7, 48), Fraction(7, 48)
        ))
        self.assertEqual(sum(multiplier), 4)

        projective = projective_orbit_tangent_vectors(polytope)
        denominator = projective[20:]
        realization = []
        for coordinate in range(4):
            direction = [0, 0, 0, 0]
            direction[coordinate] = 1
            first, _ = paffenholz_parameter_path(direction)
            realization.append(
                paired_tangent_from_vertex_path(polytope, first)
            )

        def diagonal_matrix(value):
            return tuple(
                tuple(
                    value if row == column else Fraction()
                    for column in range(4)
                )
                for row in range(4)
            )

        projective_block = tuple(
            tuple(
                constrained_reduced_log_bilinear(
                    polytope, multiplier, left, right
                )
                for right in denominator
            )
            for left in denominator
        )
        mixed_block = tuple(
            tuple(
                constrained_reduced_log_bilinear(
                    polytope, multiplier, left, right
                )
                for right in realization
            )
            for left in denominator
        )
        realization_block = tuple(
            tuple(
                constrained_reduced_log_bilinear(
                    polytope, multiplier, left, right
                )
                for right in realization
            )
            for left in realization
        )
        self.assertEqual(
            projective_block, diagonal_matrix(Fraction(-31, 13))
        )
        self.assertEqual(
            mixed_block, diagonal_matrix(Fraction(-31, 78))
        )
        self.assertEqual(
            realization_block, diagonal_matrix(Fraction(-61, 234))
        )

        tangent_basis, stress_basis = incidence_tangent_and_stress_bases(
            polytope
        )
        self.assertEqual((len(tangent_basis), len(stress_basis)), (52, 4))
        for stress in stress_basis:
            for projective_velocity in projective:
                for tangent in tangent_basis:
                    self.assertEqual(
                        incidence_stress_bilinear(
                            polytope,
                            stress,
                            projective_velocity,
                            tangent,
                        ),
                        0,
                    )

    def test_regular_24_cell_global_slack_mass_identity(self):
        polytope = paffenholz_24_cell((0, 0, 0, 0))
        polar = polytope.polar()
        _, _, primal_covariance = polytope.volume_centroid_covariance()
        _, _, polar_covariance = polar.volume_centroid_covariance()
        covariance_trace = sum(
            primal_covariance[row][column]
            * polar_covariance[column][row]
            for row in range(4)
            for column in range(4)
        )
        self.assertEqual(covariance_trace, Fraction(169, 1800))
        self.assertEqual(
            triangulation_slack_mass_trace(polytope),
            900 * covariance_trace,
        )
        circuit_matrix = polytope.admissible_matrix_waiving(())
        self.assertEqual(rank(circuit_matrix), len(polytope.vertices) - 5)
        for circuit in circuit_matrix:
            for polar_vertex in polar.vertices:
                self.assertEqual(
                    sum(
                        (
                            coefficient
                            * sum(
                                left * right
                                for left, right in zip(
                                    polytope.vertices[index],
                                    polar_vertex,
                                )
                            )
                            for index, coefficient in enumerate(circuit)
                        ),
                        Fraction(),
                    ),
                    0,
                )

        energies = []
        for primal_simplex in polytope.pulling_triangulation():
            primal_vertices = [
                polytope.vertices[index] for index in primal_simplex
            ]
            for polar_simplex in polar.pulling_triangulation():
                polar_vertices = [
                    polar.vertices[index] for index in polar_simplex
                ]
                energies.append(
                    simplex_pair_energy(primal_vertices, polar_vertices)
                )
        self.assertEqual(len(energies), 72 * 72)
        self.assertEqual(sum(value > 100 for value in energies), 1784)
        self.assertEqual(max(energies), 344)
        boundary_deficit, local_deficits = boundary_trace_deficit(polytope)
        self.assertEqual(
            boundary_deficit,
            Fraction(1, 4) - Fraction(9, 4) * covariance_trace,
        )
        self.assertEqual(boundary_deficit, Fraction(31, 800))
        self.assertEqual(len(local_deficits), 24 * 24)
        self.assertEqual(
            sum(entry["bracket"] < 0 for entry in local_deficits), 288
        )
        self.assertEqual(
            sum(entry["bracket"] > 0 for entry in local_deficits), 288
        )
        self.assertEqual(
            {entry["bracket"] for entry in local_deficits},
            {Fraction(-11, 100), Fraction(3, 16)},
        )
        incident = [
            entry for entry in local_deficits if entry["incident"]
        ]
        self.assertEqual(len(incident), 144)
        self.assertEqual(
            {entry["bracket"] for entry in incident},
            {Fraction(3, 16)},
        )

    def test_full_rank_24_cell_family_exact_invariants_and_covariance_gap(self):
        parameter = Fraction(1, 2)
        polytope = full_rank_24_cell(parameter, (1, -1, 1))
        self.assertEqual(len(polytope.facets), 24)
        self.assertEqual(sum(len(facet[0]) for facet in polytope.facets), 144)
        self.assertEqual(incidence_tangent_dimension(polytope), 48)

        invariants = full_rank_24_cell_invariants(parameter)
        primal_volume, primal_centroid, primal_covariance = (
            polytope.volume_centroid_covariance()
        )
        polar_volume, polar_centroid, polar_covariance = (
            polytope.polar().volume_centroid_covariance()
        )
        self.assertEqual(primal_centroid, (0, 0, 0, 0))
        self.assertEqual(polar_centroid, (0, 0, 0, 0))
        self.assertEqual(primal_volume, invariants["primal_volume"])
        self.assertEqual(polar_volume, invariants["polar_volume"])
        self.assertEqual(primal_volume * polar_volume, invariants["mahler"])

        primal_scalar = invariants["primal_covariance_scalar"]
        polar_scalar = invariants["polar_covariance_scalar"]
        self.assertEqual(
            primal_covariance,
            tuple(
                tuple(
                    primal_scalar if row == column else Fraction()
                    for column in range(4)
                )
                for row in range(4)
            ),
        )
        self.assertEqual(
            polar_covariance,
            tuple(
                tuple(
                    polar_scalar if row == column else Fraction()
                    for column in range(4)
                )
                for row in range(4)
            ),
        )
        self.assertLess(primal_scalar * polar_scalar, Fraction(1, 36))

    def test_24_cell_has_q_regular_integrable_tangent(self):
        polytope = paffenholz_24_cell()
        tangent_matrix = incidence_tangent_matrix(polytope)
        tangent_basis, stress_basis = incidence_tangent_and_stress_bases(
            polytope
        )
        self.assertEqual(len(tangent_basis), 50)
        self.assertEqual(len(stress_basis), 2)

        velocity = tuple(
            tangent_basis[0][index]
            + Fraction(659, 667) * tangent_basis[1][index]
            for index in range(len(tangent_basis[0]))
        )
        self.assertEqual(
            tuple(
                incidence_stress_quadratic(polytope, stress, velocity)
                for stress in stress_basis
            ),
            (0, 0),
        )
        stress_derivative = tuple(
            tuple(
                incidence_stress_bilinear(
                    polytope, stress, velocity, tangent
                )
                for tangent in tangent_basis
            )
            for stress in stress_basis
        )
        self.assertEqual(rank(stress_derivative), 2)
        kernel_coordinates = tuple(nullspace(stress_derivative))
        self.assertEqual(len(kernel_coordinates), 48)
        kernel_velocities = tuple(
            tuple(
                sum(
                    coefficient * tangent_basis[index][coordinate]
                    for index, coefficient in enumerate(coefficients)
                )
                for coordinate in range(len(tangent_basis[0]))
            )
            for coefficients in kernel_coordinates
        )
        second_normal_outputs = tuple(
            tuple(
                incidence_stress_quadratic(
                    polytope, stress, kernel_velocity
                )
                for stress in stress_basis
            )
            for kernel_velocity in kernel_velocities
        )
        self.assertEqual(rank(second_normal_outputs), 2)
        self.assertEqual(rank(second_normal_outputs[1:3]), 2)

        right = second_order_incidence_rhs(polytope, velocity)
        augmented = tuple(
            (*row, right[index]) for index, row in enumerate(tangent_matrix)
        )
        self.assertEqual(rank(augmented), rank(tangent_matrix))

        projective = projective_orbit_tangent_vectors(polytope)
        for stress in stress_basis:
            for projective_velocity in projective:
                for tangent in tangent_basis:
                    self.assertEqual(
                        incidence_stress_bilinear(
                            polytope,
                            stress,
                            projective_velocity,
                            tangent,
                        ),
                        0,
                    )
        self.assertEqual(rank((*projective, velocity)), 25)
        paffenholz_tangents = []
        for coordinate in range(4):
            direction = [0, 0, 0, 0]
            direction[coordinate] = 1
            first, _ = paffenholz_parameter_path(direction)
            paffenholz_tangents.append(
                paired_tangent_from_vertex_path(polytope, first)
            )
        self.assertEqual(rank((*projective, *paffenholz_tangents)), 28)
        self.assertEqual(
            rank((*projective, *paffenholz_tangents, velocity)), 29
        )


if __name__ == "__main__":
    unittest.main()
