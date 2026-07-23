r"""Session-driver-written INDEPENDENT verification of the codex results at
k=7 (q=6): brute-force enumeration, written from scratch, sharing no code
with search.py / test_search.py.

Model: gain graph on q vertices; symmetric assignment h[i][j] in H\{e},
h[j][i] = inv(h[i][j]); (V) outgoing values at each vertex all distinct
(hence = H\{e}); (T) no triangle product e; (Q) no 4-cycle product e.
First row NOT fixed here (full space, feasibility only) — slower but
removes reliance on the first-row symmetry argument.

Groups as permutation tuples under composition (works for any group).
"""

import itertools
import sys


def make_group(name):
    if name == "z6":
        els = list(range(6))
        mul = lambda a, b: (a + b) % 6
        inv = lambda a: (-a) % 6
        e = 0
    elif name == "s3":
        els = list(itertools.permutations(range(3)))
        mul = lambda a, b: tuple(a[b[i]] for i in range(3))
        inv = lambda a: tuple(sorted(range(3), key=lambda i: a[i]))
        e = (0, 1, 2)
    elif name == "z2":
        els = [0, 1]
        mul = lambda a, b: (a + b) % 2
        inv = lambda a: a
        e = 0
    else:
        raise ValueError(name)
    return els, mul, inv, e


def solve(name, q):
    els, mul, inv, e = make_group(name)
    non_e = [g for g in els if g != e]
    assert len(non_e) == q - 1, "need |H| = q"
    edges = [(i, j) for i in range(q) for j in range(i + 1, q)]
    h = {}
    complete = [0]
    valid = [0]
    witness = []

    def ok_partial(i, j):
        g = h[(i, j)]
        # (V): outgoing at i and at j distinct from existing
        for k in range(q):
            if k != j and (min(i, k), max(i, k)) in h:
                out_ik = h[(i, k)] if i < k else inv(h[(k, i)])
                if out_ik == g:
                    return False
        gj = inv(g)
        for k in range(q):
            if k != i and (min(j, k), max(j, k)) in h:
                out_jk = h[(j, k)] if j < k else inv(h[(k, j)])
                if out_jk == gj:
                    return False
        # (T): triangles with both other edges assigned
        for k in range(q):
            if k in (i, j):
                continue
            eik, ejk = (min(i, k), max(i, k)), (min(j, k), max(j, k))
            if eik in h and ejk in h:
                g_ik = h[eik] if i < k else inv(h[(k, i)])
                g_kj = inv(h[ejk]) if j < k else h[(k, j)]
                # product i->j->? use i->k->j vs i->j
                if mul(g_ik, g_kj) == g:
                    return False  # h_ij = h_ik h_kj  <=> triangle product e
        # (Q): 4-cycles i-j-k-l-i fully assigned after adding (i,j)
        for k in range(q):
            if k in (i, j):
                continue
            for l in range(q):
                if l in (i, j, k):
                    continue
                e_jk = (min(j, k), max(j, k))
                e_kl = (min(k, l), max(k, l))
                e_li = (min(l, i), max(l, i))
                if e_jk in h and e_kl in h and e_li in h:
                    g_jk = h[e_jk] if j < k else inv(h[(k, j)])
                    g_kl = h[e_kl] if k < l else inv(h[(l, k)])
                    g_li = h[e_li] if l < i else inv(h[(i, l)])
                    if mul(mul(mul(g, g_jk), g_kl), g_li) == e:
                        return False
        return True

    def rec(idx):
        if valid[0]:
            return
        if idx == len(edges):
            complete[0] += 1
            valid[0] += 1
            witness.append(dict(h))
            return
        i, j = edges[idx]
        for g in non_e:
            h[(i, j)] = g
            if ok_partial(i, j):
                rec(idx + 1)
            del h[(i, j)]

    rec(0)
    return valid[0], witness


if __name__ == "__main__":
    # q=6 cases must both be infeasible (codex claim + theorem)
    for name in ("z6", "s3"):
        v, _ = solve(name, 6)
        print(f"k=7, H={name}: {'FEASIBLE — CONTRADICTS THEOREM!' if v else 'infeasible (independent brute force)'}",
              flush=True)
    # q=2 positive control: Z2 must be feasible (Petersen exists)
    v, w = solve("z2", 2)
    print(f"k=3, H=z2: {'feasible (as expected)' if v else 'INFEASIBLE — pipeline bug!'}",
          flush=True)
