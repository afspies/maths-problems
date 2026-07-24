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
- Row hole two-packings tensor with any factor packing, but a common-crown
  construction shows that private incidences can concentrate where every
  such weighting has negligible mass. Full formal balance adds the exact
  common-neighborhood bound `M(Y)≤2γ(H)ρ(H)+sd`, which is still vacuous at
  the formal ratios when the factor domination numbers are comparable.
- Two-sided external privacy forces a directed cycle inside the product:
  every step changes one coordinate by an edge and the other by distance
  exactly two. Escape indegrees are bounded by the row-hole packing numbers
  and retain a red-diagonal/blue-cross-zero cell-label pattern. The
  `C₅□C₅` perfect code realizes the cycle sharply.
- The full additive integer packing/domination hierarchy retains the same
  formal 0.5643 obstruction at every level.
- Rank-one fractional tensors and unrestricted square-clique LPs both have
  certified universal obstructions; their surviving value is in graph-class
  bounds and in suggesting higher-rank or center-aware lifts.
- A nonseparable bidirectional weighted-domination blocker certifies Vizing
  for every `G□P₄`, but vertex-transitive line graphs force that standalone
  relaxation back toward `1/2`. Pure higher-rank fractional packing is also
  blocked by the split-graph `□P₄` family.
- The blocker's saturation-defect slice satisfies the exact overlap identity
  `Δ=γ-Q-Ω≤γ-Q`; the canonical half-2-packing can therefore only meet, never
  beat, Steiner at the formal point. Its fully optimized anchored value has
  an exact dual, but formal-ratio split/cycle mixtures keep it below `c`.
- Even combining both optimized anchored arms with independently capped
  rank-one packings fails on an exact asymmetric additive counterfamily
  approaching `(a,b)` in both factors. A natural two-sided ordinary-packing
  residual slice of the full blocker also collapses to `a`. These are STOPs
  for factor-marginal hybrids, not for the unsliced blocker or labelled
  product geometry.
- A shared-capacity lift `Ξ` combines a true fractional packing on the
  product with the full bidirectional blocker. Its exact dual is a product
  fractional dominator that simultaneously routes owner-indexed averaged
  integral dominators of both factors. Asymmetric-scale connected
  vertex-transitive Cayley graphs built from inefficient translate covers
  drive `Ξ/(γ(G)γ(H))` to zero. Thus even this combined owner-indexed LP is a
  universal STOP.
- The surviving typed fibre relaxation keeps the actual row label sets
  `A_g` and their imports `V_g=⋃_{x∈N(g)}A_x`. Product domination implies
  `|A_g|≥γ_H(V(H)\V_g)` in every row, with a symmetric column condition.
  Its universal value is open.
- The near-cover profile `u_K(t)=min_{|C|≤t}|V(K)\N[C]|` satisfies the
  exact two-axis inequality
  `Σ_g u_H(|A_g|)+Σ_hu_G(|B_h|)≤|G||H|`, with a defect identity whose
  final term counts isolated induced fibres. A robust adaptation of the
  random translate-cover construction proves that this bound clears every
  two-scale pair in the Cayley family that kills `Ξ`, by a diverging factor
  when both factors grow.
- Fractional factor packings satisfy the exact correlated typed inequality
  `|A|≥PQ+Σ_A(1-q_g)(1-p_h)+max{E_H,E_G}`, where the energies measure
  subset-domination minus packing mass in the actual remaining row and
  column targets. For half-integral 2-packings, every nonzero repair gap
  costs at least one half.
- For an actual product dominator, every fibre-isolated point without an
  external private neighbor charges to a repeated same-label import or
  cross-coordinate redundancy. Consequently a quantitative set of points
  carries the labelled mixed-distance escape obligation; the remaining gap
  is to close or bound the length of those escape paths.
- The formal-ratio three-arm counterfamily can also be connected through
  safe zero-weight ports while preserving `γ,ρ,ρ²` and only decreasing its
  anchored/capped values. Connectedness alone does not repair the marginal
  no-go.

## Angle-of-attack menu (be exploratory — draw from different fields)

- **Combinatorial stability:** force aggregate positive defect in the
  vertically dominated subsets in Steiner's fibre proof.
- **Packing hierarchy:** seek a corrected higher-capacity inequality with an
  additional obstruction parameter; the parameter-free `k=3` guess is dead.
- **LP/integer duality:** compare integer `k`-packing defects with fractional
  domination and identify rounding structure that product fibres enforce.
- **Typed fibre sets and escape dynamics:** retain the actual correlated row
  label sets, private-target maps, and cell-owner transitions. Even
  owner-indexed averaged factor dominators lose all positive constant.
- **Escape-cycle stability:** couple the mixed edge/distance-two cycle to the
  fixed `K₁/K₃` terminal atoms and exact row exchanges.
- **Square-graph lifts:** retain which square cliques have a common center,
  since the unrestricted fractional clique cover has unbounded loss.
- **Extremal constructions:** build graphs/subsets realizing equality in every
  step to decide whether the 0.5643 framework is structurally sharp.
- **Proof-logged constraints:** use SAT/ILP only to falsify proposed finite
  bridge lemmas and extract small obstructions, never as evidence for the
  universal conjecture.

## First steps

1. Combine the half-integral row/column repair energies with the fixed
   `K₁/K₃` terminal atoms at formal Steiner equality.
2. Prove that a positive fraction of labelled escape owners remain in the
   escape set, or that every departure charges collision,
   cross-coordinate redundancy, or an exact Steiner defect.
3. Use the near-cover and fractional defect identities only with actual
   fibre labels; their scalar relaxations remain insufficient on `C₄□C₄`.
4. Do not pursue additive `k`-packing, saturation-defect, capped-rank-one, or
   ordinary-packing residual slices further: each now has an exact STOP.
