# Independent reconstruction of Steiner's 0.5643 proof

Source: Raphael Steiner, *A constant-factor step towards Vizing's
conjecture*, arXiv:2606.14414v1 (12 June 2026). This note reconstructs the
argument rather than treating the displayed constant as a black box.

## Definitions

For a graph `G`, let `γ(G)` be its domination number and `ρ(G)` its
two-packing number. A nonnegative integer function `f` on `V(G)` is a
`k`-packing function when `f(N[v]) ≤ k` for every `v`; its maximum total
weight is `ρ^{k}(G)`. Define `γ^{k}(G)` dually using `f(N[v]) ≥ k` and minimum
total weight. For `S ⊆ V(G)`, `γ_G(S)` is the minimum size of a set (not
necessarily contained in `S`) dominating `S`, and `ρ_G(S)` is the largest
two-packing contained in `S`.

## Dependency map

```text
matching/König argument ──> Lemma 2.1: sparse S gives γ_G(S) ≤ ρ²(G)-ρ_G(S)
maximum-matching argument ─> Lemma 2.2: γ_G(S) ≤ (|S|+ρ_G(S))/2
                Lemmas 2.1 + 2.2 + induction
                              │
                              v
                 Lemma 2.3: 3γ_G(S) ≤ |S|+ρ²(G)
                              │
                     cell/fibre counting
                              v
        Theorem 1.4: γ(G□H) ≥ (3γ(G)-ρ²(G))γ(H)/4

Brešar 2017 ───────────────> (2γ(G)-ρ(G))γ(H)/3
Hou–Lu 2009 + weak duality -> ρ(G)γ(H)+ρ²(H)(γ(G)-ρ(G))/2

the three symmetric pairs of product bounds
                              │
                              v
                 exact four-parameter minimax
                              │
                              v
                    c=(5+√73)/24
```

Here and below `ρ²` abbreviates `ρ^{\{2\}}`, not the square of `ρ`.

## Re-derivation of the subset lemma

If some closed neighborhood meets `S` in at least three vertices, remove
those vertices, dominate the remainder inductively, and add the center. Each
added dominator pays one unit while deleting at least three units of `|S|`.

It remains to treat `|N[v]∩S|≤2` for every `v`. Put `r=ρ_G(S)` and
`R=ρ²(G)`.

1. Choose a maximum two-packing `P⊆S`. In the bipartite conflict graph
   between `P` and `S\P`, join two vertices when their closed neighborhoods
   intersect. König's theorem and a maximum matching give a dominating set
   for `S` of size at most an independent set `I` in this conflict graph.
   Weight `P∩I` by 2 and the symmetric difference of `P,I` by 1. The
   two-sparse hypothesis makes this a 2-packing function. Hence
   `R ≥ |P|+|I| ≥ r+γ_G(S)`, or `γ_G(S)≤R-r`.
2. In the full conflict graph on `S`, a maximum matching of size `t` lets one
   common neighbor dominate each matched pair. The unmatched vertices form
   a two-packing, so `|S|-2t≤r`, while `γ_G(S)≤|S|-t`. Therefore
   `γ_G(S)≤(|S|+r)/2`.

Taking one third of the first bound and two thirds of the second cancels `r`
and gives

`γ_G(S) ≤ (|S|+R)/3`.

## Re-derivation of the product bound

Let `D` be a minimum dominating set of `G□H`. Partition `V(H)` into
`γ(H)` parts `π_i`, each contained in the closed neighborhood of its chosen
dominating vertex. Let `D_i=D∩(V(G)×π_i)`. For each `i`, let `L_i` be the
vertices `g` whose cell `{g}×π_i` is dominated vertically from outside that
cell.

The projection of `D_i` dominates `V(G)\L_i`, while Lemma 2.3 dominates
`L_i`. Thus

`γ(G) ≤ |D_i| + (|L_i|+ρ²(G))/3`.

Summing over `i` gives

`γ(G)γ(H) ≤ |D| + (Σ_i|L_i|)/3 + ρ²(G)γ(H)/3`.

For a fixed `g`, if `m_g` cells are vertically dominated, the `H`-projection
of `D` in the `g`-fibre together with the original dominators for the other
`γ(H)-m_g` parts dominates `H`. Hence `m_g≤|D∩({g}×V(H))|`, and summing gives
`Σ_i|L_i|≤|D|`. Rearrangement yields

`γ(G□H)=|D| ≥ (3γ(G)-ρ²(G))γ(H)/4`.

## Hou–Lu input and the dual pairing

Hou and Lu prove

`γ(G□H) ≥ ρ(G)γ(H)+γ^{m}(H)`, where `m=γ(G)-ρ(G)`.

If `f` is an optimal 2-packing function and `g` an optimal `m`-dominating
function on `H`, double-counting the products over closed neighborhoods gives

`2γ^{m}(H) ≥ Σ_v g(v)f(N[v]) = Σ_w f(w)g(N[w]) ≥ mρ²(H)`.

Consequently,

`γ(G□H) ≥ ρ(G)γ(H)+ρ²(H)(γ(G)-ρ(G))/2`,

and symmetrically with `G,H` exchanged.

## Exact four-parameter optimization

Normalize

`x₁=ρ(G)/γ(G)`, `x₂=ρ²(G)/(2γ(G))`,
`y₁=ρ(H)/γ(H)`, `y₂=ρ²(H)/(2γ(H))`.

Then `0≤x₁≤x₂≤1` and `0≤y₁≤y₂≤1`. (For nonempty graphs the first
inequalities are strict, but the closed domain is harmless.) The three pairs
of bounds above say that the normalized product domination number is at least

```text
M = max{
  (2-x₁)/3, (2-y₁)/3,
  3/4-x₂/2, 3/4-y₂/2,
  x₁+y₂(1-x₁), y₁+x₂(1-y₁)
}.
```

Let `c` be the positive root of `12c²-5c-1=0`, so
`c=(5+√73)/24`. Define the threshold values

`a=2-3c=(11-√73)/8`,
`b=3/2-2c=(13-√73)/12`.

The root equation is equivalent to

`a+b(1-a)=c`.

If `x₁<a` or `y₁<a`, one of the first two bounds exceeds `c`. If `x₂<b`
or `y₂<b`, one of the next two exceeds `c`. Otherwise, monotonicity of
`x+y(1-x)` on `[0,1]²` gives

`x₁+y₂(1-x₁) ≥ a+b(1-a)=c`

(and likewise for the other mixed term). Thus `M≥c`.

This optimization is exact, not merely a lower estimate: the feasible point
`x₁=y₁=a`, `x₂=y₂=b` makes all six expressions equal to `c`. The relaxation
therefore has minimum exactly `(5+√73)/24`. Improving the global constant by
reoptimizing these same six inequalities is impossible; a new combinatorial
input is required.

## Corrected k=3 extension and why it does not raise the constant

Let `P=ρ^{\{3\}}(G)` and retain `r=ρ_G(S)`, `R=ρ^{\{2\}}(G)`. Adding
Lemma 2.3 to Lemma 2.2 gives

`5γ_G(S)≤2|S|+R+r`.

The indicator of a maximum two-packing inside `S` is a 1-packing function.
Adding it to an optimal 2-packing function shows `P≥R+r`, and hence

`5γ_G(S)≤2|S|+P`.

The same fibre count as above yields

`γ(G□H)≥(5γ(G)-ρ^{\{3\}}(G))γ(H)/7`.

This is a valid new product inequality, but it does not alter the exact
relaxed minimum. Normalize `x₃=ρ³(G)/(3γ(G))` and similarly `y₃`.
Superadditivity gives `3x₃≥2x₂+x₁`. At the old equality point, set
`x₃=y₃=d=(2b+a)/3`. Then

`5/7-3d/7=(5-2b-a)/7=c`,

while the `k=3` Hou–Lu mixed term is
`a+d(1-a)<a+b(1-a)=c`. Thus every new term is at most `c` at a feasible point
where all old terms equal `c`. A stronger structural relation, not another
numerical optimization, is necessary.
