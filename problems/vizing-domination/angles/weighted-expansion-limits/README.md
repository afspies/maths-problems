# Weighted expansion and cap-half limits

## Status

**Two exact structural consequences proved, followed by sharp no-go
constructions.** At full equality, averaging the canonical fibre packings
produces a maximum fractional packing with point cap `1/2`. Local weighted
provider cuts also retain row labels. Neither fact has enough universal
numerical leverage: the cap tensor lies far below Steiner, and connected
true-twin reservoirs absorb every nonnegative row weighting while preserving
the singleton equality skeleton.

## The cap-half packing

At full equality, let `f_i` be the canonical optimal integral 2-packing
supported on `L_i`, and put

`p_i=f_i/2`,       `p̄=k^{-1}Σ_i p_i`.

Then `p̄` is a maximum fractional packing of total `R/2`. Moreover,
`p_i(g)≤1_{g∈L_i}`. If

```text
I_g={i:g∈L_i},       S_g={i:g∈X_i},
```

row balance and column separation give

`|I_g|=|S_g|` and `I_g∩S_g=∅`.

Therefore `|I_g|≤k/2`, and

`0≤p̄(g)≤1/2` for every `g`.                                 (1)

Applying the best cap-only rank-one tensor in both factors at the formal
value `b=R/(2Γ)` gives only

```text
(4/3)b²=(121-13√73)/54≈0.18385,
c-(4/3)b²=(61√73-439)/216>0.                                (2)
```

Thus (1) is genuine equality structure but is quantitatively much weaker
than `c`.

## Connected reservoir for weighted cuts

Start with `C₄` on cyclic vertices `0,1,2,3` and replace vertex `0` by a
clique `Q` of `m` true twins. Each clone is adjacent to `1,3`, and the edges
`12,23` remain. The resulting connected graph has exactly

`(γ,ρ,ρ²)=(2,1,2)`.

It admits the two tight singleton states

```text
L={1}, X={3},       and       L={3}, X={1}.
```

Both are additive, separated, and have the same external private target
`2`. Use equally many cells of the two states. Rows `1,3` have balanced
blue/red degree `k/2`; `Q` and row `2` are neutral. For every nonnegative
row weighting `λ`, the nonzero part of the local provider cut reduces to

`(k/2)(λ₁+λ₃)≤ρ(H)(m+1)max(λ₁,λ₃)`.                         (3)

At the formal value `ρ(H)=ak`, (3) holds whenever `a(m+1)≥1`, in
particular for `m≥3`, and becomes arbitrarily slack as `m` grows.

This is an equality skeleton, not an actual near-`c` product dominator. It
proves the narrower no-go: neighborhood-cardinality cuts, even optimized
over arbitrary nonnegative row weights, cannot improve the constant from
the enumerated factor and incidence data alone. Neutral true twins absorb
the right-hand side without changing those data.

## Verdict

Further scalarization of the adaptive local cuts is a **STOP**. Any useful
expansion theorem must distinguish actual product coordinates, terminal
triangle supports, or the hard neutral cores from
`angles/neutral-core-coordinate-tax`.
