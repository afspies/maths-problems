# Indexed provider non-reuse

## Status

**Exact Hall formulation and an actual-product obstruction proved and
independently audited at GPT-5.6 Sol xhigh effort.** Indexed terminal
`K₁/K₃` data, optimal canonical 2-packings, and exact provider-row exchange
do not by themselves control provider reuse. A single selected coordinate
can serve arbitrarily many indexed terminal triangles.

The obstruction has linear Steiner projection/additivity/vertical defects,
so it does not refute a theorem using the full zero-defect package. It
identifies the exact surviving target: charge provider Hall deficiency to
the established fibre defects, with a quantitatively large amplification.

## Provider Hall deficiency

Fix a product row `g`. Let `I` index vertical cells, let `y_i∈π_i` be one
demand from each indexed terminal system, and let `A_g` be the row's
selected `H`-coordinates. Define

```text
P_g⊆I×A_g,
i∼a  iff  a∈N_H[y_i]\π_i.
```

Every left vertex has a provider. The minimum number of demands that must
reuse a provider is exactly

```text
|I|-ν(P_g)
=max_{J⊆I}(|J|-|N_{P_g}(J)|).                               (1)
```

This is the matching deficiency in Hall's theorem.

If the demand set `{y_i:i∈I}` is a two-packing in `H`, then each provider
is adjacent to at most one demand. When also `|A_g|=|I|`, the provider graph
is a perfect matching.

The existing row-hole theorem does not supply this hypothesis. It makes the
incoming private holes indexed by `J_g` a two-packing; the terminal
providers here are indexed by the outgoing cells `I_g`. No proved map
`I_g→J_g` preserves the demanded coordinate.

## Actual-product obstruction

For `m≥1`, define `H_m` with cells

```text
B_i={c_i,s_i,t_i},       R_i={r_i,a_i,w_i},
```

and edges

```text
c_i s_i, c_i t_i,
r_i a_i, r_i w_i, a_i t_i,
a_0 c_i, a_0 s_i                         (0≤i<m).
```

Put `A*={a_0,...,a_{m-1}}`.

The `2m` closed neighborhoods

```text
N[t_i]={t_i,c_i,a_i},
N[w_i]={w_i,r_i}
```

are pairwise disjoint. Thus every dominator has size at least `2m`, while
`{c_i,r_i:0≤i<m}` dominates. Hence

`γ(H_m)=2m`.                                                 (2)

The set `A*` dominates every blue cell: `a_i` covers `t_i`, and `a_0`
covers `c_i,s_i`. Therefore

`A*∪{r_i:0≤i<m}`

is a minimum, size-preserving exchange of all blue partition centers.
Nevertheless,

`N[s_i]∩A*={a_0}`                                            (3)

for every `i`. The provider graph on the blue demands has matching number
one and Hall deficiency `m-1`.

Now take `G=C₅`, with

```text
T={0,2,4},       X={1,3},
```

and define

```text
D_m=(T×A*) ∪ (X×{c_i,w_i:0≤i<m}).                           (4)
```

This set dominates `C₅□H_m`.

- On a `T`-row, `A*` dominates every blue cell.
- In a red cell, `a_i` covers `a_i,r_i`, while a neighboring `X`-row
  contains `w_i`.
- On an `X`-row, `c_i` dominates the blue cell.
- In a red cell, `w_i` covers `w_i,r_i`, while a neighboring `T`-row
  contains `a_i`.

For the displayed `2m`-cell partition,

```text
L_i=T   for every blue cell,
L_i=∅   for every red cell.                                 (5)
```

Every blue `L_i` is an exact terminal triangle:

```text
F_{C₅}(T)=K₃,
γ_{C₅}(T)=2,
ρ^{\{2\}}(C₅)=3,
3γ_{C₅}(T)=|T|+ρ^{\{2\}}(C₅)=6.
```

The unit weighting on `T` is an optimal global integer 2-packing.

For every `g∈T`,

`|I_g|=|D_m∩({g}×H_m)|=m`,

and the row performs the minimum exchange above. Yet the single point

`(g,a_0)∈D_m`

is the unique provider for all `m` demands `s_i`. Thus reuse is unbounded
under actual product domination, exact terminal atomicity, optimal terminal
capacity, and exact provider-row exchange.

## Why the overlap tax does not see cross-index reuse

For a blue index `i`, take

```text
q=(1/2)1_T,       p^{(i)}=1_{s_i}.
```

Both are fractional packings. The rank-one weight is supported on
`T×{s_i}`. Every support cell is unselected and vertically imported, but it
has no horizontal import because `B_{s_i}=∅`. Therefore it lies in neither
`A\I` nor the double-import region `J`, and the four-region tax satisfies

`K^{(i)}=0`                                                   (6)

for every index.

Thus `K` is an intra-pair overlap tax. It cannot detect the reuse of one
selected point across different indexed packings `p^{(i)}`.

## Exact boundary: the fibre defects pay

The construction does not satisfy full formal equality. Its exact Steiner
defects are:

```text
blue index: p_i=1, d_i=1, δ_i=0,
red index:  p_i=3, d_i=0, δ_i=3,
vertical slack: v=4m.
```

They satisfy the fibre identity exactly:

```text
v+3Σ_i(p_i+d_i)+Σ_iδ_i
=4m+15m+3m
=22m
=4|D_m|-2m[3γ(C₅)-ρ^{\{2\}}(C₅)].                          (7)
```

Hence any surviving provider theorem must charge the Hall deficit (1) to
`v,p_i,d_i,δ_i` or to a genuinely new product-scale defect.

## Quantitative obstruction

At the formal ratios,

`b(b-a)=(5√73-41)/72`.

Even completely disjoint row and column triangle credits give only

```text
b²+2b(b-a)
=(13-√73)/24
≈0.18567
<c.                                                         (8)
```

Starting from `b²`, the number `N` of independently additive triangle
charges needed merely to exceed Steiner satisfies

```text
N>(c-b²)/(b(b-a))
 =(249+21√73)/24
 ≈17.851.                                                   (9)
```

Thus at least eighteen independent copies are required. Row-plus-column
additivity is not close to the needed scale.

## Verdict

**STOP** for indexed atoms or the current overlap tax alone. A useful
replacement must simultaneously:

1. couple outgoing terminal incidences `I_g^△` to incoming private-hole
   two-packings `J_g`;
2. charge every Hall deficiency to the exact fibre defects or a new
   product-scale invariant; and
3. produce at least an eighteen-fold effective amplification.
