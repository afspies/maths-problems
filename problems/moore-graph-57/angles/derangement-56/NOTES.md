# Degree-57 Moore graph under the group-of-derangements ansatz

## Bottom line

The proposed gain constraints are complete and correct.  A generalization of
Smith--Montemanni's partial-transversal count gives a stronger result than an
order-56 search: if a finite group `H` of order greater than two admits such a
gain assignment, then `H` must be perfect.  Every group of order 56 is solvable
by Burnside's `p^a q^b` theorem, so no group of order 56 is perfect.  Thus all
13 groups of order 56 (the cyclic group, the two non-cyclic abelian groups, and
the ten nonabelian groups) are excluded under this ansatz.

This extends the partial-transversal idea in Smith and Montemanni,
["The Moore Graph of Diameter 2 and Degree 57 via Cyclic Derangements"]
(https://doi.org/10.3390/axioms15050332), from a cyclic group to the
abelianization of an arbitrary group.

## Verification of the gain formulation

Put `q=k-1`.  Around a root `u`, write its neighbors as `v_i` and
`B_i=N(v_i)\{u}`.  The standard Moore-bound argument gives:

1. `|B_i|=q`, and `B_i` is independent (otherwise there is a triangle through
   `v_i`).
2. For `i != j`, every vertex of `B_i` has exactly one neighbor in `B_j`.
   Two such neighbors would make a 4-cycle through `v_j`, while fewer would
   contradict degree `k`.  Hence the edges between `B_i,B_j` form a perfect
   matching `M_ij`.
3. A triangle wholly among leaves must use three distinct blocks.  A 4-cycle
   wholly among leaves must use four distinct blocks: a repeated block would
   force one matching to give a vertex two partners.  Cycles through `u` or a
   `v_i` are already excluded by the tree and matching structure.

Identify each block with `L=H`, use right multiplication, and write

```
M_ij(x) = x h_ij,       h_ji = h_ij^{-1}.
```

Relabel each `B_j`, `j>1`, through `M_1j` so that `M_1j=id`.  The remaining
conditions divide as follows.

- A triangle through normalized block 1 and blocks `i,j` exists exactly when
  `h_ij=e`.  Thus all remaining edge gains must be nonidentity.
- A 4-cycle through normalized block 1 and blocks `j,i,k` exists exactly when
  `h_ji h_ik=e`, equivalently `h_ij=h_ik`.  Excluding all such cycles says
  that the outgoing gains at each vertex are pairwise distinct.  There are
  `q-1` of them and `|H\{e}|=q-1`, so each row is exactly `H\{e}`.  This is (V).
- A leaf triangle in distinct blocks `i,j,k>1` exists exactly when
  `h_ij h_jk h_ki=e`.  Its exclusion is (T).
- A leaf 4-cycle in distinct blocks `i,j,k,l>1` exists exactly when
  `h_ij h_jk h_kl h_li=e`.  Its exclusion is (Q).

Therefore the final constraint set is exactly the one in the task:

```
(V) {h_ij : j != i} = H\{e} at every i;
(T) h_ij h_jk h_ki != e for all distinct i,j,k;
(Q) h_ij h_jk h_kl h_li != e for all distinct i,j,k,l;
    h_ji=h_ij^{-1} and h_ij != e.
```

There is no missing extra `mu=1` condition.  Conversely, these conditions
produce a `k`-regular graph on `k^2+1` vertices with no 3- or 4-cycles; equality
in the Moore bound then gives diameter 2 and `mu=1` (equivalently, the SRG
identity).

## Symmetry breaking

Choose one gain-graph vertex and call it 0 (block 2 in the task).  By (V), its
outgoing gains are a bijection to `H\{e}`.  Permuting the other `q-1` block
labels can put them in any prescribed order, so the solver fixes

```
h_0j = element j of the canonical enumeration of H\{e},  1 <= j < q.
```

This removes only block relabeling symmetry and loses no solution.  No
automorphism of `H` is fixed or quotiented by the implementation.  After the
row is fixed, an automorphism of `H` survives only when accompanied by the
unique permutation of vertices 1 through `q-1` that restores the canonical
row.  The solver deliberately leaves this residual `Aut(H)` symmetry intact.

## Generalized partial-transversal obstruction

### Theorem

If a finite group `H` with `|H|>2` admits a complete gain assignment satisfying
(V), (T), and (Q), then `H` is perfect: `H=[H,H]`.

### Proof

Choose two gain-graph vertices `a,b`, set `t=h_ab`, and for each of the
`q-2` other vertices `i` define

```
x_i = h_ai,       y_i = h_ib,       z_i = x_i y_i.
```

By (V) at `a`, the list `(x_i)` is a permutation of `H\{e,t}`.  At `b`, the
outgoing list contains `h_ba=t^{-1}` and `h_bi=y_i^{-1}`, so `(y_i)` is also a
permutation of `H\{e,t}`.

The list `(z_i)` is a third permutation of the same set:

- (V) at `i` gives `h_ia=x_i^{-1} != h_ib=y_i`, hence `z_i != e`.
- (T) on `a,i,b` gives `x_i y_i t^{-1} != e`, hence `z_i != t`.
- (Q) on `a,i,b,j` gives
  `x_i y_i y_j^{-1} x_j^{-1}=z_i z_j^{-1} != e`, hence `z_i != z_j`.

There are `q-2` distinct `z_i` values outside `{e,t}`, proving the claim.

Now map to the abelianization `A=H/[H,H]`, and let

```
P = product in A of the images of all h in H,
S_t = product in A of the images of H\{e,t} = P * image(t)^{-1}.
```

The `x`, `y`, and `z` lists all have product `S_t`.  But commutativity in `A`
and `z_i=x_i y_i` also give

```
S_t = product_i image(z_i)
    = (product_i image(x_i)) (product_i image(y_i))
    = S_t^2.
```

Cancellation gives `S_t=e`, so `image(t)=P`.  Since `t` was arbitrary (each
row contains every nonidentity gain), every nonidentity element of `H` has the
same image `P` in `A`.

If `P=e`, the abelianization is trivial and `H` is perfect.  If `P!=e`, the
kernel contains no nonidentity element, so the quotient map is injective; then
all nonidentity elements being sent to the same element forces `|H|<=2`.
This proves the theorem.

For `|H|=56=2^3*7`, Burnside's `p^a q^b` theorem says `H` is solvable.  A
nontrivial solvable group cannot be perfect, because its derived series would
never descend from `H`.  Therefore no group of order 56 can satisfy the gain
constraints.

### Sanity checks

- `H=Z2`: the endpoint construction has no intermediate vertices; the one
  nonidentity element is exactly `P`.  The obstruction correctly permits this
  case.  Exact search finds the Petersen witness, and the expanded 10-vertex
  graph passes `verify_moore(A,3)`.
- `H=Z6`: the obstruction excludes it.  Independently, exhaustive DFS without
  the obstruction returns UNSAT.  A deliberately simpler enumerator checks all
  14 row-complete (V)-assignments and finds zero satisfying (T),(Q).
- `H=S3`: its derived subgroup has order 3, so the obstruction excludes it.
  Independently, exhaustive DFS returns UNSAT; the simple enumerator checks all
  10 row-complete (V)-assignments and finds zero satisfying (T),(Q).

Thus the argument passes the required `k=3` numerical sanity check and agrees
with both exhaustive `k=7` searches.

## Implementation

`search.py` contains:

- multiplication-table implementations of tuple abelian groups and `S3`;
- an exact abelianization presolver, computing `[H,H]` from commutators;
- complete DFS after first-row fixing, with bitset row-AllDifferent state,
  minimum-remaining-values branching, eager completed-(T)/(Q) checks, and a
  necessary Hall-union check;
- independent assignment validation and expansion to the full Moore adjacency
  matrix, followed by the repository's `verify_moore` for positive smoke cases;
- JSON witnesses and run summaries.

`test_search.py` independently enumerates (V)-complete assignments for the two
order-6 UNSAT cases and checks (T),(Q) only at leaves.  It shares neither the
production DFS's cycle pruning nor its Hall-union pruning.  This guards against
an unsound pruning rule.  Because the exact algebraic presolver resolves every
order-56 group, installing OR-Tools or generating a huge SAT model would add no
evidence and was unnecessary.

## Results

The detailed verdicts and run statistics are in `RESULTS.md` and `runs/*.json`.
No degree-57 witness exists under this ansatz, so no file was written under
`certificates/`.

## Exact search and verification commands run

The result-bearing commands were:

```bash
.venv/bin/python --version
.venv/bin/python - <<'PY'
import numpy, sympy, pysat, networkx
print('numpy', numpy.__version__)
print('sympy', sympy.__version__)
print('pysat', pysat.__version__)
print('networkx', networkx.__version__)
PY
command -v kissat
command -v cadical

time .venv/bin/python angles/derangement-56/search.py smoke --output-dir angles/derangement-56/runs 2>&1 | tee /tmp/derangement56-smoke.log

.venv/bin/python angles/derangement-56/test_search.py && .venv/bin/python angles/derangement-56/search.py smoke --output-dir angles/derangement-56/runs

.venv/bin/python angles/derangement-56/search.py solve --group h1 | tee angles/derangement-56/runs/h1_result.json
.venv/bin/python angles/derangement-56/search.py solve --group h2 | tee angles/derangement-56/runs/h2_result.json

.venv/bin/python -m py_compile angles/derangement-56/search.py angles/derangement-56/test_search.py

PYTHONDONTWRITEBYTECODE=1 .venv/bin/python angles/derangement-56/test_search.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python angles/derangement-56/search.py smoke --output-dir angles/derangement-56/runs
```

The first smoke command was run before the independent tests were added; the
second is the final recorded run.  During development an equivalent inline
version of the independent order-6 enumerator produced `(146 nodes, 14 leaves,
0 valid)` for `Z6` and `(110 nodes, 10 leaves, 0 valid)` for `S3`; it was then
promoted verbatim in logic to `enumerate_row_complete` in `test_search.py` and
rerun with the command above.
