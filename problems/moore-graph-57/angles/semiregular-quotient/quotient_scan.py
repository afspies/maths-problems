"""Semiregular quotient feasibility scan for the degree-57 Moore graph.

If a group G with |G| = m acts semiregularly (all orbits of size m) on a
Moore graph of degree d, the quotient matrix C (b = n/m orbits,
C[i][j] = #neighbours in orbit j of any vertex of orbit i) satisfies:

    (1) C symmetric, integer, 0 <= C[i][j] <= min(m, d)
    (2) row sums d
    (3) C^2 + C - (d-1) I = m J        (collapse of the srg identity)
    (4) if m is odd: C[i][i] even      (within-orbit connection set S=S^-1
                                        has no involutions to pair with)

Consequences of (2)+(3): on 1-perp, C has eigenvalues 7/-8 (for d=57), so
trace C = 57 + 7a - 8(b-1-a) for some integer 0 <= a <= b-1.

NONEXISTENCE of C for a given m excludes ALL semiregular actions of ANY
group of order m — a citable exclusion lemma (modulo prior literature).

The search fills the upper triangle row by row.  Row i must satisfy
    sum_j C[i][j] = d,
    sum_j C[i][j]^2 = m + (d-1) - C[i][i]          (self pair condition)
    sum_t C[i][t] C[j][t] = m - C[i][j]  (j < i)   (cross pair condition)
with Cauchy-Schwarz / cap pruning on partial rows.

Symmetry breaking (sound for feasibility AND for exhaustive nonexistence):
the symmetry group is simultaneous row+column permutation.  Any solution
can be relabelled so that (i) vertex 0 has a maximal diagonal entry and
(ii) the off-diagonal entries of row 0 are non-increasing (sort indices
1..b-1 by C[0][j] descending).  So restricting the search to matrices
satisfying (i)+(ii) loses no equivalence class.

PSD entry caps (necessary): on 1-perp C has eigenvalues r > s (7, -8 for
d=57), and E_s = (rI + ((d-r)/b)J - C)/(r-s) is an orthogonal projection
(C = d J/b + r E_r + s E_s with E_r + E_s = I - J/b).  Write a = (d-r)/b.
Then (E_s)_ii = (r + a - C_ii)/(r-s) >= 0 gives C_ii <= r + a; and since
C_ii >= 0 also (E_s)_ii <= (r + a)/(r-s), so by Cauchy-Schwarz on the
projection Gram matrix |(E_s)_ij| <= sqrt((E_s)_ii (E_s)_jj) <=
(r + a)/(r-s), giving C_ij <= a + (r-s) * (r+a)/(r-s) = r + 2a.
"""

from __future__ import annotations

import sys
import time

import numpy as np


class Budget(Exception):
    pass


def search_quotients(d: int, m: int, max_solutions: int | None = 1,
                     require_even_diag: bool | None = None,
                     progress: bool = False,
                     max_nodes: int | None = None):
    """Returns (solutions, nodes, complete). complete=False iff the node
    budget was exhausted (result then inconclusive if no solution found)."""
    n = d * d + 1
    assert n % m == 0, f"m={m} does not divide n={n}"
    b = n // m
    if require_even_diag is None:
        require_even_diag = (m % 2 == 1)
    # PSD entry caps.  On 1-perp, C has eigenvalues r > s with
    # r+s = -1, rs = -(d-1); C = rI + ((d-r)/b) J - (r-s) E_s with E_s a
    # (scaled) orthogonal projection, so 0 <= (E_s)_ii <= 1 and
    # |(E_s)_ij| <= max (E_s)_ii.  This gives
    #   C_ii <= r + (d-r)/b,     C_ij <= r + 2(d-r)/b.
    disc = 4 * d - 3
    sq = int(round(disc ** 0.5))
    assert sq * sq == disc
    r_eig = (-1 + sq) // 2
    diag_cap = min(m, d, (r_eig * b + (d - r_eig)) // b)
    offdiag_cap = min(m, d, (r_eig * b + 2 * (d - r_eig)) // b)
    cap = offdiag_cap

    C = np.zeros((b, b), dtype=np.int64)
    solutions: list[np.ndarray] = []
    nodes = [0]

    def fill_row(i: int, j: int, rem_sum: int, rem_sq: int,
                 ips: list[int]):
        """Choose C[i][j] .. C[i][b-1].  rem_sum/rem_sq: what the suffix must
        sum to (linearly / in squares).  ips[t] for t<i: remaining inner
        product needed with row t over columns j..b-1."""
        nodes[0] += 1
        if max_nodes is not None and nodes[0] > max_nodes:
            raise Budget()
        if max_solutions is not None and len(solutions) >= max_solutions:
            return
        cols_left = b - j
        if j == b:
            if rem_sum == 0 and rem_sq == 0 and all(v == 0 for v in ips):
                next_row(i + 1)
            return
        # bounds: suffix of cols_left nonneg integers with given sum & sumsq
        if rem_sum < 0 or rem_sq < 0:
            return
        if rem_sum * rem_sum > cols_left * rem_sq:   # Cauchy-Schwarz
            return
        if rem_sq > rem_sum * cap:                    # sum x^2 <= max * sum x
            return
        if any(v < 0 for v in ips):
            return
        # upper bound on achievable remaining inner products:
        # ip with row t <= sqrt(rem_sq * sum_{cols>=j} C[t][col]^2)
        for t in range(i):
            tail_sq = int((C[t, j:] ** 2).sum())
            if ips[t] * ips[t] > rem_sq * tail_sq:
                return
        if j == i:  # diagonal entry
            hi = min(diag_cap, rem_sum)
            # symmetry breaking (sound, see docstring): vertex 0 has the
            # maximal diagonal entry
            if i > 0:
                hi = min(hi, int(C[0, 0]))
            step = 2 if require_even_diag else 1
            vals = range(0, hi + 1, step)
        else:
            hi = min(offdiag_cap, rem_sum)
            # symmetry breaking: row 0 off-diagonal entries non-increasing
            if i == 0 and j >= 2:
                hi = min(hi, int(C[0, j - 1]))
            vals = range(0, hi + 1)
        for v in vals:
            if j == i:
                # self condition fixes rem_sq for the whole row:
                # sum_t C[i][t]^2 = m + (d-1) - v ; prefix squares already
                # counted in rem_sq bookkeeping by caller for j=i (see
                # next_row) -- here rem_sq passed as None-sentinel handled
                # there.  We recompute:
                total_sq = m + (d - 1) - v
                prefix_sq = int((C[i, :i] ** 2).sum())
                new_rem_sq = total_sq - prefix_sq - v * v
                if new_rem_sq < 0:
                    continue
                C[i, i] = v
                new_ips = [ips[t] - v * int(C[t, i]) for t in range(i)]
                fill_row(i, i + 1, rem_sum - v, new_rem_sq, new_ips)
                C[i, i] = 0
            else:
                C[i, j] = v
                C[j, i] = v  # j > i here; keep symmetric view for tails
                new_ips = [ips[t] - v * int(C[t, j]) for t in range(i)]
                fill_row(i, j + 1, rem_sum - v, rem_sq - v * v, new_ips)
                C[i, j] = 0
                C[j, i] = 0

    def next_row(i: int):
        if max_solutions is not None and len(solutions) >= max_solutions:
            return
        if i == b:
            # full verification of (2),(3)
            M = C @ C + C - (d - 1) * np.eye(b, dtype=np.int64)
            assert (M == m).all(), f"internal error:\n{C}"
            solutions.append(C.copy())
            return
        if progress and i <= 3:
            print(f"  row {i}, nodes={nodes[0]:,}", file=sys.stderr)
        prefix = [int(C[i, t]) for t in range(i)]
        rem_sum = d - sum(prefix)
        # rem_sq is determined once the diagonal C[i][i] is chosen; pass a
        # loose bound for the pre-diagonal pruning step
        rem_sq_loose = m + (d - 1) - int(np.dot(prefix, prefix))
        ips = []
        for t in range(i):
            full_ip = m - int(C[i, t])           # required total <row i, row t>
            done = int(np.dot(C[i, :i], C[t, :i]))
            ips.append(full_ip - done)
        fill_row(i, i, rem_sum, rem_sq_loose, ips)

    complete = True
    try:
        next_row(0)
    except Budget:
        complete = False
    return solutions, nodes[0], complete


def run_case(d: int, m: int, max_solutions=1, max_nodes=None):
    t0 = time.time()
    sols, nodes, complete = search_quotients(
        d, m, max_solutions=max_solutions, max_nodes=max_nodes)
    dt = time.time() - t0
    if sols:
        status = "FEASIBLE"
    elif complete:
        status = "INFEASIBLE (exhaustive)"
    else:
        status = f"UNKNOWN (budget {max_nodes:,} nodes exhausted)"
    print(f"d={d} m={m} b={(d*d+1)//m}: {status} ({nodes:,} nodes, {dt:.1f}s)",
          flush=True)
    for s in sols:
        print(s, flush=True)
    return sols, complete


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d, m = int(sys.argv[1]), int(sys.argv[2])
        nsol = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        budget = int(sys.argv[4]) if len(sys.argv) > 4 else None
        run_case(d, m, max_solutions=nsol, max_nodes=budget)
    else:
        # self-test at d=7 (HoS exists, so every m with a genuine semiregular
        # action must be FEASIBLE; feasibility for other m is also fine —
        # the conditions are only necessary)
        for d, m in [(7, 25), (7, 10), (7, 5), (7, 2)]:
            run_case(d, m, max_nodes=50_000_000)
