# A two-sided fractional-packing tensor bridge

## Status

**Proved; orthogonal graph-class bound.** This construction uses fractional
packings on both factors directly, rather than Steiner's one-sided fibre
decomposition. It gives a local-concentration parameter and a clean regular
graph criterion, but no new universal constant without a further
integrality/concentration tradeoff.

The later analysis in `angles/fractional-rank-one-limits` proves that no
universal tradeoff of the proposed optimal/near-optimal rank-one form exists.

## Tensor theorem

Let `p` and `q` be nonzero fractional packing functions on `G` and `H`:

`p(N_G[u])≤1` and `q(N_H[v])≤1`

for all vertices. Put

```text
P=Σ_u p_u,  Q=Σ_v q_v,
κ(p,q)=max_{u,v}[
  q_v p(N_G[u]) + p_u q(N_H[v]) - p_u q_v
].
```

Then

`γ(G□H) ≥ γ_f(G□H) ≥ PQ/κ(p,q)`.                              (1)

The nonzero hypothesis ensures `κ>0`: for positive coordinates `p_u,q_v`,
the expression inside the maximum is at least `p_uq_v`.

### Proof

Define

`r_{u,v}=p_uq_v/κ`.

The closed neighborhood of `(u,v)` in the Cartesian product is the union of
`N_G[u]×{v}` and `{u}×N_H[v]`, whose intersection is `{(u,v)}`. Therefore

```text
Σ_{(x,y)∈N[(u,v)]} r_{x,y}
 = [q_v p(N_G[u])+p_u q(N_H[v])-p_uq_v]/κ
 ≤ 1.
```

Thus `r` is a fractional packing on `G□H` of total weight `PQ/κ`.
Fractional packing/domination LP duality and relaxation of integral
domination give (1).

## Regular graph corollary

If `G` is `r`-regular and `H` is `s`-regular, choose the uniform packings

`p_u=1/(r+1)`, `q_v=1/(s+1)`.

Then

`κ=(r+s+1)/((r+1)(s+1))`,

so

`γ(G□H)≥|V(G)||V(H)|/(r+s+1)`.                                (2)

In particular, Vizing's conjecture holds for a given regular pair whenever

`γ(G)γ(H)≤|V(G)||V(H)|/(r+s+1)`.

## Concentration obstruction

A natural attempt to make (1) universal is to demand diffuse optimal
fractional packings. Connectedness does not provide this. For `P_4`, the
unique optimal fractional packing is

`(1,0,0,1)`,

of total weight two. Adding the two middle closed-neighborhood constraints
shows that any optimum of weight two has both internal coordinates zero,
forcing the endpoints to have weight one.

Taking this packing in both factors gives `κ=1`. In particular, any
totals-only cap such as

`κ≤1/P+1/Q-1/(PQ)=3/4`

is false. Local concentration, not total fractional mass alone, controls the
tensor loss.

## Verdict

**GO** as a genuinely different graph-class/LP bridge. **PIVOT** as a
universal-constant route unless one proves a tradeoff between:

- the integral/fractional domination ratios `γ/γ_f`; and
- the minimum attainable local concentration `κ` among optimal or
  near-optimal fractional packings.

The exact tensor formula is saturated by uniform regular packings, so its
denominator cannot be lowered algebraically without new combinatorial input.
