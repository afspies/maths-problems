# Balanced incidence at the Steiner obstruction

## Status

**Proved as an exact equality and stability classification.** This combines
the fibre-slack identity with the capacity-two terminal refinement. It does
not yet contradict the formal Steiner obstruction, but it reduces every
tight fibre set to fixed numbers of singleton and triangle atoms and forces
the occupied-cell and vertical-cell incidence matrices to have identical
margins.

The argument was derived with GPT-5.6 Sol at xhigh effort and checked
algebraically in this campaign. Literature priority has not been established.

## Setup and peeling burden

Write

```text
Γ=γ(G),  r=ρ(G),  R=ρ^{\{2\}}(G),  k=γ(H),  n=|D|.
```

Use Steiner's fibre notation `D_i,L_i` and put
`t_i=γ_G(L_i)`. Choose a complete peeling of `L_i` with `ℓ_i` dense
steps and two-sparse terminal set `T_i`. Let

`r_i=ρ_G(T_i)` and `B_i=ℓ_i+(r-r_i)`.                         (1)

The burden `B_i` is nonnegative because `T_i⊆V(G)` gives `r_i≤r`.

At an exact tight peeling, every dense step lowers subset domination by one,
and terminal equality gives `γ_G(T_i)=R-r_i`. Hence

`t_i=R-r+B_i`.                                                (2)

For an arbitrary peeling, the exact peeling and terminal slack identities
give the robust version

`t_i≥R-r+B_i-δ_i`,                                            (3)

where `δ_i=|L_i|+R-3t_i`. To see this directly, each step contributes a
nonnegative domination-loss `e`, and the terminal Lemma 2.1 defect is
nonnegative. Their sum is at most the full subset slack `δ_i`.

## Aggregate stability inequality

Recall the fibre defects

```text
p_i=|D_i|-γ_G(V(G)\L_i),
d_i=γ_G(V(G)\L_i)+t_i-Γ,
v=n-Σ_i|L_i|.
```

Since `p_i+d_i=|D_i|+t_i-Γ`,

`Σ_i t_i=kΓ-n+Σ_i(p_i+d_i)`.

Summing (3), substituting the exact total fibre-slack identity

`4n-k(3Γ-R)=v+3Σ_i(p_i+d_i)+Σ_iδ_i`,

and rearranging yields

```text
4Σ_i B_i
 ≤ k(Γ+4r-3R)-v+Σ_i(p_i+d_i)+3Σ_iδ_i.                        (4)
```

Thus the distance from the parameter relation `3R=Γ+4r`, together with the
four exact fibre defects, controls the aggregate number of peeling steps and
the loss of ordinary packing in the terminal remainders.

## Formal Steiner equality

At the normalized minimax obstruction,

```text
r/Γ=a=2-3c,
R/Γ=2b=3-4c,
c=(5+√73)/24,
```

and the defining identities give

`3R=Γ+4r`.                                                    (5)

If the oriented product bound and all six minimax terms are formally tight,
then `v=p_i=d_i=δ_i=0`. Equations (4) and (5) force `B_i=0` for every
column. Therefore:

1. `ℓ_i=0`: every `L_i` is already two-sparse;
2. `r_i=r`: every `L_i` contains a maximum two-packing of `G`;
3. its conflict graph is a union of `K₁` and `K₃`;
4. the capacity-two weights supported on `L_i` are an optimal global
   2-packing.

If `z_i,t_i'` denote the numbers of singleton and triangle conflict
components, then

```text
z_i+t_i'=r,
2z_i+3t_i'=R.
```

Consequently the atom counts do not depend on `i`:

```text
z_i=3r-R,       t_i'=R-2r,
|L_i|=2R-3r,   γ_G(L_i)=R-r.                                 (6)
```

Also

`|D_i|=Γ-R+r=2R-3r=|L_i|`,                                   (7)

where the middle equality is (5).

These are formal equality conditions: the ratios contain `√73`, so no finite
graph realizes them exactly. Equation (4) is the rigorous statement for
finite near-extremizers.

## Column separation and row exchange

Put `X_i=P_G(D_i)`. Exact equality makes `X_i` a minimum dominator of
`V(G)\L_i` and gives

`|X_i|+γ_G(L_i)=Γ`.

In fact,

`N_G[x]∩L_i=∅` for every `x∈X_i`.                             (8)

Suppose instead that `x` hits a conflict component of `L_i`. If it is a
`K₁`, use `x` as that component's one dominator. If it is a `K₃`, then use
`x` together with the third target when `x` hits two targets, or with a
common witness for the other pair when `x` hits one. Completing the other
components independently gives a minimum dominator of `L_i` containing
`x`. Its union with `X_i` dominates `G` using at most `Γ-1` vertices, a
contradiction.

For a fixed row `g`, define

```text
I_g={i:g∈L_i},        S_g={i:g∈X_i},
A_g=P_H(D∩({g}×V(H))).
```

Formal equality gives

`|I_g|=|A_g|=|S_g|` and `I_g∩S_g=∅`.                         (9)

Moreover `A_g` is a minimum dominator of
`π_{I_g}=⋃_{i∈I_g}π_i`: it dominates that union by verticality, while any
smaller set together with the retained centers `h_j`, `j∉I_g`, would
dominate `H` with fewer than `k` vertices. Thus every tight row performs a
size-preserving, disjoint exchange of partition centers.

## Balanced cell matrices

Define two `V(G)×[k]` zero-one matrices:

```text
A_{g,i}=1  iff D contains a point in {g}×π_i,
V_{g,i}=1  iff g∈L_i.
```

Column-projection injectivity makes `A` zero-one. Under formal equality,
(7) gives identical column sums for `A` and `V`. Row-wise equality in
Steiner's vertical count gives

`Σ_i A_{g,i}=|D∩({g}×V(H))|=Σ_i V_{g,i}`

for every `g`. Hence `A` and `V` have identical row and column margins.
After cancelling their common entries, their red-blue symmetric difference
is a balanced bipartite graph and therefore decomposes into alternating even
cycles.

There is also a private-target injection in every column. Write the unique
point of `D_i` over an occupied row `g` as `(g,h_g)`. Since
`P_G(D_i)` is a minimal dominator of `V(G)\L_i`, it has a private target
`x_g∈V(G)\L_i` with

`N_G[x_g]∩P_G(D_i)={g}`.

The targets are distinct, giving an injection

`P_G(D_i)→V(G)\L_i,  g↦x_g∈N_G[g]`.                          (10)

The coordinate statement depends on whether the private target is external.
Put `A_x=P_H(D∩({x}×V(H)))` and define the outside-part hole set

`Q_{x,i}=π_i\N_H[A_x\setminus π_i]`.

This set is nonempty when `x∉L_i`. If the private target is external,
`x_g≠g`, then row `x_g` contains no point of `D_i`; product domination and
`N_G[x_g]∩X_i={g}` force

`Q_{x_g,i}={h_g}`.                                           (11)

Thus `(x_g,h_g)` is a private product neighbor of `(g,h_g)`. If instead
`x_g=g`, the inside-cell point may cover several holes, and only

`∅≠Q_{g,i}⊆N_H[h_g]∩π_i`                                    (12)

is forced. There is no general reason that a minimum subset dominator has
an external private target, so (12) cannot be replaced by (11) universally.
The exclusion of row points inside `π_i` in the definition of `Q` is also
essential.

Each blue edge `(g,i)` says the row points outside `π_i` dominate all of
`π_i`; each red edge records the unique point of `D` in that row and part.
Any contradiction at the Steiner obstruction may therefore be sought on one
alternating incidence cycle at a time, while every column simultaneously
carries the fixed atomic packing structure (6).

## Why margins and exchanges are not enough

There is a small exact skeleton satisfying all the cardinality, separation,
and row-exchange conditions but failing (11), hence failing to dominate the
product.

Take `G=C₄` and

```text
L₁={0}, X₁={2},     L₂={2}, X₂={0}.
```

Let `H` have cells

```text
π₁={h₁,u₁,p₁},      π₂={h₂,u₂,p₂}
```

and edges

```text
h₁u₁, h₁p₁, h₁u₂, u₁u₂, u₂p₁,
h₂u₂, h₂p₂, h₂u₁, u₁p₂.
```

Then `γ(H)=2`, `u₂` dominates `π₁`, and `u₁` dominates `π₂`. The set

`D={(2,u₁),(0,u₂)}`

induces the displayed vertical sets, column projections, balanced row
counts, tight `K₁` fibres, and minimum row exchanges. Nevertheless
`(1,p₁)` is undominated. For the private complement target `1` in column
one, the outside-part row set is empty, so all of `π₁` is a hole rather than
the singleton `{u₁}` required by the external-target equation (11).

## Verdict

**GO**, but the next lemma must use the labels and domination relations along
the alternating cycles. The margin theorem alone is realizable by arbitrary
balanced zero-one matrices. A viable exchange argument should combine:

- the private-target system forced by each injective minimum column
  projection, distinguishing the external equation (11) from the weaker
  self-private inclusion (12);
- the cross-part domination represented by every blue edge; and
- the maximum ordinary and optimal 2-packings supported inside every `L_i`.

Merely counting row or column degrees cannot improve the constant.
