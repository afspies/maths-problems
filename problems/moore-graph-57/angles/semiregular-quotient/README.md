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

**Next tools** (LEARNINGS queue item 1): analytic cyclotomic
integrality on abelian lifts (`character_notes.md` — abelian lifts need
a ∈ {13,17,21}), bit-blasted SAT + DRAT for a proof-carrying UNSAT,
before any further plain CP-SAT hours.

**Verdict so far.** No exclusion claimed; d=7 sanity analogues (b=2,5,10)
are instantly feasible, so the b=26 resistance is a real signal that
solutions, if any, are rare.
