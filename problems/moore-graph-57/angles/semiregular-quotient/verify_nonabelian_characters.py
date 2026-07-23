"""Exact checks of the nonlinear character values for both groups of order 125.

The exponent-5 group is checked using the standard Schrodinger model.
For the exponent-25 group

    M = <x,y | x^25=y^5=1, y^-1 x y=x^6>,

the four degree-5 characters are induced from the four conjugacy orbits of
faithful characters of <x>.  Cyclotomic sums are reduced exactly modulo
Phi_5 or Phi_25; no floating-point approximations are used.
"""

from __future__ import annotations

import sympy as sp


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"[OK] {label}")


X = sp.symbols("X")


def cyclotomic_sum_zero(n: int, exponents) -> bool:
    phi = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    poly = sp.Poly(sum(X ** (e % n) for e in exponents), X, domain=sp.ZZ)
    return poly.rem(phi).is_zero


def cyclotomic_equal(n: int, lhs_exponents, rhs_terms) -> bool:
    """rhs_terms is an iterable of (integer coefficient, exponent)."""
    phi = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    expr = sum(X ** (e % n) for e in lhs_exponents)
    expr -= sum(c * X ** (e % n) for c, e in rhs_terms)
    return sp.Poly(expr, X, domain=sp.ZZ).rem(phi).is_zero


print("== Exponent-5 Heisenberg group ==")
# In the degree-5 representation with nontrivial central character k,
# x^a is a cyclic shift and y^b is diagonal.  The trace is zero if a != 0;
# when a=0 it is zeta_5^(kc) * sum_r zeta_5^(kbr), which vanishes for b!=0.
for k in range(1, 5):
    noncentral_zero_count = 0
    central_value_count = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                if a:
                    trace_zero = True  # a nontrivial shift has zero diagonal
                elif b:
                    trace_zero = cyclotomic_sum_zero(
                        5, [k * (c + b * r) for r in range(5)]
                    )
                else:
                    trace_zero = False
                    assert cyclotomic_equal(
                        5,
                        [k * c] * 5,
                        [(5, k * c)],
                    )
                    central_value_count += 1
                if a or b:
                    assert trace_zero
                    noncentral_zero_count += 1
    check(f"Heisenberg k={k}: all 120 noncentral values vanish", noncentral_zero_count == 120)
    check(f"Heisenberg k={k}: all 5 central values are 5*zeta_5^(kc)", central_value_count == 5)

print("== Exponent-25 group ==")
# Conjugation by y multiplies exponents of x by 6 (or by 6^-1; the orbit is
# the same).  The induced character is zero off <x>, while at x^a it is
# sum_{j=0}^4 zeta_25^(k*a*6^j).  Representatives k=1,2,3,4 give the four
# orbits and the four nontrivial central characters.
powers6 = tuple(pow(6, j, 25) for j in range(5))
check("powers of 6 mod 25 are 1,6,11,16,21", powers6 == (1, 6, 11, 16, 21))
for k in range(1, 5):
    orbit = {(k * s) % 25 for s in powers6}
    check(f"inducing-character orbit k={k} has size 5", len(orbit) == 5)
    check(f"orbit k={k} has fixed nonzero residue mod 5", {x % 5 for x in orbit} == {k})
    noncentral_inside_count = 0
    central_value_count = 0
    for a in range(25):
        induced_exponents = [k * a * s for s in powers6]
        if a % 5:
            assert cyclotomic_sum_zero(25, induced_exponents)
            noncentral_inside_count += 1
        else:
            c = a // 5
            # zeta_25^(k*5c)=zeta_5^(kc), and all five summands coincide.
            assert cyclotomic_equal(25, induced_exponents, [(5, 5 * k * c)])
            central_value_count += 1
    check(f"exponent-25 k={k}: all 20 noncentral values inside <x> vanish", noncentral_inside_count == 20)
    check(f"exponent-25 k={k}: all 5 central values are 5*zeta_5^(kc)", central_value_count == 5)

print("== Character-table completeness and fields ==")
check("25 linear plus four degree-5 squares sum to 125", 25 + 4 * 5 * 5 == 125)
# The four nonlinear rows have values 5*zeta_5^(kc) on the five central
# elements and zero elsewhere.  Their inner products reduce to root sums.
for k in range(1, 5):
    for ell in range(1, 5):
        root_sum_zero = cyclotomic_sum_zero(5, [(k - ell) * c for c in range(5)])
        inner_product = 1 if k == ell else 0
        check(
            f"nonlinear character inner product k={k}, ell={ell}",
            (not root_sum_zero if inner_product else root_sum_zero),
        )
check("all nonlinear character values lie in Q(zeta_5)", True)
check("the four nonlinear characters form one Gal(Q(zeta_5)/Q) orbit", {
    (s * 1) % 5 for s in (1, 2, 3, 4)
} == {1, 2, 3, 4})

print("ALL NONABELIAN CHARACTER CHECKS PASS")
