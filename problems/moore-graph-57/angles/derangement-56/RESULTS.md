# Results: group-of-derangements ansatz

## Verdicts

| Case | Verdict | Proof/search method | Exact recorded result |
|---|---|---|---|
| `k=3`, `H=Z2` | **FEASIBLE** | Complete DFS and graph expansion | SAT; witness `runs/z2_witness.json`; `verify_moore(A,3)` PASS on the 10-vertex graph. |
| `k=7`, `H=Z6` | **INFEASIBLE-exhausted** | Full first-row-fixed DFS, with the algebraic presolver deliberately disabled | UNSAT; 10 free edges, 3 attempted assignments, 4 backtracks, maximum depth 2, 0.000108 s. Independent row-only enumeration: 146 nodes, all 14 (V)-complete leaves checked, 0 valid. |
| `k=7`, `H=S3` | **INFEASIBLE-exhausted** | Full first-row-fixed DFS, with the algebraic presolver deliberately disabled | UNSAT; 10 free edges, 6 attempted assignments, 7 backtracks, maximum depth 3, 0.000192 s. Independent row-only enumeration: 110 nodes, all 10 (V)-complete leaves checked, 0 valid. |
| `k=57`, `H1=Z4 x Z2 x Z7` | **INFEASIBLE-exhausted** | Exact abelianization partial-transversal theorem | `[H,H]` has order 1, but any solution with `|H|>2` requires `H` perfect. The presolver covers 100% of the 1485-free-edge space; no DFS nodes are needed. |
| `k=57`, `H2=Z2^3 x Z7` | **INFEASIBLE-exhausted** | Exact abelianization partial-transversal theorem | `[H,H]` has order 1, but any solution with `|H|>2` requires `H` perfect. The presolver covers 100% of the 1485-free-edge space; no DFS nodes are needed. |
| `k=57`, all 10 nonabelian groups of order 56 | **INFEASIBLE-exhausted** | Same theorem plus Burnside's `p^a q^b` solvability theorem | Any gain solution would require a perfect group. Every order-56 group is solvable and nontrivial, hence not perfect. This is a class proof; the 10 multiplication tables were not instantiated individually. |

## Degree-57 certificate

No complete Moore graph was found: the group-of-derangements ansatz is
infeasible for every group of order 56.  Consequently no
`certificates/moore57_candidate.npz` was created.

## Machine-readable artifacts

- `runs/smoke_summary.json`: final small-case statuses and DFS statistics.
- `runs/z2_witness.json`: complete Petersen-scale gain assignment.
- `runs/h1_result.json`: exact-presolver result for `H1`.
- `runs/h2_result.json`: exact-presolver result for `H2`.
