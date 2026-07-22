# Union-closed sets (Frankl) conjecture

## Statement
If F is a finite family of finite sets, closed under union, F ≠ {∅}, then some
element belongs to at least half the sets of F.

## Status / context
Gilmer (2022) proved a constant fraction (≥ 0.01) by an information-theoretic /
entropy argument; the constant was quickly pushed to (3-√5)/2 ≈ 0.381966 (Alweiss–
Huang–Sellke, Chase–Lovett, Sawin, Pebody), and Sawin/Yu/Cambie have nudged past it
(~0.38234). There is a known barrier: the pure Gilmer-style argument cannot exceed
(3-√5)/2 without new ideas (Chase–Lovett constructed distributional counterexamples
to the stronger entropy statement at that threshold). Gap to 1/2 is open.

## Two directions, both with finite certificates
1. **Counterexample search**: a union-closed family where every element is in < half
   the sets. Finite object, instant exact verification (check union-closure +
   element frequencies). Known small-case results: conjecture verified for families
   with ≤ 12-element ground sets and for |F| ≤ 46 (roughly — re-check literature
   bounds first and record them). Any counterexample must be weird; targeted search
   should exploit the known extremal near-misses (e.g. Duffus–Sands style lattices,
   frequency exactly 1/2 families like power sets).
2. **Barrier-side certificates**: the Chase–Lovett-style distributional
   counterexamples to strengthened statements are themselves finite checkable
   objects. Searching for distributional counterexamples at thresholds *above*
   0.382 for the specific inequality chains in the newest papers would map exactly
   where the current proof technique dies — high research value, cheap verification.

## Verifier
- Union-closure: O(|F|²) set unions, exact.
- Frequency condition: counting. Both trivial in Python over bitmask-encoded sets.
- Distributional certificates: exact rational entropy computations (sympy).

## First steps
1. Bitmask harness + verifier; reproduce the known extremal families.
2. Re-derive the (3-√5)/2 barrier example of Chase–Lovett computationally.
3. Guided search on both fronts; log all near-misses (max frequency achieved vs 1/2).
