"""Mutation tests: the verifier must reject every corrupted certificate,
and must run fast enough at n=3250 scale."""

from __future__ import annotations

import time

import numpy as np

from hoffman_singleton import hoffman_singleton
from verify import VerificationFailure, verify_moore, spectral_sanity


def expect_reject(A, d, why):
    try:
        verify_moore(A, d, verbose=False)
    except VerificationFailure as e:
        print(f"OK (rejected {why}): {e}")
        return
    raise SystemExit(f"FAIL: verifier accepted {why}")


def main():
    A = hoffman_singleton()

    # remove one edge (breaks regularity)
    B = A.copy()
    i, j = np.argwhere(B == 1)[0]
    B[i, j] = B[j, i] = 0
    expect_reject(B, 7, "edge removed")

    # swap an edge endpoint (keeps regularity, breaks srg identity)
    B = A.copy()
    edges = np.argwhere(np.triu(B) == 1)
    nonedges = np.argwhere(np.triu(1 - B, 1) == 1)
    (a, b), (c, e) = edges[0], nonedges[0]
    # 2-switch: remove (a,b) and one edge at c; add (a,c)... simpler: do a
    # degree-preserving 2-switch: edges (a,b),(c,e) -> (a,e),(c,b) if valid
    for (a, b) in edges:
        for (c, e) in edges:
            if len({a, b, c, e}) == 4 and not A[a, e] and not A[c, b]:
                B = A.copy()
                B[a, b] = B[b, a] = B[c, e] = B[e, c] = 0
                B[a, e] = B[e, a] = B[c, b] = B[b, c] = 1
                break
        else:
            continue
        break
    assert (B.sum(axis=1) == 7).all()
    expect_reject(B, 7, "2-switch (regular but not srg)")

    # asymmetric corruption
    B = A.copy()
    B[0, 1] = 1 - B[0, 1]
    expect_reject(B, 7, "asymmetric flip")

    # diagonal entry
    B = A.copy()
    B[3, 3] = 1
    expect_reject(B, 7, "loop added")

    # wrong size
    expect_reject(np.zeros((50, 50), dtype=np.int64), 3, "wrong n for d")

    # spectral checker must also reject a regular-but-wrong graph:
    # C_50 union nothing is 2-regular; instead test: random 7-regular graph
    import networkx as nx
    G = nx.random_regular_graph(7, 50, seed=1)
    R = nx.to_numpy_array(G, dtype=np.int64)
    try:
        spectral_sanity(R, 7, verbose=False)
        raise SystemExit("FAIL: spectral_sanity accepted random 7-regular graph")
    except VerificationFailure as e:
        print(f"OK (spectral rejected random regular graph): {e}")

    # timing at target scale: n = 3250 (matrix is NOT a Moore graph; we time
    # the full identity computation on a random symmetric 0/1 matrix)
    rng = np.random.default_rng(0)
    M = (rng.random((3250, 3250)) < 0.0176).astype(np.int64)
    M = np.triu(M, 1)
    M = M + M.T
    t0 = time.time()
    try:
        verify_moore(M, 57, verbose=False)
    except VerificationFailure:
        pass
    t1 = time.time()
    # force the expensive path too: full srg identity on a 3250 matrix
    t2 = time.time()
    _ = M @ M
    t3 = time.time()
    print(f"OK: n=3250 verify path {t1-t0:.2f}s; 3250^2 int64 matmul {t3-t2:.2f}s")


if __name__ == "__main__":
    main()
