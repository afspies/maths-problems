# Zero-defect escape realization

## Status

**Exact classification and universal realization theorem proved and
independently checked at GPT-5.6 Sol xhigh effort.** The current
isolation/collision/redundancy defects impose no useful global structure on
escape dynamics: at zero defect, the escape-candidate graph can be any
finite bipartite graph without isolated vertices.

This is a hard stop for generic cycle-density, bounded-path, injective-owner,
and additive escape-credit arguments. A surviving escape theorem must use
the indexed terminal `K₁/K₃` systems specific to formal Steiner equality.

## Zero-defect classification

Let `D` dominate `G□H`. Suppose

```text
I_G=I_H=D,
Ω_G=Ω_H=X_G=X_H=0.
```

Then `D` is a perfect dominating code: every product vertex has exactly one
owner in `D`.

Indeed, fibre isolation makes every selected cell uniquely dominated.
For an unselected cell:

- `Ω_G=0` permits at most one horizontal owner;
- `Ω_H=0` permits at most one vertical owner; and
- `X_G=X_H=0` forbids having one owner in each direction.

Domination supplies at least one owner, proving uniqueness.

Conversely, every perfect code has all four collision/redundancy defects
zero and is isolated in both fixed-coordinate fibres. If both factors have
no isolated vertices, every codeword has external private neighbors in both
coordinate directions, so the eligible set `T` equals `D`.

## Reversibility

For a perfect code, the mixed escape relation is undirected. Suppose an
escape from

`d=(g,h)`

to

`u=(x,z)`

uses `gx∈E(G)` and a two-step path `h-y-z` in `H`. The cells

```text
(x,h), (g,y)
```

are uniquely owned by `d`, and the corner `(x,y)` is uniquely owned by
`u`.

For the reverse escape, use `(g,z)` and `(x,y)` as the private cells of
`u`. Their corner `(g,y)` is uniquely owned by `d`. Thus every candidate
arc reverses.

## Universal realization theorem

Let `F` be any finite bipartite graph without isolated vertices, with
parts `S,T`. Let `H` be its one-subdivision: replace each edge `st` by

`s-y_{st}-t`.

Take `G=K₂` and

`D={(0,s):s∈S}∪{(1,t):t∈T}`.                                (1)

Then `D` is a perfect code in `K₂□H`.

- The opposite-row copy of a code-label cell is covered horizontally.
- `(0,y_{st})` is uniquely covered by `(0,s)`.
- `(1,y_{st})` is uniquely covered by `(1,t)`.

These cases cover every product vertex exactly once. Hence `D` is both a
dominating set and a closed-neighborhood packing, so it is minimum.

Two codewords have a mixed escape relation exactly when their `K₂`
coordinates differ and their `H` labels have distance two. By construction,

`dist_H(s,t)=2` if and only if `st∈E(F)`.

Therefore the escape-candidate graph on `D` is isomorphic to `F`.

## Sharp counterfamilies

Take `F=K_{1,k}`. Then `H` is the subdivided star with arms

`z-y_i-h_i`, `1≤i≤k`,

and

`D_k={(0,h_i):1≤i≤k}∪{(1,z)}`.                              (2)

Here

```text
γ(H)=k,
γ(K₂□H)=|D_k|=k+1,
T=D_k,
Ω_G=Ω_H=X_G=X_H=0.
```

Every leaf codeword is forced toward the center codeword in any functional
escape map, while the center chooses one leaf. There is exactly one
directed two-cycle, so

`|cyclic vertices|/|T|=2/(k+1)→0`.

Moreover

`|D_k|-γ(K₂)γ(H)=1`

while `|T|=k+1`. Consequently no fixed `ε>0` can satisfy

`|D|≥γ(G)γ(H)+ε|T|`

for all such products.

Taking `F=P_n` and orienting toward one central edge similarly produces
arbitrarily long zero-defect in-trees before the unique two-cycle.

## Verdict

The generic escape route is exhausted even at exact zero defect and for
minimum perfect codes. Neither a positive recurrent fraction, bounded
return time, matching of sources to owners, nor a fresh defect per departure
can follow from the present quantities.

The only remaining escape-shaped possibility must forbid the subdivision
realization using additional formal-Steiner data: indexed terminal
singleton/triangle atoms, red/blue cell separation, and their private-target
systems.
