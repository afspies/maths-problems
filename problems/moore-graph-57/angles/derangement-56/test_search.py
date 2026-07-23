#!/usr/bin/env python3
"""Independent checks for the gain-graph solver and obstruction."""

from __future__ import annotations

import unittest

from search import GainSearch, build_moore_adjacency, get_group, quotient_obstruction

from harness.verify import verify_moore


def enumerate_row_complete(group_key: str) -> tuple[int, int, int]:
    """Naively enumerate every (V)-assignment; check (T),(Q) only at leaves.

    This intentionally shares neither the production solver's cycle pruning
    nor its Hall-union pruning.  It is a small independent exhaustiveness check
    for the q=6 smoke cases.
    """
    group = get_group(group_key)
    q = group.order
    gain = [[-1] * q for _ in range(q)]
    used = [set() for _ in range(q)]
    for j, value in enumerate(range(1, q), start=1):
        gain[0][j] = value
        gain[j][0] = group.inverse[value]
        used[0].add(value)
        used[j].add(group.inverse[value])
    edges = [(i, j) for i in range(1, q) for j in range(i + 1, q)]
    nodes = leaves = valid = 0

    def product(values: tuple[int, ...]) -> int:
        result = 0
        for value in values:
            result = group.mul(result, value)
        return result

    def is_valid_leaf() -> bool:
        nonidentity = set(range(1, q))
        if any(set(gain[i][j] for j in range(q) if j != i) != nonidentity for i in range(q)):
            return False
        for i in range(q):
            for j in range(i + 1, q):
                for k in range(j + 1, q):
                    if product((gain[i][j], gain[j][k], gain[k][i])) == 0:
                        return False
        # Three undirected 4-cycles per set of four vertices suffice.
        for a in range(q):
            for b in range(a + 1, q):
                for c in range(b + 1, q):
                    for d in range(c + 1, q):
                        cycles = ((a, b, c, d), (a, b, d, c), (a, c, b, d))
                        for i, j, k, ell in cycles:
                            if product((gain[i][j], gain[j][k], gain[k][ell], gain[ell][i])) == 0:
                                return False
        return True

    def visit(pos: int) -> None:
        nonlocal nodes, leaves, valid
        if pos == len(edges):
            leaves += 1
            valid += int(is_valid_leaf())
            return
        i, j = edges[pos]
        for value in range(1, q):
            inverse = group.inverse[value]
            if value in used[i] or inverse in used[j]:
                continue
            nodes += 1
            gain[i][j], gain[j][i] = value, inverse
            used[i].add(value)
            used[j].add(inverse)
            visit(pos + 1)
            used[i].remove(value)
            used[j].remove(inverse)
            gain[i][j] = gain[j][i] = -1

    visit(0)
    return nodes, leaves, valid


class GainSearchTests(unittest.TestCase):
    def test_petersen_witness_verifies(self) -> None:
        group = get_group("z2")
        gain, stats = GainSearch(group).solve()
        self.assertEqual(stats.status, "SAT")
        self.assertIsNotNone(gain)
        verify_moore(build_moore_adjacency(group, gain), 3, verbose=False)

    def test_independent_z6_exhaustion(self) -> None:
        self.assertEqual(enumerate_row_complete("z6"), (146, 14, 0))

    def test_independent_s3_exhaustion(self) -> None:
        self.assertEqual(enumerate_row_complete("s3"), (110, 10, 0))

    def test_quotient_obstruction_small_sanity(self) -> None:
        self.assertIsNone(quotient_obstruction(get_group("z2")))
        self.assertIsNotNone(quotient_obstruction(get_group("z6")))
        self.assertIsNotNone(quotient_obstruction(get_group("s3")))
        self.assertIsNotNone(quotient_obstruction(get_group("h1")))
        self.assertIsNotNone(quotient_obstruction(get_group("h2")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
