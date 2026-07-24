# Capacity-two conflict refinement

## Status

**Proved and independently checked by GPT-5.6 Sol at xhigh effort.** The
two-sparse terminal case of Steiner's subset lemma has a third exact
certificate between the conflict matching bound and the ambient
2-packing. It sharpens terminal equality from arbitrary odd cliques to
isolated vertices and triangles only, and yields a strictly stronger
subset-domination inequality.

Literature priority for this formulation has not been established.

## The conflict capacity

For a graph `F`, define

`τ₂(F)=max Σ_x w_x`,

where `w_x∈{0,1,2}` and `w_x+w_y≤2` for every edge `xy∈E(F)`.

Let `S⊆V(G)` be two-sparse, let `F=F_G(S)` be its closed-neighborhood
conflict graph, and put

`s=|S|`, `r=α(F)`, `ν=ν(F)`, `γ=γ_G(S)=s-ν`, and
`R=ρ^{\{2\}}(G)`.

Every feasible weight function for `τ₂(F)`, extended by zero outside `S`,
is a 2-packing function on `G`. Indeed, a closed neighborhood meets `S` in
at most two vertices; if it meets two, those vertices are adjacent in `F`
and their weights sum to at most two. Consequently,

`R≥τ₂(F)`.                                                     (1)

## A Hall-deficiency lower bound

For every graph `F`,

`τ₂(F)≥α(F)+|V(F)|-ν(F)`.                                    (2)

To prove this, choose a maximum independent set `A` and consider the
bipartite graph consisting only of edges between `A` and `V(F)\A`. Its
maximum matching has size at most `ν(F)`. By the deficiency form of Hall's
theorem, some `I⊆A` satisfies

`|I|-|N(I)|≥|A|-ν(F)=α(F)-ν(F)`.

Assign weight two to `I`, weight zero to `N(I)`, and weight one to every
other vertex. This is feasible for `τ₂(F)` and has weight

`|V(F)|+|I|-|N(I)|≥|V(F)|+α(F)-ν(F)`.

Combining (2) with `α(F)+2ν(F)≥|V(F)|` shows that

`η(F):=τ₂(F)-2|V(F)|+3ν(F)≥0`.                               (3)

## Exact terminal slack decomposition

The terminal slack splits into three nonnegative integers:

```text
|S|+R-3γ_G(S)
 = [R-τ₂(F)]
 + [τ₂(F)-(α(F)+|F|-ν(F))]
 + [α(F)+2ν(F)-|F|].                                         (4)
```

The last term vanishes exactly when every component of `F` is a complete
odd graph. On `K_{2m+1}`,

```text
τ₂(K₁)=2,
τ₂(K_{2m+1})=2m+1  for m≥1.
```

The middle term is therefore zero on `K₁` and `K₃`, and equals `m-1` on
`K_{2m+1}` for `m≥2`. It follows that terminal equality in Steiner's
Lemma 2.3 holds exactly when

1. `F_G(S)` is a disjoint union of copies of `K₁` and `K₃`; and
2. `R=τ₂(F)=2z+3t`, where `z,t` are the numbers of those components.

This replaces the earlier, weaker odd-clique classification. Quantitatively,
the terminal slack is at least

`(# non-odd-clique components)+Σ_{K_{2m+1},m≥2}(m-1)`.

## Refined peeling inequality

Define `p_G^△(S)` recursively. If `S` is two-sparse, set

`p_G^△(S)=η(F_G(S))`.

Otherwise set

`p_G^△(S)=max_v [|N[v]∩S|-3+p_G^△(S\N[v])]`,                 (5)

where the maximum is over vertices meeting `S` at least three times. Then

`3γ_G(S)≤|S|+ρ^{\{2\}}(G)-p_G^△(S)`.                          (6)

For a dense hit of size `q`, dominate it by its center and apply (6)
recursively to the remainder. In the terminal case, (6) is (1) and (3).
This proves the result by induction.

The new parameter dominates the earlier excess-peeling parameter: extending
any peeling sequence to a terminal set only adds nonnegative `q-3` terms,
and its terminal `η` is nonnegative. Thus (6) is never weaker than the first
session's inequality and is strict whenever some maximizing branch ends in
a conflict graph other than a union of isolated vertices and triangles.

Substitution in Steiner's fibre proof gives the rigorous instance-sensitive
product bound

```text
γ(G□H) ≥ ((3γ(G)-ρ^{\{2\}}(G))/4)γ(H)
          +(1/4)Σ_i p_G^△(L_i).                               (7)
```

## Sharpness and verdict

The terminal classification itself is sharp. Take a disjoint union of `z`
isolated vertices and `t` copies of `C₅`; in each `C₅`, put in `S` three
vertices labeled `{0,2,4}` in cyclic order. The conflict graph is
`zK₁⊔tK₃`, while

`γ_G(S)=z+2t` and `ρ^{\{2\}}(G)=2z+3t`,

so equality holds. In `C₅`, the upper bound `ρ^{\{2\}}≤3` follows by
summing its five closed-neighborhood constraints, and weight one on
`{0,2,4}` attains three.

**GO** for simultaneous fibre incidence: every zero-defect terminal column
now consists only of atomic singleton and triangle blocks. **STOP** for a
purely subset-local contradiction: arbitrary mixtures of both atoms are
realized exactly, so product geometry must rule out their simultaneous
appearance across the fibre sets `L_i`.
