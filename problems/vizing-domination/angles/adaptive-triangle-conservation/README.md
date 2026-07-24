# Adaptive triangle credit and compatibility

## Status

**Exact atom-credit identity proved; a balanced exact obstruction kills the
naive target-packing bridge.** Adaptive Hall matching makes the base credit
perfectly conservative. A triangle supplies a local repair-energy unit, but
charging its distinguished selected point as an additional global unit
double-counts a point already saturated by the Hall bijection.

This is a proof-method STOP, not a theorem that no new cross-atom triangle
inequality can exist.

## Exact atom credit

Let `C⊆L_i` be a terminal atom. For each `g∈C`, use the adaptive Hall
provider `μ_g(i)` and choose

`y_g∈π_i∩N_H[μ_g(i)]`.

Put

```text
p_C=(1/|C|)Σ_{g∈C}δ_{y_g},
q_C=δ_g                       for C=K₁,
q_C=(1/2)1_C                 for C=K₃.
```

Then `p_C` is a fractional packing of total one, while `q_C` is the
canonical atom packing. Allocate the product term `PQ` sourcewise as `q_g`
to the matched provider. Since the provider lies outside the source cell,
`p_C(μ_g(i))=0`, and its assigned overlap-ledger contribution is `1-q_g`.
Every provider therefore receives exactly

`q_g+(1-q_g)=1`.                                             (1)

For a singleton, the total is one. For a triangle, the two ledgers each
contribute `3/2`, for a total of three. Summed over all atoms, (1) is exactly

`Σ_i|L_i|=|D|-v`.

At `v=0`, the Hall map is a bijection and every selected point is saturated
once.

## The tempting triangle surplus

Under the full atomic/additive external-private hypotheses, a triangle
`T⊆L_i` has a distinct selected point `d_T=(r,a)∈D_i`. For
`p=δ_a`, `q=(1/2)1_T`, an external private target of `d_T` lies in the
column repair set `D_a`. Hence `q(D_a)=0` and `γ_G(D_a)≥1`, giving one
unit of local repair energy.

It is invalid to add that unit by charging `d_T` again: at `v=0`, (1)
already assigns exactly one base unit to that point. This identifies the
precise double charge in the naive proof.

It does **not** rule out a structural inequality of the form
`M≥|D|+τ`. Such an inequality would need a genuinely cross-atom argument
showing that the repair energy cannot circulate along the Hall cycles.
Merely invoking the bijection is only a no-go for unit-capacity charging.

Formally, adding one valid unit per triangle would beat Steiner by

`(√73-7)/12>0`,

so this remains a mathematically meaningful bridge rather than a negligible
optimization tweak.

## Balanced obstruction to adaptive target packing

Let `H` have vertices `0,...,10` and edges

```text
03,05,07,08,09,12,13,19,28,24,36,39,45,58,59,5·10,68,69,89.
```

It has domination number four with centers `(0,5,8,9)` and cells

```text
π₀={3,7,8},  π₁={4,9,10},  π₂={2,5,6},  π₃={0,1}.
```

One row exchange has outgoing cells `{2,3}` and selected coordinates
`{3,4}`. The injective Hall assignment is forced to use provider `4` for
`π₂` and provider `3` for `π₃`, giving transitions `2→1` and `3→0`.
The available adaptive targets are respectively

```text
N[4]∩π₂={2,5},       N[3]∩π₃={0,1}.
```

Every cross-pair has intersecting closed neighborhoods, so no choice is a
two-packing. The reciprocal exchange with outgoing cells `{0,1}` and
providers `{0,5}` gives transitions `0→3` and `1→2`. Thus the cell
transitions are balanced Eulerian 2-cycles, yet the first exchange still
has no compatible two-packing of adaptive targets.

The harness checks the graph, partition, exchanges, and all target conflicts
exactly. This is not itself a product-dominator counterexample: a theorem
may still exploit external-private coordinates and the full projection
defect package. It does show that row exchange, minimal cells, adaptive Hall
matching, and Eulerian balance alone are insufficient.

## Verdict

The surviving triangle attack must use one of:

1. a cross-atom inequality that prevents local repair energy from circulating
   on Hall cycles;
2. the neutral-core coordinate tax from
   `angles/neutral-core-coordinate-tax`; or
3. a defect-weighted theorem tying private targets to their complete joint
   dependency regions.

Do not claim a packing of adaptive targets from Hall matching alone.
