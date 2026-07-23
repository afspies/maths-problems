"""Construct the Hoffman-Singleton graph (the degree-7 Moore graph, n=50).

Robertson's pentagon-pentagram construction:
  - 5 pentagons P_0..P_4: vertices (0, h, i), i in Z_5; (0,h,i) ~ (0,h,j)
    iff i - j = +-1 (mod 5)
  - 5 pentagrams Q_0..Q_4: vertices (1, k, j); (1,k,i) ~ (1,k,j)
    iff i - j = +-2 (mod 5)
  - (0, h, i) ~ (1, k, j)  iff  j = h*k + i (mod 5)
"""

from __future__ import annotations

import numpy as np


def hoffman_singleton() -> np.ndarray:
    def idx(part: int, h: int, i: int) -> int:
        return part * 25 + h * 5 + i

    A = np.zeros((50, 50), dtype=np.int64)
    for h in range(5):
        for i in range(5):
            # pentagon edges
            A[idx(0, h, i), idx(0, h, (i + 1) % 5)] = 1
            A[idx(0, h, (i + 1) % 5), idx(0, h, i)] = 1
            # pentagram edges
            A[idx(1, h, i), idx(1, h, (i + 2) % 5)] = 1
            A[idx(1, h, (i + 2) % 5), idx(1, h, i)] = 1
    for h in range(5):
        for k in range(5):
            for i in range(5):
                j = (h * k + i) % 5
                A[idx(0, h, i), idx(1, k, j)] = 1
                A[idx(1, k, j), idx(0, h, i)] = 1
    return A


def petersen() -> np.ndarray:
    """Petersen graph (degree-3 Moore graph, n=10): Kneser graph K(5,2)."""
    from itertools import combinations
    pairs = list(combinations(range(5), 2))
    A = np.zeros((10, 10), dtype=np.int64)
    for a, pa in enumerate(pairs):
        for b, pb in enumerate(pairs):
            if not set(pa) & set(pb):
                A[a, b] = 1
    return A


def pentagon() -> np.ndarray:
    """C_5 (degree-2 Moore graph, n=5)."""
    A = np.zeros((5, 5), dtype=np.int64)
    for i in range(5):
        A[i, (i + 1) % 5] = 1
        A[(i + 1) % 5, i] = 1
    return A


if __name__ == "__main__":
    from verify import verify_moore, spectral_sanity

    for name, builder, d in [("C5", pentagon, 2),
                             ("Petersen", petersen, 3),
                             ("Hoffman-Singleton", hoffman_singleton, 7)]:
        print(f"--- {name} (d={d}) ---")
        A = builder()
        verify_moore(A, d)
        spectral_sanity(A, d)
