# Results (negative / partial)

Citable negative results: exhausted subspaces, exclusion lemmas, barrier maps.
Each result ships with the exact search-space definition, tooling + versions,
seeds/parameters, and (where possible) solver proof logs — reproducibility is
what makes a negative result citable. Describe compute generically.

## Index

- **Order-56 derangement-group exclusion (THEOREM — the headline).** No
  group of order 56 supports the group-of-derangements ansatz for the
  degree-57 Moore graph; any group H with |H| = k−1 > 2 supporting it
  for degree k must be perfect. Closes the non-cyclic case left open by
  Smith–Montemanni (Axioms 2026) and subsumes their cyclic theorem.
  Proof + full provenance: `../writeup/perfectness.tex` (doubly
  codex-refereed, novelty-searched 2026-07-22).
  Corroborating exhaustive computations (also independently citable):
  - k=7, H=Z₆: exhaustive — infeasible (1680 = 14·120 V-complete leaves,
    0 valid), two independent implementations + a from-scratch
    enumerator with exactly matching counts.
  - k=7, H=S₃: exhaustive — infeasible (1200 = 10·120 leaves, 0 valid).
  - k=3, H=Z₂ positive control: feasible, rebuilds Petersen, passes the
    exact verifier. Artifacts: `../angles/derangement-56/runs/*.json`,
    code `search.py` + independent `test_search.py` + third-path
    `independent_check.py`.
- **m=125 semiregular quotient: negative data, NOT an exclusion** — see
  `m125-quotient/README.md`.
- **C₁₉ CEGAR non-convergence (methodological negative):** lazy-girth
  CEGAR on the 84-orbit equivariant encoding does not converge at d=57
  (229 iterations / 20.5M clauses / 3h, violations flat). Quantified in
  JOURNAL 2026-07-22; encoder + validation in `../angles/c19-sat/`.
