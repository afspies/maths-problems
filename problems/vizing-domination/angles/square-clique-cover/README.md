# Square-graph fractional clique covers

## Status

**Exact orthogonal product bounds proved and independently accepted by
GPT-5.6 Sol at xhigh effort.** They prove Vizing whenever one factor has a
centered perfect square, including every forest. A connected triangular-graph
family proves that the unrestricted relaxation has unbounded loss and cannot
give any universal constant.

Literature priority for this synthesis has not been audited.

## Parameter

Let `fcc(X)` be the fractional vertex clique-cover number of `X`. Equivalently,
its dual maximizes `Σ_x p_x` over nonnegative vertex weights satisfying
`Σ_{x∈C}p_x≤1` for every clique `C` of `X`.

Define

`σ(G)=fcc(G²)`,

where `G²` joins distinct vertices at distance at most two.

Every closed neighborhood of a graph `K` is a clique in `K²`. Consequently,

`γ(K)≥fcc(K²)`.                                               (1)

## Two-sided tensor bound

For all graphs `G,H`,

```text
γ(G□H) ≥ fcc((G□H)²) ≥ σ(G)σ(H).                             (2)
```

The graph `(G□H)²` is a spanning subgraph of the strong product
`G²⊠H²`: product distance at most two implies distance at most two in each
coordinate. Adding edges can only decrease fractional clique cover.

It remains to use

`fcc(X⊠Y)=fcc(X)fcc(Y)`.

For the upper bound, tensor fractional clique covers. For the reverse bound,
tensor dual-optimal vertex weights. Every clique of the strong product
projects to cliques in both factors, so the tensor weights satisfy every
clique constraint.

## Stronger one-sided bound

In fact,

```text
γ(G□H) ≥ max{σ(G)γ(H), γ(G)σ(H)}.                             (3)
```

Let `D` dominate `G□H` and let `p` be dual-optimal for `σ(G)`. For every
`g`, the projection to `H` of

`D∩(N_G[g]×V(H))`

dominates `H`; hence that slice contains at least `γ(H)` points. Therefore

```text
σ(G)γ(H)
 ≤ Σ_g p_g |D∩(N_G[g]×V(H))|
 = Σ_{(u,h)∈D} p(N_G[u])
 ≤ |D|.
```

The last inequality holds because `N_G[u]` is a clique of `G²`. Swapping the
factors proves (3).

Thus `σ(G)=γ(G)` proves Vizing for `G` against every graph `H`, while any
ratio `σ(G)/γ(G)>0.5643` improves Steiner for all pairs with first factor
`G`.

## Centered-perfect factors

Suppose:

1. `G²` is perfect; and
2. every clique `C` of `G²` is centered, meaning
   `C⊆N_G[v]` for some `v`.

Then

`σ(G)=γ(G)`.                                                  (4)

Centeredness converts any integral clique cover of `G²` into a dominating
set of `G` of the same size; closed neighborhoods give the reverse
conversion. Perfection makes the fractional and integral clique-cover
numbers equal. Equation (3) now proves Vizing for `G□H` for every `H`.

Every forest satisfies both hypotheses. In a tree, a set of pairwise
distance-at-most-two vertices has a radius-one center. Also a leaf is
simplicial in the tree square, and deleting it commutes with taking the
square; recursively, every tree square is chordal and hence perfect.

## Fatal universal obstruction

No fixed positive constant can be obtained from `fcc((G□H)²)` alone, even
for connected factors.

Let

`G_m=L(K_{2m+1})` and `H=P₄`.

Domination in `G_m` is edge domination in `K_{2m+1}`. A selected edge set
must cover all but at most one base vertex, so it has at least `m` edges; a
matching of size `m` attains the bound. Thus

`γ(G_m)=m`, while `γ(P₄)=2`.

For `m≥2`, `G_m` has diameter two. Each of the four fibres
`V(G_m)×{h}` is therefore a clique of `(G_m□P₄)²`, and these fibres give

```text
fcc((G_m□P₄)²)≤4,
fcc((G_m□P₄)²)/(γ(G_m)γ(P₄))≤2/m→0.                          (5)
```

Already `m=4`, or `G=L(K₉)`, gives at most `1/2`, below Steiner's constant.
Since `θ(overline{X})≤fcc(X)`, the same example rules out the corresponding
unrestricted square-graph Lovász-theta route.

## Verdict

**GO** for centered-square or center-aware lift-and-project parameters:
equation (3) is a clean pairwise theorem. **STOP** for unrestricted
fractional clique covers, theta, or other level-zero square-clique
relaxations as universal-constant routes. Their loss comes precisely from
large noncentered cliques in graph squares.
