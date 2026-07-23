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
