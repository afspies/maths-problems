# Handoff — Vizing’s domination conjecture

Read these session-five notes first:

- `angles/anchored-domination/README.md`
- `angles/bidirectional-blocker/README.md`
- `angles/combined-blocker-packing/README.md`
- `angles/cross-row-hole-packing/README.md`
- `angles/corner-dynamics/README.md`
- `angles/external-private-holes/README.md`

## Critical correction

For a fractional packing `q` on `H`, write `Q=Σq` and

`Δ_H(q)=min_{T dominates H}Σ_{t∈T}[1-q(N[t])]`.

Then exactly

```text
Δ_H(q)=γ(H)-Q-Ω_H(q),
Ω_H(q)=max_T[
  Σ_xq_x(|T∩N[x]|-1)-(|T|-γ(H))
]≥0.
```

Hence `Δ_H(q)≤γ(H)-Q`. The canonical half-2-packing at the formal ratios
can meet Steiner only when this inequality is equality; it can never improve
the constant. Do not reuse the session-four “deficit above threshold”
language.

## What is now proved

1. The optimized valid slice

   `F_a(H)=max_q[Q+aΔ_H(q)]`

   has an optimistic anchored fractional-domination dual. On the augmented
   uniform split graph,

   `F_a(S_{2k,z})=z+max{2,a(k+1)}`,

   and `F_a(C₅)=5/3`, `F_a(L(K₇))=21/11`.
2. Formal-ratio `C₅,S₂₆,₂,S₂₈,₂` mixtures have

   `F_a/γ→(1273-115√73)/576≈0.504235<c`.

   Thus optimizing the saturation-defect slice is a STOP.
3. The capped packing profile

   `Φ_H(t)=max{Σp:p fractional packing, p_v≤t}`

   gives

   `γ_f(G□H)≥Φ_G(s)Φ_H(t)/(s+t)`.

   For `S_{2k,z}`, with `M=binom(2k-1,k-1)`, the profile is exactly

   ```text
   (2M+2k+2z)t,
   1+(M+z)t,
   2+zt
   ```

   on the three consecutive intervals cut by
   `1/(M+2k+z)` and `1/M`.
4. There are finite additive pairs approaching `(a,b)` in both factors for
   which both `F_a` arms and the independently optimized capped tensor remain
   below `c`. The first factor is a bounded
   `C₅/S₂₆,₂/S₂₈,₂` mixture; the second is an
   `L(K₇)/S_{2k,z_k}` mixture. The limiting cap arm is at most

   `(-247+37√73)/264≈0.261849`.

   The exact split profile makes the finite all-caps argument uniform.
5. A natural two-sided ordinary-packing slice of the full blocker is also a
   STOP. If `U=N[P]` contains a minimum dominator, then

   `κ_G(s;U)=min_T(|T\U|+s|T∩U|)=sγ(G)`.

   This holds on all cycle/split components in the counterfamily, reducing
   the slice to the ordinary packing ratio `a`.
6. Row hole two-packings tensor with any fractional factor packing:

   `Σ_y p_y|P_y|≤γ_f(G□H)≤|D|`.

   The common-crown construction makes all external target rows lie in one
   closed neighborhood, so factor-weighted density alone can lose an
   arbitrary factor. Under full formal balance, a common neighborhood
   `Y⊆N[w]` satisfies

   `M(Y)≤2γ(H)ρ(H)+sd`,

   where `s` is the number of singleton terminal cells and `d=|L_i|`.
   This coefficient is presently vacuous at comparable formal scales.
7. If every `d∈D` has external private neighbors in both directions, its
   corner is owned by another point of `D`. Choosing one owner per corner
   creates a directed cycle. Every arc is an edge move in one factor and a
   distance-two move in the other. Full two-oriented formal equality forces
   this hypothesis; the `C₅□C₅` perfect code realizes the directed cycle
   sharply. At exact equality, an owner `(x,z)` has type-`(1,2)` indegree at
   most

   `min{|J_x|,ρ_H(N₂(z)),deg_H(z)}≤ρ(H)`,

   and symmetrically. Every arc also forces a red-diagonal/blue-cross-zero
   pattern in the cell matrices.

## Best next attacks

### A. Do not continue the combined dual

The shared-capacity lift `Ξ` combines a genuine fractional product packing
with the full bidirectional blocker. Its exact dual minimizes the mass of a
product fractional dominator `d` that simultaneously routes, for every
factor vertex, the incidence marginals of a probability distribution over
integral dominators of the other factor.

It has zero universal factor. Bollobás--Janson--Riordan translate covers in
elementary abelian 2-groups give connected vertex-transitive Cayley graphs
with unbounded neighborhood-covering multiplicity. Taking the two factor
scales very different makes every exact transitive `Ξ` term tend to zero.
This is a hard STOP, not an open bridge.

### B. Quantitative escape cycles

Use the exact Steiner defect budget to show either:

- a positive density of points has two-sided external privacy and belongs to
  controlled escape cycles; or
- failures charge positive terminal-capacity, additivity, or row slack.

Mere cycle existence is insufficient. Any useful count must use the fixed
`K₁/K₃` atoms or the alternating occupied/vertical row exchanges.

The typed fibre-set relaxation is the cleanest current container. For actual
row label sets `A_g` and open-neighborhood imports
`V_g=⋃_{x∈N(g)}A_x`, product domination implies

`|A_g|≥γ_H(V(H)\V_g)`

in every row, plus the symmetric column inequalities. This keeps the exact
labels discarded by `Ξ`. Its universal value is uncalibrated: test it first
on the asymmetric translate-cover Cayley pair.

### C. Successor-relaxation benchmark

Any new relaxation must be tested against the asymmetric translate-cover
Cayley pair. It must use actual labelled fibre incidences of one product
dominator, because product fractional domination plus owner-indexed averaged
factor dominators has already lost every positive constant.

## Hard stops

- No numerical reoptimization of Steiner's six existing inequalities.
- No additive integer packing levels.
- No canonical or optimized saturation-defect campaign.
- No shared-cap or independent-cap rank-one dichotomy.
- No row-hole weighting that ignores owner labels.
- No ordinary-packing residual slice of `Λ`.
- No full `Λ` or combined `Ξ` campaign; both have zero universal factor.
- No bare corner contradiction; `C₅□C₅` cycles it exactly.
- Finite tests are hygiene and falsification, never evidence for the
  universal conjecture.

Any proposed proof requires a fresh independent GPT-5.6 Sol xhigh review.
