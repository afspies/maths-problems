# Vizing’s domination conjecture

## Statement

For all finite simple graphs `G,H`, is

`γ(G □ H) ≥ γ(G)γ(H)`?

Here `γ` is the domination number and `□` is the Cartesian product.

## Status / context

The conjecture remains open. Clark and Suen proved the universal factor `1/2`
in 2000. Steiner's June 2026 preprint proves the first constant improvement,

`γ(G□H) ≥ ((5+√73)/24)γ(G)γ(H) ≈ 0.5643γ(G)γ(H)`

[@steiner2026]. The July 2026 preprint claiming 0.5809
[@aliabadiKrop2026] is withdrawn with the author comment “Algebraic mistake”;
its precise failure is audited in
`literature/withdrawn-2607.01109-audit.md` and it is not used as a theorem.

## Certificate + verifier

- **Universal proof:** no finite graph certificate can establish the conjecture.
  A proof artifact must be checked deductively.
- **Counterexample certificate:** two explicit finite graphs `G,H`, minimum
  dominating sets for the factors, and a proof that every set of fewer than
  `γ(G)γ(H)` vertices fails to dominate `G□H`. Exact brute force is cheap only
  for small instances; a serious large certificate would require a
  proof-logging optimization encoding.
- **Hygiene verifier:** `harness/graph_hygiene.py` computes exact small-graph
  domination numbers, products, subset domination, and integer `k`-packing /
  `k`-domination numbers. `harness/optimization.py` checks rational and
  `Q(√73)` identities. These checks prevent definition and algebra errors; they
  are explicitly not progress on the universal conjecture.

## Known structure (bake into any search)

- `ρ(G)≤ρ^{\{2\}}(G)/2≤γ(G)`, where `ρ` is the two-packing number and
  `ρ^{\{2\}}` the maximum total weight of an integer 2-packing function.
- Steiner's key subset lemma is
  `3γ_G(S)≤|S|+ρ^{\{2\}}(G)`.
- The exact relaxed four-parameter optimization behind Steiner's constant is
  already sharp. Numerical reoptimization of the same inequalities cannot
  improve 0.5643.
- This session strengthens the subset lemma by an excess-peeling defect and
  gives an exact equality/near-equality decomposition; see
  `angles/subset-slack/README.md`.
- The naive `k=3` extrapolation is false on an exact five-vertex witness, but
  the corrected inequality `5γ_G(S)≤2|S|+ρ^{\{3\}}(G)` holds and yields a new
  product bound. The old relaxed equality point extends to this bound, so it
  does not alone improve 0.5643; see `angles/k3-analogue/README.md`.

## Angle-of-attack menu (be exploratory — draw from different fields)

- **Combinatorial stability:** force aggregate positive defect in the
  vertically dominated subsets in Steiner's fibre proof.
- **Packing hierarchy:** seek a corrected higher-capacity inequality with an
  additional obstruction parameter; the parameter-free `k=3` guess is dead.
- **LP/integer duality:** compare integer `k`-packing defects with fractional
  domination and identify rounding structure that product fibres enforce.
- **Extremal constructions:** build graphs/subsets realizing equality in every
  step to decide whether the 0.5643 framework is structurally sharp.
- **Proof-logged constraints:** use SAT/ILP only to falsify proposed finite
  bridge lemmas and extract small obstructions, never as evidence for the
  universal conjecture.

## First steps

1. Determine whether the fibre sets `L_i` can all have zero peeling defect and
   terminal-tight matching structure simultaneously.
2. Classify terminal equality in the two auxiliary matching bounds more
   graph-theoretically (beyond the exact slack equations).
3. If no aggregate defect can be forced, pivot to a different product
   decomposition rather than reoptimizing Steiner's six inequalities.
