# maths-problems

Agent-driven attacks on long-open mathematics problems whose interesting
direction has a **finite explicit certificate with a cheap exact verifier** —
the regime highlighted by the July 2026 Fable-assisted counterexample to the
Jacobian conjecture. Conventions for working sessions live in
[AGENTS.md](AGENTS.md); each problem folder under [problems/](problems/) is
self-contained (statement, verifier, journal, results, writeup).

**This file is generated from `problems/*/STATUS.toml` by `tools/board.py` —
do not edit by hand.**

## Tracked problems

| Problem | Status | Question | Best result so far | DOI |
|---|---|---|---|---|
| [The missing Moore graph (degree 57)](problems/moore-graph-57/PROBLEM.md) | 🟡 partial results | Does a 57-regular graph on 3250 vertices with girth 5 (srg(3250,57,0,1)) exist? | NEW THEOREM: derangement ansatz forces H perfect; no order-56 group works (closes Smith-Montemanni 2026 open case) - writeup drafted+refereed | — |
| [Casas-Alvero conjecture](problems/casas-alvero/PROBLEM.md) | 🔵 active | If deg-d monic f shares a root with each of f', ..., f^(d-1), is f = (x-a)^d? | — | — |
| [Conway's 99-graph problem](problems/conway-99-graph/PROBLEM.md) | 🔵 active | Does srg(99,14,1,2) exist (every edge in a unique triangle, non-edge in a unique quad)? | — | — |
| [Explicit Dixmier/Poisson counterexamples](problems/dixmier-weyl/PROBLEM.md) | 🔵 active | Construct an explicit non-surjective endomorphism of a Weyl algebra A_n. | — | — |
| [Union-closed sets (Frankl) conjecture](problems/frankl-union-closed/PROBLEM.md) | 🔵 active | Does every finite union-closed family (not just {{}}) have an element in half its sets? | — | — |
| [Hadwiger-Nelson: chromatic number of the plane >= 6](problems/hadwiger-nelson/PROBLEM.md) | 🔵 active | Find a finite unit-distance graph that is not 5-colorable. | — | — |
| [Projective plane of order 12](problems/projective-plane-12/PROBLEM.md) | 🔵 active | Does a projective plane of order 12 (a symmetric 2-(157,13,1) design) exist? | — | — |
| [Zariski cancellation problem (char 0, dim 3)](problems/zariski-cancellation/PROBLEM.md) | 🔵 active | Does A[t] = C[x,y,z,t] force A = C[x,y,z]? | — | — |
| [Hadamard matrix of order 668](problems/hadamard-668/PROBLEM.md) | 🧩 scaffolded | Construct a 668x668 +-1 matrix H with H H^T = 668 I (smallest open order). | — | — |
| [Two-variable Jacobian conjecture](problems/jacobian-2var/PROBLEM.md) | 🧩 scaffolded | Is every polynomial map C^2 -> C^2 with constant nonzero Jacobian determinant injective? | — | — |
| [Word problem for the minimal unknown Artin-Tits group](problems/artin-tits-word-problem/PROBLEM.md) | ⬜ proposed | Is the word problem decidable for the 4-generator Artin-Tits group with ad=da and braid relations on all other pairs? (Gowers Polymath proposal, March 2026) | — | — |
| [Koethe's conjecture](problems/koethe/PROBLEM.md) | ⬜ proposed | Is the sum of two nil left ideals of a ring always nil? Open since 1930 | — | — |
| [Bounded gaps between primes: below 246](problems/prime-gaps/PROBLEM.md) | ⬜ proposed | Lower the unconditional bound liminf (p_{n+1} - p_n) <= 246 by re-attacking the Maynard-Tao variational problem | — | — |
| [Rota's basis conjecture](problems/rota-basis/PROBLEM.md) | ⬜ proposed | Can n bases of a rank-n matroid always be rearranged into an n x n grid whose rows are the given bases and whose columns are all bases? | — | — |
| [Slice-ribbon and exotic S4 candidates](problems/slice-ribbon/PROBLEM.md) | ⬜ proposed | Is every smoothly slice knot ribbon? Attack via obstruction computations on standing candidate families (GST knots, Gluck twists) | — | — |

## Adding a problem

```
python3 tools/new_problem.py <slug> --title "Problem name"
```

Then fill in `PROBLEM.md` (statement, certificate + verifier spec, known
structure, attack-angle menu), set `STATUS.toml` to `proposed`, and rerun
`python3 tools/board.py`.
