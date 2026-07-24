# Handoff — Vizing’s domination conjecture

Read these session-seven notes first:

- `angles/overlap-tax/README.md`
- `angles/provider-nonreuse/README.md`
- `angles/adaptive-provider-cycles/README.md`
- `angles/escape-realization/README.md`
- `angles/factor-invariant-calibration/README.md`
- `angles/incidence-balance/README.md`
- `angles/external-private-holes/README.md`
- `angles/fibre-slack/README.md`

The best universal constant remains

`c=(5+√73)/24≈0.5643`.

The withdrawn `0.5809` claim is not a theorem and was not used.

## Decisive session-seven results

### 1. Corrected two-direction repair ledger

For typed-feasible `A`, factor fractional packings `q,p`, and the notation
of `angles/typed-fractional-charging`, retain

```text
α_H=Σ_gq_g(|A_g|-γ_H(C_g)),
α_G=Σ_hp_h(|B_h|-γ_G(D_h)).
```

Then

```text
|A|≥PQ+Z+max{E_H+α_H,E_G+α_G}.                              (1)
```

The `α` terms cannot be discarded: a minimum dominator of `P₃□P₃` makes
(1) sharp with `E_H=E_G=0` and `α_H=1`.

Let `I` be the selected cells isolated from both open-coordinate import
systems, `J` the cells imported in both directions, and put

`K=w(A\I)+w(J)`.

For an actual product dominator,

```text
|A|=PQ+Z+E_H+E_G+α_H+α_G-K,                                (2)
E_H+E_G+α_H+α_G=2K+R+Δ,                                    (3)
```

where `R` counts repeated same-direction owners and `Δ` is factor-packing
load slack. These identities explain exactly why the two repair energies
cannot be added. Minimum dominators of `K₂□K₂` and `P₃□P₃` make the scalar
bound sharp.

### 2. Generic escape closure is a hard STOP

At zero isolation/collision/cross-redundancy defect, the dominator is a
perfect code and its mixed escape relation is undirected.

Every finite bipartite graph `F` without isolated vertices is realized as
such an escape graph: subdivide every edge of `F`, take the product with
`K₂`, and place codewords from the two parts in opposite rows. Subdivided
stars have cyclic fraction `2/(k+1)→0` and only one unit of Vizing surplus;
paths have arbitrarily long in-trees.

Therefore no generic cycle-density, bounded-return, matching, or
`ε|T|`-credit theorem can follow from the present escape defects. Any
surviving dynamic theorem must use the indexed Steiner fibres themselves.

### 3. Factor-invariant relations cannot cut the optimizer

For every fixed `L`, there are finite graphs with

```text
γ>L,       ρ=1,       ρ^{\{2\}}=2.
```

A direct `G(n,1/2)` union bound proves this. Mixing these graphs with
isolated vertices and `C₅` components in exact domination-mass proportions

```text
c=(5+√73)/24,
t=(47-5√73)/24,
s=(√73-7)/6
```

makes

```text
ρ/γ→a=(11-√73)/8,
ρ²/(2γ)→b=(13-√73)/12.
```

Thus Steiner's formal minimizer is a limit of actual graph invariants.
Relations using only `γ,ρ,ρ²` are a hard STOP, including stronger scalar
packing hierarchies or connectedness-free realizability objections.

### 4. Provider reuse is Hall deficiency, but indexed atoms do not control it

For a fixed row, form the provider graph from indexed demands to selected
row labels. Reuse is exactly

```text
|I|-ν(P)=max_{J⊆I}(|J|-|N(J)|).                             (4)
```

The external-private theorem makes incoming holes indexed by `J_g` a
two-packing. Terminal triangle demands are indexed by outgoing cells
`I_g`. There is no proved coordinate-preserving map between them.

An explicit actual dominator of `C₅□H_m` has:

- exact terminal `K₃` fibres;
- globally optimal canonical 2-packings;
- exact minimum row exchanges; and
- one selected point serving all `m` indexed demands.

The natural per-index overlap tax is zero. The example has linear exact
Steiner defects, so it does not refute a theorem using the full defect
package. It does prove that terminal atoms, optimality, and row exchange
alone are insufficient.

### 5. The constant requirement is severe

At the formal ratios, even disjoint row and column triangle credits yield
only

`b²+2b(b-a)=(13-√73)/24≈0.18567<c`.

Starting from `b²`, the required number of independently additive copies is

```text
N>(c-b²)/(b(b-a))
 =(249+21√73)/24
 ≈17.851.
```

A useful bridge must therefore create at least eighteen-fold effective
amplification. A one- or two-direction local improvement cannot move the
universal constant.

### 6. Adaptive providers do match perfectly

The fixed-demand obstruction has a universal adaptive counterpart. For
every row `g`, Hall's theorem gives an injection

```text
μ_g:I_g→A_g,
μ_g(i)∉π_i,
N_H[μ_g(i)]∩π_i≠∅.
```

The matching chooses the target inside `π_i` after choosing its distinct
provider. Globally it leaves exactly

`v=|D|-Σ_i|L_i|`

selected points unused. At `v=0` and column equality, its loopless cell
transitions form an Eulerian labelled digraph. Under the full
external-private hypotheses, they transfer injectively to singleton holes
and give, for every row set `U`,

```text
Σ_{g∈U}|I_g|
≤ρ(H)|N_G(U)|+2Σ_{x∈N_G(U)}e_x.
```

This theorem survives the `C₅□H_m` obstruction by choosing `t_i` with
provider `a_i`; it does not match the pre-prescribed `s_i`. Its
triangle-only scalar consequence is weaker than the old all-incidence
bound, so there is still no constant improvement.

## Only live attack

Work on the adaptive labelled cycles from
`angles/adaptive-provider-cycles`, retaining all coordinates. The target is
compatibility with the triangle-energy witness:

1. choose the point in each terminal triangle so it is both detected by the
   parity/repair energy and adjacent to the matched distinct provider;
2. use the local expansion cuts before aggregating, and prove that every
   failure of external-private transport consumes a quantified unit of
   `v`, `p_i`, `d_i`, or `δ_i`;
3. aggregate the resulting credit at product scale; and
4. calculate the coefficient before investing in a long proof, because
   less than eighteen-fold basic triangle credit cannot beat Steiner.

The alternative is a genuinely high-rank labelled dual whose constraints
couple the fibre indices before taking factor marginals. It must be tested
against both the `C₅□H_m` provider obstruction and the actual
factor-invariant mixture.

## Hard stops

- No numerical reoptimization of Steiner's six inequalities.
- No relation using only `γ,ρ,ρ²` or the additive packing hierarchy.
- No generic escape closure, positive cycle density, or bounded path length.
- No local `K₁/K₃` parity theorem or per-index rank-one overlap tax.
- No provider non-reuse theorem that ignores `v,p_i,d_i,δ_i`.
- No cap, saturation-defect, anchored, or ordinary-packing residual slice.
- No unrestricted square-clique or owner-averaged factor LP.
- Finite verification remains hygiene and falsification only.

Any proposed defect-weighted Hall or high-rank labelled theorem requires a
fresh independent GPT-5.6 Sol xhigh audit.
