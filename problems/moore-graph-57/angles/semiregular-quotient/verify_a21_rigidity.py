"""Exact arithmetic checks for the 2026-07-23 order-125 analysis.

This is scratch paper only.  It checks:
  * nonabelian Wedderburn dimensions and all trace/Fourier constants;
  * the central and quotient-coset congruences and the resulting parameter lists;
  * scalar-multiplier orbits for C125 and C25 x C5;
  * PG(2,5) incidence counts and every mass-four Fourier pattern;
  * the complete mass-four pattern counts for all three abelian groups.

All calculations use integers and finite enumeration.
"""

from __future__ import annotations

from itertools import product
from math import comb, gcd


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"[OK] {label}")


def units(n: int) -> tuple[int, ...]:
    return tuple(x for x in range(n) if gcd(x, n) == 1)


def scalar_orbits(elements, scalars, action):
    unseen = set(elements)
    out = []
    while unseen:
        x = min(unseen)
        orbit = {action(s, x) for s in scalars}
        out.append(frozenset(orbit))
        unseen -= orbit
    return tuple(out)


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


print("== Nonabelian block bookkeeping ==")
check(
    "Wedderburn dimensions sum to 3250",
    26 + 24 * 26 + 4 * (26 * 5 * 5) == 3250,
)
check("degree-5 multiplicity block has size 26*5 = 130", 26 * 5 == 130)
check("degree-5 isotypic component has dimension 5*130 = 650", 5 * 130 == 650)
check(
    "degree-5 block trace is 7m-8(130-m)=15m-1040",
    all(7 * m - 8 * (130 - m) == 15 * m - 1040 for m in range(131)),
)

# Central inversion before imposing the Galois orbit equality.
# Constant: (-143) + 24*(-208) + 5*(-1)*(-1040) = 65.
check(
    "central Fourier-inversion constant is 65",
    -143 - 24 * 208 + 5 * 1040 == 65,
)
check("central congruence is f(z)=1 mod 3", 125 % 3 == 2 and 65 % 3 == 2)

# After Galois invariance, write m for the common degree-5 block multiplicity
# and L for the sum over the 24 nontrivial linear blocks.
for a in (13, 17, 21):
    for m in range(61, 70):
        L = 1729 - a - 20 * m
        numerator = 15 * a + 15 * L + 65 - 75 * m
        check(
            f"central simplification a={a}, m={m}: 125 f=125(208-3m)",
            numerator == 125 * (208 - 3 * m),
        )
check("1 <= 208-3m <= 26 iff 61 <= m <= 69", [
    m for m in range(131) if 1 <= 208 - 3 * m <= 26
] == list(range(61, 70)))

check("nonzero quotient-coset inversion constant is 65", -143 + 208 == 65)
check("F(q)=2 mod 3 for q nonzero", 25 % 3 == 1 and 65 % 3 == 2)
check("trace lower bound 4+24*2=52", 4 + 24 * 2 == 52)
check("15a-143 >= 52 gives a >= 13", [
    a for a in range(0, 26) if 15 * a - 143 >= 52
][0] == 13)

print("== Refined nonabelian trace-level patterns ==")
nonabelian_cases = {}
for a in (13, 17, 21):
    cases = []
    for m in range(61, 70):
        S_num = 5 * a + 4 * m - 341
        if S_num < 0 or S_num % 4:
            continue
        S = S_num // 4
        baseline_num = 345 - a - 4 * m
        check(f"linear baseline integral for a={a}, m={m}", baseline_num % 4 == 0)
        baseline = baseline_num // 4
        for weights in weak_compositions(S, 6):
            linear_multiplicities = tuple(baseline + w for w in weights)
            assert all(0 <= x <= 26 for x in linear_multiplicities)
            L = 4 * sum(linear_multiplicities)
            assert a + L + 20 * m == 1729
        cases.append((m, S, comb(S + 5, 5)))
    nonabelian_cases[a] = tuple(cases)
check("a=13 forces m=69 and zero quotient excess", nonabelian_cases[13] == ((69, 0, 1),))
check(
    "a=17 permits m=64..69 with line-mass m-64",
    nonabelian_cases[17] == tuple((m, m - 64, comb(m - 59, 5)) for m in range(64, 70)),
)
check(
    "a=21 permits m=61..69 with line-mass m-59",
    nonabelian_cases[21] == tuple((m, m - 59, comb(m - 54, 5)) for m in range(61, 70)),
)
check("a=17 has 462 aggregate patterns", sum(x[2] for x in nonabelian_cases[17]) == 462)
check("a=21 has 8001 aggregate patterns", sum(x[2] for x in nonabelian_cases[21]) == 8001)

print("== Task 2 scalar arithmetic ==")
check("T=(25f-76)/3 gives T=25e-17 when f=1+3e", all(
    (25 * (1 + 3 * e) - 76) // 3 == 25 * e - 17 for e in range(20)
))
check("T >= -17 and T=8 mod 25", all(
    25 * e - 17 >= -17 and (25 * e - 17) % 25 == 8 for e in range(20)
))
ehat_candidates = tuple(x for x in range(-16, 17) if x % 5 == 1)
check("Fourier candidates are exactly -14,-9,-4,1,6,11,16", ehat_candidates == (-14, -9, -4, 1, 6, 11, 16))
check("corresponding m7 values are 11..17", tuple((x + 69) // 5 for x in ehat_candidates) == tuple(range(11, 18)))
check("mass is (172-124)/3=16", (172 - 124) // 3 == 16)

print("== PG(2,5) incidence and all C5^3 mass-four patterns ==")
p = 5


def canonical(v):
    for x in v:
        if x % p:
            inv = pow(x, -1, p)
            return tuple((inv * y) % p for y in v)
    raise ValueError("zero vector")


points = sorted({
    canonical(v) for v in product(range(p), repeat=3) if v != (0, 0, 0)
})
hyperplanes = sorted({
    canonical(v) for v in product(range(p), repeat=3) if v != (0, 0, 0)
})
incidence = tuple(
    tuple(sum(point[i] * covector[i] for i in range(3)) % p == 0 for point in points)
    for covector in hyperplanes
)
check("PG(2,5) has 31 points and 31 hyperplanes", len(points) == len(hyperplanes) == 31)
check("each hyperplane contains 6 projective points", all(sum(row) == 6 for row in incidence))
check("each point lies on 6 hyperplanes", all(sum(incidence[h][j] for h in range(31)) == 6 for j in range(31)))
check("number of labelled mass-four point multisets is C(34,4)=46376", comb(34, 4) == 46376)

c5cubed_patterns = 0
for weights in weak_compositions(4, 31):
    c5cubed_patterns += 1
    K = tuple(sum(weights[j] for j in range(31) if incidence[h][j]) for h in range(31))
    m_by_hyperplane = tuple(13 + x for x in K)
    assert all(13 <= x <= 17 for x in m_by_hyperplane)
    assert 4 * sum(m_by_hyperplane) == 1708
check("enumerated all 46376 C5^3 patterns", c5cubed_patterns == 46376)
check("every C5^3 mass-four pattern has m7 in [13,17] and global sum 1708", True)

print("== Scalar orbits for C125 ==")
u125 = units(125)
orbits125 = scalar_orbits(
    range(1, 125),
    u125,
    lambda s, x: (s * x) % 125,
)
order125 = lambda x: 125 // gcd(x, 125)
summary125 = sorted((order125(next(iter(o))), len(o)) for o in orbits125)
check("C125 has one scalar orbit of each size/order 4,20,100", summary125 == [(5, 4), (25, 20), (125, 100)])
check("mass 16 uniquely gives e_order5=4, others zero", [
    (e5, e25, e125)
    for e5 in range(5)
    for e25 in range(2)
    for e125 in range(2)
    if 4 * e5 + 20 * e25 + 100 * e125 == 16
] == [(4, 0, 0)])
check("C125 m7 values: 24 chars at 17 and 100 at 13 sum to 1708", 24 * 17 + 100 * 13 == 1708)

print("== Scalar orbits for C25 x C5 ==")
u25 = units(25)
elements255 = tuple((x, y) for x in range(25) for y in range(5) if (x, y) != (0, 0))
orbits255 = scalar_orbits(
    elements255,
    u25,
    lambda s, xy: ((s * xy[0]) % 25, ((s % 5) * xy[1]) % 5),
)


def order255(xy):
    x, y = xy
    ox = 1 if x == 0 else 25 // gcd(x, 25)
    oy = 1 if y == 0 else 5
    return max(ox, oy)


summary255 = sorted((order255(next(iter(o))), len(o)) for o in orbits255)
check("C25xC5 has six order-5 size-4 scalar orbits", summary255.count((5, 4)) == 6)
check("C25xC5 has five order-25 size-20 scalar orbits", summary255.count((25, 20)) == 5)
check("orbit sizes exhaust 124 elements", sum(size for _, size in summary255) == 124)
patterns255 = tuple(weak_compositions(4, 6))
check("mass equation kills order-25 excess and leaves 126 order-5 patterns", len(patterns255) == comb(9, 5) == 126)
for weights in patterns255:
    # Four characters annihilate the full 5-torsion subgroup: m=17.
    # For each of the six nonzero restriction kernels there are 20
    # characters, with m=13+the corresponding line weight.
    assert all(13 <= 13 + w <= 17 for w in weights)
    assert 4 * 17 + 20 * sum(13 + w for w in weights) == 1708
check("every C25xC5 mass-four pattern has valid m7 range and global sum 1708", True)

print("== Galois orbit counts ==")
check("C5^3: 31 character orbits of size 4", 31 * 4 == 124)
check("C25xC5: six size-4 and five size-20 character orbits", 6 * 4 + 5 * 20 == 124)
check("C125: character orbit sizes 4,20,100", 4 + 20 + 100 == 124)
check("nonabelian global weighting is L + 5*sum(m_pi)", 24 * 26 + 5 * (4 * 130) == 3224)
check("1729 is 1 mod 4, so a is 1 mod 4", 1729 % 4 == 1)

print("ALL EXACT ARITHMETIC CHECKS PASS")
