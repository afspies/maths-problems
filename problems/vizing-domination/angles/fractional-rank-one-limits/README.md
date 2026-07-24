# Rank-one fractional tensors: limits and a diffuse gain

## Status

**Exact no-go and graph-class bounds proved; independently reviewed by
GPT-5.6 Sol at xhigh effort.** Optimal or near-optimal rank-one packing
tensors cannot support a universal integrality-gap/concentration theorem.
A deliberately suboptimal diffuse packing can nevertheless beat Steiner on
explicit connected pairs.

## Universal ceiling

For fractional packings `p,q`, write

```text
A_u=p(N_G[u]), B_v=q(N_H[v]), P=Σp, Q=Σq,
κ=max_{u,v}(q_vA_u+p_uB_v-p_uq_v).
```

Then every rank-one tensor certificate satisfies

```text
PQ/κ ≤ min{|V(H)|γ_f(G), |V(G)|γ_f(H)}.                       (1)
```

Put `a=max_u A_u` and `η=max_v q_v`. Choosing maximizing vertices gives
`κ≥aη`, since `B_v≥q_v`. The scaled packing `p/a` is feasible, so
`P/a≤γ_f(G)`, while `Q/η≤|V(H)|`. This proves the first bound; symmetry gives
the second.

For `H=P₄`, equation (1) implies that the normalized factor is at most

`2/a_G`, where `a_G=γ(G)/γ_f(G)`.

Thus no rank-one tensor can improve Steiner for every `G`: it is already
incapable of doing so when

`a_G≥48/(5+√73)≈3.544`.

## Optimal concentration is maximally bad against `P₄`

The unique optimal fractional packing of `P₄` is

`q=(1,0,0,1)`.

Adding its two middle closed-neighborhood constraints shows that an optimum
of total two has zero internal weights and unit endpoint weights.

Every optimal packing `p` of a nonempty graph has
`max_u A_u=1`, or it could be scaled upward. With the displayed `q`, every
closed-neighborhood load `B_v` equals one, and the tensor expression at an
endpoint is `A_u`. Hence

`κ(p,q)=1` for every optimal p.                                  (2)

This persists quantitatively. If

```text
P≥(1-ε_G)γ_f(G),       Q≥2(1-ε_H)
```

with `q` on `P₄`, then

`κ(p,q)≥(1-ε_G)(1-2ε_H)`                                     (3)

for `0≤ε_H≤1/2`. The first factor follows by scaling. The two middle
constraints on `P₄` imply that some endpoint has weight at least
`1-2ε_H`.

Equations (2)--(3) rule out a universal theorem asserting that a large
integrality gap forces diffuse optimal or fixed-tolerance near-optimal
packings.

## Connected obstruction family

Fix `1≤k≤m`. Form a split graph with:

- clique vertices `c₁,...,c_m,a,b`;
- independent vertices `x_S` for all `S∈([m] choose k)`, plus `x_a,x_b`;
- edges `c_i x_S` exactly when `i∈S`, and private edges `ax_a,bx_b`.

Then

```text
γ=m-k+3,       γ_f=m/k+2.                                    (4)
```

If `t` coordinate clique vertices are selected, every `k`-set avoiding them
must select its own independent vertex. The bound

`t+binom(m-t,k)≥m-k+1`

and the two private pairs prove the integral lower bound; selecting
`m-k+1` coordinates together with `a,b` attains it.

Fractionally, weight each coordinate by `1/k` and `a,b` by one. The dual
packing puts weight `1/binom(m-1,k-1)` on every `x_S` and weight one on both
private vertices. Both have total `m/k+2`.

Moreover every optimal packing puts zero weight on the clique and unit
weight on both private vertices. If `z` is total clique weight and `W` the
total hard-element weight, summing the coordinate constraints gives
`mz+kW≤m`; the two private constraints give at most `1-z` each. The total is
therefore at most

`m/k+2-(m/k+1)z`.

For `m=24,k=12`, the integrality gap is `15/4`. By (1), no rank-one tensor
against `P₄` can certify a normalized factor above `8/15<0.5643`.

## A diffuse packing that does help

Take instead the hard-only split graph with `m=8,k=4`, omitting the two
private gadgets. It has

`γ(G)=5` and `γ_f(G)=2`.

Put weight `1/35` on each of its 70 independent `4`-set vertices and zero
on the eight clique vertices. This is optimal. For a packing `p` on `G`,
define

`s(p)=max_u(A_u+2p_u)`.

Use the suboptimal uniform packing `(1/3,1/3,1/3,1/3)` on `P₄`. Its internal
closed-neighborhood loads are one and its endpoint loads are `2/3`, so the
tensor denominator is exactly `s(p)/3`. Hence

```text
γ(G□P₄)≥4γ_f(G)/s(p).                                        (5)
```

For the displayed split-graph packing, clique vertices have `A_u=1,p_u=0`
and element vertices have `A_u=p_u=1/35`; therefore `s(p)=1`. Equation (5)
gives

`γ(G□P₄)≥8`,

a normalized factor `8/(5·2)=4/5`, well above Steiner's universal constant.

## Verdict

**STOP** for a universal rank-one proof based on optimality tolerance or
coordinate concentration. **GO** for higher-rank/nonseparable tensors and
for graph-specific choices of deliberately diffuse suboptimal packings.
