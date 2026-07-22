# Hadamard matrix of order 668

## Statement
A Hadamard matrix of order n is an n×n ±1 matrix H with H Hᵀ = n·I. Conjectured to
exist for every n ≡ 0 (mod 4). Order 668 is the smallest open case (428 was settled
in 2005 by Kharaghani–Tayfeh-Rezaie; 668, 716, 892, … remain open).

## Certificate + verifier
Trivial and exact: a 668×668 ±1 matrix; check H Hᵀ = 668 I in integer arithmetic.
Milliseconds. This is the purest "explicit object + instant verifier" problem on the
list — the entire difficulty is navigating a 2^(668²) space with structure.

## Approach notes — go through structured constructions, not raw search
- 668 = 4·167, 167 prime ≡ 3 (mod 4). Known construction families to try to hit 668:
  - **Williamson-type**: four symmetric circulant ±1 matrices A,B,C,D of order 167
    with A²+B²+C²+D² = 668·I. Reduces to a quadruple of ±1 sequences with
    autocorrelation conditions — searchable; 167 is large for exhaustion but
    amenable to guided/heuristic search (this is how 428 fell: Turyn-type / Williamson
    at order 107).
  - **Turyn-type sequences / T-sequences, base sequences** BS(m, n) feeding
    Goethals–Seidel arrays: 668 = 4·167 needs T-sequences of length 167.
  - **Skew-Hadamard routes, Paley-type twists over GF(167)**.
- The 2005 order-428 success used a combination of structural reduction (Turyn-type
  sequences of length 36) + careful computer search. The move: pick the reduction
  whose residual search space is smallest, then throw modern SAT/ILP + model-guided
  proposals at the autocorrelation system.
- Deliverables even without a hit: verifier + reduction library (Williamson,
  Goethals–Seidel, Turyn) with exact autocorrelation checkers, exhaustion results on
  sub-spaces (e.g. "no Williamson quadruple of order 167 with symmetry group X"),
  which are publishable negative results.

## First steps
1. Write the exact verifier + the Williamson/Goethals–Seidel assemblers, and
   re-derive a known order (e.g. 428 from published Turyn sequences) end-to-end.
2. Enumerate which reduction routes are open vs already excluded for 668 (check
   literature: some Williamson orders are proven empty — 167 status?).
3. Attack the most promising residual sequence-search with SAT + guided proposals.
