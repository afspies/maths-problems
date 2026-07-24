# Combined product packing and integral-blocker lift

## Status

**Exact product theorem and exact LP dual; exact zero-factor obstruction.**
This lift makes a genuine fractional packing on `G□H` and the two
directional integral-domination blockers share the same local capacity. It
strictly contains both previously separate certificate classes.

Nevertheless, it retains no positive universal factor: connected
vertex-transitive Cayley graph pairs satisfy

`Ξ(G,H)/(γ(G)γ(H))→0`.

The obstruction uses exact finite translate coverings with unbounded
covering multiplicity, not a finite enumeration.

## Definition

For `K=G□H`, let `W` be a nonnegative array on `V(K)`, and let
`a_{g,v},b_{u,h}` be nonnegative arrays. Define `Ξ(G,H)` as the maximum of

`Σ_{x∈V(K)}W_x+Σ_gτ_H(a_{g,·})+Σ_hτ_G(b_{·,h})`              (1)

subject to, for every `(u,v)∈V(K)`,

```text
W(N_K[(u,v)])
+ Σ_{g∈N_G[u]}a_{g,v}
+ Σ_{h∈N_H[v]}b_{u,h}
≤1.                                                         (2)
```

Here `τ_J(w)` is the minimum `w`-weight of an integral dominating set of
`J`.

Taking `W=0` recovers the full bidirectional blocker `Λ`. Taking `a=b=0`
recovers the fractional packing LP of the product. The shared constraint is
the new point: `Ξ` is not merely the maximum of two numerical bounds.

## Product theorem

For every pair of finite graphs,

`γ(G□H)≥Ξ(G,H)`.                                             (3)

Let `D` dominate `K`. Since `D` dominates every product vertex,

`Σ_xW_x≤Σ_{d∈D}W(N_K[d])`.

For every `g`, the `H`-coordinates of the points of `D` in
`N_G[g]×V(H)` dominate `H`; the symmetric statement holds for every `h`.
Applying the weighted integral blockers and then (2) gives

```text
Σ_xW_x+Σ_gτ_H(a_g)+Σ_hτ_G(b^h)
 ≤Σ_(u,v)∈D [
     W(N_K[(u,v)])
     +Σ_{g∈N_G[u]}a_{g,v}
     +Σ_{h∈N_H[v]}b_{u,h}]
 ≤|D|.
```

Minimize over `D` and maximize over feasible arrays.

## Exact dual

The dual minimizes

`Σ_{u,v}d_{u,v}`                                             (4)

over `d≥0` satisfying two kinds of conditions.

First, `d` is a fractional dominator of the product:

`d(N_K[x])≥1` for every `x∈V(K)`.                            (5)

Second, for each `g∈V(G)` there is a probability distribution `μ_g` on the
integral dominating sets of `H` whose incidence marginal

`z^g_v=Pr_{T∼μ_g}[v∈T]`

satisfies

`z^g_v≤Σ_{u∈N_G[g]}d_{u,v}` for every `v`.                   (6)

Symmetrically, for each `h∈V(H)` there is a probability distribution `ν_h`
on integral dominating sets of `G` with marginals

`y^h_u≤Σ_{v∈N_H[h]}d_{u,v}`.                                (7)

To derive this, introduce epigraph variables for every blocker term:

```text
α_g≤Σ_{v∈T}a_{g,v}  for every T dominating H,
β_h≤Σ_{u∈S}b_{u,h}  for every S dominating G.
```

The dual multipliers on each family have total at least one; scaling them
down to total exactly one only relaxes (6)--(7), so they may be normalized
as probability distributions. Finite LP strong duality gives equality
between (1)--(2) and (4)--(7).

This is the main conceptual gain. A cheap dual object must simultaneously:

1. fractionally dominate the product; and
2. route an owner-indexed average integral dominator of each factor through
   every opposite-factor neighborhood slice.

All failed marginal reductions discard at least one of these requirements.

## Exact vertex-transitive formula

If `G,H` are vertex-transitive of degrees `r,s`, automorphism averaging is
lossless and all three arrays may be taken constant on their relevant
orbits. The remaining one-constraint LP gives

```text
Ξ(G,H)=max{
  |V(G)||V(H)|/(r+s+1),
  |V(G)|γ(H)/(r+1),
  |V(H)|γ(G)/(s+1)
}.                                                          (8)
```

The last two terms are the exact blocker value. The first is the exact
fractional product value. Thus the triangular-line-graph family that drives
`Λ/(γ(G)γ(H))` toward `1/2` is not an obstruction to `Ξ`: for
`G=H=L(K_{2m+1})`, the first term normalized by `m²` is

`(2m+1)²/(8m-3)`.

Likewise `Ξ(G,P₄)≥2γ(G)` because `Λ` already reaches Vizing's target there.
For `C₄□C₄`, (8) is `max{16/5,8/3}=16/5`, giving the exact counterexample
to the Vizing-level claim.

## Covering-multiplicity obstruction

For a vertex-transitive graph `X`, put

```text
n_X=|V(X)|,
R_X=|N_X[x]|,
κ_X=γ(X)R_X/n_X.
```

Equation (8) becomes

```text
Ξ(G,H)/(γ(G)γ(H))
=max{
  1/κ_G,
  1/κ_H,
  R_GR_H/[κ_Gκ_H(R_G+R_H-1)]
}.                                                          (9)
```

There are connected undirected Cayley graphs with unbounded `κ`. Let
`Q=(ℤ₂)^m` and let `S⊆Q` contain zero. For

`X=Cay(Q,S\{0})`,

the closed neighborhoods are precisely the translates of `S`. Therefore

```text
γ(X)=τ(S,Q),
R_X=|S|,
κ_X=τ(S,Q)|S|/|Q|,                                         (10)
```

where `τ(S,Q)` is the minimum number of translates of `S` covering `Q`.

Bollobás, Janson, and Riordan prove that, when
`n=k^{1+o(1)}` and `n/k→∞`, almost every `k`-subset of any group of order
`n` has translate-covering multiplicity at least
`(1-o(1))log k` [@bollobasJansonRiordan2011, Theorem 4.1 and Remark 4.2].
Choose `n=2^m` and `k≈n/log n`. A random `k`-subset of `Q` also affinely
spans with probability tending to one: the probability that it lies in any
affine hyperplane is at most

`2(n-1)2^{-k}=o(1)`.

Thus one may choose a high-multiplicity, affinely spanning `S`, translate it
so that `0∈S`, and use (10). Exponent two makes `S` inverse-closed, and
affine spanning makes the Cayley graph connected.

Given `ε>0`, first choose `G` with `κ_G>1/ε`. Holding `R_G,κ_G` fixed,
choose `H` with

`κ_H>max{1/ε,R_G/(εκ_G)}`.

The first two terms in (9) are below `ε`, while

```text
R_GR_H/[κ_Gκ_H(R_G+R_H-1)]
≤R_G/(κ_Gκ_H)<ε.                                            (11)
```

Hence

`inf_{G,H} Ξ(G,H)/(γ(G)γ(H))=0`,                             (12)

even over connected vertex-transitive graphs.

For comparison, the formal-ratio additive counterfamily that kills the
three marginal arms had a componentwise blocker lower bound

`(14479-997√73)/9504≈0.627170>c`.

That benchmark is exact but irrelevant to the global obstruction (12).

## Verdict

**STOP as a universal route.** The combined lift has zero universal
normalized value even after retaining every owner-indexed distribution.
Connectedness and vertex transitivity do not repair it.

The dual remains diagnostically useful: any successor needs a constraint
not implied by fractional product domination plus averaged integral factor
dominators. The missing information must depend on the actual labelled fibre
incidences of one product dominating set.
