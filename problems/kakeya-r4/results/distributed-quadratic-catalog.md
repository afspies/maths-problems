# Distributed quadratic catalogs force an explicit QW2 witness

## Theorem

Let `B` be a family of `N` delta-tubes in `B(0,2)`, and let
`S_1,...,S_M` be positive-volume degree-two semialgebraic grains of uniformly
bounded Boolean complexity. Define

`zeta_(T,j)=|T intersect S_j|/|T|`

and the average distributed catalog overlap

`q=N^-1 sum_T sum_j zeta_(T,j)`.

Define the normalized polynomial-Wolff load

`Delta=sup_(j,delta≤lambda≤1)
 #{T:zeta_(T,j)≥lambda}/
 (|S_j| delta^-3 lambda^-4)`.

Put `H=sum_j |S_j|^(1/4)`. Then

`q≤M delta+C Delta^(1/4) delta^(-3/4) N^(-1/4) H`.              (1)

Equivalently,

`Delta≥c N delta³ (q-M delta)_+^4/H^4`.                         (2)

If every `|S_j|≤C delta` and `q≥2M delta`, then

`Delta≥c N delta² (q/M)^4`.                                    (3)

Thus distributed coverage by a finite quadratic catalog produces an
explicit polynomial, overlap level, and tube subfamily with large QW2 load;
no carrier needs to be assigned in advance.

## Proof

For fixed `j`, let

`n_j(t)=#{T:zeta_(T,j)≥t}`.

Layer cake and the definition of `Delta` give

`sum_T zeta_(T,j)=integral_0^1 n_j(t) dt`

`≤N delta+
  integral_delta^1 min(N,Delta |S_j| delta^-3 t^-4) dt`.

For `K>0`,

`integral_0^infinity min(N,K t^-4) dt
 =(4/3) N^(3/4) K^(1/4)`.

Use this upper bound with `K=Delta |S_j|delta^-3`, sum over `j`, and divide
by `N`. This proves (1). Rearrangement gives (2). Under
`|S_j|≤C delta`, Hölder's trivial bound gives

`H≤C M delta^(1/4)`.

Substitute this in (2) and use `q-Mdelta≥q/2` to get (3).

## Exact exponent ledger

Suppose

`N≥beta delta^(-3+tau)`, `M≤delta^-h`, `q≥delta^s`.

At exponent level, `s<1-h` ensures `q≥2Mdelta`. Formula (3) then forces

`Delta≥c beta delta^(-(1-tau-4h-4s))`.                          (4)

If QW2 is bounded by `Delta≤delta^-b`, distributed coverage is impossible
whenever

`4h+tau+4s+b<1`.                                                (5)

The harness verifies (4)–(5) exactly over rational exponents.

For a direction-separated family, Katz–Rogers supplies
`b>0` arbitrarily small. In the full-size, constant-overlap case
`N≈delta^-3`, `q≈1`, equation (5) forces at least
`M≥delta^(-1/4+o(1))` grains. This is weaker than the
`delta^-1` threshold for full containment in one carrier, because here a
tube's overlap may be distributed thinly across many grains.

## Certificate and scope

The supremum in `Delta` can be discretized into dyadic overlap levels. Put

`L≤1+ceil(log_2(2M/q))`.

When `q≥2Mdelta`, there are an explicit catalog polynomial `P_j`, a level
`lambda in [q/(2M),1]`, and a subfamily `T'` such that

`lambda≤zeta_(T,j)<2lambda` for every `T in T'`,

`#T'/N≥c q/(M L lambda)≥c q/(M L)`,

and its QW2 load is at least

`c N delta² q^4/(M^4 L)`.

Thus the output is overlap-balanced and retains a quantified tube fraction;
for density-balanced shadings it retains the same fraction of shading mass.
The logarithm is the cost of insisting on this explicit high-retention
dyadic witness; the sharp supremum bound (3) has no logarithmic loss.

This theorem does not infer large `q` from small union volume. It converts a
pre-existing distributed catalog-capture conclusion into the explicit
semialgebraic certificate required by Bridge B. It also explains why
assigning each tube to one preferred grain loses less entropy than permitting
diffuse membership in many grains: the latter pays `M^4`.
