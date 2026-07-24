# Isolation-to-escape charging

## Status

**Exact product-specific charging lemma proved and independently audited by
GPT-5.6 Sol at xhigh effort.** Fibre isolation is now split quantitatively into three outcomes:
a labelled private-corner escape obligation, a same-label collision, or
cross-coordinate redundancy. The lemma is exact on the `C₅□C₅` and
`K₂□P₃` perfect codes.

This is the missing bridge between the scalar partial-cover defect identity
and the private-corner dynamics. It does not yet close escape paths into a
positive density of cycles.

## Definitions

Let `D⊆V(G)×V(H)` be a product dominating set. Write

```text
A_g={h:(g,h)∈D},
B_h={g:(g,h)∈D},
V_x=⋃_{g∈N_G(x)}A_g.
```

For the `G→H` orientation, let `I_G` be the set of selected points
`(g,h)∈D` for which `g` is isolated in the induced graph `G[B_h]`.
Equivalently, `(g,h)` has no same-label selected neighbor in the
`G`-direction.

Put

```text
r_{x,h}=|N_G(x)∩B_h|,
Ω_G=Σ_{x,h}(r_{x,h}-1)_+,
X_H=Σ_x|V_x∩N_H[A_x]|.
```

Here `Ω_G` counts repeated same-label horizontal imports, while `X_H`
counts imported labels that are redundantly covered inside their arrival
row.

Let `Bad_G⊆I_G` consist of points with no horizontal external-private
neighbor.

## One-oriented charging lemma

If `G` has no isolated vertices, then

`|Bad_G|≤2Ω_G+X_H`.                                         (1)

For each bad `(g,h)`, choose one neighbor `x` of `g`. Since `(x,h)` is
not private to `(g,h)`, it has another dominator.

If `r_{x,h}≥2`, charge the owner to the collision `(x,h)`. At most
`r_{x,h}` isolated same-label owners can choose this target, and

`r≤2(r-1)` for `r≥2`.

If `r_{x,h}=1`, the other dominator cannot have label `h`; it must be a
point `(x,z)` in row `x`, with `z∈N_H[h]`. Therefore

`h∈V_x∩N_H[A_x]`.

Only the unique same-label owner can charge this cross label. Summing the
two cases proves (1). The coefficient two is necessary when two isolated
same-label owners share one target.

## Exact relation to partial-cover slack

Let `a_x=|A_x|` and use the near-cover profile

`u_H(t)=min_{|C|≤t}|V(H)\N_H[C]|`.

Define

```text
R_H=Σ_x(|V_x|-u_H(a_x)),
e_H(A_x)=|H|-u_H(a_x)-|N_H[A_x]|.
```

Since `D` really dominates the product,

`H\N_H[A_x]⊆V_x`.

Consequently

`X_H=R_H-Σ_x e_H(A_x)`.                                     (2)

For a merely typed-feasible set, the exact correction is

```text
X_H
 =R_H-Σ_xe_H(A_x)
  +Σ_x|(H\V_x)\N_H[A_x]|.                                  (3)
```

Thus the genuinely missed product cells are precisely the obstruction to
extending the escape charge from actual domination to the typed
relaxation.

## Two-oriented consequence

Assume also that `H` has no isolated vertices. Define
`I_H,Ω_H,X_G,Bad_H` symmetrically. Let `T⊆D` be the points that
are fibre-isolated in both directions and have external private neighbors
in both directions. Inclusion--exclusion and (1) give

```text
|T|≥[
 I_G+I_H-|D|
 -2Ω_G-2Ω_H-X_H-X_G
]_+.                                                        (4)
```

Every point of `T` has a labelled private-corner escape owner at an exact
mixed `(1,2)` or `(2,1)` move, by the theorem in
`../corner-dynamics/README.md`.

Equation (4) is a density theorem for escape obligations. It is stronger
than the previous statement that formal equality gives at least one escape
cycle.

## Sharp examples

1. For the perfect code in `C₅□C₅`,

   ```text
   I_G=I_H=5,
   Ω_G=Ω_H=X_G=X_H=0.
   ```

   Equation (4) forces all five selected points into `T`; their obligations
   form the known labelled 5-cycle.
2. For `D={(0,0),(1,2)}⊂K₂□P₃`, both isolation counts equal two and
   all four energy terms vanish. Equation (4) forces the sharp escape
   2-cycle.
3. The diagonal minimum dominator of `K₂□K₂` has both points isolated in
   both fibres, but `X_G=X_H=2`. Neither point has an external-private
   neighbor. Thus the cross-redundancy subtraction is indispensable.
4. The diagonal typed witness in `C₄□C₄` is not a product dominator.
   Its genuinely missed cells appear exactly as the final term in (3),
   preventing a false escape conclusion.

## Remaining obstruction

Many points in `T` need not give many cycles: an escape owner may lie
outside `T`, and a functional digraph can have long in-trees feeding a
single cycle. The next theorem must prove one of:

1. a positive fraction of escape owners remain inside `T`;
2. bounded labelled escape-path length before returning to `T`; or
3. every departure from `T` charges new collision, cross-redundancy, or
   one of the exact Steiner defects.

**GO** for a closure/path-length lemma using the red-diagonal,
blue-cross-zero transition rule. **STOP** for counting isolation without
subtracting `Ω` and `X`.
