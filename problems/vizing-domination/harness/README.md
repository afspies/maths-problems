# Exact hygiene harness

This directory verifies definitions and small examples. It is **not** evidence
towards Vizing's conjecture: finite graph checks cannot prove the universal
inequality.

`graph_hygiene.py` provides exact brute-force domination numbers, subset
domination, Cartesian products, two-packings, and integer `k`-packing and
`k`-dominating functions. `optimization.py` evaluates Steiner's normalized six
lower bounds using `fractions.Fraction` and records both sides of the invalid
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
packings, and exercise the coordinate-hole adversarial skeleton. The suite
currently contains 20 tests.
