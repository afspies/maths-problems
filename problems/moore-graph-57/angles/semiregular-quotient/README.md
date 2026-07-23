# Angle: semiregular quotient matrices

**Idea.** Any group acting semiregularly with order m on the Moore graph
yields a b×b quotient matrix C (b = 3250/m) with C² + C − 56I = mJ, row
sums 57, even diagonal for odd m. Nonexistence of C excludes ALL
semiregular order-m actions at once. Intersecting the Mačaj–Širáň odd
order list with divisors of 3250: candidate semiregular orders are
exactly {1, 5, 13, 25, 125} — m=125 (b=26) is the top target, a small
finite question apparently never posed at this granularity.

**Status: OPEN — m=125 confirmed hard.** DFS (`quotient_scan.py`,
2·10⁹ nodes) and CP-SAT (`cp_quotient.py`, ~30h cumulative incl. two
full 12h fixed-a cluster runs) all UNKNOWN; see
`../../results/m125-quotient/`. Fixed-a trace decomposition (odd
a ∈ {11..23} exhausts the case) does not qualitatively help at 12h scale.

**Analytic state (2026-07-23, all verified — see `character_notes.md`
and the four `verify_*.py` scripts):**
- **Abelian order-125 lifts force a = 21** (mod-3 lemma; kills a ∈
  {13,17} analytically). Nonabelian lifts force a ∈ {13,17,21}.
  So bare-C UNSAT at {13,17,21} kills ALL order-125 semiregular
  actions; a = 21 alone kills every abelian group.
- Abelian a=21 diagonal data is multiplier-orbit rigid: 46,376 / 126 / 1
  aggregate patterns for Z₅³ / Z₂₅×Z₅ / Z₁₂₅ (Z₁₂₅ uniquely forced).
  No analytic kill; joint realizability needs the computational route.
- Mod 5 the quotient equation collapses to (C−2I)² ≡ 0; rank caps
  min(26−a, a+1, 12).

**Computational pipeline (`sat/`):** bit-blasted CNF encoder
(one-hot + table products + truth-table adders), sound symmetry breaking,
row-0 cube splitting (a=21 → 8 cubes, a=17 → 78, a=13 → 488), optional
theorem-backed mod-5 clauses, kissat + drat-trim proof checking. All
validation gates pass (d=7 analogues SAT + decode-verified; deliberate
UNSAT with drat-trim-VERIFIED proof; cube-union soundness). ~8.3M
clauses (11.6M with --mod5) per fixed-a instance.

**Verdict so far.** No exclusion claimed; d=7 sanity analogues (b=2,5,10)
are instantly feasible, so the b=26 resistance is a real signal that
solutions, if any, are rare. a=21 cube campaign (cluster) is the
current front; a ∈ {11,15,19,23} matter only for the group-free
bare-C question.
