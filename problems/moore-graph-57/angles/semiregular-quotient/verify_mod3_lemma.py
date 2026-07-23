"""Independent verification of the mod-3 lemma for abelian order-125 lifts.

CLAIM (derived by a GPT-5.6-sol xhigh consult, 2026-07-23; verified here
from scratch): for any Moore graph of degree 57 with an ABELIAN group G,
|G| = 125, acting semiregularly (b = 26 orbits), the diagonal-multiplicity
function

    f(g) := #{ i : g in S_ii },   g in G, g != 0

(S_ii = within-orbit connection sets, S_ii = -S_ii, 0 not in S_ii)
satisfies f(g) ≡ 1 (mod 3) for EVERY nonzero g.  Hence f(g) >= 1, so

    tr C = sum_i |S_ii| = sum_{g != 0} f(g) >= 124  =>  15a - 143 >= 124
    =>  a >= 18.

Combined with the Galois mod-4 filter a in {13,17,21}
(character_notes.md, verified in verify_mod5_and_filter.py):

    ****  every abelian order-125 lift has a = 21 exactly.  ****

Derivation being checked (all steps below verified exactly):
  Fourier inversion over abelian G:
    125 f(g) = sum_chi chibar(g) tr(Chat_chi)
  with tr(Chat_1) = tr C = 15a - 143 and, for chi != 1,
    tr(Chat_chi) = 15 m7(chi) - 208        [m7 + m(-8) = 26]
  and sum_{chi != 1} chibar(g) = -1 for g != 0.  So
    125 f(g) = (15a - 143) + 15 T(g) + 208 = 15a + 65 + 15 T(g),
  where T(g) = sum_{chi != 1} chibar(g) m7(chi) is a RATIONAL integer
  (m7 is Galois-invariant; T is an algebraic integer fixed by Gal).
  Mod 3:  125 ≡ 2, 15 ≡ 0, 65 ≡ 2  =>  2 f(g) ≡ 2  =>  f(g) ≡ 1 (mod 3).

Part B validates the identical machinery end-to-end on a REAL object: the
Hoffman-Singleton graph (d=7) with its fixed-point-free order-5 shift
automorphism (i -> i+1 in Robertson coordinates), b = 10 orbits, where the
general identity reads  5 f(g) = tr C + 5 T(g) + 30  i.e.
f(g) = a + 2 + T(g)  (no mod-3 phenomenon at d=7 -- the congruence is a
d=57/m=125-specific gift: gcd argument needs 3 | (r - s) = 15, 3 ∤ m).

Part C pins the correct F5 rank caps for N = C - 2I mod 5 (a consult
off-by-one is corrected: the bound is min(26-a, a+1, 12), NOT min(a,25-a)).

Exact arithmetic throughout (sympy integers / cyclotomics).
"""
from __future__ import annotations

import sys
import os

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "harness"))
from hoffman_singleton import hoffman_singleton  # noqa: E402

ok = True


def check(name, cond):
    global ok
    print(f"  [{'OK' if cond else 'FAIL'}] {name}")
    ok = ok and bool(cond)


print("== A. symbolic derivation, d=57 / m=125 / b=26 ==")
a, m7, T, f = sp.symbols('a m7 T f', integer=True)
# trace of a chi!=1 block with eigenvalues 7 (m7 times), -8 (26-m7 times)
check("tr Chat_chi = 15*m7 - 208", sp.expand(7*m7 - 8*(26 - m7) - (15*m7 - 208)) == 0)
# trace of the chi=1 block C: eigenvalues 57, 7^a, (-8)^(25-a)
check("tr C = 15*a - 143", sp.expand(57 + 7*a - 8*(25 - a) - (15*a - 143)) == 0)
# 125 f(g) = (15a-143) + sum_{chi!=1} chibar(g) (15 m7(chi) - 208)
#          = (15a-143) + 15 T(g) - 208 * (-1)
lhs = (15*a - 143) + 15*T + 208
check("125 f(g) = 15a + 65 + 15 T(g)", sp.expand(lhs - (15*a + 65 + 15*T)) == 0)
# mod 3: 125 ≡ 2, 15 ≡ 0, 65 ≡ 2  =>  2f ≡ 2  =>  f ≡ 1 (mod 3)
check("125 ≡ 2, 15 ≡ 0, 65 ≡ 2 (mod 3)", (125 % 3, 15 % 3, 65 % 3) == (2, 0, 2))
check("=> f(g) ≡ 1 (mod 3)  [2 invertible mod 3]", sp.gcd(2, 3) == 1)
# f >= 0 integer with f ≡ 1 mod 3  =>  f >= 1; 124 nonzero g
check("tr C >= 124  =>  a >= ceil(267/15) = 18", sp.ceiling(sp.Rational(267, 15)) == 18)
check("intersect abelian filter {13,17,21} -> {21}",
      [x for x in (13, 17, 21) if x >= 18] == [21])
# consistency: a=21 => tr C = 172 = 124 + 3*16 with 124 values ≡ 1 mod 3
check("a=21: tr C = 172, 172 - 124 = 48 divisible by 3",
      15*21 - 143 == 172 and (172 - 124) % 3 == 0)
check("diag cap consistent: 172 <= 26*8", 172 <= 208)
# ALSO: a=23 would give tr C = 202 >= 124 -- mod-3 does NOT kill a=23;
# it's the mod-4 Galois filter that kills it. Record the division of labor.
check("mod-3 alone kills a in {11,13,15,17} (tr C < 124)",
      all(15*x - 143 < 124 for x in (11, 13, 15, 17)))

print("== B. end-to-end machinery validation on Hoffman-Singleton (d=7, m=5, b=10) ==")
A = sp.Matrix(hoffman_singleton().tolist())
n = 50
check("A is 50x50 symmetric 0/1, 7-regular",
      A.shape == (50, 50) and A == A.T and all(sum(A[i, j] for j in range(n)) == 7 for i in range(n)))
check("Moore identity A^2 + A - 6I = J", A*A + A - 6*sp.eye(n) == sp.ones(n, n))

# orbits of the shift sigma: (part, h, i) -> (part, h, i+1): orbit = (part, h),
# representative i = 0. vertex index = part*25 + h*5 + i.
def vidx(part, h, i):
    return part * 25 + h * 5 + (i % 5)

orbits = [(p, h) for p in range(2) for h in range(5)]
b = 10
# sigma is an automorphism (check!) and fixed-point-free by construction
P = sp.zeros(n, n)
for p in range(2):
    for h in range(5):
        for i in range(5):
            P[vidx(p, h, i + 1), vidx(p, h, i)] = 1
check("sigma (i -> i+1) is an automorphism: P A P^T = A", P * A * P.T == A)
check("sigma is fixed-point-free of order 5",
      all(P[i, i] == 0 for i in range(n)) and P**5 == sp.eye(n))

# connection sets S_ij = { t : (p,h,0) ~ (p',h',t) }
S = {}
for I, (p, h) in enumerate(orbits):
    for J, (q, k) in enumerate(orbits):
        S[I, J] = frozenset(t for t in range(5) if A[vidx(p, h, 0), vidx(q, k, t)] == 1)
check("S_ji = -S_ij", all(S[J, I] == frozenset((-t) % 5 for t in S[I, J])
                          for I in range(b) for J in range(b)))
check("S_ii symmetric, 0 not in S_ii",
      all(S[I, I] == frozenset((-t) % 5 for t in S[I, I]) and 0 not in S[I, I]
          for I in range(b)))

C = sp.Matrix(b, b, lambda I, J: len(S[I, J]))
check("row sums 7", all(sum(C[I, J] for J in range(b)) == 7 for I in range(b)))
check("C^2 + C - 6I = 5J", C*C + C - 6*sp.eye(b) == 5*sp.ones(b, b))

# a = multiplicity of eigenvalue 2 (the d=7 'r') on 1-perp
cp = sp.factor(C.charpoly(sp.symbols('x')).as_expr())
evs = C.eigenvals()
a_val = evs.get(sp.Integer(2), 0)
check(f"spectrum is 7, 2^a, (-3)^(9-a) with a = {a_val}",
      set(evs) == {sp.Integer(7), sp.Integer(2), sp.Integer(-3)}
      and evs[sp.Integer(7)] == 1 and evs[sp.Integer(-3)] == 9 - a_val)
check("trace identity tr C = 5a - 20", sp.trace(C) == 5*a_val - 20)

# character blocks over Z[zeta_5], EXACT: elements as integer coefficient
# 4-vectors in basis {1, z, z^2, z^3}, reduced via z^4 = -1 - z - z^2 - z^3.
def cyc(t):  # zeta^t as coeff vector
    t %= 5
    if t < 4:
        v = [0, 0, 0, 0]
        v[t] = 1
        return tuple(v)
    return (-1, -1, -1, -1)


def cadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def cscale(c, x):
    return tuple(c * a for a in x)


def cmul(x, y):
    raw = [0] * 8
    for i in range(4):
        for j in range(4):
            raw[i + j] += x[i] * y[j]
    out = (raw[0], raw[1], raw[2], raw[3])
    for e in range(4, 8):
        out = cadd(out, cscale(raw[e], cyc(e)))
    return out


ZERO, ONE = (0, 0, 0, 0), (1, 0, 0, 0)
check("Z[zeta] sanity: sum_{t=0..4} zeta^t = 0 and zeta^2*zeta^3 = 1",
      cadd(cadd(cadd(cadd(cyc(0), cyc(1)), cyc(2)), cyc(3)), cyc(4)) == ZERO
      and cmul(cyc(2), cyc(3)) == ONE)

m2 = {}
for k in range(1, 5):
    Chat = [[ZERO] * b for _ in range(b)]
    for I in range(b):
        for J in range(b):
            v = ZERO
            for t in S[I, J]:
                v = cadd(v, cyc(k * t))
            Chat[I][J] = v
    # (Chat - 2I)(Chat + 3I) must vanish identically
    L = [[cadd(Chat[I][J], cscale(-2 if I == J else 0, ONE)) for J in range(b)]
         for I in range(b)]
    R = [[cadd(Chat[I][J], cscale(3 if I == J else 0, ONE)) for J in range(b)]
         for I in range(b)]
    prod_ok = True
    for I in range(b):
        for J in range(b):
            acc = ZERO
            for t in range(b):
                acc = cadd(acc, cmul(L[I][t], R[t][J]))
            if acc != ZERO:
                prod_ok = False
    check(f"chi_{k}: (Chat-2I)(Chat+3I) = 0 exactly over Z[zeta_5]", prod_ok)
    tr = ZERO
    for I in range(b):
        tr = cadd(tr, Chat[I][I])
    is_rat = tr[1] == tr[2] == tr[3] == 0
    m2k = sp.Rational(tr[0] + 30, 5)
    check(f"chi_{k}: tr = {tr[0]} rational integer, m2 = {m2k} in [0,10]",
          is_rat and m2k.is_integer and 0 <= m2k <= 10)
    m2[k] = int(m2k)
check("m2 Galois-invariant (constant over k=1..4)", len(set(m2.values())) == 1)
check("global multiplicity: a + 4*m2 = full-graph mult of 2 = 28",
      a_val + sum(m2.values()) == 28)

# f(g) and the general identity  m f(g) = tr C + sum_{chi != 1} chibar(g) tr Chat
# (chibar_k(g) = zeta^{-kg}; tr Chat_k is the rational integer 5*m2[k] - 30)
for g in range(1, 5):
    fg = sum(1 for I in range(b) if g in S[I, I])
    Tsum = ZERO
    for k in range(1, 5):
        Tsum = cadd(Tsum, cscale(5 * m2[k] - 30, cyc(-k * g)))
    check(f"g={g}: T-sum rational and f = {fg} matches (tr C + T-sum)/5",
          Tsum[1] == Tsum[2] == Tsum[3] == 0
          and sp.Rational(sp.trace(C) + Tsum[0], 5) == fg)

print("== C. corrected F5 rank caps for N = C - 2I (d=57) ==")
# rank_Q(C - 7I) = 26 - a  (eigenvalue 7 has mult a; 57,-8 shifted nonzero)
# rank_Q(C + 8I) = a + 1   (eigenvalue -8 has mult 25-a)
# integer matrix rank mod p <= rank over Q (minor vanishing descends);
# C - 7I ≡ C + 8I ≡ C - 2I =: N (mod 5); isotropy of im(N) inside 1-perp
# (nondegenerate, dim 25) gives rank <= 12.
print("  a  : cap = min(26-a, a+1, 12)")
caps = {}
for av in (11, 13, 15, 17, 19, 21, 23):
    caps[av] = min(26 - av, av + 1, 12)
    print(f"  {av} : {caps[av]}")
check("a=21 cap is 5 (consult said 4 -- off by one, corrected)", caps[21] == 5)
check("a=23 cap is 3", caps[23] == 3)

print()
print("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
