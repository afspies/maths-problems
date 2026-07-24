# External private targets and row hole packings

## Status

**Proved and independently accepted by two GPT-5.6 Sol reviewers at xhigh
effort.** In every fully tight atomic Steiner column, every occupied
projection vertex has an external private target. The corresponding
singleton coordinate holes landing in one row form a two-packing in the
other factor. A quantitative version charges failures of two-packing to the
exact vertical row slack.

These are new equality/stability constraints in this campaign. Literature
priority has not been established. They do not yet improve the universal
constant.

## External-private theorem

Let `L⊆V(G)` be two-sparse. Suppose:

1. `F_G(L)` is a disjoint union of `K₁` and `K₃`;
2. the canonical weight function `f`, equal to two on each `K₁` target and
   one on every `K₃` target, is an optimal global integer 2-packing of `G`;
3. `X` is a minimum dominator of `T=V(G)\L`; and
4. `|X|+γ_G(L)=γ(G)`.

Then every `x∈X` has an external private target `y∈T\X`:

`y≠x` and `N_G[y]∩X={x}`.                                   (1)

First, `X` is anticomplete to `L`. Any vertex hitting a `K₁` or `K₃`
conflict component can be included in a minimum dominator of that component:
use it alone on a singleton; on a triangle use it with the third target if
it hits two targets, or with a common witness for the other pair if it hits
one. Complete the remaining components independently. If `x∈X` hit `L`,
the resulting minimum `L`-dominator would overlap `X`, contradicting
condition 4.

Now suppose `x` has no external private target. Minimality of `X` makes `x`
self-private, so `X\{x}` dominates `T\{x}`. Since `f` is optimal and
`f(N[x])=0`, some `w∈N[x]` must satisfy

`f(N[w])=2`;                                                  (2)

otherwise `f+1_x` would be feasible. We have `w≠x` and `w∉X`. Saturation
means that `w` hits the weight-two target of one `K₁`, or two weight-one
targets in one `K₃`. In either case the componentwise construction above
gives a minimum `L`-dominator `B` containing `w`.

Replacing `x` by `w` preserves domination of `T`: `w` covers `x`, and every
other target formerly relying on `x` has another member of `X`, or it would
be external-private. Therefore

`(X\{x}∪{w})∪B`

dominates `G` and has size at most

`|X|+γ_G(L)-1=γ(G)-1`,

a contradiction.

The additivity hypothesis is essential. In `K_{2,3}`, take `L` to be one
vertex in the part of size three and `X` the other two vertices in that part.
The atomic supported 2-packing is globally optimal and both members of `X`
are self-private only, but

`|X|+γ_G(L)=3>γ(G)=2`.

## A limited quantitative column statement

Retain atomicity, additivity, and minimum domination, but allow the canonical
supported weight to have total `τ₂(F_G(L))<R=ρ²(G)`. Let `S⊆X` be the
vertices with only a self-private target. The replacement proof shows that
every closed neighborhood containing a member of `S` has canonical
`f`-mass at most one. Hence for every two-packing `P⊆S`,

`f+1_P`

is a global 2-packing, and therefore

`ρ_G(S)≤R-τ₂(F_G(L))`.                                       (3)

One cannot replace `ρ_G(S)` by `|S|`: self-private members need not form a
two-packing. An opposite minimum dominating pair in `C₄` is the smallest
warning. Simultaneously replacing both can uncover targets dominated by
exactly that pair.

## Row hole-packing theorem

Return to Steiner's product notation. Fix an `H`-row indexed by `y∈V(G)`.
Let

```text
A=A_y=P_H(D∩({y}×V(H))),
I={i:y∈L_i},
e=|A|-|I|≥0.
```

Choose an external private target for each applicable occupied point. Let
`J` be the columns whose chosen target is `y`, and write `a_i∈π_i` for the
singleton hole forced by product domination. Put `P={a_i:i∈J}`.

The sets `I,J` are disjoint, and row `y` has no point in a cell `π_i` with
`i∈J`. Thus `A` dominates every `π_i\{a_i}` for `i∈J`, while it dominates
every whole cell indexed by `I`.

Let `C` be a minimum dominator of `P` in `H`. Then

`A∪C∪{h_l:l∉I∪J}`

dominates `H` and has size at most

`k+e+γ_H(P)-|J|`, where `k=γ(H)`.

Consequently

`|J|-γ_H(P)≤e`.                                              (4)

The general matching-cover bound

`γ_H(P)≤(|P|+ρ_H(P))/2≤(|J|+ρ(H))/2`

then gives the quantitative row inequality

`|J|≤ρ(H)+2e`.                                               (5)

If `e=0`, equation (4) forces `γ_H(P)=|P|`. Equivalently, no vertex can
dominate two holes: `P` is a two-packing in `H`.

Summing (5) over rows, if `M` is the number of chosen external-private
incidences and `v=|D|-Σ_i|L_i|`, yields

`M≤|V(G)|ρ(H)+2v`.                                           (6)

At full formal equality, `M=|D|` and `v=0`, so

`|D|≤|V(G)|ρ(H)`,                                            (7)

and symmetrically `|D|≤|V(H)|ρ(G)`.

At Steiner's formal ratios, (7) implies

`|V(G)|≥(c/a)γ(G)≈1.83822γ(G)`,

where `a=2-3c`. This improves the elementary three-disjoint-set count
`|V(G)|≥3cγ(G)≈1.69300γ(G)`, but it remains order-dependent and does not
contradict the formal obstruction.

## A corner-completion obstruction

Applying the external-private theorem in both directions does not force an
undominated rectangle corner. In `C₅□C₅`,

`D={(i,2i mod 5):i∈Z₅}`

is a perfect dominating set. For `p_i=(i,2i)`, the vertices

```text
q_i=(i+1,2i),   r_i=(i,2i+1)
```

are external private neighbors in the two coordinate directions. Their
corner `(i+1,2i+1)` is nevertheless dominated by
`p_{i+1}=(i+1,2i+2)`. The corners cycle perfectly through `D`.

## Verdict

**GO** for an order-free coupling among the row hole packings, or a
cardinality lower bound on the two-packing number of self-private sets in
near-tight columns. **STOP** for a bare symmetric-corner argument and for
claiming that one unit of additivity slack pays for every self-private
vertex.
