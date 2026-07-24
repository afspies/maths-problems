# Anchored fractional domination and concentration profiles

## Status

**Exact duality and exact counterfamilies proved; independently checked by
GPT-5.6 Sol at xhigh effort.** The saturation-defect slice of the
bidirectional blocker lift is an anchored fractional-domination parameter.
Even after optimizing its fractional packing, it stays strictly below
Steiner on disjoint-union factors approaching the formal packing ratios.

A natural diffuseness repair also fails. There are pairs approaching both
formal packing ratios for which the two optimized anchored values and the
rank-one capped tensor stay strictly below Steiner, even when the two
coordinate caps are optimized independently.

Literature priority for these formulations has not been established.

## Exact overlap identity

For a fractional packing `q` on `H`, write

```text
Q=Σq,
Δ_H(q)=min_{T dominates H} Σ_{t∈T}[1-q(N[t])].
```

For a dominating set `T`, put

`E_T(q)=Σ_x q_x(|T∩N[x]|-1)≥0`.

Double counting gives

`Σ_{t∈T}q(N[t])=Q+E_T(q)`.

Therefore

```text
Δ_H(q)=γ(H)-Q-Ω_H(q),
Ω_H(q)=max_{T dominates H}
       [E_T(q)-(|T|-γ(H))]≥0.                                (1)
```

In particular,

`Δ_H(q)≤γ(H)-Q`.                                             (2)

Let `Γ=γ(G)`, `r=ρ(G)`, and normalize

```text
α=r/Γ,   x=Q/γ(H),   ω=Ω_H(q)/γ(H).
```

The blocker complement from the previous angle becomes exactly

`α+(1-α)x-αω`.                                               (3)

At Steiner's formal point `α=a,x=b`, equation (3) is
`c-aω≤c`. Thus the canonical half-2-packing can never improve Steiner.
For an optimized packing, improvement requires

`(1-a)(x-b)>aω`;                                             (4)

in particular `x>b`.

## Optimized complement and anchored dual

Define the blocker-valid optimized slice

`F_a(H)=max_q [Q+aΔ_H(q)]`,                                  (5)

where the maximum is over fractional packings.

There is also an optimistic version restricting the minimum in `Δ` to
minimum-cardinality dominating sets. Let `A` be the closed-neighborhood
matrix and

`M_γ(H)=conv{1_T:T is a minimum dominating set}`.

LP duality and minimax give its exact anchored form

```text
B_a(H)=min {
  1ᵀd :
  Ad≥1,
  d≥az for some z∈M_γ(H)
}.                                                          (6)
```

Thus `B_a` is the cheapest fractional dominator containing `a` times an
average minimum integral dominator. Since the valid `Δ` minimizes over more
sets,

`F_a(H)≤B_a(H)`.

## Exact split and cycle values

Let `S_{2k,z}` have:

- `2k` coordinate vertices forming a clique;
- one independent hard vertex for every `k`-subset of `[2k]`; and
- `z` further clique vertices, each with one private leaf.

Then

```text
γ(S_{2k,z})=k+1+z,
ρ(S_{2k,z})=2+z,
ρ²(S_{2k,z})=4+2z.                                         (7)
```

The two normalized packing ratios coincide. An exact orbit calculation
gives

`F_a(S_{2k,z})=z+max{2,a(k+1)}`.                             (8)

For the upper bound, average minimum dominators consisting of `k+1`
coordinate vertices and all `z` private clique vertices. Their expected
coverage multiplicities are one on each private leaf, `(k+1)/2` on every
hard target, and `k+1+z` on every clique vertex. The packing constraints
then bound (5). Equality comes either from the two-unit diffuse hard packing
or from the private leaves.

For `C₅`, automorphism averaging gives

`F_a(C₅)=5/3`                                                (9)

for the formal `a<5/6`.

For the triangular graph `T=L(K₇)`,

```text
γ(T)=3,   ρ(T)=1,   ρ²(T)=3,
F_a(T)=21/11.                                               (10)
```

Indeed, every closed neighborhood has size 11, so every fractional packing
has total at most `21/11`. Averaging over all three-edge matchings of `K₇`,
which are minimum dominating sets of `L(K₇)`, gives

`Δ_T(q)≤3-11Q/7`.

Since `a<7/11`, this proves

`Q+aΔ_T(q)≤3a+(1-11a/7)Q≤21/11`,

with equality at the uniform packing.

## Formal-ratio counterfamily

Use disjoint-union mixtures of `C₅,S₂₆,S₂₈`. The `C₅`
domination-mass fraction is

`(√73-7)/6`,

and the remaining diagonal ratio is `(41-3√73)/64`, between `1/4` and
`4/17`. Rational multiplicities approach these proportions, so both packing
ratios approach `(a,b)`.

Equations (8)--(9) give

`F_a/γ→(1273-115√73)/576≈0.504235<c`.                        (11)

The exact gap is

`(139√73-1153)/576>0`,

certified by `139²·73-1153²=81024`. Hence even the fully optimized
saturation-defect slice cannot be forced above Steiner by the formal packing
ratios.

## Capped packing profiles

Define

`Φ_H(t)=max{Σp:p fractional packing, p_v≤t for all v}`.       (12)

Its exact dual is

```text
Φ_H(t)=min {
  Σλ+tΣμ :
  Aλ+μ≥1,
  λ,μ≥0
}.                                                          (13)
```

Packings with caps `s,t` on `G,H` give the rank-one product certificate

`γ_f(G□H)≥Φ_G(s)Φ_H(t)/(s+t)`.                               (14)

The split profile is also exact. Put

```text
d=k+z+1,
M=binom(2k-1,k-1),
n=2M+2k+2z.
```

Then, for `0≤t≤1`,

```text
Φ_{S_{2k,z}}(t)=
  nt                         if 0≤t≤1/(M+2k+z),
  1+(M+z)t                  if 1/(M+2k+z)≤t≤1/M,
  2+zt                       if 1/M≤t≤1.                    (15)
```

To prove this, symmetrize a packing to weights `x,y,u,v` on hard,
coordinate, private-clique, and leaf orbits. The relevant constraints are

```text
x+ky≤1,
Mx+2ky+zu≤1,
2ky+zu+v≤1,
u+v≤1.
```

The three upper bounds in (15) follow respectively from the cap, by writing
the objective as

`Mx+[Mx+2ky+zu]+zv`,

and from twice the middle constraint plus `zv`. Equality is attained by the
three orbit solutions meeting at the displayed breakpoints. In particular,

`Φ_{S_{2k,z}}(t)/d=(z/d)t+e_{k,z}(t),  0≤e_{k,z}(t)≤2/d`      (16)

uniformly over every cap.

The shared-cap specialization is not a universal repair. Fix
`G=S₂₆` and let `H=S_{2ℓ,2}` with `ℓ→∞`. Both anchored values lie below
Steiner, but for every shared cap `t`,

```text
Φ_G(t)≤|V(G)|t,
Φ_H(t)≤4,
```

so the normalized value `Φ_G(t)Φ_H(t)/(2t)` tends to zero.
These connected factors are not in the near-Steiner ratio regime.

## A full independent-cap counterfamily

The stronger hybrid, consisting of both anchored arms and (14) with
independent caps, also fails at the formal ratios.

For the first factor `G`, use disjoint unions whose domination-mass shares
approach

```text
λ_G=(√73-7)/6
```

of `C₅`, with the rest a mixture of `S₂₆,₂` and `S₂₈,₂`. The split part has
diagonal packing ratio

`θ_G=(41-3√73)/64`;

the `S₂₆,₂` share inside that part is

`ν=(441-51√73)/16`.

Both normalized packing ratios tend to `(a,b)`, and (8)--(9) give

`F_a(G)/γ(G)→(1273-115√73)/576≈0.504235<c`.                  (17)

For the second factor `H`, give `T=L(K₇)` domination-mass share

`λ_H=(√73-7)/4`

and use large `S_{2k,z_k}` components in the remaining share, where

`(z_k+2)/(k+1+z_k)→θ_H=(19-√73)/36`.

Again both packing ratios tend to `(a,b)`. Equation (10) and the split value
give

`F_a(H)/γ(H)→(2443-217√73)/1056≈0.557719<c`.                 (18)

The exact positive gap in (18) is

`(87√73-741)/352`,

and `87²·73-741²=3456`.

It remains to control every pair of caps. Normalize the profiles by
domination number and call them `g(s),h(t)`. For `C₅`,

`Φ_C₅(s)/γ(C₅)=(5/2)min{s,1/3}`.

For a split component with two private pairs,

`Φ(s)≤2+2s`.

It follows that

```text
g(s)≤λ_G(5/2)min{s,1/3}+r(1+s),
r=(47-5√73)/48.
```

The exact inequalities

```text
r<1/11,
(5/2)λ_G+r=(5√73-31)/16<1
```

imply the convenient global envelope

`g(s)≤s+1/11`.                                               (19)

For `L(K₇)`, regularity gives

`Φ_T(t)/γ(T)=7min{t,1/11}`.

The split estimate

`z_kt≤Φ_{S_{2k,z_k}}(t)≤z_kt+2`

therefore gives the limiting second profile

`h(t)=7λ_H min{t,1/11}+(1-λ_H)θ_Ht`.                         (20)

For every fixed `s`, `h(t)/(s+t)` is maximized at `t=1/11`.
Below that point (20) is a linear ray. Above it, write `h(t)=A+Bt`;
then

`A-B=(-811+97√73)/264>0`,

so the quotient decreases. Combining (19)--(20),

```text
sup_{s,t} g(s)h(t)/(s+t)
 ≤h(1/11)
 =(-247+37√73)/264
 ≈0.261849<c.                                               (21)
```

The exact gap is

`(151-13√73)/132>0`.

This limiting construction has finite witnesses, uniformly over all caps.
For a large split component of domination number `d`, write its normalized
profile as

`ψ(t)=(z/d)t+e(t),   0≤e(t)≤2/d`.

The first factor is a mixture of fixed finite components, so
`g(s)≤Ks` for a fixed constant `K`. The contribution of the split error to
the normalized tensor is therefore at most

`g(s)e(t)/(s+t)≤2K/d`,

even when both caps tend to zero. Choose the large split parameter first,
then approximate the irrational component shares by rational
multiplicities. The three displayed strict gaps persist for sufficiently
advanced finite approximants.

## Connectedization

The counterfamily can be made connected without changing either packing
ratio or losing any of the three strict upper obstructions.

Call `p` a safe port of a component `K` when

```text
γ_K(V(K)\{p})=γ(K)
```

and optimal ordinary and integer 2-packing witnesses both assign zero to
`p`. Join the ports of disjoint components by any tree. A dominator of the
connected graph must still contribute at least `γ(K)` vertices inside every
old component, because new edges reach only its port and the other targets
still require `γ_K(V\{p})` vertices. Old component dominators give equality.
Edge addition can only decrease `ρ,ρ²`, while the union of the zero-port
packing witnesses remains feasible, so both packing numbers are preserved.

The required safe ports exist:

- in `C₅`, use a vertex outside chosen optimal packing witnesses;
- in `S_{2k,z}`, use a coordinate-clique vertex and the complementary-hard
  plus private-leaf witnesses; and
- in `L(K₇)`, use any line vertex, an ordinary packing edge avoiding it, and
  a three-edge matching avoiding it.

Adding edges shrinks the feasible capped-packing polytope and enlarges closed
neighborhood loads; it cannot increase `Φ` or the optimized anchored value
`F_a`. Consequently the connectedized finite approximants still approach
the formal packing ratios and keep both anchored arms and every
independently capped tensor strictly below `c`.

## Verdict

**STOP** for the canonical deficit, the fully optimized complement slice,
and the three-arm hybrid consisting of both anchored values and the
independently capped rank-one tensor. **GO, unresolved** only for:

1. the full blocker lift `Λ`, beyond this slice;
2. a genuinely nonseparable certificate using the full fibre labels.
