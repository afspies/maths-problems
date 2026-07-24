# Terminal conflict graphs: exact equality and stability

## Status

**Proved.** In Steiner's two-sparse terminal regime, subset domination is
exactly a matching-cover parameter of an auxiliary graph. This yields a
graph-theoretic classification of equality in Lemma 2.2 and a sharper
classification of terminal equality in Lemma 2.3.

The later capacity certificate in `angles/terminal-capacity` further sharpens
full Lemma 2.3 equality from arbitrary odd cliques to `K₁/K₃` unions.

Literature priority for this formulation has not been established.

## Conflict graph

Let `S⊆V(G)` satisfy

`|N_G[v]∩S|≤2` for every `v∈V(G)`.

Define the conflict graph `F=F_G(S)` on vertex set `S` by joining distinct
`s,t` when

`N_G[s]∩N_G[t]≠∅`.

Equivalently, an edge of `F` is a pair of target vertices that one vertex of
`G` can dominate simultaneously.

### Exact parameter translation

Let `s=|S|`, `r=ρ_G(S)`, and `γ=γ_G(S)`. Then

`r=α(F)` and `γ=s-ν(F)`.                                       (1)

The first identity is immediate: a subset of `S` is a two-packing in `G`
exactly when it is independent in `F`.

For the second, a matching of size `ν(F)` lets one common witness dominate
each matched pair; dominate every unmatched target vertex by itself. This
uses `s-ν(F)` vertices. Conversely, assign every target vertex to one member
of an arbitrary dominating set `D`. Each member of `D` receives at most two
targets. The two-target classes form disjoint edges of `F`, hence a matching
of size at least `s-|D|`. Therefore `|D|≥s-ν(F)`.

Consequently the slack in Steiner's Lemma 2.2 is exactly

`b=s+r-2γ=α(F)+2ν(F)-|V(F)|`.                                  (2)

## Extremal matching-cover theorem

For every finite graph `F`,

`α(F)+2ν(F)≥|V(F)|`,                                           (3)

with equality if and only if every connected component of `F` is a complete
graph of odd order.

### Proof

Fix a maximum matching `M`. Its unmatched vertex set `U` is independent, so
`|U|=|V(F)|-2ν(F)≤α(F)`, proving (3).

Suppose `F` is connected and equality holds. Then `U` is a maximum
independent set. It is nonempty: otherwise equality would give `α(F)=0`.
Every endpoint of every edge of `M` has a neighbor in `U`, or it could be
added to `U`.

For a matched edge `xy`, its endpoints cannot have distinct neighbors
`u,v∈U`, because `u-x-y-v` would be an augmenting path. In fact all
`U`-neighbors of `x` and `y` form one common singleton; call it the vertex
assigned to `xy`.

There can be no edge between two matched edges assigned to distinct
`u,v∈U`: together with the two matching edges and the endpoint-to-`U` edges,
such an edge gives an alternating augmenting path of length five. Thus
blocks assigned to distinct vertices of `U` have no edges between them.
Since `U` itself is independent, connectivity forces `|U|=1`. Equality then
gives `α(F)=1`, so `F` is complete, while the single unmatched vertex makes
its order odd.

Conversely, `K_{2q+1}` has `α=1` and `ν=q`. Both sides of (3) and the
property of being a union of odd cliques are additive over components.

## Consequences for Steiner equality

In the terminal notation of `angles/subset-slack`, put

`R=ρ^{\{2\}}(G)` and `a=R-r-γ`.

The exact terminal slack is

`δ_G(S)=a+b`,

where `b` is given by (2). Hence terminal equality in Steiner's Lemma 2.3
requires:

1. `F_G(S)` is a disjoint union of odd cliques; and
2. `R=r+γ`.

If the odd-clique components have orders `2m_j+1`, then

`r=#components`, `γ=Σ_j(m_j+1)`, and terminal equality forces
`R=Σ_j(m_j+2)`.

The all-ones function on `S` is a 2-packing function, so `R≥|S|`. Therefore
the component sizes must also satisfy

`Σ_j(1-m_j)≥0`.                                                (4)

Equivalently, the number of isolated conflict vertices must be at least
`Σ_{m_j≥2}(m_j-1)`; triangles are neutral. Large odd cliques cannot appear
without enough isolated components to pay for them.

Equation (2) is also a stability theorem. It is the sum of the nonnegative
integer defects

`α(C)+2ν(C)-|C|`

over conflict components `C`. Every component that is not an odd clique
contributes at least one. Thus `b≤2` allows at most `b` non-odd-clique
components.

## Fibre verdict

Every two-sparse terminal remainder of a tight Steiner fibre set `L_i` must
have the odd-clique decomposition above and zero ambient packing slack.
This is a substantially sharper equality classification, but it is still
columnwise: no cross-`i` incompatibility has yet been proved. The next
product-side question is whether one minimum dominator `D` can induce these
odd-clique terminal structures simultaneously for all `i`.
