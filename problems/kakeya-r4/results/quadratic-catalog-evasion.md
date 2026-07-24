# QW2 forces evasion of low-entropy quadratic catalogs

## Lemma

Let `T` be a direction-separated family of delta-tubes in `R4` with

`#T≥delta^(-3+tau)`.

Assume the degree-two polynomial Wolff axiom with loss `A`:

`#{T: |T intersect S_P|≥lambda|T|}
 ≤ A |S_P| delta^-3 lambda^-4`

for every coefficient-normalized polynomial `P` of degree at most two, where
`S_P=N_(C delta)(Z(P)) intersect B(0,2)`.

Let `P_1,...,P_M` be any explicit catalog with `M≤delta^-h`. Then the
fraction of `T` carried at overlap at least `lambda` by at least one catalog
member is at most

`C A delta^(1-h-tau) lambda^-4`.                                (1)

In exponent notation, if `lambda=delta^a` and `A≤delta^-b`, the saving in
(1) is

`1-h-tau-4a-b`.                                                 (2)

Thus if this number is positive, every such low-entropy quadratic catalog
misses a `1-o(1)` fraction of the Kakeya directions.

## Proof

The fixed-degree tubular-neighborhood estimate gives `|S_P|≤C delta`.
The QW2 axiom therefore permits at most

`C A delta^-2 lambda^-4`

tubes for one polynomial. Sum this bound over `M≤delta^-h` catalog members
and divide by `#T≥delta^(-3+tau)`. This gives (1). Substituting
`lambda=delta^a` and `A≤delta^-b` gives (2).

All exponent conversions are checked exactly in
`harness/grain_union_ledger.py`.

## Meaning for carrier extraction

This lemma is deliberately one-way and noncircular:

- input: an explicit catalog and a separately verified QW2 axiom;
- output: most directions evade that catalog.

It does not extract a polynomial from small union volume. Conversely, any
proposed degree-two inverse theorem that says a low-entropy catalog captures
most of a near-full direction family must spend at least the entire power in
(2), or contradict QW2.

For bounded or subpolynomial catalogs, `h=0`. At constant overlap and
subpolynomial QW2 loss, a `delta^(-3+o(1))` family therefore cannot have a
positive fraction of its directions carried by the catalog. A successful
quadratic reduction must instead output roughly `delta^-1` carriers, exploit
substantial direction multiplicity, or find additional organization—exactly
the regime addressed by the harmonic transverse-stack union lemma.
