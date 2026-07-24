# Adaptive provider matchings and labelled cell cycles

## Status

**Universal Hall refinement proved and independently audited at GPT-5.6 Sol
xhigh effort.** In every row of an actual product dominator, the vertically
dominated cells can be matched injectively to distinct selected row
coordinates that genuinely touch those cells. At zero vertical slack and
column equality, these adaptive provider transitions form a loopless
Eulerian cell digraph and hence decompose into directed labelled cycles.

Under the full atomic/additive column hypotheses, the matching composes
injectively with external private targets and gives local expansion cuts.
The theorem does not improve Steiner's constant: its demand coordinate is
chosen after the provider, whereas the existing triangle-energy argument may
prescribe a different coordinate.

## Setup

Fix a minimum dominating set `{h₁,...,h_k}` of `H` and a partition
`π₁,...,π_k` with `π_i⊆N_H[h_i]`. For a product dominator `D`, put

```text
D_i=D∩(G×π_i),
X_i=P_G(D_i),
L_i=V(G)\N_G[X_i].
```

Thus `g∈L_i` means that no point of `D_i` in a closed neighboring
`G`-row can dominate the `i`-cell at row `g`. For a row `g`, define

```text
I_g={i:g∈L_i},
A_g=P_H(D∩({g}×H)).
```

## Universal adaptive Hall theorem

There is an injection

`μ_g:I_g→A_g`                                                 (1)

such that

```text
μ_g(i)∉π_i,
N_H[μ_g(i)]∩π_i≠∅                                           (2)
```

for every `i∈I_g`.

After finding the matching, choose

`y_{g,i}∈N_H[μ_g(i)]∩π_i`.

The demands `y_{g,i}` therefore have pairwise distinct selected providers.
They are adaptive: neither the theorem nor its proof works for arbitrary
pre-prescribed points of the cells.

### Proof

The row set `A_g` dominates `π_{I_g}=⋃_{i∈I_g}π_i`. Indeed, for
`g∈L_i`, no point of `D_i` in a closed neighboring `G`-row can own a cell
point `(g,h)`, so product domination forces an owner with first coordinate
`g`.

Moreover,

`γ_H(π_{I_g})=|I_g|`.                                        (3)

The centers `{h_i:i∈I_g}` give the upper bound. If a smaller set dominated
`π_{I_g}`, adjoining the retained centers `{h_l:l∉I_g}` would dominate
`H` with fewer than `k=γ(H)` vertices.

Form a bipartite graph on `I_g` and `A_g`, joining `i` to `a` when
`a∉π_i` and `N_H[a]∩π_i≠∅`. If `J⊆I_g`, then its neighbor set
`N(J)` dominates `π_J`: for each `i∈I_g`, the set `A_g\π_i`
dominates `π_i`, and any such row coordinate that dominates a point of
`π_i` is, by definition, in `N(J)`. Therefore

```text
N(J)∪{h_l:l∈I_g\J}
```

dominates `π_{I_g}`. Equation (3) forces `|N(J)|≥|J|`.
Hall's theorem proves (1).

The exclusion in (2) also follows directly from the product notation: a
point of `D_i` in row `g` would put `g` in `N_G[X_i]`, contradicting
`g∈L_i`. Hence every matched incidence gives a genuine cell transition

`i→j`, where `μ_g(i)∈π_j` and `j≠i`.                         (4)

## Exact global slack and Eulerian cycles

The map

`(g,i)↦(g,μ_g(i))`

injects the blue-incidence set

`B={(g,i):g∈L_i}`

into `D`. Its exact number of unused selected points is

```text
|D|-|B|
=|D|-Σ_i|L_i|
=v.                                                         (5)
```

Give each blue incidence the cell edge (4). The outdegree of cell `i` is
`|L_i|`. The indegree of cell `j` is the number of matched points in
`D_j`, at most `|D_j|`.

If

```text
v=0,       |D_i|=|L_i|  for every i,                        (6)
```

then every selected point is matched and every cell has equal indegree and
outdegree. The cell digraph is loopless and Eulerian, so it decomposes into
directed cycles. Every edge carries actual labels

```text
y∈π_i,       a∈π_j,       a∈N_H[y].
```

This is stronger than decomposing two equal-margin zero-one matrices:
the row pairing itself respects domination in `H`.

## Transfer to external private holes

Assume additionally the full local atomic/additive hypotheses of
`angles/external-private-holes`, so every matched point `(g,a)∈D_j` has an
external private target `x∼g`. Product domination then makes `a` the
singleton outside-part hole in row `x` for cell `j`.

The composite

`Φ(g,i)=(x,μ_g(i))`                                          (7)

is injective. Two equal outputs would use the same coordinate `a`, hence
the same cell `j`, and make `x` an external private target for two distinct
members of the minimum projection `X_j`, impossible.

Let `J_x^μ` be the matched cells landing at row `x`, let `P_x^μ` be their
hole coordinates, and put

`e_x=|A_x|-|I_x|`.

The row-hole theorem applied to this subset gives

```text
|J_x^μ|-γ_H(P_x^μ)≤e_x,
|J_x^μ|≤ρ(H)+2e_x.                                          (8)
```

In particular, `P_x^μ` is a two-packing when `e_x=0`.

Because every external target of a source row in `U` lies in `N_G(U)`,
equations (7)--(8) give the local cut

```text
Σ_{g∈U}|I_g|
≤ρ(H)|N_G(U)|+2Σ_{x∈N_G(U)}e_x.                             (9)
```

Here `N_G(U)` is the open neighborhood union, since the targets are
external. For nonnegative row weights `λ_g`, the same charging yields

```text
Σ_g λ_g|I_g|
≤Σ_x(ρ(H)+2e_x) max_{g∈N_G(x)}λ_g.                          (10)
```

The statements remain valid after restricting the source incidences to
terminal triangles.

At `v=0`, the transfer is a bijection between outgoing blue incidences and
chosen private-hole occurrences. On the row factor it gives a directed
multigraph `g→x` with outdegree `|I_g|` and indegree `|J_g^μ|`. It
decomposes into cycles and paths, but pure cycle closure would require the
additional, unproved rowwise identity `|I_g|=|J_g^μ|`.

## Stress test and limitation

In the `C₅□H_m` provider obstruction, the theorem matches blue cell `B_i`
to the distinct coordinate `a_i` using the adaptive target `t_i`. Thus the
cell transitions are `B_i→R_i`. The pre-prescribed targets `s_i` still all
have unique provider `a₀`; their Hall deficiency `m-1` is untouched.

The two complementary `C₅` rows contain exactly the `4m=v` unmatched
selected points. The used red columns have `L=∅` and projection
`X=V(C₅)`, so their matched points do not satisfy the external-private
column theorem. The cycle and private-hole conclusions fail exactly where
the established defects are positive.

For triangle incidences, the global consequence at formal equality is only

`3k(R-2r)≤|V(G)|ρ(H)`.

This is weaker than the existing all-incidence inequality

`k(2R-3r)≤|V(G)|ρ(H)`,

their difference being the nonnegative singleton count `3r-R`.
Therefore the new theorem does not improve `c`.

## Verdict

The adaptive cell-level provider problem is solved: it has zero Hall
deficiency. The remaining bridge is narrower and label-sensitive:

1. make the triangle-energy witness compatible with the adaptive matching;
2. exploit the local weighted expansion cuts (9)--(10); or
3. charge failure of the external-private transfer to the exact column
   defects.

**STOP** for claiming a matching of pre-fixed demands, a
coordinate-preserving map `i→i`, or automatic rowwise cycle closure.
