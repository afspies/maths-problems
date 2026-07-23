r"""C7-equivariant SAT search for the (57, 7, 1) Moore graph.

The prescribed order-7 automorphism fixes exactly the adjacent vertices
``r1, r2``.  It rotates the 56 other neighbours of ``r1`` in eight cycles
``u[c][t]``, rotates ``B_R = N(r2) \\ {r1}`` by
``(tau, alpha) -> (tau+1, alpha)``, and sends each block leaf
``(c,t,a)`` to ``(c,t+1,a)``.  The sets ``{r1,r2}``, the ``u`` vertices,
``B_R``, and all block leaves are pairwise disjoint by construction in the
encoding (in a real Moore graph this follows from mu=1), giving exactly
``2 + 56 + 56 + 56*56 = 3250`` vertices.

Every non-tree edge is represented by one entry of a 56 by 56 permutation
matrix: 24 same-cycle P matrices, 196 cross-cycle Q matrices, and eight
B_R-to-block R matrices.  Thus there are exactly 228*3136 = 715008 primary
variables.  Girth is imposed lazily: a decoded exact-int64 adjacency matrix
is searched for triangles and 4-cycles, and their matching-edge conjunctions
are blocked.

The optional trace constraints (on by default) use a1(g^q)=49 for q=1,2,3:
``sum_c trace(P[c][q]) = 7``.  Citation: Ishida arXiv:2606.29183 Thm 1.2 /
Kovacikova, a1=7*a0+35, a0=2 — conditional on preprint.  Each true diagonal
entry accounts for its full seven-vertex t-orbit; the other vertex types make
no contribution for nonidentity powers.

The optional gauge normalization is sound symmetry breaking.  First,
``Q[0][c'][0]`` is fixed to identity for ``c'=1..7`` using the per-cycle
S_56 freedom to relabel the ``a`` index within cycles 1..7 relative to cycle
0.  Second, ``R[0]`` is fixed to identity (row ``7*alpha+delta`` maps to the
same ``a``) using cycle 0's own S_56 relabeling freedom similarly.  These are
pure relabelings and cost no solutions.  The residual t-origin Z7^8, cycle
permutation S_8, and B_R S_8 x Z7^8 symmetries are deliberately unbroken.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "harness"))
from verify import verify_moore  # noqa: E402

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver


class EquivariantMooreSAT:
    """Fixed-edge C7 encoder for d=57."""

    def __init__(self, d: int = 57, p: int = 7,
                 a1_per_power: int | None = 49,
                 solver: str = "cadical195", normalize: bool = True):
        assert (d, p) == (57, 7), "this encoding is specifically for d=57,p=7"
        self.d, self.p, self.s = d, p, 8
        self.L = 56
        self.n = d * d + 1
        self.a1 = a1_per_power
        self.pool = IDPool()
        self.solver = Solver(name=solver)
        self.n_clauses = 0
        self._build(normalize)

    # ---------------- variable layout ----------------

    def var_P(self, c: int, q: int, a: int, b: int) -> int:
        return self.pool.id(("P", c, q, a, b))

    def var_Q(self, c: int, cp: int, q: int, a: int, b: int) -> int:
        return self.pool.id(("Q", c, cp, q, a, b))

    def var_R(self, c: int, rho: int, a: int) -> int:
        return self.pool.id(("R", c, rho, a))

    def edge_var(self, c, t, a, cp, tp, b):
        """Literal for block leaf ``(c,t,a) ~ (cp,tp,b)``."""
        if c == cp:
            q0 = (tp - t) % self.p
            assert q0 != 0
            if q0 <= 3:
                return self.var_P(c, q0, a, b)
            return self.var_P(c, self.p - q0, b, a)
        if c < cp:
            return self.var_Q(c, cp, (tp - t) % self.p, a, b)
        return self.var_Q(cp, c, (t - tp) % self.p, b, a)

    def edge_var_br(self, tau: int, alpha: int, c: int, t: int,
                    a: int) -> int:
        """Literal for ``(tau,alpha) in B_R ~ (c,t,a)``."""
        rho = 7 * alpha + ((tau - t) % self.p)
        return self.var_R(c, rho, a)

    # ---------------- construction ----------------

    def _add(self, clauses):
        for clause in clauses:
            self.solver.add_clause(clause)
            self.n_clauses += 1

    def _exactly_one(self, lits):
        self._add(CardEnc.equals(lits, bound=1, vpool=self.pool,
                                 encoding=EncType.seqcounter).clauses)

    def _matrix_var(self, key, row, col):
        if key[0] == "P":
            return self.var_P(key[1], key[2], row, col)
        if key[0] == "Q":
            return self.var_Q(key[1], key[2], key[3], row, col)
        return self.var_R(key[1], row, col)

    def _build(self, normalize: bool):
        P = [("P", c, q) for c in range(8) for q in range(1, 4)]
        Q = [("Q", c, cp, q) for c in range(8)
             for cp in range(c + 1, 8) for q in range(7)]
        R = [("R", c) for c in range(8)]
        self.mats = P + Q + R
        self.n_primary_vars = len(self.mats) * self.L * self.L
        assert len(self.mats) == 228
        assert self.n_primary_vars == 715008

        for key in self.mats:
            get = lambda row, col, k=key: self._matrix_var(k, row, col)
            for row in range(self.L):
                self._exactly_one([get(row, col) for col in range(self.L)])
            for col in range(self.L):
                self._exactly_one([get(row, col) for row in range(self.L)])

        if self.a1 is not None:
            assert self.a1 == 49, "the fixed-edge C7 trace value is 49"
            for q in range(1, 4):
                diag = [self.var_P(c, q, a, a)
                        for c in range(8) for a in range(self.L)]
                self._add(CardEnc.equals(diag, bound=7, vpool=self.pool,
                                         encoding=EncType.totalizer).clauses)

        if normalize:
            for cp in range(1, 8):
                for a in range(self.L):
                    self._add([[self.var_Q(0, cp, 0, a, a)]])
            for rho in range(self.L):
                self._add([[self.var_R(0, rho, rho)]])

    # ---------------- vertex layout and decode ----------------

    def _index_u(self, c: int, t: int) -> int:
        return 2 + c * self.p + t

    def _index_br(self, tau: int, alpha: int) -> int:
        return 2 + 56 + tau * 8 + alpha

    def _index(self, c: int, t: int, a: int) -> int:
        return 2 + 56 + 56 + (c * self.p + t) * self.L + a

    @property
    def leaf_base(self) -> int:
        return 2 + 56

    @property
    def block_base(self) -> int:
        return 2 + 56 + 56

    def vertex_of(self, idx: int):
        """Return ``('BR',tau,alpha)`` or ``('B',c,t,a)`` for a leaf."""
        assert idx >= self.leaf_base
        if idx < self.block_base:
            tau, alpha = divmod(idx - self.leaf_base, 8)
            return "BR", tau, alpha
        block, a = divmod(idx - self.block_base, self.L)
        c, t = divmod(block, self.p)
        return "B", c, t, a

    def leaf_of(self, idx: int):
        """C19-compatible block-leaf inverse index."""
        kind, *coords = self.vertex_of(idx)
        assert kind == "B"
        return tuple(coords)

    def matching_edge_var(self, x: int, y: int) -> int:
        vx, vy = self.vertex_of(x), self.vertex_of(y)
        if vx[0] == vy[0] == "B":
            return self.edge_var(*vx[1:], *vy[1:])
        if vx[0] == "BR" and vy[0] == "B":
            return self.edge_var_br(vx[1], vx[2], *vy[1:])
        if vx[0] == "B" and vy[0] == "BR":
            return self.edge_var_br(vy[1], vy[2], *vx[1:])
        raise AssertionError("a CEGAR violation used a non-matching edge")

    def g_permutation(self) -> np.ndarray:
        perm = np.arange(self.n, dtype=np.int64)
        for c in range(8):
            for t in range(7):
                perm[self._index_u(c, t)] = self._index_u(c, (t + 1) % 7)
                for a in range(56):
                    perm[self._index(c, t, a)] = self._index(c, (t + 1) % 7, a)
        for tau in range(7):
            for alpha in range(8):
                perm[self._index_br(tau, alpha)] = self._index_br(
                    (tau + 1) % 7, alpha)
        return perm

    def decode(self, model) -> np.ndarray:
        pos = {lit for lit in model if lit > 0}
        A = np.zeros((self.n, self.n), dtype=np.int64)

        def edge(x, y):
            A[x, y] = A[y, x] = 1

        edge(0, 1)
        for c in range(8):
            for t in range(7):
                u = self._index_u(c, t)
                edge(0, u)
                for a in range(56):
                    edge(u, self._index(c, t, a))
        for tau in range(7):
            for alpha in range(8):
                edge(1, self._index_br(tau, alpha))

        for c in range(8):
            for q in range(1, 4):
                for a in range(56):
                    for b in range(56):
                        if self.var_P(c, q, a, b) in pos:
                            for t in range(7):
                                edge(self._index(c, t, a),
                                     self._index(c, (t + q) % 7, b))
        for c in range(8):
            for cp in range(c + 1, 8):
                for q in range(7):
                    for a in range(56):
                        for b in range(56):
                            if self.var_Q(c, cp, q, a, b) in pos:
                                for t in range(7):
                                    edge(self._index(c, t, a),
                                         self._index(cp, (t + q) % 7, b))
        for c in range(8):
            for alpha in range(8):
                for delta in range(7):
                    rho = 7 * alpha + delta
                    for a in range(56):
                        if self.var_R(c, rho, a) in pos:
                            for t in range(7):
                                tau = (t + delta) % 7
                                edge(self._index_br(tau, alpha),
                                     self._index(c, t, a))
        return A

    # ---------------- CEGAR ----------------

    def _violation_clauses(self, A: np.ndarray, max_tri: int = 60000,
                           max_quad: int = 100000, seed: int = 0):
        """Find exact-int64 short-cycle violations and return blocking cuts.

        Shifting every vertex of any violation by g preserves each P/Q/R
        literal: P and Q preserve t-differences, while R preserves tau-t.
        Consequently all seven translated cycles have the same literal
        conjunction, including cycles mixing B_R-block and block-block edges,
        and one clause blocks the whole orbit.
        """
        A = np.asarray(A, dtype=np.int64)
        P2 = A @ A
        upper = np.triu(np.ones(A.shape, dtype=bool), 1)
        tri = np.argwhere(upper & (A == 1) & (P2 > 0))
        quad = np.argwhere(upper & (A == 0) & (P2 >= 2))
        self.last_violations = (len(tri), len(quad))
        rng = np.random.default_rng(seed + self.n_clauses)
        rng.shuffle(tri)
        rng.shuffle(quad)
        clauses = set()

        def add_clause(edges):
            literals = tuple(sorted(-self.matching_edge_var(x, y)
                                    for x, y in edges))
            clauses.add(literals)

        ntri = 0
        for x, y in tri:
            if x < self.leaf_base:
                continue
            for z in np.flatnonzero(A[x] & A[y]):
                if z < self.leaf_base:
                    continue
                add_clause(((int(x), int(y)), (int(y), int(z)),
                            (int(z), int(x))))
                ntri += 1
                if ntri >= max_tri:
                    break
            if ntri >= max_tri:
                break

        nquad = 0
        for x, y in quad:
            if x < self.leaf_base or y < self.leaf_base:
                continue
            common = [int(w) for w in np.flatnonzero(A[x] & A[y])
                      if w >= self.leaf_base]
            for i in range(len(common)):
                for j in range(i + 1, len(common)):
                    w1, w2 = common[i], common[j]
                    add_clause(((int(x), w1), (w1, int(y)),
                                (int(y), w2), (w2, int(x))))
                    nquad += 1
                    if nquad >= max_quad:
                        break
                if nquad >= max_quad:
                    break
            if nquad >= max_quad:
                break
        return [list(clause) for clause in clauses]

    def run(self, max_iters: int = 100000, time_budget: float = 3600,
            log_every: int = 1, log=print, cut_file: str | None = None):
        """Run resumable CEGAR, returning SAT, UNSAT, or TIMEOUT."""
        t0 = time.time()
        if cut_file and Path(cut_file).exists():
            reloaded = 0
            with open(cut_file) as fh:
                for line in fh:
                    self.solver.add_clause([int(x) for x in line.split()])
                    self.n_clauses += 1
                    reloaded += 1
            log(f"reloaded {reloaded:,} persisted cuts from {cut_file}")
        sink = open(cut_file, "a") if cut_file else None
        iteration = 0
        while True:
            iteration += 1
            if time.time() - t0 > time_budget or iteration > max_iters:
                if sink:
                    sink.close()
                return ("TIMEOUT", {"iters": iteration,
                                    "clauses": self.n_clauses,
                                    "elapsed": time.time() - t0})
            if not self.solver.solve():
                log(f"[{iteration}] UNSAT after {self.n_clauses:,} clauses, "
                    f"{time.time()-t0:.1f}s")
                if sink:
                    sink.close()
                return "UNSAT", None
            A = self.decode(self.solver.get_model())
            new = self._violation_clauses(A)
            if not new:
                log(f"[{iteration}] girth-5 model found! verifying...")
                verify_moore(A, self.d)
                if sink:
                    sink.close()
                return "SAT", A
            self._add(new)
            if sink:
                for clause in new:
                    sink.write(" ".join(map(str, clause)) + "\n")
                sink.flush()
            if iteration % log_every == 0:
                vt, vq = self.last_violations
                log(f"[{iteration}] viol tri={vt:,} quad={vq:,}; "
                    f"+{len(new):,} cuts (total {self.n_clauses:,}), "
                    f"{time.time()-t0:.1f}s")
