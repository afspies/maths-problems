"""CP-SAT version of the semiregular quotient feasibility problem.

Same mathematical object as quotient_scan.py (see its docstring for the
derivation and soundness of caps/symmetry breaking): find a symmetric
integer b x b matrix C, b = (d^2+1)/m, with

    row sums d,   C^2 + C - (d-1) I = m J,
    C[i][i] even if m odd,   C[i][i] <= diag_cap,   C[i][j] <= offdiag_cap,

or prove none exists.  CP-SAT gives real propagation on the quadratic
constraints and a trustworthy INFEASIBLE verdict (its UNSAT proofs are not
exported, so an infeasibility here is 'solver-verified' — to be replicated
independently before being cited as a theorem).

Symmetry breaking (sound, same argument as quotient_scan.py): C[0][0] is a
maximal diagonal entry; row 0 off-diagonal non-increasing.
"""

from __future__ import annotations

import sys
import time

import numpy as np
from ortools.sat.python import cp_model


def build(d: int, m: int, a_mult: int | None = None):
    """a_mult: optionally fix the multiplicity a of eigenvalue r on 1-perp
    via the trace identity tr C = d + r*a + s*(b-1-a).  Running all valid
    a values exhausts the space (a is determined by any concrete C)."""
    n = d * d + 1
    assert n % m == 0
    b = n // m
    disc = 4 * d - 3
    sq = int(round(disc ** 0.5))
    assert sq * sq == disc
    r = (-1 + sq) // 2
    diag_cap = min(m, d, (r * b + (d - r)) // b)
    offdiag_cap = min(m, d, (r * b + 2 * (d - r)) // b)

    mdl = cp_model.CpModel()
    C = {}
    for i in range(b):
        for j in range(i, b):
            cap = diag_cap if i == j else offdiag_cap
            v = mdl.new_int_var(0, cap, f"C_{i}_{j}")
            C[i, j] = C[j, i] = v
    # even diagonal for odd m
    if m % 2 == 1:
        for i in range(b):
            h = mdl.new_int_var(0, diag_cap // 2, f"h_{i}")
            mdl.add(C[i, i] == 2 * h)
    # row sums
    for i in range(b):
        mdl.add(sum(C[i, j] for j in range(b)) == d)
    # optional fixed spectral multiplicity via trace
    if a_mult is not None:
        s_eig = -1 - r
        trace = d + r * a_mult + s_eig * (b - 1 - a_mult)
        assert trace >= 0
        mdl.add(sum(C[i, i] for i in range(b)) == trace)
    # products
    P = {}
    for i in range(b):
        for j in range(i, b):
            for t in range(b):
                a, bb = C[i, t], C[j, t]
                key = tuple(sorted([(min(i, t), max(i, t)),
                                    (min(j, t), max(j, t))]))
                if key not in P:
                    cap_a = diag_cap if key[0][0] == key[0][1] else offdiag_cap
                    cap_b = diag_cap if key[1][0] == key[1][1] else offdiag_cap
                    pv = mdl.new_int_var(0, cap_a * cap_b, f"P_{key}")
                    mdl.add_multiplication_equality(
                        pv, [C[key[0]], C[key[1]]])
                    P[key] = pv
    def prod(i, j, t):
        key = tuple(sorted([(min(i, t), max(i, t)),
                            (min(j, t), max(j, t))]))
        return P[key]
    # quotient equation
    for i in range(b):
        for j in range(i, b):
            rhs = m + (d - 1) * (i == j) - C[i, j]
            mdl.add(sum(prod(i, j, t) for t in range(b)) == rhs)
    # symmetry breaking
    for i in range(1, b):
        mdl.add(C[i, i] <= C[0, 0])
    for j in range(1, b - 1):
        mdl.add(C[0, j + 1] <= C[0, j])
    return mdl, C, b


def solve(d: int, m: int, time_limit: float = 3600, workers: int = 8,
          log: bool = False, a_mult: int | None = None):
    mdl, C, b = build(d, m, a_mult=a_mult)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_workers = workers
    solver.parameters.log_search_progress = log
    t0 = time.time()
    status = solver.solve(mdl)
    dt = time.time() - t0
    name = solver.status_name(status)
    atag = f" a={a_mult}" if a_mult is not None else ""
    print(f"d={d} m={m} b={b}{atag}: {name} in {dt:.1f}s", flush=True)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        M = np.array([[solver.value(C[i, j]) for j in range(b)]
                      for i in range(b)], dtype=np.int64)
        chk = M @ M + M - (d - 1) * np.eye(b, dtype=np.int64)
        assert (chk == m).all(), "solution fails exact check!"
        print(M, flush=True)
        return name, M
    return name, None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d, m = int(sys.argv[1]), int(sys.argv[2])
        tl = float(sys.argv[3]) if len(sys.argv) > 3 else 3600
        am = int(sys.argv[4]) if len(sys.argv) > 4 else None
        wk = int(sys.argv[5]) if len(sys.argv) > 5 else 8
        solve(d, m, time_limit=tl, log=True, a_mult=am, workers=wk)
    else:
        for d, m in [(7, 25), (7, 10), (7, 5)]:
            solve(d, m, time_limit=60)
