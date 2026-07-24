# Two-sided private-corner dynamics

## Status

**Exact product-specific cycle lemma.** If every point of a product
dominating set has external private neighbors in both coordinate directions,
then the dominating set contains a directed cycle whose steps change one
coordinate by an edge and the other by distance exactly two. The
`C₅□C₅` perfect code shows that this conclusion is sharp: all corner
obligations can circulate around one such cycle.

This is a genuine labelled-fibre constraint, not a factor-marginal
inequality. It does not yet give a positive density defect or improve the
universal constant.

## Escape-cycle lemma

Let `D` dominate `G□H`. Suppose that for every `d=(g,h)∈D` there are
external private neighbors

```text
q_d=(x,h),  where xg∈E(G),
r_d=(g,y),  where yh∈E(H),
```

such that

`N[q_d]∩D=N[r_d]∩D={d}`.                                    (1)

The corner `c_d=(x,y)` must be dominated by a point
`φ(d)∈D\{d}`. There are only two possibilities:

```text
φ(d)=(x,z),  with xg∈E(G) and dist_H(h,z)=2; or
φ(d)=(w,y),  with dist_G(g,w)=2 and yh∈E(H).                 (2)
```

Indeed, a dominator of `(x,y)` lies in its `G`-column or its `H`-row.
In the first case it has the form `(x,z)` with `z∈N_H[y]`. Privacy of
`q_d=(x,h)` forces `z∉N_H[h]`. Since `y∈N_H(h)`, this says exactly
`dist_H(h,z)=2`. The second case is symmetric. The corner itself cannot
belong to `D`, since it would also dominate both private neighbors in (1).

Choose one such owner `φ(d)` for each `d`. This gives a loopless functional
digraph on the finite set `D`, so it contains a directed cycle. Every arc of
that cycle is one of the mixed `(1,2)` or `(2,1)` moves in (2).

Equivalently, put an edge between `(g,h)` and `(g',h')` when either

```text
gg'∈E(G) and dist_H(h,h')=2,
```

or the symmetric condition holds. Every two-sided externally private
dominating set contains a cycle in this mixed-distance graph.

If both factors are bipartite, every directed cycle contains an even number
of each type of move: an edge flips the relevant bipartition and a
distance-two step preserves it.

## Label and indegree refinement

Retain the full row/column notation from the fibre proof. Let `J_x` be the
set of columns whose chosen horizontal external-private target lands in row
`x`, and let

`e_x=|A_x|-|I_x|`

be its vertical row slack. A fixed column has at most one occupied point
whose chosen private target is `x`, because private targets are injective
inside the column. Therefore, for a destination `d'=(x,z)`,

`indeg_{(1,2)}(d')≤|J_x|≤ρ(H)+2e_x`.                         (3)

The symmetric row construction gives

`indeg_{(2,1)}(d')≤ρ(G)+2e'_z`.                              (4)

Thus at exact two-oriented equality every escape owner has indegree at most

`ρ(G)+ρ(H)`.

There is a sharper local form at zero row slack. The predecessor hole
coordinates of all type `(1,2)` arcs entering `(x,z)` lie in the row
two-packing `P_x` and are all at distance two from `z`. Their intermediate
private coordinates on the length-two paths to `z` are distinct, because
the closed neighborhoods of holes in `P_x` are disjoint. Hence

```text
indeg_{(1,2)}(x,z)
 ≤min{|J_x|, ρ_H(N₂(z)), deg_H(z)},                           (5)
```

and symmetrically with the factors exchanged.

The arcs also retain nontrivial cell labels. If a type `(1,2)` arc starts at
`(g,h)∈D_i` and ends at `(x,z)∈D_j`, then

```text
i∈S_g∩J_x,   j∈S_x,
i∉I_x,       j∉I_g.                                        (6)
```

The last exclusion follows from `x∈X_j`, `gx∈E(G)`, and the fact that
`X_j` is anticomplete to `L_j`. Hence an escape arc is a red-diagonal,
blue-cross-zero transition in the balanced cell matrices, not merely an
unlabelled edge of the mixed-distance graph.

Equations (3)--(6) are not yet a density theorem. A functional digraph of
bounded indegree may have a long in-tree feeding one cycle. Progress now
requires a bound on labelled escape-path length or a rule coupling
successive transitions.

## Relation to formal Steiner equality

Under the full two-oriented formal equality hypotheses, the
external-private theorem applies in both coordinate directions to every
point of `D`. Hence (1) holds and the escape-cycle lemma is compulsory.
This packages the previously missing corner labels into a concrete global
object.

It is important that this is an equality-structure statement, not the claim
that a finite graph realizes the irrational formal ratios. A quantitative
advance needs a stability version that either produces many disjoint escape
cycles or charges every failure of (1) to the exact Steiner defect budget.

## Sharpness

For

`D={(i,2i):i∈ℤ₅}⊂C₅□C₅`,

choose

```text
q_i=(i+1,2i),   r_i=(i,2i+1).
```

The corner `(i+1,2i+1)` is dominated by
`φ(i,2i)=(i+1,2i+2)`. Thus `φ` is a directed 5-cycle of the first type in
(2): the first coordinate moves by an edge and the second by distance two.
No contradiction is possible from a bare corner-completion argument.

There is no larger universal lower bound on cycle length. In `K₂□P₃`,

`D={(0,0),(1,2)}`

is a perfect dominating set with two-sided external private neighbors, and
the two opposite corner obligations point to one another. Thus the escape
digraph can be a directed 2-cycle.

## Verdict

The generic dynamics route is a **STOP**. The exact theorem in
`../escape-realization/README.md` realizes every finite bipartite graph
without isolates as a zero-defect escape graph of a minimum perfect code.
Consequently neither bounded path length nor positive cycle density follows
even after all current collision and cross-redundancy defects vanish.

Only a theorem using the additional indexed `K₁/K₃` terminal labels at the
formal Steiner obstruction remains viable.
