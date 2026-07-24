# A corrected k=3 subset inequality

## Candidate

The formulas for `k=1` and `k=2` suggest

`γ_G(S) ≤ (|S|+ρ^{\{k\}}(G))/(k+1)`.

For `k=3` this would say

`4γ_G(S) ≤ |S|+ρ^{\{3\}}(G)`.                                  (K3)

The dense-neighborhood part of a hoped-for proof looks plausible: if a
closed neighborhood meets `S` in at least four vertices, delete those
vertices and add its center. The proof fails in the sparse terminal case,
and (K3) is false even when every closed neighborhood meets `S` in at most
two vertices.

## Exact counterexample

Let `V(G)={0,1,2,3,4}` and

`E(G)={01,03,04,12,14,23}`.

Take `S={2,3,4}`. The intersections `N[v]∩S`, for `v=0,...,4`, are

```text
{3,4}, {2,4}, {2,3}, {2,3}, {4}.
```

No vertex dominates all of `S`, while `{0,1}` does, so `γ_G(S)=2`.

The weights `(0,0,1,1,2)` form a 3-packing function of total weight 4, so
`ρ^{\{3\}}(G)≥4`. Conversely, if a 3-packing function had total weight
`W≥5`, the constraints on `N[0]` and `N[1]` would force respectively
`w_2≥2` and `w_3≥2`; then the constraint on `N[2]={1,2,3}` would be
violated. Hence `ρ^{\{3\}}(G)=4`.

Thus (K3) asserts `8≤3+4=7`, a contradiction.

The harness checks this example using exact integer enumeration. The failure
shows that the `k=2` matching/König mechanism does not extrapolate by merely
raising the local capacity.

## A valid replacement

There is nevertheless a uniform `k=3` inequality:

`5γ_G(S) ≤ 2|S|+ρ^{\{3\}}(G)`.                                 (K3′)

Put `r=ρ_G(S)`, `R=ρ^{\{2\}}(G)`, and `P=ρ^{\{3\}}(G)`.
Steiner's Lemma 2.3 and his matching Lemma 2.2 give

`3γ_G(S)≤|S|+R`, and `2γ_G(S)≤|S|+r`.

The indicator of a maximum two-packing contained in `S` is a 1-packing
function on `G`. Adding it to an optimal 2-packing function produces a
3-packing function, so `P≥R+r`. Adding the displayed subset inequalities
therefore proves (K3′).

The five-vertex counterexample to (K3) is equality in (K3′):
`5·2=2·3+4`.

The exact defect identity is also useful:

```text
2|S|+P-5γ_G(S)
  = (|S|+R-3γ_G(S))
  + (|S|+r-2γ_G(S))
  + (P-R-r).
```

All three terms are nonnegative. Thus improving (K3′) in the relevant fibre
family means ruling out their simultaneous near-equality.

Substituting (K3′) for the subset bound in Steiner's fibre argument gives

`γ(G□H) ≥ ((5γ(G)-ρ^{\{3\}}(G))/7)γ(H)`,                       (P3)

and symmetrically with `G,H` exchanged.

## Exact global reoptimization verdict

The new theorem does **not** improve the universal 0.5643 constant when merely
added to Steiner's existing inequalities. Normalize

`x₁=ρ/γ`, `x₂=ρ²/(2γ)`, `x₃=ρ³/(3γ)`.

Superadditivity above gives `3x₃≥2x₂+x₁`. At Steiner's exact relaxed
minimizer, let

`c=(5+√73)/24`,
`a=2-3c`, `b=3/2-2c`,

and set `x₁=y₁=a`, `x₂=y₂=b`,
`x₃=y₃=d=(2b+a)/3=(85-7√73)/72`. This is feasible and saturates
the new packing relation.
The normalized (P3) term is

`5/7-3d/7=(5-2b-a)/7=c`.

The corresponding Hou–Lu `k=3` mixed term is
`a+d(1-a)<a+b(1-a)=c`, because `a<d<b`. All six original Steiner terms
already equal `c`. Hence the enlarged relaxed minimax still has exact value
`c`; numerical optimization without another combinatorial constraint is a
dead end.

**Verdict:** (K3′) and (P3) are rigorous new inequalities, but they need a
new structural relation stronger than `ρ³≥ρ²+ρ` to improve the global
constant.
