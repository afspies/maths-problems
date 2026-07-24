# Actual calibration of Steiner's factor invariants

## Status

**Probabilistic existence theorem proved and independently audited at
GPT-5.6 Sol xhigh effort.** Steiner's formal minimizing point for

```text
x₁=ρ(G)/γ(G),       x₂=ρ^{\{2\}}(G)/(2γ(G))
```

is the limit of actual finite graphs. Thus no universal inequality involving
only `γ,ρ,ρ^{\{2\}}` can exclude the formal point by claiming that it is an
unrealizable artifact of the four-parameter relaxation.

The construction is disconnected. No connected realization is claimed.
That is enough for the universal conjecture and for ruling out an
unqualified factor-invariant inequality.

## Dense integrality-gap component

For every fixed integer `L`, there exists a finite graph `K` such that

```text
γ(K)>L,       ρ(K)=1,       ρ^{\{2\}}(K)=2.                  (1)
```

Take `K∼G(n,1/2)`. With probability tending to one, all three of the
following hold:

1. every pair of vertices lies in some closed neighborhood;
2. every triple of vertices lies in some closed neighborhood;
3. no set of at most `L` vertices dominates.

For a fixed pair, failure of the first property has probability at most

`(3/4)^{n-2}`:

unless the pair is adjacent, an outside vertex is a common neighbor with
probability `1/4`. A union bound over pairs tends to zero.

For a fixed triple, an outside vertex is adjacent to all three with
probability `1/8`. Hence failure of the second property has probability at
most

`(7/8)^{n-3}`,

and the union bound over triples again tends to zero.

For a fixed `s`-set `S`, the probability that `S` dominates is

`(1-2^{-s})^{n-s}≤exp(-(n-s)2^{-s})`.

Summing this over `0≤s≤L` and all `s`-sets tends to zero. This proves the
simultaneous existence of the three properties.

The pair property gives `ρ(K)=1`: any two vertices belong to one closed
neighborhood, so their closed neighborhoods intersect.

The triple property gives `ρ^{\{2\}}(K)=2`. If a nonnegative integer
2-packing had total weight at least three, then either:

- one vertex had weight at least three;
- vertices of weights two and one lay together in a closed neighborhood,
  by the pair property; or
- three positive-weight vertices lay together in a closed neighborhood,
  by the triple property.

Every case violates the capacity-two constraint. Weight two on one vertex
is feasible, proving equality in (1).

In particular, the tempting inequality

`γ(G)≤2(ρ^{\{2\}}(G)-ρ(G))`

is false by an arbitrarily large factor, despite holding on every graph
through six vertices and on the split-cover hygiene gadgets tested in this
campaign.

## Exact mixture at Steiner's point

Put

```text
c=(5+√73)/24,
a=(11-√73)/8,
b=(13-√73)/12.
```

Define three positive domination-mass fractions

```text
d=c=(5+√73)/24,
t=3a-2b=(47-5√73)/24,
s=4(b-a)=(√73-7)/6.
```

They satisfy

`d+t+s=1`.                                                   (2)

Use:

- one dense component `K_m` from (1), with `γ(K_m)→∞`;
- isolated vertices, whose `(x₁,x₂)` ratios are `(1,1)`; and
- copies of `C₅`, whose ratios are `(1/2,3/4)` because
  `γ(C₅)=2`, `ρ(C₅)=1`, and `ρ^{\{2\}}(C₅)=3`.

Choose the numbers of isolated vertices and `C₅` copies so that their
fractions of the total domination number tend to `t` and `s`; the dense
component then has fraction tending to `d`. Domination and both packing
parameters are additive over disjoint unions. Since the dense component
has fixed packing totals `1,2` but domination tending to infinity, its
normalized packing contribution vanishes. Therefore

```text
x₁→t+s/2
   =(11-√73)/8
   =a,

x₂→t+3s/4
   =(13-√73)/12
   =b.                                                       (3)
```

Thus the exact point at which all six of Steiner's scalar inequalities
equal `c` is an actual graph limit, not merely a point in an over-relaxed
parameter box.

## Consequence

Any improved universal constant must use information beyond the three
factor invariants `γ,ρ,ρ^{\{2\}}`. Continuity-based optimization over a new
universal relation among only these invariants cannot cut the Steiner
point: actual graph sequences converge to it.

This strengthens the campaign's stop rule. The remaining viable information
is product-specific and label-correlated: typed near-cover profiles,
indexed terminal systems, repair cardinality slacks, and the exact
overlap/multiplicity ledger.
