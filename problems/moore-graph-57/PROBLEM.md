# The missing Moore graph (degree 57)

## Statement
Does a Moore graph of degree 57 exist? Equivalently: a 57-regular graph on 3250
vertices with girth 5 — equivalently a strongly regular graph srg(3250, 57, 0, 1).
Hoffman–Singleton (1960) showed Moore graphs of diameter 2 can only have degree
2, 3, 7, or 57; the first three exist (C₅, Petersen, Hoffman–Singleton). Degree 57
has been open ever since.

## Certificate + verifier
- **Existence**: a 3250×3250 adjacency matrix A. Verify in integer arithmetic:
  A·𝟙 = 57·𝟙, A² + A - 56·I = J. Seconds. Purest possible certificate.
- **Non-existence**: no cheap certificate in general, but partial exclusions
  (e.g. "no such graph with automorphism group containing G") are finite,
  citable results — that's how all known structural progress was made.

## Known structure (bake into any search)
- Aschbacher/Higman: the graph cannot be vertex-transitive; its automorphism
  group has order ≤ 375 (Mačaj–Širáň 2010).
- **2026 state (see literature/exclusion-map.md — the campaign's cited map):**
  Ishida's preprint (arXiv:2606.29183) rules out involutions, so |Aut| is odd —
  only the 24 odd orders in Mačaj–Širáň's list survive; exact displacement
  counts are known for elements of order 7/11/13/19 (order 13 acts freely,
  order 19 fixes exactly one vertex). Makhnev's 2020 nonexistence claim is
  rebutted (Faber–Keegan); the problem is open. Smith–Montemanni (Axioms 2026)
  excluded the cyclic group in the derangements ansatz; this campaign's
  perfectness theorem (writeup/) excludes ALL order-56 groups there.
- No exhaustive search under any prescribed automorphism has ever been
  published — that structural gap is what this campaign's equivariant
  SAT/CP infrastructure targets.
- Any two adjacent vertices have 0 common neighbors; any two non-adjacent have
  exactly 1 — so the graph is a friendship-like incidence geometry; local
  structure around a vertex is a 57-star plus a partition of the remaining 3192
  vertices into 57 groups of 56.
- Eigenvalues fixed: 57, 7 (multiplicity 1729), -8 (multiplicity 1520).
- Substructure approaches: does it contain a Petersen or Hoffman–Singleton
  subgraph? Prior work on forced/forbidden substructures constrains assembly.

## Angle-of-attack menu (be exploratory — these come from different fields)
- **Prescribed small automorphisms**: assume an order-2 or order-3 automorphism,
  orbit-decompose, reduce to a smaller exact-cover/SAT instance. Systematically
  map which small groups are excluded vs open.
- **Algebraic/association-scheme constructions**: search for the graph as a
  fusion/switching of known combinatorial objects (Hoffman–Singleton copies,
  cocliques in known srgs, designs on 3250 points).
- **Spectral/SDP relaxations**: KNOWN DEAD in plain form — the standard
  spectral LMIs admit an explicit fractional feasible point (LEARNINGS.md),
  so only integrality/rank-augmented or high-level moment relaxations
  could ever bite. Don't rebuild vanilla SDP.
- **Local-gluing search**: build the neighborhood geometry (57 blocks of 56)
  and treat completion as constraint satisfaction with heavy symmetry breaking.
- **Probabilistic/entropy heuristics** to estimate where in the space solutions
  could concentrate, to steer rather than to prove.

## First steps
1. Verifier + spectral sanity-checker; validate on Hoffman–Singleton (degree 7).
2. Literature map: exact current automorphism-group exclusions (with citations).
3. Pick the smallest unexcluded symmetry assumption; encode; run.
