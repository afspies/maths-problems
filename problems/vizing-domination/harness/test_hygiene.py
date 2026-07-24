from fractions import Fraction
from itertools import combinations
import unittest

from graph_hygiene import (
    Graph,
    bipartite_one_subdivision,
    complete,
    cycle,
    fractional_tensor_lower_bound,
    path,
    uniform_set_cover_split_graph,
)
from optimization import (
    Surd73,
    steiner_exact_constants,
    steiner_lower_envelope,
    withdrawn_claimed_term,
    withdrawn_cps_term,
)


class GraphHygieneTests(unittest.TestCase):
    def test_domination_numbers(self) -> None:
        self.assertEqual(path(4).domination_number(), 2)
        self.assertEqual(cycle(4).domination_number(), 2)
        self.assertEqual(complete(5).domination_number(), 1)

    def test_cartesian_product(self) -> None:
        product_graph = path(2).cartesian_product(path(2))
        self.assertEqual(len(product_graph.edges), 4)
        self.assertTrue(all(len(product_graph.closed_neighborhood(v)) == 3 for v in range(4)))
        self.assertEqual(product_graph.domination_number(), 2)

    def test_vizing_hygiene_on_small_named_graphs(self) -> None:
        graphs = [path(2), path(3), path(4), cycle(3), cycle(4), complete(4)]
        for left in graphs:
            for right in graphs:
                self.assertGreaterEqual(
                    left.cartesian_product(right).domination_number(),
                    left.domination_number() * right.domination_number(),
                )

    def test_k_function_definitions(self) -> None:
        graph = path(3)
        self.assertEqual(graph.k_packing_number(1), graph.two_packing_number())
        self.assertEqual(graph.k_domination_number(1), graph.domination_number())
        self.assertGreaterEqual(graph.k_packing_number(2), 2 * graph.two_packing_number())
        self.assertLessEqual(graph.k_domination_number(2), 2 * graph.domination_number())

    def test_subset_domination_lemma_2_3(self) -> None:
        graphs = [path(4), cycle(4), cycle(5), complete(4)]
        for graph in graphs:
            rho2 = graph.k_packing_number(2)
            for mask in range(1 << graph.n):
                subset = [v for v in range(graph.n) if mask & (1 << v)]
                self.assertLessEqual(3 * graph.domination_number(subset), len(subset) + rho2)

    def test_terminal_conflict_graph_formula(self) -> None:
        graphs = [path(5), cycle(4), cycle(5), complete(5)]
        for graph in graphs:
            for mask in range(1 << graph.n):
                subset = [v for v in range(graph.n) if mask & (1 << v)]
                if all(
                    len(graph.closed_neighborhood(v) & frozenset(subset)) <= 2
                    for v in range(graph.n)
                ):
                    conflict = graph.closed_neighborhood_conflict_graph(subset)
                    self.assertEqual(
                        graph.domination_number(subset),
                        len(subset) - conflict.matching_number(),
                    )
                    self.assertEqual(graph.two_packing_number(subset), conflict.independence_number())

    def test_matching_cover_extremal_classification(self) -> None:
        # Exhaust every graph through five vertices.
        for n in range(6):
            pairs = list(combinations(range(n), 2))
            for edge_mask in range(1 << len(pairs)):
                graph = Graph.from_edges(
                    n,
                    [edge for i, edge in enumerate(pairs) if edge_mask & (1 << i)],
                )
                equality = graph.independence_number() + 2 * graph.matching_number() == n
                self.assertEqual(equality, graph.is_disjoint_union_of_odd_cliques())

    def test_terminal_capacity_two_refinement(self) -> None:
        # The terminal structural defect vanishes exactly on unions of K1 and K3.
        for n in range(6):
            pairs = list(combinations(range(n), 2))
            for edge_mask in range(1 << len(pairs)):
                graph = Graph.from_edges(
                    n,
                    [edge for i, edge in enumerate(pairs) if edge_mask & (1 << i)],
                )
                alpha = graph.independence_number()
                matching = graph.matching_number()
                tau_two = graph.edge_capacity_two_number()
                self.assertGreaterEqual(tau_two, alpha + n - matching)
                defect = tau_two - 2 * n + 3 * matching
                self.assertGreaterEqual(defect, 0)
                tight_components = graph.is_disjoint_union_of_odd_cliques() and all(
                    len(component) in {1, 3}
                    for component in graph.connected_components()
                )
                self.assertEqual(defect == 0, tight_components)

        graph = cycle(5)
        subset = [0, 2, 4]
        conflict = graph.closed_neighborhood_conflict_graph(subset)
        self.assertEqual(conflict, complete(3))
        self.assertEqual(graph.domination_number(subset), 2)
        self.assertEqual(graph.k_packing_number(2), 3)
        self.assertEqual(graph.conflict_refined_peeling_parameter(subset), 0)

    def test_conflict_refined_subset_inequality(self) -> None:
        graphs = [path(5), cycle(4), cycle(5), complete(5)]
        for graph in graphs:
            rho_two = graph.k_packing_number(2)
            for mask in range(1 << graph.n):
                subset = [v for v in range(graph.n) if mask & (1 << v)]
                parameter = graph.conflict_refined_peeling_parameter(subset)
                self.assertGreaterEqual(parameter, graph.excess_peeling_parameter(subset))
                self.assertLessEqual(
                    3 * graph.domination_number(subset),
                    len(subset) + rho_two - parameter,
                )

    def test_strengthened_peeling_inequality(self) -> None:
        graphs = [path(5), cycle(4), cycle(5), complete(5)]
        for graph in graphs:
            rho2 = graph.k_packing_number(2)
            for mask in range(1 << graph.n):
                subset = [v for v in range(graph.n) if mask & (1 << v)]
                self.assertLessEqual(
                    3 * graph.domination_number(subset),
                    len(subset) + rho2 - graph.excess_peeling_parameter(subset),
                )

    def test_steiner_rational_grid(self) -> None:
        grid = [Fraction(i, 12) for i in range(13)]
        # c > 9/16, so this is a nontrivial exact smoke test without decimals.
        for x1 in grid:
            for x2 in grid:
                for y1 in grid:
                    for y2 in grid:
                        if x1 <= x2 and y1 <= y2:
                            self.assertGreaterEqual(
                                steiner_lower_envelope(x1, x2, y1, y2),
                                Fraction(9, 16),
                            )

    def test_withdrawn_algebra_fails(self) -> None:
        # A=B=10 and x=y=7 are admissible normalized deficits.
        self.assertEqual(withdrawn_cps_term(10, 10, 7, 7), 51)
        self.assertEqual(withdrawn_claimed_term(10, 10, 7, 7), 69)

    def test_exact_steiner_threshold_identities(self) -> None:
        c, a, b = steiner_exact_constants()
        one = Surd73(Fraction(1))
        d = (b.scale(2) + a).scale(Fraction(1, 3))
        self.assertEqual(a, Surd73(Fraction(2)) - c.scale(3))
        self.assertEqual(b, Surd73(Fraction(3, 2)) - c.scale(2))
        self.assertEqual(a + b * (one - a), c)
        self.assertEqual(c * c.scale(12) - c.scale(5) - one, Surd73(Fraction(0)))
        self.assertEqual(Surd73(Fraction(5, 7)) - d.scale(Fraction(3, 7)), c)
        self.assertEqual(b - d, (b - a).scale(Fraction(1, 3)))
        c5_share = (b - a).scale(4)
        diagonal_ratio = Surd73(Fraction(41, 64), Fraction(-3, 64))
        self.assertEqual(
            c5_share,
            Surd73(Fraction(-7, 6), Fraction(1, 6)),
        )
        self.assertEqual(
            a,
            c5_share.scale(Fraction(1, 2)) + (one - c5_share) * diagonal_ratio,
        )
        self.assertEqual(
            b,
            c5_share.scale(Fraction(3, 4)) + (one - c5_share) * diagonal_ratio,
        )
        triangle_provider_bound = b * (b.scale(2) - a)
        self.assertEqual(
            triangle_provider_bound,
            Surd73(Fraction(10, 9), Fraction(-1, 9)),
        )
        self.assertEqual(
            c - triangle_provider_bound,
            Surd73(Fraction(-65, 72), Fraction(11, 72)),
        )
        anchored_limit = Surd73(Fraction(1273, 576), Fraction(-115, 576))
        anchored_gap = c - anchored_limit
        self.assertEqual(
            anchored_gap,
            Surd73(Fraction(-1153, 576), Fraction(139, 576)),
        )
        self.assertEqual(139 * 139 * 73 - 1153 * 1153, 81024)

    def test_independent_cap_counterfamily_identities(self) -> None:
        c, a, b = steiner_exact_constants()
        one = Surd73(Fraction(1))

        c5_share = Surd73(Fraction(-7, 6), Fraction(1, 6))
        split_ratio = Surd73(Fraction(41, 64), Fraction(-3, 64))
        self.assertEqual(
            a,
            c5_share.scale(Fraction(1, 2)) + (one - c5_share) * split_ratio,
        )
        self.assertEqual(
            b,
            c5_share.scale(Fraction(3, 4)) + (one - c5_share) * split_ratio,
        )

        line_share = Surd73(Fraction(-7, 4), Fraction(1, 4))
        large_split_ratio = Surd73(Fraction(19, 36), Fraction(-1, 36))
        self.assertEqual(
            a,
            line_share.scale(Fraction(1, 3))
            + (one - line_share) * large_split_ratio,
        )
        self.assertEqual(
            b,
            line_share.scale(Fraction(1, 2))
            + (one - line_share) * large_split_ratio,
        )

        right_anchored = Surd73(Fraction(2443, 1056), Fraction(-217, 1056))
        self.assertEqual(
            c - right_anchored,
            Surd73(Fraction(-741, 352), Fraction(87, 352)),
        )
        self.assertEqual(87 * 87 * 73 - 741 * 741, 3456)

        cap_limit = Surd73(Fraction(-247, 264), Fraction(37, 264))
        self.assertEqual(
            c - cap_limit,
            Surd73(Fraction(151, 132), Fraction(-13, 132)),
        )
        self.assertGreater(151 * 151 - 13 * 13 * 73, 0)
        exact_cap_gap = c - cap_limit.scale(2)
        self.assertEqual(
            exact_cap_gap,
            Surd73(Fraction(183, 88), Fraction(-21, 88)),
        )
        self.assertEqual(183 * 183 - 21 * 21 * 73, 1296)

        profile_slope_drop = Surd73(Fraction(-811, 264), Fraction(97, 264))
        self.assertGreater(97 * 97 * 73 - 811 * 811, 0)

    def test_combined_lift_transitive_benchmarks(self) -> None:
        # The exact transitive formula is the maximum of the product
        # fractional term and the two directional blocker terms.
        c4_fractional = Fraction(4 * 4, 2 + 2 + 1)
        c4_blocker = Fraction(4 * 2, 2 + 1)
        self.assertEqual(max(c4_fractional, c4_blocker), Fraction(16, 5))
        self.assertLess(Fraction(16, 5), 2 * 2)

        c, _, _ = steiner_exact_constants()
        normalized_c4 = Surd73(Fraction(4, 5))
        self.assertEqual(
            normalized_c4 - c,
            Surd73(Fraction(71, 120), Fraction(-1, 24)),
        )
        self.assertGreater(71 * 71 - 5 * 5 * 73, 0)

    def test_k3_counterexample(self) -> None:
        graph = Graph.from_edges(
            5,
            [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3)],
        )
        subset = [2, 3, 4]
        self.assertEqual(graph.domination_number(subset), 2)
        self.assertEqual(graph.k_packing_number(3), 4)
        self.assertGreater(
            4 * graph.domination_number(subset),
            len(subset) + graph.k_packing_number(3),
        )
        self.assertEqual(
            5 * graph.domination_number(subset),
            2 * len(subset) + graph.k_packing_number(3),
        )

    def test_corrected_k3_subset_inequality(self) -> None:
        graphs = [path(5), cycle(4), cycle(5), complete(5)]
        for graph in graphs:
            rho3 = graph.k_packing_number(3)
            for mask in range(1 << graph.n):
                subset = [v for v in range(graph.n) if mask & (1 << v)]
                self.assertLessEqual(
                    5 * graph.domination_number(subset),
                    2 * len(subset) + rho3,
                )

    def test_all_level_packing_domination_gadget(self) -> None:
        graph = Graph.from_edges(
            5,
            [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3)],
        )
        subset = [2, 3, 4]
        for k in range(7):
            self.assertEqual(graph.k_packing_number(k), 3 * k // 2)
            self.assertEqual(graph.k_domination_number(k), (3 * k + 1) // 2)
        gamma = graph.domination_number(subset)
        size = len(subset)
        for m in range(1, 4):
            self.assertEqual(3 * m * gamma, m * size + graph.k_packing_number(2 * m))
        for m in range(4):
            self.assertEqual(
                (3 * m + 2) * gamma,
                (m + 1) * size + graph.k_packing_number(2 * m + 1),
            )

    def test_fractional_tensor_regular_bound(self) -> None:
        left = cycle(4)
        right = cycle(4)
        weights = [Fraction(1, 3)] * 4
        self.assertTrue(left.is_fractional_packing_function(weights))
        self.assertEqual(
            fractional_tensor_lower_bound(left, right, weights, weights),
            Fraction(16, 5),
        )
        self.assertGreaterEqual(
            left.cartesian_product(right).domination_number(),
            Fraction(16, 5),
        )

    def test_p4_fractional_packing_concentration(self) -> None:
        graph = path(4)
        concentrated = [Fraction(1), Fraction(0), Fraction(0), Fraction(1)]
        self.assertTrue(graph.is_fractional_packing_function(concentrated))
        self.assertEqual(sum(concentrated), 2)
        self.assertEqual(
            fractional_tensor_lower_bound(graph, graph, concentrated, concentrated),
            Fraction(4),
        )

    def test_fractional_rank_one_split_examples(self) -> None:
        hard = uniform_set_cover_split_graph(4, 2)
        self.assertEqual(hard.domination_number(), 3)
        hard_weights = [Fraction(0)] * 4 + [Fraction(1, 3)] * 6
        self.assertTrue(hard.is_fractional_packing_function(hard_weights))
        self.assertEqual(sum(hard_weights), 2)
        diffuse_p4 = [Fraction(1, 3)] * 4
        self.assertEqual(
            fractional_tensor_lower_bound(hard, path(4), hard_weights, diffuse_p4),
            8,
        )

        augmented = uniform_set_cover_split_graph(4, 2, private_pairs=2)
        self.assertEqual(augmented.domination_number(), 5)
        augmented_weights = (
            [Fraction(0)] * 6
            + [Fraction(1, 3)] * 6
            + [Fraction(1)] * 2
        )
        self.assertTrue(augmented.is_fractional_packing_function(augmented_weights))
        self.assertEqual(sum(augmented_weights), 4)
        diffuse_augmented = (
            [Fraction(0)] * 6
            + [Fraction(1, 3)] * 6
            + [Fraction(0)] * 2
        )
        self.assertTrue(augmented.is_fractional_packing_function(diffuse_augmented))
        self.assertEqual(
            fractional_tensor_lower_bound(
                augmented,
                augmented,
                diffuse_augmented,
                diffuse_augmented,
            ),
            12,
        )

    def test_incidence_skeleton_requires_coordinate_holes(self) -> None:
        left = cycle(4)
        right = Graph.from_edges(
            6,
            [
                (0, 1),
                (0, 2),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4),
                (3, 5),
                (1, 3),
                (1, 5),
            ],
        )
        self.assertEqual(right.domination_number(), 2)
        part_one = {0, 1, 2}
        part_two = {3, 4, 5}
        self.assertTrue(right.dominates([4], part_one))
        self.assertTrue(right.dominates([1], part_two))

        # D={(2,u1),(0,u2)} in row-major product indexing.
        chosen = {2 * right.n + 1, 4}
        product_graph = left.cartesian_product(right)
        self.assertFalse(product_graph.dominates(chosen))
        self.assertFalse(product_graph.dominates(chosen, [1 * right.n + 2]))

        vertical_sets = []
        for part in (part_one, part_two):
            outside = set(range(right.n)) - part
            vertical_sets.append(
                {
                    g
                    for g in range(left.n)
                    if all(
                        any(
                            g * right.n + source in chosen
                            and source in right.closed_neighborhood(h)
                            for source in outside
                        )
                        for h in part
                    )
                }
            )
        self.assertEqual(vertical_sets, [{0}, {2}])

    def test_external_private_atomic_column(self) -> None:
        graph = cycle(4)
        terminal = {0}
        complement = set(range(graph.n)) - terminal
        projection = {2}
        supported = (2, 0, 0, 0)

        self.assertTrue(graph.is_k_packing_function(supported, 2))
        self.assertEqual(sum(supported), graph.k_packing_number(2))
        self.assertTrue(graph.dominates(projection, complement))
        self.assertEqual(graph.domination_number(complement), len(projection))
        self.assertEqual(
            len(projection) + graph.domination_number(terminal),
            graph.domination_number(),
        )
        external_private = {
            y
            for y in complement - projection
            if graph.closed_neighborhood(y) & projection == projection
        }
        self.assertEqual(external_private, {1, 3})

    def test_external_private_needs_additivity(self) -> None:
        graph = Graph.from_edges(
            5,
            [(u, v) for u in (0, 1) for v in (2, 3, 4)],
        )
        terminal = {2}
        complement = set(range(graph.n)) - terminal
        projection = {3, 4}
        supported = (0, 0, 2, 0, 0)

        self.assertTrue(graph.is_k_packing_function(supported, 2))
        self.assertEqual(sum(supported), graph.k_packing_number(2))
        self.assertEqual(graph.domination_number(complement), len(projection))
        self.assertGreater(
            len(projection) + graph.domination_number(terminal),
            graph.domination_number(),
        )
        for x in projection:
            private = {
                y
                for y in complement
                if graph.closed_neighborhood(y) & projection == {x}
            }
            self.assertEqual(private, {x})

    def test_two_sided_private_corners_can_cycle(self) -> None:
        factor = cycle(5)
        product_graph = factor.cartesian_product(factor)
        chosen_pairs = {(i, 2 * i % 5) for i in range(5)}
        chosen = {g * factor.n + h for g, h in chosen_pairs}

        self.assertTrue(product_graph.dominates(chosen))
        for vertex in range(product_graph.n):
            self.assertEqual(len(product_graph.closed_neighborhood(vertex) & chosen), 1)
        for i in range(5):
            point = (i, 2 * i % 5)
            horizontal_private = ((i + 1) % 5, point[1])
            vertical_private = (point[0], (point[1] + 1) % 5)
            corner = (horizontal_private[0], vertical_private[1])
            next_point = ((i + 1) % 5, (2 * (i + 1)) % 5)
            self.assertIn(
                next_point[0] * factor.n + next_point[1],
                product_graph.closed_neighborhood(corner[0] * factor.n + corner[1]),
            )
            self.assertNotIn(
                next_point[0] * factor.n + next_point[1],
                product_graph.closed_neighborhood(
                    horizontal_private[0] * factor.n + horizontal_private[1]
                ),
            )
            self.assertNotIn(
                next_point[1],
                factor.closed_neighborhood(point[1]),
            )
            self.assertIn(
                vertical_private[1],
                factor.closed_neighborhood(point[1])
                & factor.closed_neighborhood(next_point[1]),
            )

    def test_private_corner_escape_cycle_can_have_length_two(self) -> None:
        left = path(2)
        right = path(3)
        product_graph = left.cartesian_product(right)
        chosen_pairs = ((0, 0), (1, 2))
        chosen = {g * right.n + h for g, h in chosen_pairs}
        self.assertTrue(product_graph.dominates(chosen))

        for point, horizontal, vertical, corner, owner in (
            ((0, 0), (1, 0), (0, 1), (1, 1), (1, 2)),
            ((1, 2), (0, 2), (1, 1), (0, 1), (0, 0)),
        ):
            source = point[0] * right.n + point[1]
            horizontal_vertex = horizontal[0] * right.n + horizontal[1]
            vertical_vertex = vertical[0] * right.n + vertical[1]
            corner_vertex = corner[0] * right.n + corner[1]
            owner_vertex = owner[0] * right.n + owner[1]
            self.assertEqual(
                product_graph.closed_neighborhood(horizontal_vertex) & chosen,
                {source},
            )
            self.assertEqual(
                product_graph.closed_neighborhood(vertical_vertex) & chosen,
                {source},
            )
            self.assertIn(
                owner_vertex,
                product_graph.closed_neighborhood(corner_vertex),
            )

    def test_typed_fibre_cardinality_is_strictly_weaker(self) -> None:
        factor = Graph.from_edges(3, [(0, 1)])
        chosen_pairs = {(0, 2), (1, 2), (2, 0), (2, 1)}
        product_graph = factor.cartesian_product(factor)
        chosen = {g * factor.n + h for g, h in chosen_pairs}

        self.assertEqual(factor.domination_number(), 2)
        self.assertEqual(product_graph.domination_number(), 5)
        self.assertEqual(factor.typed_fibre_number(factor), 4)
        self.assertFalse(product_graph.dominates(chosen))

        row_sets = {
            g: {h for x, h in chosen_pairs if x == g}
            for g in range(factor.n)
        }
        for g in range(factor.n):
            open_neighbors = set(factor.closed_neighborhood(g)) - {g}
            imported = set().union(
                *(row_sets[x] for x in open_neighbors),
            )
            missed_type = set(range(factor.n)) - imported
            self.assertGreaterEqual(
                len(row_sets[g]),
                factor.domination_number(missed_type),
            )

    def test_typed_fibre_number_on_small_named_pairs(self) -> None:
        for left, right, expected in (
            (path(2), path(3), 2),
            (path(3), path(3), 3),
            (path(4), path(4), 4),
            (path(4), cycle(4), 4),
            (cycle(4), cycle(4), 4),
        ):
            self.assertEqual(left.typed_fibre_number(right), expected)
            self.assertGreaterEqual(
                expected,
                left.domination_number() * right.domination_number(),
            )

    def test_typed_partial_cover_profile_inequality(self) -> None:
        for left, right in (
            (path(3), path(3)),
            (Graph.from_edges(3, [(0, 1)]), Graph.from_edges(3, [(0, 1)])),
        ):
            left_profile = left.near_cover_profile()
            right_profile = right.near_cover_profile()
            for mask in range(1 << (left.n * right.n)):
                chosen = {
                    cell
                    for cell in range(left.n * right.n)
                    if mask & (1 << cell)
                }
                if not left.is_typed_fibre_feasible(right, chosen):
                    continue
                row_sizes = [
                    sum(g * right.n <= cell < (g + 1) * right.n for cell in chosen)
                    for g in range(left.n)
                ]
                column_sizes = [
                    sum(cell % right.n == h for cell in chosen)
                    for h in range(right.n)
                ]
                self.assertLessEqual(
                    sum(right_profile[size] for size in row_sizes)
                    + sum(left_profile[size] for size in column_sizes),
                    left.n * right.n,
                )

    def test_typed_profile_exact_isolation_slack(self) -> None:
        for factor, chosen_pairs, expected_slack in (
            (cycle(4), {(g, g) for g in range(4)}, 8),
            (cycle(5), {(g, 2 * g % 5) for g in range(5)}, 5),
        ):
            profile = factor.near_cover_profile()
            row_sets = [
                {h for x, h in chosen_pairs if x == g}
                for g in range(factor.n)
            ]
            column_sets = [
                {g for g, y in chosen_pairs if y == h}
                for h in range(factor.n)
            ]
            row_remainders = []
            for g, row in enumerate(row_sets):
                imported = set().union(
                    *(row_sets[x] for x in factor.open_neighborhood(g))
                )
                row_remainders.append(len(imported) - profile[len(row)])

            column_excess = []
            column_isolates = []
            for column in column_sets:
                closed = set().union(
                    *(factor.closed_neighborhood(g) for g in column)
                )
                open_union = set().union(
                    *(factor.open_neighborhood(g) for g in column)
                )
                column_excess.append(
                    factor.n - profile[len(column)] - len(closed)
                )
                column_isolates.append(len(column - open_union))

            scalar_slack = (
                factor.n * factor.n
                - sum(profile[len(row)] for row in row_sets)
                - sum(profile[len(column)] for column in column_sets)
            )
            self.assertEqual(scalar_slack, expected_slack)
            self.assertEqual(
                scalar_slack,
                sum(row_remainders)
                + sum(column_excess)
                + sum(column_isolates),
            )

    def test_typed_fractional_charging_identity(self) -> None:
        for factor, chosen_pairs, expected_gap in (
            (cycle(4), {(g, g) for g in range(4)}, Fraction(4, 9)),
            (cycle(5), {(g, 2 * g % 5) for g in range(5)}, Fraction(0)),
        ):
            weight = Fraction(1, 3)
            total = factor.n * weight
            rows = [
                {h for x, h in chosen_pairs if x == g}
                for g in range(factor.n)
            ]
            columns = [
                {g for g, y in chosen_pairs if y == h}
                for h in range(factor.n)
            ]

            energy_h = Fraction(0)
            for g, row in enumerate(rows):
                imported = set().union(
                    *(rows[x] for x in factor.open_neighborhood(g))
                )
                target = set(range(factor.n)) - imported
                energy_h += weight * (
                    factor.domination_number(target) - weight * len(target)
                )

            energy_g = Fraction(0)
            for h, column in enumerate(columns):
                imported = set().union(
                    *(columns[y] for y in factor.open_neighborhood(h))
                )
                target = set(range(factor.n)) - imported
                energy_g += weight * (
                    factor.domination_number(target) - weight * len(target)
                )

            kernel = sum(
                weight + weight - weight * weight
                for _ in chosen_pairs
            )
            gap = kernel - total * total
            complement = sum(
                (1 - weight) * (1 - weight)
                for _ in chosen_pairs
            )
            self.assertEqual(gap, expected_gap)
            self.assertGreaterEqual(gap, max(energy_h, energy_g))
            self.assertEqual(
                len(chosen_pairs),
                total * total + complement + gap,
            )

    def test_isolation_to_escape_charging_is_sharp(self) -> None:
        def oriented_terms(
            left: Graph,
            right: Graph,
            chosen_pairs: set[tuple[int, int]],
        ) -> tuple[int, int, int]:
            rows = [
                {h for x, h in chosen_pairs if x == g}
                for g in range(left.n)
            ]
            columns = [
                {g for g, y in chosen_pairs if y == h}
                for h in range(right.n)
            ]
            isolated = sum(
                not (left.open_neighborhood(g) & columns[h])
                for g, h in chosen_pairs
            )
            collisions = sum(
                max(len(left.open_neighborhood(x) & columns[h]) - 1, 0)
                for x in range(left.n)
                for h in range(right.n)
            )
            cross_redundancy = 0
            for x in range(left.n):
                imported = set().union(
                    *(rows[g] for g in left.open_neighborhood(x))
                )
                vertically_covered = set().union(
                    *(right.closed_neighborhood(h) for h in rows[x])
                )
                cross_redundancy += len(imported & vertically_covered)
            return isolated, collisions, cross_redundancy

        for left, right, chosen_pairs in (
            (
                cycle(5),
                cycle(5),
                {(g, 2 * g % 5) for g in range(5)},
            ),
            (
                path(2),
                path(3),
                {(0, 0), (1, 2)},
            ),
        ):
            i_g, omega_g, x_h = oriented_terms(left, right, chosen_pairs)
            i_h, omega_h, x_g = oriented_terms(
                right,
                left,
                {(h, g) for g, h in chosen_pairs},
            )
            product_graph = left.cartesian_product(right)
            chosen = {g * right.n + h for g, h in chosen_pairs}
            two_sided_private = 0
            for g, h in chosen_pairs:
                source = g * right.n + h
                horizontal = any(
                    product_graph.closed_neighborhood(x * right.n + h) & chosen
                    == {source}
                    for x in left.open_neighborhood(g)
                )
                vertical = any(
                    product_graph.closed_neighborhood(g * right.n + y) & chosen
                    == {source}
                    for y in right.open_neighborhood(h)
                )
                two_sided_private += horizontal and vertical

            lower_bound = (
                i_g
                + i_h
                - len(chosen_pairs)
                - 2 * omega_g
                - 2 * omega_h
                - x_g
                - x_h
            )
            self.assertEqual(two_sided_private, len(chosen_pairs))
            self.assertEqual(lower_bound, two_sided_private)

    def test_zero_defect_escape_graph_realizes_bipartite_graphs(self) -> None:
        left = path(2)
        for left_size, right_size, edges in (
            (1, 4, {(0, right) for right in range(4)}),
            (2, 2, {(0, 0), (1, 0), (1, 1)}),
        ):
            right = bipartite_one_subdivision(left_size, right_size, edges)
            chosen_pairs = {
                *((0, vertex) for vertex in range(left_size)),
                *(
                    (1, left_size + vertex)
                    for vertex in range(right_size)
                ),
            }
            chosen = {
                g * right.n + h
                for g, h in chosen_pairs
            }
            product_graph = left.cartesian_product(right)

            # The construction is an efficient dominating set, hence also a
            # closed-neighborhood packing and therefore minimum.
            self.assertEqual(
                {
                    len(product_graph.closed_neighborhood(vertex) & chosen)
                    for vertex in range(product_graph.n)
                },
                {1},
            )
            self.assertEqual(
                product_graph.domination_number(),
                len(chosen_pairs),
            )

            # Mixed (1,2) escape adjacency recovers exactly the original
            # bipartite graph.
            recovered = {
                (source, target)
                for source in range(left_size)
                for target in range(right_size)
                if right.open_neighborhood(source)
                & right.open_neighborhood(left_size + target)
            }
            self.assertEqual(recovered, edges)

        for arms in range(1, 5):
            subdivided_star = bipartite_one_subdivision(
                arms,
                1,
                {(leaf, 0) for leaf in range(arms)},
            )
            self.assertEqual(subdivided_star.domination_number(), arms)
            self.assertEqual(
                path(2).cartesian_product(
                    subdivided_star
                ).domination_number(),
                arms + 1,
            )

    def test_four_region_overlap_tax_identity(self) -> None:
        def audit(
            left: Graph,
            right: Graph,
            chosen_pairs: set[tuple[int, int]],
            q: tuple[Fraction, ...],
            p: tuple[Fraction, ...],
        ) -> dict[str, Fraction | set[tuple[int, int]]]:
            rows = [
                {h for x, h in chosen_pairs if x == g}
                for g in range(left.n)
            ]
            columns = [
                {g for g, y in chosen_pairs if y == h}
                for h in range(right.n)
            ]
            universe = {
                (g, h)
                for g in range(left.n)
                for h in range(right.n)
            }
            no_horizontal_import = {
                (g, h)
                for g, h in universe
                if not any(
                    h in rows[x]
                    for x in left.open_neighborhood(g)
                )
            }
            no_vertical_import = {
                (g, h)
                for g, h in universe
                if not any(
                    g in columns[y]
                    for y in right.open_neighborhood(h)
                )
            }
            isolated = (
                chosen_pairs
                & no_horizontal_import
                & no_vertical_import
            )
            missed = (
                no_horizontal_import
                & no_vertical_import
            ) - chosen_pairs
            double_import = universe - (
                no_horizontal_import | no_vertical_import
            )

            def weight(points: set[tuple[int, int]]) -> Fraction:
                return sum(
                    (q[g] * p[h] for g, h in points),
                    Fraction(0),
                )

            energy_h = Fraction(0)
            alpha_h = Fraction(0)
            for g in range(left.n):
                target = {
                    h
                    for h in range(right.n)
                    if (g, h) in no_horizontal_import
                }
                gamma = right.domination_number(target)
                energy_h += q[g] * (
                    gamma - sum((p[h] for h in target), Fraction(0))
                )
                alpha_h += q[g] * (len(rows[g]) - gamma)

            energy_g = Fraction(0)
            alpha_g = Fraction(0)
            for h in range(right.n):
                target = {
                    g
                    for g in range(left.n)
                    if (g, h) in no_vertical_import
                }
                gamma = left.domination_number(target)
                energy_g += p[h] * (
                    gamma - sum((q[g] for g in target), Fraction(0))
                )
                alpha_g += p[h] * (len(columns[h]) - gamma)

            complement = sum(
                (
                    (1 - q[g]) * (1 - p[h])
                    for g, h in chosen_pairs
                ),
                Fraction(0),
            )
            overlap_tax = (
                weight(chosen_pairs - isolated)
                + weight(double_import)
            )
            repeated_owner_mass = Fraction(0)
            for g, h in universe:
                horizontal_owners = sum(
                    h in rows[x]
                    for x in left.open_neighborhood(g)
                )
                vertical_owners = sum(
                    g in columns[y]
                    for y in right.open_neighborhood(h)
                )
                repeated_owner_mass += q[g] * p[h] * (
                    horizontal_owners
                    - bool(horizontal_owners)
                    + vertical_owners
                    - bool(vertical_owners)
                )
            load_slack = sum(
                (
                    p[h]
                    * (
                        1
                        - sum(
                            (q[x] for x in left.closed_neighborhood(g)),
                            Fraction(0),
                        )
                    )
                    + q[g]
                    * (
                        1
                        - sum(
                            (p[y] for y in right.closed_neighborhood(h)),
                            Fraction(0),
                        )
                    )
                    for g, h in chosen_pairs
                ),
                Fraction(0),
            )
            packing_product = (
                sum(q, Fraction(0)) * sum(p, Fraction(0))
            )
            right_hand_side = (
                packing_product
                + complement
                + energy_h
                + energy_g
                + alpha_h
                + alpha_g
                - overlap_tax
                + weight(missed)
            )
            self.assertEqual(right_hand_side, len(chosen_pairs))
            self.assertEqual(
                2 * (len(chosen_pairs) - packing_product - complement),
                energy_h
                + energy_g
                + alpha_h
                + alpha_g
                + repeated_owner_mass
                + load_slack,
            )
            return {
                "energy_h": energy_h,
                "energy_g": energy_g,
                "alpha_h": alpha_h,
                "alpha_g": alpha_g,
                "overlap_tax": overlap_tax,
                "repeated_owner_mass": repeated_owner_mass,
                "load_slack": load_slack,
                "missed": missed,
                "double_import": double_import,
            }

        half = (Fraction(1, 2), Fraction(1, 2))
        anti_diagonal = audit(
            path(2),
            path(2),
            {(0, 1), (1, 0)},
            half,
            half,
        )
        self.assertEqual(anti_diagonal["energy_h"], Fraction(1, 2))
        self.assertEqual(anti_diagonal["energy_g"], Fraction(1, 2))
        self.assertEqual(anti_diagonal["overlap_tax"], Fraction(1, 2))

        endpoint = (
            Fraction(0),
            Fraction(0),
            Fraction(1),
        )
        p3_minimum = audit(
            path(3),
            path(3),
            {(0, 0), (1, 2), (2, 1)},
            endpoint,
            endpoint,
        )
        self.assertEqual(
            path(3).cartesian_product(path(3)).domination_number(),
            3,
        )
        self.assertEqual(p3_minimum["energy_h"], 1)
        self.assertEqual(p3_minimum["energy_g"], 1)
        self.assertEqual(p3_minimum["overlap_tax"], 1)

        p3_cardinality_slack = audit(
            path(3),
            path(3),
            {(0, 1), (2, 0), (2, 2)},
            endpoint,
            endpoint,
        )
        self.assertEqual(p3_cardinality_slack["energy_h"], 0)
        self.assertEqual(p3_cardinality_slack["energy_g"], 0)
        self.assertEqual(p3_cardinality_slack["alpha_h"], 1)
        self.assertEqual(p3_cardinality_slack["alpha_g"], 0)

        endpoints = (
            Fraction(1),
            Fraction(0),
            Fraction(0),
            Fraction(1),
        )
        p4_witness = audit(
            path(4),
            path(4),
            {(0, 1), (1, 0), (1, 3), (2, 3), (3, 1)},
            endpoints,
            endpoints,
        )
        self.assertEqual(p4_witness["energy_h"], 1)
        self.assertEqual(p4_witness["energy_g"], 1)
        self.assertEqual(p4_witness["overlap_tax"], 1)
        self.assertEqual(p4_witness["missed"], set())

        third = tuple(Fraction(1, 3) for _ in range(5))
        perfect_code = audit(
            cycle(5),
            cycle(5),
            {(g, 2 * g % 5) for g in range(5)},
            third,
            third,
        )
        self.assertEqual(perfect_code["overlap_tax"], 0)
        self.assertEqual(perfect_code["missed"], set())

        typed_only = audit(
            cycle(4),
            cycle(4),
            {(g, g) for g in range(4)},
            tuple(Fraction(1, 3) for _ in range(4)),
            tuple(Fraction(1, 3) for _ in range(4)),
        )
        self.assertTrue(typed_only["missed"])

    def test_indexed_provider_reuse_obstruction(self) -> None:
        left = cycle(5)
        terminal = {0, 2, 4}
        complement = {1, 3}
        self.assertEqual(left.domination_number(terminal), 2)
        self.assertTrue(
            left.is_k_packing_function((1, 0, 1, 0, 1), 2)
        )
        self.assertEqual(left.k_packing_number(2), 3)

        for count in range(1, 4):
            def vertex(index: int, offset: int) -> int:
                return 6 * index + offset

            blue_cells = []
            red_cells = []
            edges = set()
            a_zero = vertex(0, 4)
            for index in range(count):
                c_i, s_i, t_i, r_i, a_i, w_i = (
                    vertex(index, offset)
                    for offset in range(6)
                )
                blue_cells.append({c_i, s_i, t_i})
                red_cells.append({r_i, a_i, w_i})
                edges.update(
                    {
                        (c_i, s_i),
                        (c_i, t_i),
                        (r_i, a_i),
                        (r_i, w_i),
                        (a_i, t_i),
                        (a_zero, c_i),
                        (a_zero, s_i),
                    }
                )

            right = Graph.from_edges(6 * count, edges)
            packing_witnesses = [
                right.closed_neighborhood(vertex(index, offset))
                for index in range(count)
                for offset in (2, 5)
            ]
            self.assertEqual(
                len(set().union(*packing_witnesses)),
                sum(map(len, packing_witnesses)),
            )
            centers = {
                vertex(index, offset)
                for index in range(count)
                for offset in (0, 3)
            }
            self.assertTrue(right.dominates(centers))
            self.assertEqual(right.domination_number(), 2 * count)

            exchange = {
                vertex(index, 4)
                for index in range(count)
            }
            exchange |= {
                vertex(index, 3)
                for index in range(count)
            }
            self.assertTrue(right.dominates(exchange))
            for index in range(count):
                demand = vertex(index, 1)
                self.assertEqual(
                    right.closed_neighborhood(demand)
                    & {
                        vertex(other, 4)
                        for other in range(count)
                    },
                    {a_zero},
                )

            # Fixed demands s_i all reuse a_0, but the universal adaptive
            # row matching chooses t_i and the distinct provider a_i.
            adaptive_providers = {
                index: vertex(index, 4)
                for index in range(count)
            }
            self.assertEqual(
                len(set(adaptive_providers.values())),
                count,
            )
            for index, provider in adaptive_providers.items():
                adaptive_target = vertex(index, 2)
                self.assertIn(
                    provider,
                    right.closed_neighborhood(adaptive_target),
                )
                self.assertNotIn(provider, blue_cells[index])
                self.assertIn(provider, red_cells[index])

            row_coordinates = {
                g: (
                    {
                        vertex(index, 4)
                        for index in range(count)
                    }
                    if g in terminal
                    else {
                        vertex(index, offset)
                        for index in range(count)
                        for offset in (0, 5)
                    }
                )
                for g in range(left.n)
            }
            chosen_pairs = {
                (g, h)
                for g, coordinates in row_coordinates.items()
                for h in coordinates
            }
            product_graph = left.cartesian_product(right)
            chosen = {
                g * right.n + h
                for g, h in chosen_pairs
            }
            self.assertTrue(product_graph.dominates(chosen))

            fibre_sets = []
            for cell in blue_cells + red_cells:
                fibre_sets.append(
                    {
                        g
                        for g in range(left.n)
                        if right.dominates(
                            row_coordinates[g] - cell,
                            cell,
                        )
                    }
                )
            self.assertEqual(
                fibre_sets,
                [terminal] * count + [set()] * count,
            )

            vertical_slack = (
                len(chosen_pairs)
                - sum(map(len, fibre_sets))
            )
            projection_additivity_subset_slack = (
                3 * count * (1 + 1)
                + 3 * count * 3
                + 3 * count
            )
            oriented_slack = (
                4 * len(chosen_pairs)
                - right.domination_number()
                * (
                    3 * left.domination_number()
                    - left.k_packing_number(2)
                )
            )
            self.assertEqual(vertical_slack, 4 * count)
            self.assertEqual(
                vertical_slack + projection_additivity_subset_slack,
                oriented_slack,
            )

    def test_bidirectional_blocker_certifies_small_p4_pairs(self) -> None:
        right = path(4)
        endpoints = {0, 3}
        self.assertTrue(
            all(len(right.closed_neighborhood(v) & endpoints) <= 1 for v in range(right.n))
        )
        for left in (path(2), path(3), path(4), cycle(4)):
            self.assertGreaterEqual(
                left.cartesian_product(right).domination_number(),
                2 * left.domination_number(),
            )

    def test_c5_blocker_saturation_defect_can_vanish(self) -> None:
        graph = cycle(5)
        weights = (
            Fraction(1, 2),
            Fraction(0),
            Fraction(1, 2),
            Fraction(0),
            Fraction(1, 2),
        )
        self.assertTrue(graph.is_fractional_packing_function(weights))
        loads = [
            sum((weights[u] for u in graph.closed_neighborhood(v)), Fraction(0))
            for v in range(graph.n)
        ]
        best_defect = min(
            sum((1 - loads[v] for v in chosen), Fraction(0))
            for size in range(graph.n + 1)
            for chosen in combinations(range(graph.n), size)
            if graph.dominates(chosen)
        )
        self.assertEqual(best_defect, 0)

    def test_common_crown_kills_private_row_density(self) -> None:
        base = cycle(4)
        crown = Graph.from_edges(
            7,
            list(base.edges)
            + [
                (4, 0),
                (0, 5),
                (4, 5),
                (2, 6),
                (4, 6),
            ],
        )
        owners = {0, 2}
        targets = {5, 6}
        self.assertEqual(crown.domination_number(), 2)
        self.assertTrue(crown.dominates(owners))
        self.assertEqual(crown.closed_neighborhood(4) & targets, targets)
        self.assertEqual(crown.closed_neighborhood(5) & owners, {0})
        self.assertEqual(crown.closed_neighborhood(6) & owners, {2})

        right = Graph.from_edges(2, [])
        product_graph = crown.cartesian_product(right)
        chosen = {g * right.n + h for g in owners for h in range(right.n)}
        self.assertEqual(product_graph.domination_number(), 4)
        self.assertTrue(product_graph.dominates(chosen))
        for owner, target in ((0, 5), (2, 6)):
            for h in range(right.n):
                private = target * right.n + h
                source = owner * right.n + h
                self.assertEqual(
                    product_graph.closed_neighborhood(private) & chosen,
                    {source},
                )


if __name__ == "__main__":
    unittest.main()
