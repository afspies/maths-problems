# Cross-row hole packings

## Status

**One exact product-packing lemma and two exact obstructions proved.** Row
hole two-packings tensor with any factor packing, but their weighted mass can
capture an arbitrarily small fraction of the private incidences. Full formal
balance adds a common-neighborhood inequality, but its coefficient is too
weak at Steiner's ratios.

The results were proposed and adversarially checked by GPT-5.6 Sol at xhigh
effort. They close row-hole density arguments that do not use all alternating
incidence labels.

## Product packing from row holes

Let `P_y⊆V(H)` be a two-packing for every `y∈V(G)`. If `p` is a fractional
packing on `G`, define

`W(y,a)=p_y 1[a∈P_y]`.

Then `W` is a fractional packing on `G□H`. In the closed neighborhood of
`(u,h)`, the same-row contribution is at most `p_u`, because `P_u` meets
`N_H[h]` at most once. Every remaining contribution has `H`-coordinate `h`
and comes from a row in `N_G(u)`. Hence

`W(N[(u,h)])≤Σ_{y∈N_G[u]}p_y≤1`.

Consequently

`Σ_y p_y|P_y|≤γ_f(G□H)≤γ(G□H)`.                              (1)

More generally, an integer `q`-packing function `f` on `G` gives an integer
`q`-packing on the product of total `Σ_y f_y|P_y|`.

## Common-crown obstruction

Start with a graph `B` and a minimum dominating set
`X={x₁,...,x_m}`. Add vertices `w,y₁,...,y_m` and edges

```text
wx₁,
x_i y_i and w y_i for every i.
```

The resulting graph `G` still has domination number `m`: map `w` back to
`x₁` and each `y_i` back to `x_i` in any dominator. Each `y_i` is an
external private target of `x_i`, but all targets lie in `N[w]`. Therefore
every fractional packing satisfies

`Σ_i p(y_i)≤1`.                                              (2)

Moreover

```text
ρ(B)≤ρ(G)≤ρ(B)+1,
ρ²(B)≤ρ²(G)≤ρ²(B)+2.                                       (3)
```

Thus large base families retain their normalized packing parameters while
the fractional mass on all private-target rows is negligible.

This is realized by an actual product. Take `H` edgeless on `k` vertices and
`D=X×V(H)`. Then `D` is minimum, every `(y_i,a_j)` is an external private
product neighbor of `(x_i,a_j)`, each `P_{y_i}=V(H)` is a two-packing, and
the total hole incidence is `mk=|D|`. Nevertheless (1) captures at most
`k=|D|/m`.

The construction violates the formal fibre conditions: `H` has
`ρ(H)/γ(H)=1`, owner rows have vertical slack, and `|L_i|=|X_i|` fails.
It therefore kills privacy-and-row-packing density alone, not every
full-balance argument.

## What full balance adds

Assume the formal balanced system. Write

```text
k=γ(H),
d=|X_i|=|L_i|,
m_y=|I_y|=|A_y|,
```

and let `s` be the number of singleton partition cells. If
`Y⊆N_G[w]` is a set of external-target rows and `M(Y)` counts the private
incidences landing there, then

`M(Y)≤2kρ(H)+sd`.                                            (4)

Indeed, every `L_i` is two-sparse, so

`Σ_{y∈Y}m_y=Σ_i|Y∩L_i|≤2k`.

There are at most `2k` nonzero rows in `Y`, and each carries at most
`ρ(H)` holes. A zero row has `A_y=∅`; its external hole equals the entire
cell, so it can target only a singleton cell. Those columns contribute at
most `sd` further incidences.

At formal values `d=cγ(G)` and `ρ(H)=ak`, concentration of all `dk`
incidences in one closed neighborhood would require only

`s/k≥1-2ak/(cγ(G))`.                                        (5)

When the factor domination numbers are comparable,
`2a/c≈1.088>1`, so (5) is vacuous. Balance alone does not countwise exclude
common-neighborhood concentration.

## Verdict

**STOP** for a lower-density theorem based only on row two-packings,
private-target injections, or one factor packing. **GO** only for a lemma
using owner-specific coordinate coverage along alternating occupied/vertical
cycles, or for a new bound on singleton partition cells.
