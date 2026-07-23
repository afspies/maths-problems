"""Consistency tests for the fixed-edge C7 equivariant encoding."""

import numpy as np
import unittest

from equivariant_sat import EquivariantMooreSAT


def planted_assumptions(enc, p_permutations=None):
    p_permutations = p_permutations or {}
    assumptions = []
    for key in enc.mats:
        perm = p_permutations.get(key, list(range(56)))
        for row, col in enumerate(perm):
            assumptions.append(enc._matrix_var(key, row, col))
    return assumptions


def permutation_with_fixed_points(k):
    assert 0 <= k <= 54 or k == 56
    perm = list(range(56))
    tail = list(range(k, 56))
    if tail:
        tail = tail[1:] + tail[:1]
        perm[k:] = tail
    return perm


class EncodingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The all-identity assignment intentionally does not obey trace=49.
        cls.enc = EquivariantMooreSAT(a1_per_power=None)

    def test_primary_variable_count(self):
        self.assertEqual(len(self.enc.mats), 228)
        self.assertEqual(self.enc.n_primary_vars, 715008)

    def test_edge_var_round_trip_and_equivariance(self):
        enc = self.enc
        rng = np.random.default_rng(20260722)
        for _ in range(1000):
            c, cp = rng.integers(0, 8, size=2)
            t, tp = rng.integers(0, 7, size=2)
            if c == cp and t == tp:
                tp = (tp + 1) % 7
            a, b = rng.integers(0, 56, size=2)
            v = enc.edge_var(c, t, a, cp, tp, b)
            self.assertEqual(v, enc.edge_var(cp, tp, b, c, t, a))
            self.assertEqual(v, enc.edge_var(c, (t + 1) % 7, a, cp,
                                             (tp + 1) % 7, b))

            tau = int(rng.integers(0, 7))
            alpha = int(rng.integers(0, 8))
            vr = enc.edge_var_br(tau, alpha, c, t, a)
            self.assertEqual(vr, enc.edge_var_br((tau + 1) % 7, alpha, c,
                                                 (t + 1) % 7, a))
            x, y = enc._index_br(tau, alpha), enc._index(c, t, a)
            self.assertEqual(vr, enc.matching_edge_var(x, y))
            self.assertEqual(vr, enc.matching_edge_var(y, x))

    def test_hand_planted_decode_is_regular_and_equivariant(self):
        enc = self.enc
        assumptions = planted_assumptions(enc)
        self.assertTrue(enc.solver.solve(assumptions=assumptions))
        A = enc.decode(enc.solver.get_model())
        self.assertEqual(A.dtype, np.int64)
        self.assertEqual(A.shape, (3250, 3250))
        self.assertTrue(np.array_equal(A, A.T))
        self.assertFalse(np.diag(A).any())
        self.assertTrue(np.all(A.sum(axis=1) == 57))
        perm = enc.g_permutation()
        # Equivalent to P_g @ A @ P_g.T without materializing dense P_g.
        self.assertTrue(np.array_equal(A[np.ix_(perm, perm)], A))

    def test_trace_constraint_counting(self):
        traced = EquivariantMooreSAT()
        p_permutations = {}
        # For each q, seven matrices have one fixed point and one has none.
        for q in range(1, 4):
            for c in range(8):
                p_permutations[("P", c, q)] = permutation_with_fixed_points(
                    1 if c < 7 else 0)
        assumptions = planted_assumptions(traced, p_permutations)
        self.assertTrue(traced.solver.solve(assumptions=assumptions))
        A = traced.decode(traced.solver.get_model())
        perm = traced.g_permutation()
        for q in range(1, 4):
            pq = np.arange(traced.n)
            for _ in range(q):
                pq = perm[pq]
            direct_a1 = int(A[np.arange(traced.n), pq].sum())
            diagonal_count = sum(
                p_permutations[("P", c, q)][a] == a
                for c in range(8) for a in range(56))
            self.assertEqual(diagonal_count, 7)
            self.assertEqual(direct_a1, 7 * diagonal_count)
            self.assertEqual(direct_a1, 49)

    def test_single_cut_is_invariant_for_mixed_br_cycle(self):
        """Mixed BR/block cycles' translates have one literal set."""
        enc = self.enc

        def literals(vs):
            return sorted(enc.matching_edge_var(vs[i], vs[(i + 1) % len(vs)])
                          for i in range(len(vs)))

        triangle = [enc._index_br(2, 3), enc._index(1, 5, 11),
                    enc._index(4, 0, 17)]
        quadrilateral = [enc._index_br(6, 1), enc._index(0, 2, 9),
                         enc._index(3, 4, 22), enc._index(7, 1, 31)]
        perm = enc.g_permutation()
        for vertices in (triangle, quadrilateral):
            shifted = [int(perm[v]) for v in vertices]
            self.assertEqual(literals(vertices), literals(shifted))


if __name__ == "__main__":
    unittest.main()
