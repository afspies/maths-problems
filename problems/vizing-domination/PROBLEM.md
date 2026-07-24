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
- In the two-sparse terminal regime, the closed-neighborhood conflict graph
  converts subset domination exactly to matching cover. Lemma 2.2 is tight
  exactly for disjoint unions of odd cliques. A further capacity-two
  certificate sharpens equality in Lemma 2.3 to unions of `K₁` and `K₃`.
- Every unit of slack in Steiner's oriented product bound splits exactly into
  vertical, projection, partition-additivity, and subset-domination defects.
- At formal Steiner equality, every fibre set is already terminal, supports
  maximum ordinary and optimal 2-packings, has fixed `K₁/K₃` counts, and
  participates in balanced disjoint row/column exchanges.
- Exact atomic/additive columns have no self-private projection vertices.
  Their external private targets force singleton holes, and all holes landing
  in one row form a two-packing in the other factor; row slack `e` weakens
  this to the exact bound `|J|≤ρ+2e`.
- The full additive integer packing/domination hierarchy retains the same
  formal 0.5643 obstruction at every level.
- Rank-one fractional tensors and unrestricted square-clique LPs both have
  certified universal obstructions; their surviving value is in graph-class
  bounds and in suggesting higher-rank or center-aware lifts.
- A nonseparable bidirectional weighted-domination blocker certifies Vizing
  for every `G□P₄`, but vertex-transitive line graphs force that standalone
  relaxation back toward `1/2`. Pure higher-rank fractional packing is also
  blocked by the split-graph `□P₄` family.

## Angle-of-attack menu (be exploratory — draw from different fields)

- **Combinatorial stability:** force aggregate positive defect in the
  vertically dominated subsets in Steiner's fibre proof.
- **Packing hierarchy:** seek a corrected higher-capacity inequality with an
  additional obstruction parameter; the parameter-free `k=3` guess is dead.
- **LP/integer duality:** compare integer `k`-packing defects with fractional
  domination and identify rounding structure that product fibres enforce.
- **Hybrid blocker/Steiner certificates:** couple weighted integral
  domination blockers to the exact fibre defects; both pure fractional
  higher rank and the standalone blocker have certified obstructions.
- **Square-graph lifts:** retain which square cliques have a common center,
  since the unrestricted fractional clique cover has unbounded loss.
- **Extremal constructions:** build graphs/subsets realizing equality in every
  step to decide whether the 0.5643 framework is structurally sharp.
- **Proof-logged constraints:** use SAT/ILP only to falsify proposed finite
  bridge lemmas and extract small obstructions, never as evidence for the
  universal conjecture.

## First steps

1. Seek an order-free coupling among the two-packings of singleton holes in
   different rows. Bare row summation only gives an order lower bound.
2. Bound the cardinality of self-private vertices in a near-tight column
   from their two-packing number and the ambient capacity defect.
3. In parallel, couple the bidirectional blocker lift to Steiner's defect
   identity or to the fractional product bound.
4. Do not pursue the additive `k`-packing hierarchy further: it is now proved
   to preserve the exact obstruction at every level.
