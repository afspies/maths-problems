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

## Session 2 deltas

- Two-sparse subset domination is exactly `|S|-ν(F_G(S))`; the matching
  bound is tight iff the conflict graph is a disjoint union of odd cliques.
- The total slack in Steiner's oriented product theorem has an exact
  four-source decomposition. Any near extremizer must simultaneously satisfy
  row, column, partition-additivity, and subset-structure constraints.
- Every additive integer packing/domination level preserves the exact
  Steiner obstruction. The five-vertex gadget has
  `ρ^k=⌊3k/2⌋`, `γ^k=⌈3k/2⌉`, so local hierarchy slack cannot be forced.
- Fractional packing tensors give a genuinely orthogonal bound with local
  concentration `κ`. `P4` proves that totals or connectedness alone do not
  control `κ`.

## Revised next move

Do one of two things:

1. combine the row-wise minimum `H`-set conditions with the column-wise
   injective projections and odd-clique terminal structures; or
2. prove a quantitative tradeoff between `γ/γ_f` and the least attainable
   tensor concentration among near-optimal fractional packings.

Do not extend the additive `k`-packing hierarchy further.

## Session 3 deltas

- Terminal odd-clique equality was not the end of the classification.
  Capacity-two weights plus Hall deficiency exclude every `K_{2m+1}` with
  `m≥2`; only `K₁` and `K₃` survive.
- The terminal capacity defect can be propagated through peeling to give a
  rigorous subset inequality strictly stronger than the excess-only version.
- At the formal Steiner ratios, exact fibre equality eliminates all peeling:
  every `L_i` contains maximum ordinary and optimal 2-packings with the same
  fixed singleton/triangle counts.
- Tight complement dominators are anticomplete to their `L_i`. The occupied
  and vertical cell matrices have identical margins and disjoint row
  supports, but an exact skeleton shows those facts still do not encode
  product domination.
- The missing incidence data are coordinate holes. External private targets
  force a singleton hole; self-private targets allow a larger hole set. Do
  not silently apply the singleton claim to self-private vertices.
- Optimal rank-one fractional packings cannot provide a universal
  integrality-gap/concentration tradeoff: `P4` forces concentration one.
  Deliberately suboptimal diffuse packings can still give strong class bounds.
- Fractional clique covers of graph squares give a clean one-sided theorem
  and centered-perfect graph classes, but triangular graphs show unbounded
  universal loss.

## Revised next move after session 3

1. Prove or refute an aggregate lower bound on the number of external private
   targets in each tight complement dominator.
2. Couple singleton coordinate holes to the disjoint minimum exchanges in
   `H` and the fixed `K₁/K₃` atoms in the columns.
3. In parallel, try a nonseparable higher-rank packing ansatz or a
   center-aware lift of the square-clique LP.

Do not return to terminal atom ratios, optimal rank-one concentration, or an
unrestricted square-clique/theta relaxation.
