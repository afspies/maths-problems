# Exclusion map: the missing Moore graph srg(3250, 57, 0, 1)

> Compiled 2026-07-22 by a web-research agent; spot-verified by the session
> driver. Verification notes: Ishida arXiv:2606.29183 confirmed directly on
> arXiv (title, author, abstract, dates match). Smith–Montemanni Axioms
> 15(5):332 (2026): DOI 10.3390/axioms15050332 resolves to MDPI (paper is
> registered); MDPI blocks scraping, so its content is corroborated only by
> two independent research passes agreeing in detail — treat fine-grained
> claims (exact congruence 27 ≡ 0 mod 56 etc.) with slight caution.

**Scope.** Current state of knowledge (checked July 2026) on the hypothetical
Moore graph Γ of degree 57, diameter 2, girth 5, on 3250 vertices with
92,625 edges; spectrum {57¹, 7¹⁷²⁹, (−8)¹⁵²⁰}; intersection array
{57,56;1,1}. Open since Hoffman–Singleton (1960). Status tags:
**(a)** peer-reviewed, **(b)** preprint, **(c)** folklore/derived/unverified.

**Headline (2026).** Two claimed non-existence proofs (Yang–Zhu 2019,
Makhnev 2020) are unpublished and the latter is explicitly rebutted;
existence remains open. The automorphism state of the art: |Aut(Γ)| ≤ 375,
and — by a June 2026 preprint of Ishida — **Aut(Γ) contains no involution,
so its order is odd**, leaving exactly the 24 odd orders of Mačaj–Širáň's
list (below) as possible.

---

## 1. Automorphism exclusions

### 1.1 The chain of results

- **Aschbacher 1971 (a).** Aut(Γ) is not a rank-3 permutation group; hence Γ
  is not distance-transitive. M. Aschbacher, *The nonexistence of rank three
  permutation groups of degree 3250 and subdegree 57*, J. Algebra **19**
  (1971), 538–540. doi:10.1016/0021-8693(71)90087-1. Aschbacher's analysis is
  also the source of the six-fold fixed-point-subgraph alternative used by
  all later work (Lemma below).
- **G. Higman, 1960s, unpublished (a via published accounts).** Γ is not
  vertex-transitive. Recorded in P. J. Cameron, *Automorphism groups of
  graphs*, Selected Topics in Graph Theory 2 (1983), 89–127; full proof in
  P. J. Cameron, *Permutation Groups*, LMS Student Texts 45, CUP 1999 (proof
  of Theorem 3.13), and Brouwer–Haemers, *Spectra of Graphs*, Springer 2012,
  Prop. 11.5.2. The argument shows an involution fixes exactly 56 vertices
  forming a star K₁,₅₅. The Mačaj–Širáň slides (Rio, Dec 2008) attribute to
  Higman the stronger statements: |Aut(Γ)| **not divisible by 4**, hence
  Aut(Γ) **solvable** — treat "solvable" as **(c)** unless checked against
  Cameron's text.
- **Fixed-subgraph theorem for involutions (a).** If t ∈ Aut(Γ) is an
  involution then Fix(t) ≅ K₁,₅₅ (56 fixed vertices). Higman's argument;
  recorded explicitly as Makhnev–Paduchikh 2001, Lemma 4; also
  Makhnev–Paduchikh 2009, Prop. 1.
- **Makhnev–Paduchikh 2001 (a).** If |Aut(Γ)| is even then |Aut(Γ)| ≤ 550.
  A. A. Makhnev, D. V. Paduchikh, *Automorphisms of Aschbacher graphs*,
  Algebra and Logic **40**(2) (2001), 69–74. doi:10.1023/A:1010217919915.
- **Makhnev–Paduchikh 2009 (a).** *On the automorphism group of the
  Aschbacher graph*, Proc. Steklov Inst. Math. **267**, Suppl. 1 (2009),
  S149–S163; announcement Dokl. Math. **79**(3) (2009), 365–368.
  doi:10.1134/S0081543809070141. Further structure analysis of the
  even-order case. **Caveat:** full text not accessed; superseded by
  Mačaj–Širáň and now Ishida in any case.
- **Fixed-subgraph alternative for odd prime order (a).**
  (Makhnev–Paduchikh 2001, Lemma 3; Mačaj–Širáň 2010, Lemma 4; going back to
  Aschbacher.) If x ∈ Aut(Γ) has odd prime order p, then one of:
  1. Fix(x) = ∅ and p ∈ {5, 13};
  2. Fix(x) = single vertex and p ∈ {3, 19};
  3. Fix(x) = star K₁,₁₊₇ℓ (ℓ ≥ 0) and p = 7;
  4. Fix(x) = pentagon (C₅) and p ∈ {5, 11};
  5. Fix(x) = Petersen graph and p = 3;
  6. Fix(x) = Hoffman–Singleton graph and p = 5.
  Consequently the only primes dividing |Aut(Γ)| are 2, 3, 5, 7, 11, 13, 19;
  |Aut(Γ)| divides 2·3⁴·5⁶·7²·11·13·19.
- **Mačaj–Širáň 2010 (a) — the main quantitative theorem.** M. Mačaj,
  J. Širáň, *Search for properties of the missing Moore graph*, Linear
  Algebra Appl. **432**(9) (2010), 2381–2398. doi:10.1016/j.laa.2009.07.018.
  - |Aut(Γ)| ≤ 375. Precisely:
  - **If |Aut(Γ)| is odd:** |Aut(Γ)| ∈ {1, 3, 5, 7, 11, 13, 15, 19, 21, 25,
    27, 35, 39, 45, 55, 57, 75, 81, 125, 135, 147, 171, 275, 375}
    (24 orders; max 375 = 3·5³).
  - **If |Aut(Γ)| is even:** |Aut(Γ)| ∈ {2, 6, 10, 14, 18, 22, 38, 50, 54,
    110} (max 110) — now moot given Ishida.
  - Except for 110, every possible order has ≤ 2 distinct prime factors.
  - Lemma 12 tabulates displacement pairs (a₀(x), a₁(x)) per prime order
    (a₀ = #fixed vertices, a₁ = #vertices moved to a neighbour):
    p=7: a₀ ∈ {2,9,16,23,30,37,44,51} with a₁ in arithmetic progressions
    mod 105; p=11: a₁ ∈ {55,220,385}; p=13: a₁ ∈ {65,260,455};
    p=19: a₁ ∈ {57,342}. (Reconstructed from Ishida §7 + 2008 slides; LAA
    text paywalled.)
  - Method: Higman's character method (χ₁(x) = (8a₀(x) − a₁(x) + 50)/15 ∈ ℤ),
    orbit-matrix conditions (quotient B with B² + B − 56I = row-block J
    structure, eigenvalues ⊆ {57,7,−8}, Tr(B) ≡ 80 − 8m mod 15), Sylow
    theory, GAP small-groups computations.
- **Kováčiková 2015 / arXiv:1812.05353 (b; PhD thesis).** Computer-assisted
  counts of induced ≤10-vertex subgraphs: for order 7, a₁(x) divisible by
  49, eliminating a₀ ∈ {44,51} and pinning a₁ = 7a₀ + 35 (thesis Thm 5.1).
  Also: #induced copies of any 10-vertex graph depends only on #induced
  Petersen subgraphs.
- **Ishida 2026 (b) — newest.** Y. Ishida, *No involutions in the missing
  Moore graph*, arXiv:2606.29183 (v1 28 Jun 2026; v2 8 Jul 2026).
  [VERIFIED on arXiv 2026-07-22.]
  **Theorem 1.1: Aut(Γ) has no element of order 2; hence |Aut(Γ)| is odd.**
  Method: trace–rank identity from the Brauer quotient of p-permutation
  lattices — for prime order p and spectral idempotent E_θ preserving the
  p-adic vertex lattice, the character value equals rank_{F_p}(E_θ[F] mod p)
  on fixed vertices; at p=2 with Fix(t) = K₁,₅₅ forces a₁(t) = −368 < 0,
  contradiction. **Theorem 1.2** (exact displacement counts, odd primes):

  | p  | a₀(x)                  | a₁(x)                         |
  |----|------------------------|-------------------------------|
  | 7  | ∈ {2, 9, 16, 23, 30, 37} | 7·a₀(x) + 35                |
  | 11 | 5                      | 55                            |
  | 13 | 0                      | 65                            |
  | 19 | 1                      | 57                            |

  For p ∈ {3,5} neither spectral idempotent is p-integral and the method
  gives nothing. Not yet peer-reviewed.

### 1.2 Status table: element orders

| Element order | Fixed subgraph | Displacement constraints | Status / source |
|---|---|---|---|
| 2 | K₁,₅₅ | **excluded entirely** (a₁ = −368 < 0) | (b) Ishida 2026 |
| 3 | K₁ or Petersen | character congruences only | open; (a) M–P 2001 / M–Š 2010 |
| 5 | ∅, C₅, or HS | character congruences only | open; (a) M–P 2001 / M–Š 2010 |
| 7 | K₁,₁₊₇ℓ | a₀ ∈ {2,…,37}, a₁ = 7a₀+35 | open; (b) Kováčiková, Ishida |
| 11 | C₅ | a₀ = 5, a₁ = 55 | open; (b) Ishida 2026 |
| 13 | ∅ | a₀ = 0, a₁ = 65 (semiregular!) | open; (b) Ishida 2026 |
| 19 | K₁ | a₀ = 1, a₁ = 57 | open; (b) Ishida 2026 |
| other primes | — | impossible | (a) M–Š 2010 |

Note (session): an order-3 element fixing exactly ONE vertex is impossible
by character integrality: a₁ = 0 (triangle-freeness at the fixed star) gives
χ₁ = (8·1 − 0 + 50)/15 ∉ ℤ. So order 3 forces Fix ≅ Petersen. [Re-derived
during Codex consult; consistent with M–Š Lemma 12.]

### 1.3 Status table: group orders

| Group order | Status | Source |
|---|---|---|
| even (any) | **excluded** | (b) Ishida 2026 |
| odd ∉ list | excluded | (a) M–Š 2010 |
| {1,3,5,7,11,13,15,19,21,25,27,35,39,45,55,57,75,81,125,135,147,171,275,375} | not excluded (24 cases) | (a)+(b) |
| > 375 | excluded | (a) M–Š 2010 |

**No published improvement of 375 between 2010 and 2026.** Only direct
attacks post-2010: Kováčiková (2015), Ishida (2026).

Session corollary (for semiregular searches): a group acting semiregularly
must have order dividing 3250 = 2·5³·13 AND in the odd list above →
**semiregular orders are exactly {1, 5, 13, 25, 125}**; m = 125 is the
largest, giving b = 26 orbits.

### 1.4 Claimed non-existence proofs (both unaccepted)

- **Yang–Zhu 2019 (c).** *The missing Moore graph is really missing*,
  manuscript Oct 2019 (ScienceOpen; never on arXiv today, never published).
  "Fractal block designs". No independent verification; not cited as valid
  anywhere. Treat as invalid.
- **Makhnev 2020 (b, rebutted).** arXiv:2010.13443 (Russian). Claims the DRG
  {55,54,2;1,1,54} (second subconstituent of an edge) cannot exist.
  **Rebutted** by V. Faber, J. Keegan, *Existence of a Moore graph of degree
  57 is still open*, arXiv:2210.09577 (2022–23): the constraint system
  "factors into small diagonal blocks all of which have solutions". Never
  published. Community consensus: open.

---

## 2. Substructure results

- **Petersen-minus-an-edge (a/c).** Every path of length 3 lies in a unique
  pentagon ⟹ Γ contains induced Petersen-minus-an-edge (Dalfó survey,
  credited to W. J. Martin). **Induced Petersen: open** (Godsil). Nothing
  published excludes/forces induced Petersen or induced HS.
- **Dalfó 2019 survey (a).** C. Dalfó, *A survey on the missing Moore
  graph*, Linear Algebra Appl. **569** (2019), 1–14.
  doi:10.1016/j.laa.2018.12.035. Contents:
  - **Independence number:** α(Γ) ≤ 400 (ratio bound 3250/(1+57/8)).
  - **Independent-copies bounds** (Prop. 4.2; partly Fiol–Garriga 2006):
    max # pairwise independent copies: K₁ → 400; K₂ → 225; C₅ → 100;
    Petersen → 55; HS → 15. Equality forces a completely regular code.
  - **If a 400-coclique exists** (Fiol–Garriga 2006 / Thm 5.5): graph on the
    other 2850 vertices is DRG {49,48,8;1,1,42}, spectrum
    {49¹, 7¹³³⁰, (−1)³⁹⁹, (−8)¹¹²⁰}.
  - **Second subconstituents** (Thm 5.2): Γ(u) is DRG {56,55,1;1,1,56} on
    3192 vertices — antipodal 56-cover of K₅₇; Γ(uv) is DRG {55,54,2;1,1,54}
    on 2970. Reconstruction from either ⟺ existence of Γ.
  - **Line graph** L(Γ) is DRG {112,56,55;1,1,4}; Γ edge-distance-regular.
  - **Prop. 5.4 (negative):** graphs induced at distance 2 from C₅/Petersen,
    or distance 1 from HS, have ≥ 5 distinct eigenvalues.
  - Sabidussi 1996; Schwenk 1995 (talk) — subgraph spectra.
- **Renteln 2020/2021 (a, with correction).** AJC **77**(3) (2020) 373–382;
  correction AJC **79**(1) (2021) 193–194. Post-correction: (i) canonical
  I₃₂₅⊗(P+P⁻¹) block form impossible; (ii) only equal-parts biregular
  bipartition has bidegree (32,32); (iii) equal-size bipartitions:
  rk(B) ≤ 1522, diagonal blocks invertible, 24.5 ≤ ⟨a⟩ ≤ 32.
- **Ducey 2017 (a).** *On the critical group of the missing Moore graph*,
  Discrete Math. **340**(5) (2017), 1104–1109; arXiv:1509.00327. Critical
  group determined up to two possibilities (5-part open).
- **Chromatic number (c — literature gap).** Nothing published. Trivially
  χ ≥ ⌈3250/400⌉ = 9. χ′ ∈ {57,58} (Vizing), undetermined.
- **Latin-rectangle equivalence (a).** Smith–Montemanni 2024: existence of Γ
  ⟹ complete decreasing set of MOLRs with n = 56; converse fails (Wanless
  2024: decreasing set of 32 MOLRs not from a valid t-subgraph).

---

## 3. Prior computational searches

**No exhaustive search under any nontrivial prescribed automorphism group
has ever been published.** Orbit-matrix analyses constrain but never
enumerate. What exists:

- **Mačaj–Širáň 2010:** GAP over small-groups library — group-theoretic
  case analysis only, no graph-level enumeration.
- **Smith–Montemanni 2023 (a).** EURO J. Comput. Optim. **11** (2023)
  100060. Heuristic edge-max: 18-month run stalled at deficit ~41,391 of
  92,625 edges. No symmetry assumed. Non-proof evidence of nonexistence.
- **Smith–Montemanni 2024 (a).** Symmetry **16**(12) (2024) 1563. Defines
  **t-subgraphs** (t branches of the distance tree; t = 57 ⟺ Γ exists).
  Unrestricted heuristics: t ≤ 15. Cyclic assumption (matchings = powers of
  one 56-cycle): CP-SAT reaches **t ≤ 20**; t = 21 unresolved after 4–5-day
  runs. Byproduct: 19 MOLRs with n = 56 (GitHub:
  DerekSmithSouthWales/19MOLRS).
- **Smith–Montemanni 2026 (a).** Axioms **15**(5) (2026) 332.
  doi:10.3390/axioms15050332. [DOI verified to resolve; content
  double-sourced.] **Theorem 1: the full Moore graph cannot have all
  matchings from a cyclic group of derangements** (counting: 27 ≢ 0 mod 56).
  Remaining split: (2) matchings from a non-cyclic group of derangements —
  necessarily semiregular of order exactly 56 → the 13 groups of order 56, finite
  case list, OPEN; (3) matchings not a group (all-involutions — NB HS is
  built from 15 involutions not forming a group; none; mixed). Conjectures:
  no potential t-subgraph for t ≥ 21.
- **Kováčiková 2015 (b).** Induced-subgraph counting (linear algebra, not
  search).
- **SAT note (c).** No published pure-SAT/ILP feasibility attack at any
  scale. Genuine gap.

**Exhausted subspaces:** rank-3 / vertex-transitive; any even-order group
(preprint-level); odd orders outside M–Š list; all-matchings-cyclic
construction; cyclic t-subgraphs exist up to t = 20 (no contradiction below
t = 21 under that assumption).

---

## 4. Spectral / SDP / polynomial-method attempts

- **Classical feasibility:** passes all standard conditions (integrality,
  Krein, absolute bound); listed feasible in Brouwer's srg tables.
- **SDP: nothing published.** No Terwilliger-algebra SDP, no Lasserre
  attempt on this parameter set. Gap, not exclusion. (Codex consult: the
  basic local SDP is provably feasible — explicit fractional point with
  spectrum 57¹ 7⁵⁷ (−8)⁵⁷ 0³¹³⁵ — so plain SDP cannot exclude; only
  integrality/rank-augmented or high-level moment relaxations could.)
- **Character/lattice methods (the actual frontier):** Higman's character
  method + Ishida's trace–rank upgrade (exact modular rank equalities).
  Stops at p ∈ {3,5} (idempotents not p-integral).
- **Ducey's SNF/p-adic constraints** (§2).
- **Faber–Keegan 2022 (b):** arXiv:2210.09577 — constraint framework for
  the {55,54,2;1,1,54} DRG; diagonal-block systems solvable (no exclusion).
- **Spectral Moore theorems** (Cioabă–Koolen–Nozaki et al.,
  arXiv:2004.09221): cite the problem, no new exclusion.

---

## 5. Counting facts (cycle structure)

Verified against spectrum {57¹, 7¹⁷²⁹, (−8)¹⁵²⁰}:

| Fact | Value | Status |
|---|---|---|
| Vertices / edges | 3250 / 92,625 | (a) |
| Distance-2 counts from vertex / edge | 3192 / 2970 | (a) |
| Pentagons per **vertex** | k(k−1)²/2 = **89,376** | (a) Dalfó §2 |
| Pentagons per **edge** | (k−1)² = **3136** | (c) see warning |
| Pentagons per **2-path** | k−1 = **56** | (a) |
| Pentagons per **3-path** | exactly **1** | (a) |
| Total pentagons | tr(A⁵)/10 = **58,094,400** | (c) derived |
| Total hexagons | **2,662,660,000** | (c) derived from spectrum |
| Hexagons per vertex / edge | 4,915,680 / 172,480 | (c) derived |

**Warning:** Dalfó's UPC preprint says 3192 pentagons per edge; the
consistent value is (k−1)² = 3136 (5·58,094,400/92,625 = 3136 exactly).

---

## 6. Open smallest cases (search targets)

1. **Order 3** — Fix = Petersen forced (single-vertex case dies on character
   integrality). Untouched by Ishida (3-adic obstruction). Most attractive
   analytic target.
2. **Order 5** — Fix ∈ {∅, C₅, HS}. 5-adic obstruction. The HS-fixed case
   is tantalizing and open.
3. **Orders 7, 11, 13, 19** — exact displacement counts known (Ishida
   Thm 1.2); none has a published exhaustive search. **C₁₃ acts freely**
   (a₀=0) on 3250 = 13·250; C₁₉ has exactly one fixed vertex, 171 orbits of
   19 among the remaining 3249... (3249 = 171·19).
4. **Group orders:** all 24 odd orders; largest unexcluded 375, 275, 171,
   147, 135, 125. No published exhaustion of any specific one.
5. **Construction subspaces:** non-cyclic order-56 derangement groups (13
   groups, finite case analysis, explicitly open); all-involution matchings
   (HS-style); unstructured.
6. **t-subgraph frontier:** decide potential-21-subgraph existence.

---

## 7. Bibliography

(As numbered in the survey text above; chronological within topic.)

1. M. Aschbacher, J. Algebra 19 (1971) 538–540.
2. P. J. Cameron, Selected Topics in Graph Theory 2 (1983) 89–127.
3. P. J. Cameron, Permutation Groups, CUP 1999.
4. A. A. Makhnev, D. V. Paduchikh, Algebra and Logic 40(2) (2001) 69–74.
5. A. A. Makhnev, D. V. Paduchikh, Proc. Steklov Inst. Math. 267 S1 (2009)
   S149–S163.
6. M. Mačaj, J. Širáň, Linear Algebra Appl. 432 (2010) 2381–2398.
7. K. Kováčiková, PhD thesis, Comenius Univ. 2015; arXiv:1812.05353.
8. Y. Ishida, arXiv:2606.29183 (2026).
9. A. J. Hoffman, R. R. Singleton, IBM J. Res. Develop. 4 (1960) 497–504.
10. M. Miller, J. Širáň, Electron. J. Combin. DS14v2 (2013).
11. C. Dalfó, Linear Algebra Appl. 569 (2019) 1–14.
12. A. E. Brouwer, W. H. Haemers, Spectra of Graphs, Springer 2012.
13. A. E. Brouwer, H. Van Maldeghem, Strongly Regular Graphs, CUP 2022.
14. M. A. Fiol, E. Garriga, Linear Multilinear Algebra 54(2) (2006) 123–140.
15. G. Sabidussi, European J. Combin. 17 (1996) 69–87.
16. A. J. Schwenk, Kalamazoo talk, 1995 (unpublished).
17. J. E. Ducey, Discrete Math. 340(5) (2017) 1104–1109.
18. P. Renteln, Australas. J. Combin. 77(3) (2020) 373–382; corr. 79(1)
    (2021) 193–194.
19. D. H. Smith, R. Montemanni, EURO J. Comput. Optim. 11 (2023) 100060.
20. D. H. Smith, R. Montemanni, Symmetry 16(12) (2024) 1563.
21. D. H. Smith, R. Montemanni, Axioms 15(5) (2026) 332.
22. A. A. Makhnev, arXiv:2010.13443 (2020) — rebutted.
23. V. Faber, J. Keegan, arXiv:2210.09577 (2022–23).
24. X. Yang, X. Zhu, ScienceOpen manuscript (2019) — unaccepted.
