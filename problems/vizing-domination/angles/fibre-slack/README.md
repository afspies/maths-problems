# Exact slack decomposition for Steiner's fibre bound

## Status

**Proved, pending only literature-priority audit.** The proof of Steiner's
Theorem 1.4 admits an exact decomposition of its total slack into four
nonnegative combinatorial sources. This is a quantitative equality/stability
theorem for the product-side argument.

## Setup

Use the notation of `literature/steiner-reconstruction.md`. Let

- `k=γ(H)` and `R=ρ^{\{2\}}(G)`;
- `D` be a minimum dominating set of `G□H`;
- `D_i` be the part of `D` over the `i`th member of a partition of `V(H)`;
- `L_i⊆V(G)` be the set of vertically dominated `i`-cells.

For each `i`, define

```text
δ_i = |L_i|+R-3γ_G(L_i),
p_i = |D_i|-γ_G(V(G)\L_i),
d_i = γ_G(V(G)\L_i)+γ_G(L_i)-γ(G).
```

Also define the vertical-count slack

`v=|D|-Σ_i|L_i|`

and the total oriented product-bound slack

`E=4|D|-k(3γ(G)-R)`.

All are nonnegative:

- `δ_i≥0` is Steiner's subset Lemma 2.3;
- the projection of `D_i` dominates `V(G)\L_i`, so `p_i≥0`;
- the union of minimum dominators of `L_i` and its complement dominates `G`,
  so `d_i≥0`;
- Steiner's per-fibre count gives `Σ_i|L_i|≤|D|`, so `v≥0`.

## Exact identity

The slacks satisfy

`E = v + 3Σ_i(p_i+d_i) + Σ_iδ_i`.                              (1)

Indeed,

```text
3(p_i+d_i)+δ_i
  = 3|D_i|-3γ(G)+|L_i|+R.
```

Summing over `i` and adding `v=|D|-Σ_i|L_i|` gives (1).

This is an identity, not another inequality. It records every loss in
Steiner's proof of the oriented bound

`4γ(G□H)≥(3γ(G)-R)γ(H)`.

## Equality classification

Equality in the oriented product bound holds if and only if all of the
following hold:

1. `Σ_i|L_i|=|D|`;
2. `|D_i|=γ_G(V(G)\L_i)` for every `i`;
3. `γ(G)=γ_G(V(G)\L_i)+γ_G(L_i)` for every `i`;
4. `3γ_G(L_i)=|L_i|+R` for every `i`.

Condition 2 also forces the projection `P_G(D_i)` to be injective and to be
a minimum dominator of `V(G)\L_i`, because

`γ_G(V\L_i)≤|P_G(D_i)|≤|D_i|`.

Condition 4 invokes the complete recursive equality classification from
`angles/subset-slack`. Every two-sparse terminal remainder has the
odd-clique conflict decomposition from `angles/terminal-conflict`.

There is also a row-wise consequence of condition 1. For a fixed `g∈V(G)`,
let `m_g` be the number of vertically dominated cells and
`D_g=D∩({g}×V(H))`. Steiner proves `m_g≤|D_g|`; equality of the sums forces
`m_g=|D_g|` for every `g`. The `H`-projection of `D_g`, together with the
chosen partition centers `h_i` for the nonvertical cells, is then a
minimum dominating set of `H` of size `k`; the two contributions are
disjoint. Moreover, column projection injectivity gives
`|P_H(D_g)∩π_i|≤1` for every `i`, and for `i` with `g∈L_i`, the set
`P_H(D_g)\π_i` dominates all of `π_i`.

## Stability

Because the middle defects in (1) have coefficient three:

- if `E≤2`, then every `p_i=d_i=0`;
- in general, at most `⌊E/3⌋` indices can have a positive projection or
  partition-additivity defect;
- the remaining budget is exactly the vertical slack plus the sum of subset
  slacks, whose terminal portions count non-odd-clique conflict components.

Thus any sequence asymptotically approaching Steiner's oriented bound must
simultaneously approach:

- row-wise equality in the vertical-cell count;
- injective minimum projections in every column;
- exact additivity of domination across every `L_i` partition; and
- the recursive odd-clique terminal structure in every tight column.

## Verdict

Equation (1) is a genuine cross-proof stability result, but it does not yet
show that the four requirements are incompatible. The next viable attack is
to exploit their simultaneous row/column incidence structure. Treating any
one defect family in isolation is now known to be insufficient.
