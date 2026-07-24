from fractions import Fraction
from itertools import combinations
import unittest

from graph_hygiene import (
    Graph,
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


if __name__ == "__main__":
    unittest.main()
