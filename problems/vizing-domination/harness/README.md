# Exact hygiene harness

This directory verifies definitions and small examples. It is **not** evidence
towards Vizing's conjecture: finite graph checks cannot prove the universal
inequality.

`graph_hygiene.py` provides exact brute-force domination numbers, subset
domination, Cartesian products, two-packings, integer `k`-packing and
`k`-dominating functions, near-cover profiles, and the small-instance typed
fibre relaxation. `optimization.py` evaluates Steiner's normalized six lower
bounds using `fractions.Fraction` and records both sides of the invalid
algebraic replacement in arXiv:2607.01109v1.

Run:

```bash
cd problems/vizing-domination/harness
python3 -m unittest -v
```

The named-graph fixtures include `P2 □ P2 = C4`, whose domination number is 2,
and exact checks of Lemma 2.3, the peeling-defect strengthening, and the
corrected `k=3` subset inequality on every subset of several small graphs.
They also exhaust the matching-cover equality classification through five
vertices, verify its capacity-two `K₁/K₃` refinement, check the all-level
packing/domination equality gadget, validate exact split-graph fractional
packings, and exercise the coordinate-hole adversarial skeleton. New fixtures
check the external-private atomic theorem and its additivity obstruction, the
`C₅□C₅` cycling-corner obstruction, `P₄` blocker targets, zero saturation
defect on `C₅`, and a diffuse split-graph tensor. Additional fixtures cover
exact anchored/capped surd identities, the common-crown concentration
witness, the `C₄` combined-lift benchmark, and the `K₂□P₃` length-two escape
cycle. The typed-fibre fixture separates cardinality feasibility from actual
product domination. New exhaustive fixtures verify the two-axis near-cover
profile inequality, its exact isolation slack, the correlated fractional
charging identity, and the corrected `s+t-st` cap obstruction. Session-seven
fixtures verify the four-region overlap and multiplicity identities,
cardinality-slack correction, the realization of arbitrary bipartite escape
graphs by one-subdivision perfect codes, and the indexed-provider reuse
obstruction together with its distinct adaptive provider matching. The
session-eight fixtures exhaust the joint-dependency stability lemma on named
small graphs, verify the balanced eleven-vertex adaptive-target obstruction,
the covering triangle block design, and the cap-half and triangle-mixture
identities in `Q(√73)`. The suite currently contains 41 tests.
