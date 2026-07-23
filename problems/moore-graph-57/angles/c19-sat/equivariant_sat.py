r"""C_p-equivariant SAT search for Moore graphs with a prescribed order-p
automorphism fixing exactly one vertex.

Setting (d = s*p, n = d^2+1): automorphism g of prime order p fixes the root
r, rotates the d = s*p neighbours in s cycles u[c][t] (t in Z_p), and acts
freely on the d*(d-1) leaves.  Leaves get g-equivariant labels (c, t, a),
a in [d-1]: block B[c][t] = N(u[c][t]) \ {r}, g(c,t,a) = (c,t+1,a).

Forced structure (girth 5): each block is independent; between any two
blocks there is a perfect matching; matchings are g-equivariant, so they are
determined by one permutation matrix per g-orbit of block pairs:
  - P[c][q], q = 1..(p-1)/2:  (c,t,a) ~ (c,t+q,b)   iff P[c][q][a][b]
  - Q[c][c'][q], c<c', q in Z_p: (c,t,a) ~ (c',t+q,b) iff Q[c][c'][q][a][b]
(s*(p-1)/2 + s(s-1)/2*p orbits; for d=57,p=19,s=3: 27+57 = 84.)

Remaining constraints = girth 5 among leaves: no triangles (3 distinct
blocks) and no 4-cycles (4 distinct blocks); all other short cycles are
impossible by the forced structure.  A d-regular graph on d^2+1 vertices
with girth 5 is automatically srg(n,d,0,1) by counting, so no mu-clauses
are needed.

Optional trace constraints: a1(g^q) = #vertices moved to a neighbour by g^q.
Only leaf orbits with diagonal matching fixed points contribute (p each):
  sum_c trace(P[c][q]) = a1(g^q) / p    for q = 1..(p-1)/2.
For d=57, Ishida (arXiv:2606.29183) Thm 1.2 gives a1 = 57, so the sum is 3.

Girth constraints are added lazily (CEGAR): solve, decode the full graph,
find triangles/4-cycles exactly (integer matmul), block each violating
g-orbit with one clause, repeat.  UNSAT of the accumulated formula is a
valid proof of nonexistence for the prescribed symmetry (all added clauses
are consequences of girth 5).
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "harness"))
from verify import verify_moore  # noqa: E402

from pysat.formula import IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


class EquivariantMooreSAT:
    def __init__(self, d: int, p: int, a1_per_power: int | None = None,
                 solver: str = "cadical195", normalize: bool = True):
        assert d % p == 0
        self.d, self.p, self.s = d, p, d // p
        self.L = d - 1                       # leaves per block
        self.n = d * d + 1
        self.a1 = a1_per_power               # a1(g^q), same for all q, or None
        self.pool = IDPool()
        self.solver = Solver(name=solver)
        self.n_clauses = 0
        self._build(normalize)

    # ---------------- variable layout ----------------

    def var_P(self, c: int, q: int, a: int, b: int) -> int:
        return self.pool.id(('P', c, q, a, b))

    def var_Q(self, c: int, cp: int, q: int, a: int, b: int) -> int:
        return self.pool.id(('Q', c, cp, q, a, b))

    def edge_var(self, c, t, a, cp, tp, b):
        """SAT literal asserting leaf (c,t,a) ~ leaf (cp,tp,b)."""
        p = self.p
        if c == cp:
            q0 = (tp - t) % p
            assert q0 != 0
            if q0 <= (p - 1) // 2:
                return self.var_P(c, q0, a, b)
            return self.var_P(c, p - q0, b, a)
        if c < cp:
            return self.var_Q(c, cp, (tp - t) % p, a, b)
        return self.var_Q(cp, c, (t - tp) % p, b, a)

    # ---------------- construction ----------------

    def _add(self, clauses):
        for cl in clauses:
            self.solver.add_clause(cl)
            self.n_clauses += 1

    def _exactly_one(self, lits):
        self._add(CardEnc.equals(lits, bound=1, vpool=self.pool,
                                 encoding=EncType.seqcounter).clauses)

    def _build(self, normalize: bool):
        d, p, s, L = self.d, self.p, self.s, self.L
        half = (p - 1) // 2
        # permutation constraints
        mats = [('P', c, q) for c in range(s) for q in range(1, half + 1)] + \
               [('Q', c, cp, q) for c in range(s) for cp in range(c + 1, s)
                for q in range(p)]
        self.mats = mats
        for key in mats:
            get = (lambda a, b, k=key: self.var_P(k[1], k[2], a, b)
                   if k[0] == 'P' else self.var_Q(k[1], k[2], k[3], a, b))
            for a in range(L):
                self._exactly_one([get(a, b) for b in range(L)])
            for b in range(L):
                self._exactly_one([get(a, b) for a in range(L)])
        # trace constraints on same-cycle matchings
        if self.a1 is not None:
            assert self.a1 % p == 0
            k = self.a1 // p
            for q in range(1, half + 1):
                diag = [self.var_P(c, q, a, a) for c in range(s)
                        for a in range(L)]
                self._add(CardEnc.equals(diag, bound=k, vpool=self.pool,
                                         encoding=EncType.totalizer).clauses)
        # gauge normalization: Q[0][c'][0] := identity for c' = 1..s-1
        if normalize:
            for cp in range(1, s):
                for a in range(L):
                    for b in range(L):
                        lit = self.var_Q(0, cp, 0, a, b)
                        self._add([[lit if a == b else -lit]])

    # ---------------- decode ----------------

    def _index(self, c, t, a=None):
        """Vertex index: 0 = root; neighbours; leaves."""
        if a is None:
            return 1 + c * self.p + t
        return 1 + self.s * self.p + (c * self.p + t) * self.L + a

    def decode(self, model) -> np.ndarray:
        d, p, s, L, n = self.d, self.p, self.s, self.L, self.n
        pos = set(l for l in model if l > 0)
        A = np.zeros((n, n), dtype=np.int64)
        for c in range(s):
            for t in range(p):
                u = self._index(c, t)
                A[0, u] = A[u, 0] = 1
                for a in range(L):
                    w = self._index(c, t, a)
                    A[u, w] = A[w, u] = 1
        # matchings
        half = (p - 1) // 2
        for c in range(s):
            for q in range(1, half + 1):
                for a in range(L):
                    for b in range(L):
                        if self.var_P(c, q, a, b) in pos:
                            for t in range(p):
                                x = self._index(c, t, a)
                                y = self._index(c, (t + q) % p, b)
                                A[x, y] = A[y, x] = 1
        for c in range(s):
            for cp in range(c + 1, s):
                for q in range(p):
                    for a in range(L):
                        for b in range(L):
                            if self.var_Q(c, cp, q, a, b) in pos:
                                for t in range(p):
                                    x = self._index(c, t, a)
                                    y = self._index(cp, (t + q) % p, b)
                                    A[x, y] = A[y, x] = 1
        return A

    def leaf_of(self, idx: int):
        base = 1 + self.s * self.p
        assert idx >= base
        block, a = divmod(idx - base, self.L)
        c, t = divmod(block, self.p)
        return c, t, a

    # ---------------- CEGAR ----------------

    def _violation_clauses(self, A: np.ndarray, max_tri: int = 60000,
                           max_quad: int = 100000, seed: int = 0):
        """Blocking clauses for triangles and 4-cycles among leaves.
        Violating pairs are sampled uniformly (shuffled) so cuts spread over
        the whole graph instead of clustering at low vertex indices.
        Also records self.last_violations = (#tri pairs, #quad pairs)."""
        # float64 matmul is used ONLY to *select candidate* violating pairs
        # (fast path); every emitted clause is then built from exact integer
        # adjacency lists (A[x] & A[y]), so a hypothetical float error can
        # only miss candidates (weaker formula), never emit an unsound cut.
        # A "no violations" outcome is re-checked by the exact verifier.
        Af = A.astype(np.float64)
        P2 = (Af @ Af).astype(np.int64)
        clauses = set()
        base = 1 + self.s * self.p
        rng = np.random.default_rng(seed + self.n_clauses)

        def evar(x, y):
            cx, tx, ax = self.leaf_of(x)
            cy, ty, ay = self.leaf_of(y)
            return self.edge_var(cx, tx, ax, cy, ty, ay)

        # triangles: adjacent pair with a common neighbour
        tri = np.argwhere((P2 > 0) & (A == 1) &
                          (np.arange(self.n)[:, None] < np.arange(self.n)))
        quad = np.argwhere((P2 >= 2) & (A == 0) &
                           (np.arange(self.n)[:, None] < np.arange(self.n)))
        self.last_violations = (len(tri), len(quad))
        rng.shuffle(tri)
        rng.shuffle(quad)
        ntri = 0
        for x, y in tri:
            if x < base:
                continue
            commons = np.flatnonzero(A[x] & A[y])
            for z in commons:
                if z < base:
                    continue
                cl = tuple(sorted((-evar(x, y), -evar(y, z), -evar(x, z))))
                if cl not in clauses:
                    clauses.add(cl)
                    ntri += 1
            if ntri >= max_tri:
                break
        nquad = 0
        for x, y in quad:
            if x < base or y < base:
                continue
            commons = [w for w in np.flatnonzero(A[x] & A[y]) if w >= base]
            for i in range(len(commons)):
                for j in range(i + 1, len(commons)):
                    w1, w2 = commons[i], commons[j]
                    cl = tuple(sorted((-evar(x, w1), -evar(w1, y),
                                       -evar(y, w2), -evar(w2, x))))
                    if cl not in clauses:
                        clauses.add(cl)
                        nquad += 1
            if nquad >= max_quad:
                break
        return [list(c) for c in clauses]

    def run(self, max_iters: int = 100000, time_budget: float = 3600,
            log_every: int = 1, log=print, cut_file: str | None = None):
        """Returns ('SAT', A) with a verified Moore graph, ('UNSAT', None),
        or ('TIMEOUT', stats).  cut_file: persist/reload CEGAR cuts (one
        clause per line, ints) so runs are resumable."""
        t0 = time.time()
        if cut_file and Path(cut_file).exists():
            reloaded = 0
            with open(cut_file) as fh:
                for line in fh:
                    self.solver.add_clause([int(x) for x in line.split()])
                    self.n_clauses += 1
                    reloaded += 1
            log(f"reloaded {reloaded:,} persisted cuts from {cut_file}")
        sink = open(cut_file, 'a') if cut_file else None
        it = 0
        nviol = 0
        while True:
            it += 1
            if time.time() - t0 > time_budget or it > max_iters:
                if sink:
                    sink.close()
                return ('TIMEOUT', {'iters': it,
                                    'clauses': self.n_clauses,
                                    'elapsed': time.time() - t0})
            if not self.solver.solve():
                log(f"[{it}] UNSAT after {self.n_clauses:,} clauses, "
                    f"{time.time()-t0:.1f}s")
                if sink:
                    sink.close()
                return ('UNSAT', None)
            A = self.decode(self.solver.get_model())
            new = self._violation_clauses(A)
            if not new:
                log(f"[{it}] girth-5 model found! verifying...")
                verify_moore(A, self.d)
                if sink:
                    sink.close()
                return ('SAT', A)
            self._add(new)
            if sink:
                for cl in new:
                    sink.write(' '.join(map(str, cl)) + '\n')
                sink.flush()
            nviol += len(new)
            if it % log_every == 0:
                vt, vq = getattr(self, 'last_violations', ('?', '?'))
                log(f"[{it}] viol tri={vt:,} quad={vq:,}; +{len(new):,} cuts "
                    f"(total {self.n_clauses:,}), {time.time()-t0:.1f}s")
