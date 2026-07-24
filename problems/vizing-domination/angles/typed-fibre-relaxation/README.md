# Typed fibre-set relaxation

## Status

**Exact labelled relaxation with three new product-specific bridges;
universal value open.** This is the minimal information that the zero-factor combined LP
discarded: a coordinate imported from a neighboring row covers only that
coordinate, while a coordinate owned in the row covers its entire closed
neighborhood.

No improved universal constant is claimed. The mandatory asymmetric and
comparable-scale robust Cayley tests are now passed by the partial-cover
profile theorem in `../typed-partial-cover/`.

## Exact row condition

Let `D⊆V(G□H)` and write its actual row fibres as

`A_g={h:(g,h)∈D}`.

The labels imported horizontally into row `g` are

`V_g=⋃_{x∈N_G(g)}A_x`,                                      (1)

where `N_G(g)` is the open neighborhood. The set `D` dominates `G□H` if
and only if, for every row,

`V(H)\V_g⊆N_H[A_g]`.                                        (2)

Indeed, a point `(g,h)` is dominated horizontally precisely when
`h∈V_g`; otherwise it must be dominated by an owned point
`(g,a)` with `a∈N_H[h]`.

Taking subset-domination numbers in (2) gives the exact necessary
inequality

`|A_g|≥γ_H(V(H)\V_g)`.                                      (3)

Consequently every product dominator satisfies

`|D|=Σ_g|A_g|≥Σ_gγ_H(V(H)\V_g)`.                             (4)

There is a symmetric column condition obtained from

`B_h={g:(g,h)∈D}`.

## Cardinality relaxation

Define `Θ(G,H)` by minimizing `Σ_g|A_g|` over set systems
`A_g⊆V(H)`, with derived column sets `B_h`, subject to (3) in every row and
its symmetric counterpart in every column. Then

`γ(G□H)≥Θ(G,H)`.                                             (5)

The containment version (2) is exactly product domination and would be
tautological. The cardinality version (3) is a strict relaxation: it retains
which labels are imported, but forgets whether the owned labels actually
form the required subset dominator.

Unlike the combined blocker/packing LP, `Θ` cannot be symmetrized merely to
owner marginals without changing its definition. Its variables are the
actual correlated label sets.

## Two universal baselines

Write `a_g=|A_g|`. Since

```text
γ(H)
≤γ_H(V(H)\V_g)+|V_g|
≤a_g+Σ_{x∈N_G(g)}a_x,
```

the integer row-mass vector `a` is a `γ(H)`-dominating function on `G`.
Therefore

`Θ(G,H)≥γ^{\{γ(H)\}}(G)`,                                   (6)

and symmetrically

`Θ(G,H)≥γ^{\{γ(G)\}}(H)`.                                   (7)

There is also a direct repair theorem. For a typed-feasible set system,
let

`M_g=(V(H)\V_g)\N_H[A_g]`

be the labels that are still genuinely missed in row `g`. Feasibility gives

`γ_H(M_g)≤γ_H(V(H)\V_g)≤|A_g|`.

Add a minimum dominator of `M_g` inside row `g`, independently for every
row. All previously missed product vertices are then dominated, so

```text
γ(G□H)
≤Σ_g|A_g|+Σ_gγ_H(M_g)
≤2Σ_g|A_g|.
```

Taking the typed minimum yields

`Θ(G,H)≥γ(G□H)/2≥(c/2)γ(G)γ(H)`.                            (8)

Thus `Θ` retains a positive universal factor, unlike `Λ` and `Ξ`.

The missed-set correction

`χ_H(A)=Σ_gγ_H(M_g)`

and its column analogue are exact intermediate defect parameters:

`γ(G□H)≤|A|+min{χ_H(A),χ_G(A)}`.                             (9)

Any escape-label strengthening should track the repair owners of the missed
sets, because private-corner dynamics only exists once those sets vanish.

## Subsequent exact bridges

Three later theorems make the labels quantitatively useful.

1. The near-cover profiles

   `u_K(t)=min_{|C|≤t}|V(K)\N_K[C]|`

   satisfy, for every typed set,

   `Σ_g u_H(|A_g|)+Σ_hu_G(|B_h|)≤|G||H|`.

   The proof has an exact defect identity whose final terms count isolated
   induced fibres. Robust random Cayley graphs force this profile bound far
   above `γ(G)γ(H)` at all growing pairs of scales.
2. For fractional packings `q,p`, the exact correlated inequality is

   ```text
   |A|≥PQ+Σ_A(1-q_g)(1-p_h)+max{E_H,E_G},
   E_H=Σ_gq_g[γ_H(H\V_g)-p(H\V_g)],
   ```

   with a symmetric definition of `E_G`. For half-integral 2-packings every
   nonzero repair gap costs at least one half.
3. For an actual product dominator, isolated fibres are charged to
   external-private escape obligations, repeated same-label imports, or
   cross-coordinate redundancy. This produces a quantitative lower bound
   on the number of points carrying the labelled mixed-distance escape rule.

See `../typed-partial-cover/`, `../typed-fractional-charging/`, and
`../isolation-escape-charging/`.

## Strictness

The relaxation is genuinely weaker than product domination. Let
`G=H=K₂⊔K₁`, with edge vertices `0,1` and isolate `2`, and take

`D={(0,2),(1,2),(2,0),(2,1)}`.

All row and column cardinality conditions hold with total four: each edge
row imports the isolate label and owns one label, while the isolate row owns
two labels. But `D` misses product cells. In fact

`γ((K₂⊔K₁)□(K₂⊔K₁))=5`,

because the product components are `C₄,K₂,K₂,K₁`. Hence containment (2)
cannot be recovered from cardinalities alone.

## Escape compatibility

At two-sided external-private equality, every point `(g,h)∈D` also has an
escape owner at exact Cartesian distance three: either a `(1,2)` or `(2,1)`
knight move. Thus a strengthened typed relaxation may add the labelled
red-diagonal/blue-cross-zero transition rules from
`../corner-dynamics/README.md`.

The distance-three statement is sharp. In `K₂□P₃`,

`D={(0,0),(1,2)}`

is a perfect dominating set, and the two points form a directed escape
2-cycle. Hence no universal lower bound on escape-cycle length is available.

## Verdict

**GO — primary labelled candidate.** The strongest target

`Θ(G,H)≥γ(G)γ(H)`                                            (10)

would imply Vizing's conjecture and is not claimed. The Cayley benchmark is
now cleared. The remaining hard tests are:

1. the connected formal-ratio safe-port family;
2. `K₂□P₃` and `C₅□C₅`, which realize the shortest and odd escape cycles;
3. typed systems in which the profile slack is concentrated entirely in
   isolated fibres.

The immediate theorem-shaped target is no longer a better repair factor.
It is to combine the quantized fractional repair energies with the fixed
`K₁/K₃` terminal atoms, or to prove a closure/path-length theorem for the
dense set of labelled escape obligations. Finite instances may falsify
proposed strengthenings but are not evidence for the conjecture.
