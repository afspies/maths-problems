"""Exact integer-arithmetic verifier for Moore graph certificates.

A Moore graph of degree d and diameter 2 is a d-regular graph on n = d^2 + 1
vertices with girth 5, equivalently srg(n, d, 0, 1). The certificate is the
adjacency matrix A; the verification identities (all over the integers) are:

    1. A symmetric, 0/1 entries, zero diagonal
    2. A @ 1 = d * 1                      (regularity)
    3. A @ A + A - (d-1) I = J            (srg identity, lambda=0, mu=1)

Identity 3 with lambda=0/mu=1 forces girth 5 (no triangles: adjacent pairs
have 0 common neighbours; no 4-cycles: non-adjacent pairs have exactly 1).

All arithmetic is int64. Entries of A@A are bounded by d <= 57 << 2^63, so
the computation is exact.
"""

from __future__ import annotations

import numpy as np


class VerificationFailure(Exception):
    pass


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise VerificationFailure(msg)


def verify_moore(A: np.ndarray, d: int, verbose: bool = True) -> bool:
    """Verify A is the adjacency matrix of a Moore graph of degree d.

    Raises VerificationFailure with a diagnostic message on any failure.
    Returns True on success.
    """
    n = d * d + 1
    A = np.asarray(A)
    check(A.shape == (n, n), f"shape {A.shape} != ({n},{n})")
    check(np.issubdtype(A.dtype, np.integer), f"dtype {A.dtype} not integer")
    A = A.astype(np.int64)

    check(bool(((A == 0) | (A == 1)).all()), "entries not all 0/1")
    check(bool((np.diag(A) == 0).all()), "nonzero diagonal")
    check(bool((A == A.T).all()), "not symmetric")

    rowsums = A.sum(axis=1)
    check(bool((rowsums == d).all()),
          f"row sums != {d}: min={rowsums.min()}, max={rowsums.max()}")

    # srg identity: A^2 + A - (d-1) I = J.
    # A^2 is computed in pure int64 (numpy integer matmul never touches
    # floating point).  NOTE: a float64 BLAS matmul is NOT acceptable here
    # even though classical dot products of 0/1 values are exact — a
    # Strassen-like dgemm performs block subtractions whose intermediates
    # are not bounded by the final entries, voiding the exactness argument
    # (referee finding, 2026-07-22).  ~40 s at n = 3250: fine for a
    # certificate check.
    A2 = A @ A
    M = A2 + A - (d - 1) * np.eye(n, dtype=np.int64)
    check(bool((M == 1).all()), "A^2 + A - (d-1)I != J")

    if verbose:
        print(f"OK: valid Moore graph certificate, degree {d}, n = {n}")
    return True


def _is_prime(m: int) -> bool:
    """Deterministic Miller-Rabin for m < 3.3e24 (fixed witness set)."""
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def rank_mod_p(M: np.ndarray, p: int) -> int:
    """Exact rank of an integer matrix mod prime p via Gaussian elimination."""
    M = (M % p).astype(np.int64)
    n_rows, n_cols = M.shape
    rank = 0
    row = 0
    for col in range(n_cols):
        piv = None
        for r in range(row, n_rows):
            if M[r, col] % p:
                piv = r
                break
        if piv is None:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = pow(int(M[row, col]), p - 2, p)
        M[row] = (M[row] * inv) % p
        mask = M[row + 1:, col] != 0
        if mask.any():
            M[row + 1:][mask] = (M[row + 1:][mask]
                                 - np.outer(M[row + 1:, col][mask], M[row])) % p
        rank += 1
        row += 1
        if row == n_rows:
            break
    return rank


def spectral_sanity(A: np.ndarray, d: int, verbose: bool = True) -> bool:
    """Exact spectral multiplicity check.

    For a Moore graph of degree d, eigenvalues are d (mult 1), r, s where
    r,s = (-1 +- sqrt(4d-3))/2, with multiplicities
        m_r = ((n-1) - 2d/ (r - s) * ... )  -- computed from trace identities.
    We verify: rank(A - r I) = n - m_r and rank(A - s I) = n - m_s, computed
    exactly modulo a prime p chosen so that r, s are integers mod p and p is
    large enough that rank mod p equals rank over Q generically; a rank
    DEFICIENCY >= claimed multiplicity is guaranteed mod every p, and the
    complementary rank bound makes the check exact (see below).

    Since rank_Fp(M) <= rank_Q(M) for any prime p, showing
    rank_p(A - rI) <= n - m_r AND rank_p(A - sI) <= n - m_s with
    (n - m_r) + (n - m_s) = n + 1 pins both ranks exactly (eigenspaces of
    distinct eigenvalues intersect trivially and the d-eigenvector is
    outside both).
    """
    n = d * d + 1
    disc = 4 * d - 3
    sq = int(round(disc ** 0.5))
    if sq * sq == disc:
        # integer eigenvalues (d = 3, 7, 57): exact multiplicities from trace
        p = 10 ** 9 + 7
        r, s = (-1 + sq) // 2, (-1 - sq) // 2
        m_r = ((n - 1) * (-s) - d) // (r - s)
        m_s = (n - 1) - m_r
    else:
        # d = 2 (C5): eigenvalues (-1 +- sqrt(5))/2 irrational, conjugate
        # multiplicities are equal; work with roots of x^2 + x - (d-1) mod p,
        # over a prime p = 3 mod 4 (easy sqrt) with disc a quadratic residue
        p = 10 ** 9 + 7
        while not (p % 4 == 3 and pow(disc, (p - 1) // 2, p) == 1
                   and _is_prime(p)):
            p += 2
        sq = pow(disc, (p + 1) // 4, p)
        assert sq * sq % p == disc % p
        inv2 = pow(2, p - 2, p)
        r, s = (-1 + sq) * inv2 % p, (-1 - sq) * inv2 % p
        m_r = m_s = (n - 1) // 2

    I = np.eye(n, dtype=np.int64)
    rank_r = rank_mod_p(A - r * I, p)
    rank_s = rank_mod_p(A - s * I, p)
    check(rank_r == n - m_r, f"rank(A - {r}I) mod p = {rank_r}, expected {n - m_r}")
    check(rank_s == n - m_s, f"rank(A - {s}I) mod p = {rank_s}, expected {n - m_s}")

    if verbose:
        print(f"OK: spectrum {{{d}^1, ({r} mod p)^{m_r}, ({s} mod p)^{m_s}}} "
              f"verified (exact ranks mod {p})")
    return True
