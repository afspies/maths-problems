# Joint-dependency stability

## Status

**Proved exact defect-weighted subset lemma; independently audited at
GPT-5.6 Sol xhigh effort.** The result controls whole regions that jointly
depend on a subset of a complement dominator. A common-crown construction
shows that it cannot by itself make arbitrarily chosen private targets into
a packing.

## The lemma

Let `L⊆V(G)`, put `T=V(G)\L`, and let `X` dominate `T`. Define

```text
e=|X|-γ_G(T),
d=γ_G(T)+γ_G(L)-γ(G).
```

For `S⊆X`, define the joint-dependency region

`C_X(S)={v∈T: ∅≠N[v]∩X⊆S}`.

Then

`|S|-γ_G(C_X(S))≤e+d`.                                      (1)

In particular, if `X` is a minimum dominator of `T` and domination is
additive across `L,T`, then

`γ_G(C_X(S))=|S|` for every `S⊆X`.                           (2)

### Proof

Let `Q` be a minimum dominator of `C_X(S)`. Every vertex of
`T\C_X(S)` that is dominated by `X` has an `X`-neighbor outside `S`.
Therefore `(X\S)∪Q` dominates `T`. Adding a minimum dominator of `L`
dominates `G`, so

```text
γ(G)≤|X|-|S|+γ_G(C_X(S))+γ_G(L).
```

Rearranging and substituting the definitions of `e,d` proves (1). Since
`S` itself dominates `C_X(S)`, the reverse inequality in the zero-defect
case proves (2).

For a Steiner column, `X_i=P_G(D_i)` dominates `V(G)\L_i`, and its excess
over a minimum complement dominator is at most `p_i`. Thus the dependency
deficit is bounded exactly by `p_i+d_i`.

## Why this does not solve target compatibility

Equation (2) controls the entire region `C_X(S)`, not one selected private
target per member of `S`. In common-crown graphs, `e=d=0` while external
private targets chosen for different members of `X` can all lie in one
closed neighborhood. The rest of each dependency region carries the
domination burden required by (2).

Thus it is invalid to infer that a system of private targets is a
two-packing, or even that its domination number is `|S|`. A successful
triangle bridge must connect the chosen target coordinates to the full
dependency regions, or use the Cartesian-product coordinate tax directly.
