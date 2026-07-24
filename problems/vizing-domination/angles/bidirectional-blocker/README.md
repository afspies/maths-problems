# Bidirectional weighted-domination blocker lift

## Status

**Valid exact product bound, with exact universal obstructions.** This
genuinely nonseparable lift uses all weighted integral domination
inequalities of both factors. It certifies Vizing exactly for every
`G□P₄`, surviving both the split-graph and triangular-line-graph obstructions
to earlier fractional relaxations. Vertex-transitive line graphs show that
the standalone lift still tends to the Clark–Suen factor `1/2`.

The theorem and obstruction were proposed by GPT-5.6 Sol at xhigh effort and
independently adversarially accepted. Literature priority has not been
audited.

## Definition

For nonnegative vertex weights `w` on a graph `K`, define the weighted
integral domination blocker

`τ_K(w)=min_{S dominates K} Σ_{x∈S}w_x`.

Let `Λ(G,H)` maximize

`Σ_g τ_H(a_{g,·})+Σ_h τ_G(b_{·,h})`                          (1)

over nonnegative arrays `a_{g,v},b_{u,h}` satisfying, for every
`(u,v)∈V(G)×V(H)`,

`Σ_{g∈N_G[u]}a_{g,v}+Σ_{h∈N_H[v]}b_{u,h}≤1`.                (2)

Unlike a rank-one tensor, the rows and columns of both arrays are
independent, and the objective applies the integral domination blocker
before summing.

## Product theorem

For all finite graphs,

`γ(G□H)≥Λ(G,H)`.                                             (3)

Let `D` dominate the product. For every `g`, the `H`-coordinates of points
of `D` in `N_G[g]×V(H)` dominate `H`; for every `h`, the `G`-coordinates of
points of `D` in `V(G)×N_H[h]` dominate `G`. Applying the corresponding
weighted blocker inequalities and counting each point `(u,v)∈D` gives

```text
Σ_g τ_H(a_g)+Σ_h τ_G(b^h)
 ≤ Σ_(u,v)∈D [
       Σ_{g∈N_G[u]}a_{g,v}
       +Σ_{h∈N_H[v]}b_{u,h}]
 ≤ |D|.
```

There is also the exact ceiling

`Λ(G,H)≤γ(G)γ(H)`.                                           (4)

Fix minimum dominators `A` of `G` and `B` of `H`. Bound each `τ_H(a_g)`
using `B` and each `τ_G(b^h)` using `A`, then sum (2) over `A×B`. Since
`A,B` dominate their factors, every term used in the blocker upper bounds
appears at least once.

## Exactness on `P₄`

Label the endpoints of `P₄` by `1,4`. Set

```text
b_{u,1}=b_{u,4}=1,
b_{u,2}=b_{u,3}=0,
a=0.
```

Every closed neighborhood of `P₄` contains at most one endpoint, so (2) is
feasible. The objective equals `2γ(G)`. Together with (4),

`Λ(G,P₄)=2γ(G)=γ(G)γ(P₄)`                                    (5)

for every `G`.

Pure higher-rank fractional packing cannot make the same repair. Always

`γ_f(G□H)≤min{|V(H)|γ_f(G),|V(G)|γ_f(H)}`,                  (6)

by copying a fractional dominator of one factor into every layer. On the
`m=24,k=12` connected split graph from the rank-one angle against `P₄`,
the right side is at most `16`, below
`30(5+√73)/24`. Thus arbitrary nonseparable fractional packing alone is
also a universal STOP on this pair.

## A saturation-defect complement

The blocker lift has a precise complement to a fractional packing. Let `P`
be an ordinary maximum two-packing set in `G`, with `|P|=ρ(G)`. For a
fractional packing `q` on `H`, put `Q=Σq` and

`Δ_H(q)=min_{T dominates H} Σ_{v∈T}[1-q(N_H[v])]`.

Then

`Λ(G,H)≥Qγ(G)+ρ(G)Δ_H(q)`.                                  (7)

Indeed, set `b_{u,h}=q_h` for every `u`, and for each `g∈P` set

`a_{g,v}=1-q(N_H[v])`,

with all other `a`-rows zero. Every `N_G[u]` contains at most one member of
the ordinary two-packing `P`, so the capacity constraint holds. The
`b`-columns contribute `Qγ(G)`, while each active `a`-row contributes
`Δ_H(q)`.

The word **ordinary** is essential: the support of a capacity-two function
can meet one closed neighborhood more than once.

At the formal Steiner point, take `q=f/2` for an optimal integer 2-packing
on `H`. Then `Q=bγ(H)` and `ρ(G)=aγ(G)`, so (7), normalized, is

`b+a Δ_H(q)/γ(H)`.

Since `c=b+a(1-b)`, this reaches Steiner exactly at

`Δ_H(q)=(1-b)γ(H)`                                            (8)

and improves it above that threshold.

The packing ratios alone do not force (8) for this canonical `q`. On `C₅`,
half-weight on `{0,2,4}` has `Δ=0`. For even `m`, the augmented uniform
split graph `S_m` with `k=m/2` satisfies

```text
γ(S_m)=m/2+3,   ρ(S_m)=4,   ρ²(S_m)=8,
x₁=x₂=8/(m+6).
```

Weight one on two complementary hard vertices and the two private leaves.
This is an optimal fractional packing of total four, and a minimum dominator
can be chosen entirely from vertices with saturated closed neighborhoods,
so again `Δ=0`.

Disjoint-union mixtures of `C₅,S₂₆,S₂₈` approach the irrational formal
point while retaining zero canonical deficit. The necessary `C₅`
domination-mass fraction is

`(√73-7)/6≈0.257334`,

and the remaining diagonal ratio is approximately `0.240125`, between
`1/4` and `4/17`. This refutes a ratio-only lower bound on the canonical
deficit. It is not an upper obstruction to optimizing (7) over all `q`, nor
to the full blocker lift.

There is a complementary diffuseness estimate. For fractional packings
`p,q` of totals `P,Q` and maximum coordinates `η_p,η_q`, the rank-one
denominator satisfies

`κ(p,q)≤η_p+η_q`,

and hence

`γ_f(G□H)≥PQ/(η_p+η_q)`.                                    (9)

The zero-deficit split examples have extremely diffuse hard-only packings.
Thus the current sharp target is a defect–diffuseness dichotomy: either an
optimized `q` makes (7) beat Steiner, or diffuse packings in both factors
make (9) do so. This dichotomy remains unproved.

## Vertex-transitive obstruction

If `G,H` are vertex-transitive of degrees `r,s`, automorphism averaging is
lossless: the feasible region is invariant and `τ` is concave as a minimum
of linear functions. The averaged arrays are constant, and exact
optimization gives

`Λ(G,H)=max{|V(G)|γ(H)/(r+1), |V(H)|γ(G)/(s+1)}`.            (10)

Take `G=H=L(K_{2m+1})`. Then

```text
|V(G)|=m(2m+1),   r=4m-2,   γ(G)=m,
```

so

`Λ(G,G)/γ(G)²=(2m+1)/(4m-1)→1/2`.                           (11)

Already at `m=7`, this is `5/9`, below Steiner's constant. Therefore the
standalone blocker lift cannot improve the universal factor.

## Verdict

**PIVOT** from pure higher-rank fractional packing and from `Λ` alone.
**GO** for the explicit defect–diffuseness dichotomy or another second-order
hybrid that makes the blocker lift pay precisely when the fractional
certificate is weak. Any proposed hybrid must survive both the split-graph
`□P₄` family and `L(K_{2m+1})□L(K_{2m+1})`.
