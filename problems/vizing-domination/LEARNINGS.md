# Learnings — Vizing’s domination conjecture

## Rigorous deltas

- Steiner's four-parameter relaxation is exactly sharp at
  `x₁=y₁=(11-√73)/8`, `x₂=y₂=(13-√73)/12`. Numerical reoptimization of the
  same bounds is a STOP.
- Lemma 2.3 has an exact recursive slack decomposition. Equality requires
  three-hit, domination-tight dense reductions and simultaneous equality in
  both terminal matching/packing bounds. Slack at most two forbids any
  domination loss during peeling.
- The excess-peeling parameter gives a strict subset inequality and an
  additive product term, but that term depends on Steiner's fibre sets. It
  becomes a universal advance only if their aggregate defect can be forced.
- The naive `k=3` formula fails even in the two-sparse terminal regime.
  The corrected formula `5γ_G(S)≤2|S|+ρ³(G)` is tight on the counterexample.
- The corrected `k=3` product inequality is also active at Steiner's old
  relaxed worst point. A strict relation beyond `ρ³≥ρ²+ρ` is needed.

## Source hygiene

- arXiv:2607.01109 is withdrawn. Its error is the false replacement
  `AB-xy → 3AB-2Ay-2xB+xy`, not a subtle flaw later in the minimization.
- Literature priority for the peeling closure and corrected `k=3` synthesis
  has not been established. Describe them as session-derived results, not
  publication-priority claims.

## What to do first next time

Attack simultaneous tightness in the fibre sets `L_i`. Try to prove that
`Σ_i p_G(L_i)>0`, or that terminal equality in all `L_i` conflicts with the
same minimum dominating set `D`. If this fails, classify equality in the
terminal matching constructions more graph-theoretically. Do not spend a
session numerically optimizing the current inequalities.

