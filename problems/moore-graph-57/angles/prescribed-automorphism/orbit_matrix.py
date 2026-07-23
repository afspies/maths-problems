"""Orbit-matrix machinery for Moore graph search with a prescribed
automorphism of prime order p (Behbahani-Lam style).

Setting: sigma is an automorphism of prime order p of a Moore graph of
degree d (n = d^2+1 vertices), with f fixed points and b_p = (n-f)/p orbits
of size p.  Orbits O_1..O_b (sizes n_i in {1, p}).  The orbit matrix is
    C[i][j] = |N(u) cap O_j|   for any u in O_i   (well-defined).

Necessary conditions (derived from A @ 1 = d 1 and A^2 = J + (d-1)I - A by
summing the srg identity over columns of an orbit):

  (R)  sum_j C[i][j] = d
  (Q)  sum_t C[i][t] * C[j][t] * n_j / n_t  =  n_j + (d-1)*[i==j] - C[i][j]
  (S)  C[i][j] * n_i = C[j][i] * n_j        (edge count between orbits)
  (F)  if n_i = 1, n_j = p:  C[i][j] in {0, p}   (invariant subset of orbit)
       if n_i = n_j = 1:     C[i][j] in {0, 1}
  (D)  C[i][i] even when n_i = p (within-orbit circulant is symmetric,
       no loops), and C[i][i] = 0 when n_i = 1.

Note (Q) for the pair (i,j) involves only rows i and j, enabling row-by-row
DFS: generate candidate rows, keep those compatible with all previous rows.

Lifting: block (i,j) of A is the p x p circulant given by a difference set
S_ij subset Z_p, |S_ij| = C[i][j], S_ji = -S_ij, S_ii = -S_ii, 0 not in
S_ii.  The full srg identity becomes, for every pair (i <= j) and every
g in Z_p:

  (L)  sum_t sum_h [h in S_it][g - h in S_tj]  + [g in S_ij]
         =  1 + (d-1) * [i == j and g == 0]

which we encode as exactly-k cardinality constraints over product variables
(CNF, solved with a SAT solver).
"""

from __future__ import annotations

import itertools
from typing import Iterator

import numpy as np


# ---------------------------------------------------------------------------
# Orbit-matrix search
# ---------------------------------------------------------------------------

def _candidate_rows(d: int, p: int, sizes: list[int], i: int,
                    self_even: bool = True) -> Iterator[tuple[int, ...]]:
    """All vectors row with sum d, 0 <= row[j] <= sizes[j], respecting (F)
    and (D) for row index i."""
    b = len(sizes)
    n_i = sizes[i]

    def domains(j: int) -> list[int]:
        n_j = sizes[j]
        if j == i:
            if n_i == 1:
                return [0]
            return [v for v in range(0, min(n_j, d) + 1) if v % 2 == 0]
        if n_i == 1 and n_j == p:
            return [0, p]
        if n_i == 1 and n_j == 1:
            return [0, 1]
        return list(range(0, min(n_j, d) + 1))

    doms = [domains(j) for j in range(b)]

    def rec(j: int, remaining: int, acc: list[int]):
        if j == b:
            if remaining == 0:
                yield tuple(acc)
            return
        max_rest = sum(max(doms[t]) for t in range(j + 1, b))
        for v in doms[j]:
            if v > remaining or remaining - v > max_rest:
                continue
            acc.append(v)
            yield from rec(j + 1, remaining - v, acc)
            acc.pop()

    yield from rec(0, d, [])


def _pair_ok(rows: list[tuple[int, ...]], sizes: list[int], d: int,
             i: int, j: int) -> bool:
    """Check condition (Q) for the pair (i, j) (rows i, j complete)."""
    lhs = sum(rows[i][t] * rows[j][t] * sizes[j] // sizes[t]
              for t in range(len(sizes)))
    rhs = sizes[j] + (d - 1) * (i == j) - rows[i][j]
    return lhs == rhs


def search_orbit_matrices(d: int, p: int, f: int,
                          max_solutions: int | None = None,
                          canonical: bool = True) -> list[np.ndarray]:
    """DFS for orbit matrices of a Moore graph of degree d with a prescribed
    order-p automorphism having f fixed points.  Fixed orbits come first.

    canonical=True adds a (sound) symmetry-breaking constraint: among the
    size-p orbits, rows must be lexicographically non-increasing on the
    sub-vector of entries that are invariant under reordering size-p orbits
    -- we use the weaker but valid pair (C[i][i], C[i][fixed block]) sorted
    non-increasingly.  This only prunes isomorphic reorderings of orbits, it
    cannot lose all representatives of an equivalence class.
    """
    n = d * d + 1
    assert (n - f) % p == 0
    b_p = (n - f) // p
    sizes = [1] * f + [p] * b_p
    b = len(sizes)

    solutions: list[np.ndarray] = []
    rows: list[tuple[int, ...]] = []

    def rec(i: int):
        if max_solutions is not None and len(solutions) >= max_solutions:
            return
        if i == b:
            solutions.append(np.array(rows, dtype=np.int64))
            return
        for row in _candidate_rows(d, p, sizes, i):
            # symmetry (S) against fixed previous rows
            ok = True
            for j in range(i):
                if row[j] * sizes[i] != rows[j][i] * sizes[j]:
                    ok = False
                    break
            if not ok:
                continue
            # canonical ordering among size-p orbits: non-increasing
            # (diagonal, fixed-block) signature
            if canonical and i > f:
                sig_prev = (rows[i - 1][i - 1], rows[i - 1][:f])
                sig_cur = (row[i], row[:f])
                if sig_cur > sig_prev:
                    continue
            rows.append(row)
            if all(_pair_ok(rows, sizes, d, i, j) for j in range(i + 1)):
                rec(i + 1)
            rows.pop()

    rec(0)
    return solutions


# ---------------------------------------------------------------------------
# Lifting an orbit matrix to an adjacency matrix via SAT
# ---------------------------------------------------------------------------

def lift_orbit_matrix(C: np.ndarray, d: int, p: int, f: int,
                      solver_name: str = "cadical195",
                      enumerate_all: bool = False,
                      max_models: int = 10):
    """Given an orbit matrix C, search for difference sets S_ij realizing an
    actual Moore graph.  Returns list of adjacency matrices (possibly empty).

    Variable x[(i,j,g)] (i < j, g in Z_p, both orbits size p): vertex (i,a)
    adjacent to (j,b) iff b - a = g.  For i == j: g and p-g are the same
    edge set; we use variables for g = 1..(p-1)//2.
    Fixed-vertex blocks are forced by C (all-or-nothing), no variables.
    """
    from pysat.formula import CNF, IDPool
    from pysat.card import CardEnc, EncType
    from pysat.solvers import Solver

    b = C.shape[0]
    sizes = [1] * f + [p] * (b - f)
    pool = IDPool()
    cnf = CNF()

    def value(i: int, j: int, g: int):
        """Return (kind, payload): ('const', 0/1) or ('var', lit)."""
        g = g % p
        if sizes[i] == 1 and sizes[j] == 1:
            return ('const', int(C[i, j]) if g == 0 else 0)
        if sizes[i] == 1:  # fixed -> orbit: all-or-nothing
            return ('const', 1 if C[i, j] == p else 0)
        if sizes[j] == 1:
            return ('const', 1 if C[j, i] == p else 0)
        if i == j:
            if g == 0:
                return ('const', 0)
            gg = min(g, p - g)
            return ('var', pool.id(('x', i, i, gg)))
        if i < j:
            return ('var', pool.id(('x', i, j, g)))
        return value(j, i, (-g) % p)

    # cardinality constraints |S_ij| = C[i][j]
    for i in range(b):
        for j in range(i, b):
            if sizes[i] == 1 or sizes[j] == 1:
                continue  # forced, no vars
            if i == j:
                lits = [value(i, i, g)[1] for g in range(1, (p - 1) // 2 + 1)]
                k = int(C[i, i])
                assert k % 2 == 0
                cnf.extend(CardEnc.equals(lits, bound=k // 2, vpool=pool,
                                          encoding=EncType.totalizer).clauses)
            else:
                lits = [value(i, j, g)[1] for g in range(p)]
                cnf.extend(CardEnc.equals(lits, bound=int(C[i, j]), vpool=pool,
                                          encoding=EncType.totalizer).clauses)

    # product variables and srg identity (L)
    def and_var(l1: int, l2: int) -> int:
        key = ('and', min(l1, l2), max(l1, l2))
        v = pool.id(key)
        if key not in and_var.done:
            and_var.done.add(key)
            cnf.append([-v, l1])
            cnf.append([-v, l2])
            cnf.append([v, -l1, -l2])
        return v
    and_var.done = set()

    for i in range(b):
        for j in range(i, b):
            for g in range(p if sizes[j] > 1 or sizes[i] > 1 else 1):
                if i == j and sizes[i] == 1 and g == 0:
                    continue  # trivial diagonal
                target = 1 + (d - 1) * (i == j and g == 0)
                const_sum = 0
                terms: list[int] = []
                for t in range(b):
                    for h in range(p if sizes[t] > 1 else 1):
                        va = value(i, t, h)
                        vb = value(t, j, g - h)
                        if va == ('const', 0) or vb == ('const', 0):
                            continue
                        if va[0] == 'const' and vb[0] == 'const':
                            const_sum += 1
                        elif va[0] == 'const':
                            terms.append(vb[1])
                        elif vb[0] == 'const':
                            terms.append(va[1])
                        else:
                            terms.append(and_var(va[1], vb[1]))
                # + [g in S_ij] term
                vij = value(i, j, g)
                if vij[0] == 'const':
                    const_sum += vij[1]
                else:
                    terms.append(vij[1])
                k = target - const_sum
                if k < 0 or k > len(terms):
                    return []  # orbit matrix infeasible at lift level
                if not terms:
                    continue
                cnf.extend(CardEnc.equals(terms, bound=k, vpool=pool,
                                          encoding=EncType.totalizer).clauses)

    # solve; enumeration blocks on the structural x-variables only
    x_vars = [v for key, v in pool.obj2id.items()
              if isinstance(key, tuple) and key[0] == 'x']
    models = []
    with Solver(name=solver_name, bootstrap_with=cnf.clauses) as s:
        while s.solve():
            m = s.get_model()
            pos = set(l for l in m if l > 0)
            models.append(pos)
            if not enumerate_all or len(models) >= max_models:
                break
            s.add_clause([-v if v in pos else v for v in x_vars])

    # build adjacency matrices
    out = []
    offsets = np.cumsum([0] + sizes)
    n = d * d + 1
    for pos in models:
        A = np.zeros((n, n), dtype=np.int64)
        for i in range(b):
            for j in range(i, b):
                for a in range(sizes[i]):
                    for bb in range(sizes[j]):
                        g = (bb - a) % p
                        kind, payload = value(i, j, g)
                        adj = payload if kind == 'const' else int(payload in pos)
                        if i == j and a == bb:
                            adj = 0
                        u, v = offsets[i] + a, offsets[j] + bb
                        if adj:
                            A[u, v] = A[v, u] = 1
        out.append(A)
    return out
