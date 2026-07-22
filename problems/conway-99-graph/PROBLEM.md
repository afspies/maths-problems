# Conway's 99-graph problem

## Statement
Does a graph on 99 vertices exist in which every edge lies in a unique triangle
and every non-edge lies in a unique quadrilateral? Equivalently: does the strongly
regular graph srg(99, 14, 1, 2) exist? Asked by Biggs (1969), popularized by Conway,
who offered $1000 for a resolution. Open in both directions.

## Certificate + verifier
- **Existence**: a 99×99 adjacency matrix A. Verify in integer arithmetic:
  A·𝟙 = 14·𝟙 and A² = 14·I + A + 2·(J - I - A). Milliseconds. Smallest, most
  charming certificate on our entire list.
- **Non-existence**: full exhaustion of srg(99,14,1,2) is currently out of reach,
  but exclusions under symmetry assumptions are finite citable results, and a
  completed case analysis over all automorphism possibilities would settle the
  problem negatively — plausibly within reach of a serious SAT campaign, since
  known results already force the automorphism group to be very small.

## Known structure (bake into any search)
- Eigenvalues fixed: 14, 3 (multiplicity 54), -5 (multiplicity 44).
- Feasibility conditions (Krein, absolute bound) all pass — no classical
  obstruction; the parameter set is famous precisely because it's so unobstructed.
- Automorphism constraints: known work (e.g. Makhnev-school and others) restricts
  possible prime orders of automorphisms — re-derive the exact current status
  with citations before searching; last known state was that very few prime
  orders remain unexcluded, which both guides existence search (assume a
  surviving symmetry) and scopes a nonexistence campaign.
- Local structure: neighborhoods are perfect matchings (λ=1 means each vertex's
  14 neighbors pair into 7 edges) — the graph is locally 7·K₂. This is a strong
  assembly constraint.

## Angle-of-attack menu (be exploratory — these come from different fields)
- **SAT/exact-cover with symmetry breaking**: direct encoding of the local
  7·K₂ + unique-quadrilateral conditions; prescribed automorphism variants.
- **Algebraic constructions**: search inside known objects — group-divisible
  designs, partial geometries, switching classes of known srgs, two-graph
  descendants, cyclotomic/Cayley-like constructions over structures of order
  dividing 99 (Z₃³, Z₉×Z₁₁, ...), even though pure Cayley routes may be excluded.
- **Regular two-graph / Seidel switching**: srg(99,14,1,2) sits near known
  switching classes; explore descendants/ancestors systematically.
- **Continuous relaxations**: SDP feasibility of partial patterns; spectral
  embedding heuristics (the 3-eigenspace has dim 54 — Euclidean representation
  in R^54 with two allowed inner products) to steer combinatorial search.
- **Nonexistence side**: organize a case-tree over surviving automorphism orders
  + a plan for the trivial-automorphism case (canonical-form search with orderly
  generation — estimate feasibility honestly before committing).

## First steps
1. Verifier; validate on known srgs (Paley(13)? use srg(50,7,0,1) H-S subgraph
   and Paley graphs as tests).
2. Literature map of automorphism exclusions for srg(99,14,1,2), with citations.
3. Run the two cheapest fronts in parallel: prescribed-symmetry SAT and
   switching-class exploration.
