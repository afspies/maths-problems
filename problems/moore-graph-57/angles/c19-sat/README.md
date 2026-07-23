# Angle: C₁₉-equivariant SAT (prescribed order-19 automorphism)

**Idea.** An order-19 automorphism fixes exactly one vertex
(Mačaj–Širáň; a₁ = 57 per Ishida's preprint). Encode the graph
equivariantly: permutation-matrix variables per block-pair orbit (84
orbits × 56² ≈ 263k primary vars), a₁ trace constraints, gauge
normalization, girth enforced lazily (CEGAR — every cut is a girth-5
consequence, so UNSAT would be a valid conditional exclusion).

**Status: encoder validated, CEGAR route CLOSED at d=57.**
`equivariant_sat.py` rediscovers Petersen (d=3) instantly and
Hoffman–Singleton (d=7) in 37 iterations / 0.1s (`validate.py`), so the
encoding is trusted. At d=57: 229 iterations / 20.5M clauses / 3h with
violation counts FLAT (~55–90k triangles, ~1M 4-cycle pairs per model) —
lazy girth does not converge at this scale. Quantified in JOURNAL
2026-07-22 and `../../results/README.md`.

**Verdict.** Methodological negative: pure CEGAR is dead here; eager
structural reduction (orbit-matrix level, algebraic ansatz, or eager
subsets of triangle constraints) is prerequisite for any future run.
The 18.7M-clause cut file was deliberately not migrated (regenerable via
`run_d57.py`; reload cost exceeds value).

**Caveat for any future UNSAT claim.** a₁ = 57 is Ishida-pinned
(preprint); the peer-reviewed alternative a₁ = 342 branch must also be
run (trace bound 18, not 3) for an unconditional order-19 exclusion.
