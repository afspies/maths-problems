# Attack angles

- `subset-slack/` — **promising, proved:** exact equality/near-equality slack
  decomposition and a strengthened excess-peeling subset inequality, with an
  instance-sensitive product corollary.
- `k3-analogue/` — **partial result:** the natural parameter-free extension
  fails on an exact five-vertex witness, but a corrected inequality
  `5γ_G(S)≤2|S|+ρ³(G)` and its product corollary are proved. Exact
  reoptimization shows they do not alone raise 0.5643.
- `terminal-conflict/` — **proved:** terminal subset domination is exactly a
  matching-cover parameter. Lemma 2.2 is tight exactly for conflict graphs
  that are disjoint unions of odd cliques, with quantitative stability.
- `terminal-capacity/` — **proved refinement:** a Hall-deficiency
  capacity-two certificate sharpens terminal equality to unions of `K₁` and
  `K₃` and gives a stronger peeling inequality.
- `fibre-slack/` — **proved:** the total slack in Steiner's oriented product
  bound decomposes exactly into vertical, projection, partition-additivity,
  and subset-domination defects, giving row/column equality conditions.
- `incidence-balance/` — **proved classification:** formal Steiner equality
  eliminates every peeling step, fixes the singleton/triangle counts in
  every column, and forces balanced disjoint row exchanges; a unique-hole
  condition isolates the missing coordinate-level bridge.
- `external-private-holes/` — **proved bridge:** exact atomic/additive
  columns have no self-private projection vertices; singleton holes landing
  in one row satisfy a quantitative subset-domination inequality and become
  a two-packing at zero row slack.
- `packing-hierarchy/` — **proved obstruction:** the full additive hierarchy
  of integer `k`-packing subset/product bounds is derived and shown to retain
  Steiner's exact 0.5643 minimax obstruction.
- `fractional-tensor/` — **proved orthogonal bridge:** tensoring fractional
  packings with an exact local-concentration denominator gives a two-sided
  product bound and a regular-graph criterion; `P4` blocks totals-only caps.
- `fractional-rank-one-limits/` — **proved no-go plus graph-class gain:**
  rank-one tensors have an exact universal ceiling, while a diffuse
  suboptimal packing beats Steiner on an explicit split-graph pair.
- `square-clique-cover/` — **proved orthogonal bound:** fractional clique
  covers of graph squares give a one-sided product theorem and prove Vizing
  for centered-perfect-square factors, but have unbounded universal loss.
- `bidirectional-blocker/` — **proved nonseparable lift and obstruction:**
  weighted integral domination blockers certify every `G□P₄` exactly, while
  vertex-transitive line graphs drive the standalone lift back to `1/2`.

Next work should couple the row hole packings across different rows without
using factor order, or build a second-order hybrid of the blocker lift with
Steiner/fractional certificates.
