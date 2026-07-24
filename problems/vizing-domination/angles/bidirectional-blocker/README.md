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

For every dominating set `T`, put

`E_T(q)=Σ_x q_x(|T∩N_H[x]|-1)≥0`.

Double counting gives

`Σ_{t∈T}q(N[t])=Q+E_T(q)`.

Consequently

```text
Δ_H(q)=γ(H)-Q-Ω_H(q),
Ω_H(q)=max_T [E_T(q)-(|T|-γ(H))]≥0.                          (8)
```

In particular `Δ_H(q)≤γ(H)-Q`. Therefore the canonical packing reaches
Steiner only at the absolute ceiling

`Δ_H(q)=(1-b)γ(H)`,

and can never improve it. More generally, writing
`x=Q/γ(H)` and `ω=Ω_H(q)/γ(H)`, the normalized complement value is

`a+(1-a)x-aω`.                                               (9)

Improvement over Steiner would require both `x>b` and the exact
surplus-overlap inequality

`(1-a)(x-b)>aω`.                                             (10)

Even optimizing over every fractional packing does not force this from the
formal packing ratios. On `C₅`, the optimized complement value is `5/3`.
For the augmented uniform split graph `S_{2k}`,

```text
γ(S_{2k})=k+3,   ρ(S_{2k})=4,   ρ²(S_{2k})=8.
```

If `a(k+1)≥2`, an exact orbit calculation gives

`max_q [Q+aΔ(q)]=a(k+1)+2`.                                  (11)

Disjoint-union mixtures of `C₅,S₂₆,S₂₈` approach the irrational formal
point in both packing ratios. Additivity and (11) give the limiting optimized
normalized value

`(1273-115√73)/576≈0.504235<c`.                              (12)

The exact positive gap is

`(139√73-1153)/576`,

with `139²·73-1153²=81024`. Thus the entire saturation-defect complement
slice is a **STOP** from Steiner's packing ratios, not merely its canonical
choice of `q`. This does not upper-bound the full blocker lift `Λ`.

There is a complementary diffuseness estimate. For fractional packings
`p,q` of totals `P,Q` and maximum coordinates `η_p,η_q`, the rank-one
denominator satisfies

`κ(p,q)≤η_p+η_q`,

and hence

`γ_f(G□H)≥PQ/(η_p+η_q)`.                                    (13)

The split components defeating (7) have extremely diffuse hard-only
packings, so they do not refute a combined theorem. However, even the
unrestricted claim “low complement value in both factors forces a useful
common concentration cap” is false on the connected pairs
`S₂₆,S_{2ℓ}` as `ℓ→∞`; their complement values stay below Steiner while
every shared-cap rank-one profile is negligible after normalization.
Even independent caps do not repair this at the formal ratios. The exact
asymmetric construction in `../anchored-domination/README.md` has both
packing ratios tending to `(a,b)`, both optimized complement values below
`c`, and

`sup_{s,t} Φ_G(s)Φ_H(t)/((s+t)γ(G)γ(H))<c`.

Thus the entire three-arm marginal hybrid is a STOP.

There is a tempting genuinely two-sided slice of `Λ`. Choose maximum
ordinary two-packings `P,Q`, put `U=N_G[P],V=N_H[Q]`, and activate the
`a`-rows indexed by `P` and the `b`-columns indexed by `Q`. For

`κ_G(s;U)=min_{T dominates G} (|T\U|+s|T∩U|)`,

the resulting feasible objective contains

`ρ(G)κ_H(t;V)+ρ(H)κ_G(1-t;U)`.                               (14)

This coupled slice is also exactly blocked by the formal-ratio split
mixtures. If `U` contains a minimum dominator, then

`κ_G(s;U)=sγ(G)`.

The lower bound is immediate because every vertex weight is at least `s`;
the minimum dominator inside `U` gives equality. For `C₅`, one maximum
two-packing neighborhood contains a minimum dominator. For every
`S_{2k,z}`, take the two complementary hard vertices and all private leaves
as `P`; their closed-neighborhood union contains the standard minimum
dominator of `k+1` coordinate vertices and all `z` private clique vertices.
The property is preserved by disjoint union. Hence (14), normalized on the
formal-ratio mixtures, is identically

`ta+(1-t)a=a<c`.

This closes a natural coupled residual allocation, not the full `Λ`.

## Vertex-transitive obstruction

If `G,H` are vertex-transitive of degrees `r,s`, automorphism averaging is
lossless: the feasible region is invariant and `τ` is concave as a minimum
of linear functions. The averaged arrays are constant, and exact
optimization gives

`Λ(G,H)=max{|V(G)|γ(H)/(r+1), |V(H)|γ(G)/(s+1)}`.            (15)

Take `G=H=L(K_{2m+1})`. Then

```text
|V(G)|=m(2m+1),   r=4m-2,   γ(G)=m,
```

so

`Λ(G,G)/γ(G)²=(2m+1)/(4m-1)→1/2`.                           (16)

Already at `m=7`, this is `5/9`, below Steiner's constant. Therefore the
standalone blocker lift cannot improve the universal factor.

In fact the normalized value can tend to zero even on connected
vertex-transitive graphs. If `X` is vertex-transitive, put

`κ_X=γ(X)|N_X[x]|/|V(X)|`.

Formula (15) says that the two normalized blocker arms are `1/κ_G` and
`1/κ_H`. Bollobás, Janson, and Riordan's translate-cover theorem supplies
affinely spanning sets in elementary abelian 2-groups with
`κ_X→∞` [@bollobasJansonRiordan2011, Theorem 4.1 and Remark 4.2].
Their Cayley graphs are connected and have the translates as closed
neighborhoods. Hence

`inf_{G,H} Λ(G,H)/(γ(G)γ(H))=0`

even over connected vertex-transitive factors.

## Verdict

**STOP** for the saturation-defect complement, independently capped
rank-one repair, the coupled ordinary-packing slice (14), pure higher-rank
fractional packing, and `Λ` alone. The full `Λ` has zero universal factor.
**GO** only for a certificate using the actual labelled incidences of a
product dominator. Averaged owner-indexed factor dominators are also
insufficient; see `../combined-blocker-packing/README.md`.
