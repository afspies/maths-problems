r"""Encode<->decode consistency test for the d=57 (s=3) case, which is the
only case that exercises cross-cycle Q variables and the gauge
normalization — untested by the d=3/d=7 validations (both have s=1).

Checks on a freshly solved model (permutation + trace constraints only):
  1. every leaf-leaf edge of the decoded A maps back (edge_var) to a
     positive literal of the model;
  2. every positive structural variable produces exactly its p=19 edges in
     A (checked in aggregate: edge counts match 84 * 56 * 19 / adjustment);
  3. decoded graph is 57-regular with the forced tree structure;
  4. the gauge blocks Q[0][c'][0] decode to identity matchings;
  5. a1 structure: #\{v : v ~ g^q(v)\} = 57 for each q (trace constraint,
     checked on A directly by applying the automorphism).
"""

import sys
import numpy as np

from equivariant_sat import EquivariantMooreSAT


def main():
    enc = EquivariantMooreSAT(57, 19, a1_per_power=57)
    assert enc.solver.solve(), "base constraints unsatisfiable?!"
    model = enc.solver.get_model()
    pos = set(l for l in model if l > 0)
    A = enc.decode(model)
    n, p, s, L = enc.n, enc.p, enc.s, enc.L
    base = 1 + s * p

    # 3. regularity and tree structure
    assert (A.sum(axis=1) == 57).all(), "not 57-regular"
    assert A[0, 1:base].all() and A[0, base:].sum() == 0, "root edges wrong"

    # 1. every leaf-leaf edge maps to a positive literal
    leaf_edges = np.argwhere(np.triu(A, 1)[base:, base:] == 1) + base
    for x, y in leaf_edges:
        cx, tx, ax = enc.leaf_of(int(x))
        cy, ty, ay = enc.leaf_of(int(y))
        v = enc.edge_var(cx, tx, ax, cy, ty, ay)
        assert v in pos, f"edge ({x},{y}) has no positive literal (var {v})"

    # 2. edge counts: 84 orbit matrices x 56 matched pairs x 19 shifts,
    # but same-cycle orbits (27 of them) produce 56*19 edges each and
    # cross-cycle orbits (57) also 56*19 — total leaf-leaf edges must be
    # 84 * 56 * 19 / 1 ... each edge counted once in decode:
    expect = 84 * 56 * 19
    got = int(np.triu(A, 1)[base:, base:].sum())
    assert got == expect, f"leaf-leaf edge count {got} != {expect}"

    # 4. gauge blocks are identity
    for cp in range(1, s):
        for t in range(p):
            for a in range(L):
                x = enc._index(0, t, a)
                y = enc._index(cp, t, a)
                assert A[x, y] == 1, f"gauge block c'={cp} not identity"

    # 5. a1(g^q) = 57 on the decoded graph, g = leaf/neighbour shift t->t+1
    perm = np.zeros(n, dtype=np.int64)
    perm[0] = 0
    for c in range(s):
        for t in range(p):
            perm[enc._index(c, t)] = enc._index(c, (t + 1) % p)
            for a in range(L):
                perm[enc._index(c, t, a)] = enc._index(c, (t + 1) % p, a)
    # check perm is an automorphism of A
    assert (A[np.ix_(perm, perm)] == A).all(), "g is not an automorphism!"
    for q in range(1, p):
        pq = perm.copy()
        for _ in range(q - 1):
            pq = perm[pq]
        a1 = sum(1 for v in range(n) if pq[v] != v and A[v, pq[v]])
        assert a1 == 57, f"a1(g^{q}) = {a1} != 57"

    print("ENCODING CONSISTENCY: all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
