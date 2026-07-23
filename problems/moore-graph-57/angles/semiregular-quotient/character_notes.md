# Character-level lifting constraints for semiregular quotients (m = 125)

Session derivation, 2026-07-22. To be applied once quotient matrices C are
in hand (CP-SAT run). All statements below are for a Moore graph Γ of
degree 57 with a group G, |G| = m = 125, acting semiregularly (b = 26
orbits), G abelian (the nonabelian order-125 groups need the analogous
representation-theoretic version with 2-dim'l... — no: both nonabelian
groups of order 125 have irreducible degrees {1 (25 times), 5 (4 times)};
the 5-dim'l irreps give 130x130 blocks — handle separately).

## Setup (abelian G)

Choose orbit representatives; identify each orbit with G. Adjacency is
G-invariant, so block (i,j) of A is the G-circulant of a connection set
S_ij ⊆ G:  (i, x) ~ (j, y)  ⟺  y − x ∈ S_ij, with

  |S_ij| = C[i][j],   S_ji = −S_ij,   S_ii = −S_ii, 0 ∉ S_ii.

Fourier over G block-diagonalizes A into 125 blocks of size 26: for each
character χ, the block is  Ĉ_χ[i,j] = χ(S_ij) = Σ_{g∈S_ij} χ(g).

- Ĉ_χ is Hermitian (S_ji = −S_ij).
- χ = 1 gives Ĉ_1 = C, eigenvalues {57, 7^a, (−8)^{25−a}}.
- For χ ≠ 1 the srg identity forces  Ĉ_χ² + Ĉ_χ − 56 I = 0, i.e. every
  eigenvalue of Ĉ_χ is 7 or −8. Write m₇(χ) for the multiplicity of 7;
  m₇(χ) + m₈(χ) = 26.

## Constraints

1. **Global multiplicity:**  Σ_{χ≠1} m₇(χ) = 1729 − a.
2. **Galois invariance:** m₇ is constant on Galois orbits of characters
   (conjugating χ conjugates Ĉ_χ entrywise; 7, −8 are rational).
   - G = Z₅³: all 124 nontrivial χ have order 5; Gal(Q(ζ₅)/Q) has order 4;
     orbits partition 124 into 31 orbits of size 4. Hence
     **1729 − a ≡ 0 (mod 4)**, i.e. a ≡ 1 (mod 4).
   - G = Z₂₅×Z₅: 24 chars of order 5 (six 4-orbits), 100 of order 25
     (five 20-orbits): 1729 − a = 4u + 20v, u ∈ [0,156]... (weak but
     nontrivial mod-4 constraint: 1729 − a ≡ 0 mod 4 again ⟸ 4 | both).
   - G = Z₁₂₅: orbit sizes 4 / 20 / 100 → same mod-4 constraint.
   So for every abelian order-125 group: **a ≡ 1 (mod 4)**.
3. **Quotient-level a-window (independent of G):** trace identities give
   tr C = 15a − 143, C_ii even (m odd), PSD diag cap C_ii ≤ 8:
   a odd, 11 ≤ a ≤ 23.
4. **Combining 2+3 (abelian G):**  a ∈ {13, 17, 21}.
   ⟹ any CP-SAT quotient matrix C with a ∉ {13,17,21} cannot lift over an
   abelian group of order 125. (Compute a from C as the multiplicity of
   eigenvalue 7 — exact rank of C − 7I mod a prime p ∉ {2,3,5,13}, plus
   the complementary rank of C + 8I to pin it, as in harness/verify.py.)
5. **Trace equations per character (lifting stage):**
   Σ_i χ(S_ii) = tr Ĉ_χ = 15 m₇(χ) − 208 ∈ Z for every χ — a system of
   cyclotomic-integer equations tying the within-orbit connection sets to
   the multiplicity pattern. For Z₅³ with all χ of order 5: χ(S_ii) ∈
   Z[ζ₅]; the rationality of the total forces strong symmetry on the
   multiset {S_ii}.

## VERIFIED LEMMA (2026-07-23): abelian lifts force a = 21

Sharpening of constraint 4, found by a GPT-5.6-sol xhigh consult and
independently re-derived + exactly verified in `verify_mod3_lemma.py`
(38/38 checks; machinery validated end-to-end on a real HoS order-5
semiregular quotient).

For g ≠ 0 define f(g) = #{i : g ∈ S_ii}. Fourier inversion +
the per-character trace identities give

    125 f(g) = 15a + 65 + 15 T(g),   T(g) = Σ_{χ≠1} χ̄(g) m₇(χ) ∈ Z.

Mod 3 (15 ≡ 0, 125 ≡ 2, 65 ≡ 2):  **f(g) ≡ 1 (mod 3)**, hence
f(g) ≥ 1 for all 124 nonzero g, so tr C = Σ f(g) ≥ 124, i.e.
15a − 143 ≥ 124 ⟹ a ≥ 18. Intersecting with a ∈ {13, 17, 21}:

    ****  any ABELIAN order-125 semiregular lift has a = 21.  ****

Consequences: (i) the "character-filtered a ∈ {13,17}" search targets
are DEAD for abelian lifts — a = 21 is the only abelian target;
(ii) every nonzero g lies in some diagonal set S_ii (the S_ii cover
G ∖ {0}), with Σ|S_ii| = 172 and each f(g) ∈ {1, 4, 7, …};
(iii) Parseval on f gives Σ_g f(g)² = (1/125)[172² + Σ_{χ≠1}(15m₇(χ)−208)²]
— an open lever on the surviving a = 21 case (m₇ mean 1708/124 ≈ 13.8).

Corrected F₅ rank caps (consult's min(a,25−a) was off by one): with
N = C − 2I mod 5, rank_F5(N) ≤ min(26−a, a+1, 12) — for a = 21 the cap
is 5; for a = 23 it is 3. (From rank_Q(C−7I) = 26−a, rank_Q(C+8I) = a+1,
both ≡ N mod 5, plus total isotropy of im N in 1⊥.)

## VERIFIED (2026-07-23, second consult): nonabelian groups + a=21 structure

Rigorized by a second GPT-5.6-sol xhigh job; exact checks re-run by the
session driver (all pass): `verify_a21_rigidity.py` (constants, PG(2,5)
incidences, all three pattern enumerations), `verify_nonabelian_characters.py`
(deg-5 character values for both nonabelian groups, exact cyclotomics).

**Nonabelian theorem.** For both nonabelian order-125 groups (Z = [G,G] =
Z(G) ≅ Z₅, irreps 25 linear + four of degree 5 with tr ψ = 5λ on Z, 0 off
Z): central elements satisfy f(z) = 208 − 3μ ≡ 1 (mod 3) (μ = common
deg-5 block multiplicity, 61 ≤ μ ≤ 69, Galois-forced equal across the
four blocks; global identity a + L + 20μ = 1729); noncentral cosets
satisfy 25 F(q̄) = 15a + 65 + 15 T_lin(q̄) ⟹ F(q̄) ≡ 2 (mod 3) on the 24
nonzero cosets of G/Z. Net: tr C ≥ 52 ⟹ a ≥ 13, plus a ≡ 1 (mod 4)
(six linear 4-orbits + one 4-orbit of deg-5 irreps):
**nonabelian lifts force a ∈ {13, 17, 21}** — no further narrowing from
character data (per-element deg-5 constraints refuted: inversion needs
tr(π(g⁻¹)D_π), not tr π(g)·tr D_π).

**CAMPAIGN CONSEQUENCE: every order-125 semiregular lift (any group) has
a ∈ {13, 17, 21}; abelian ⟹ a = 21. Bare-C UNSAT at {13,17,21} kills
m=125 entirely; a=21 alone kills all abelian groups.** a ∈ {11,15,19,23}
matter only for the group-free bare-C question, not for lifts.

**Abelian a = 21 diagonal rigidity.** The chain T(g) = 25e(g) − 17,
ê(χ) = 5 m₇(χ) − 69 (pointwise integrality rigorously forced) implies
e := (f−1)/3 is constant on scalar-multiplier orbits, mass Σe = 16:
- Z₅³: e = multiset of 4 points of PG(2,5) (all C(34,4) = 46,376 pass
  every trace/Galois/window check; m₇ = 13 + K(hyperplane) ∈ [13,17]);
- Z₂₅×Z₅: order-25 orbits forced 0; six order-5 orbit values sum to 4
  (126 patterns);
- Z₁₂₅: UNIQUE forced pattern — f = 13 on the four order-5 elements,
  f = 1 on the other 120 (e₅ = 4, e₂₅ = e₁₂₅ = 0).
These pin only per-character trace sums, NOT individual entries — no
finite hand-certificate; joint realizability of the S_ij needs a
group-ring/SAT completion (verdict C). Z₁₂₅ is the most-constrained
lift target (unique aggregate pattern) if a lift-level search is run.

Entrywise pruning facts for any a=21 completion search, from
(Ĉ_χ−7I)(Ĉ_χ+8I) = 0: diag −8 ≤ h_ii ≤ 7, Σ_j |h_ij|² = (7−h_ii)(8+h_ii),
all Galois conjugates bounded by 8 (Kronecker-style).

## Status / next actions

- [ ] When CP-SAT returns quotient matrices: compute a for each; discard
      (for abelian G) any with a ∉ {13,17,21}.
- [ ] Enumerate ALL quotient matrices (not just one) if feasible-verdict:
      the a-filter may kill all of them for abelian G — that alone would
      reduce semiregular-125 to the two nonabelian groups.
- [ ] Nonabelian order-125 groups (Heisenberg H₅ = extraspecial 5^{1+2} of
      exponent 5, and the exponent-25 one): irreps are 25 linear + 4 of
      degree 5. Linear characters factor through G/[G,G] ≅ Z₅²; the
      degree-5 blocks are 130×130 with eigenvalues in {7,−8} — same
      framework, bigger blocks; the linear-character constraints alone
      give a mod-4-type condition via the 24 nontrivial linear characters
      (six Galois 4-orbits): m₇ sums ≡ ... (work out when needed).
