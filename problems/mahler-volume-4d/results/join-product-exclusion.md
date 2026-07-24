# Sharp Mahler factorization for joins, products, and free sums

## Theorem

Let \(K\subset\mathbb R^p\) and \(L\subset\mathbb R^q\) be convex bodies.
Write \(\mathcal P\) for the non-symmetric Mahler product.

For the Cartesian product and free sum in complementary linear subspaces,

\[
\boxed{
\mathcal P(K\times L)=\mathcal P(K\oplus L)
=\frac{p!\,q!}{(p+q)!}\mathcal P(K)\mathcal P(L).
}
\]

For their affine join, of dimension \(d=p+q+1\),

\[
\boxed{
\mathcal P(K*L)
=
\left(\frac{p!\,q!}{d!}\right)^2
\frac{(d+1)^{d+1}}
{(p+1)^{p+1}(q+1)^{q+1}}
\mathcal P(K)\mathcal P(L).
}
\]

These identities include the earlier pyramid factor when \(q=0\).

Since the join factor cancels the two lower-dimensional simplex constants,
the sharp non-symmetric Mahler conjecture is closed under joins: if it holds
in dimensions \(p\) and \(q\), it holds for every \(p+q+1\)-dimensional join,
with equality only for the join of simplices, itself a simplex.

## Proof for products and free sums

Put both factors in Santaló position. The polar of the product is

\[
(K\times L)^\circ
=\{(u,v):h_K(u)+h_L(v)\le1\}.
\]

For fixed \(v\in L^\circ\), its \(u\)-section is
\((1-h_L(v))K^\circ\). Gauge-polar integration gives

\[
\begin{aligned}
|(K\times L)^\circ|
&=|K^\circ|\,q|L^\circ|
\int_0^1 r^{q-1}(1-r)^p\,dr\\
&=\frac{p!\,q!}{(p+q)!}|K^\circ||L^\circ|.
\end{aligned}
\]

Every section has zero first moment in the \(K^\circ\) coordinates, and
radial integration preserves the zero centroid of \(L^\circ\). Hence the
origin is the Santaló point. Multiplying by
\(|K\times L|=|K||L|\) proves the product formula.

The free-sum polar is \(K^\circ\times L^\circ\), while the same beta integral
gives

\[
|K\oplus L|=\frac{p!\,q!}{(p+q)!}|K||L|.
\]

This proves the second identity.

## Proof for joins

Affinely realize the join as

\[
J=\operatorname{conv}\bigl(
K\times\{0\}\times\{0\},
\{0\}\times L\times\{1\}
\bigr).
\]

Its height-\(t\) section is \((1-t)K\times tL\), so

\[
|J|=\frac{p!\,q!}{d!}|K||L|.
\]

Translate by \(z=(0,0,\tau)\). At dual height \(r\), the polar section is

\[
(1+\tau r)K^\circ
\times
(1-(1-\tau)r)L^\circ,
\]

for \(-1/\tau\le r\le1/(1-\tau)\). A second beta integral gives

\[
|(J-z)^\circ|
=
\frac{p!\,q!}{d!}
\frac{|K^\circ||L^\circ|}
{(1-\tau)^{p+1}\tau^{q+1}}.
\]

Horizontal first moments vanish. The vertical centroid vanishes, equivalently
the displayed volume is minimized, at

\[
\tau=\frac{q+1}{d+1}.
\]

Substitution and multiplication by \(|J|\) prove the join formula.

## Four-dimensional consequences

The only nontrivial join split in dimension four, besides a pyramid, is
\((p,q)=(1,2)\). Using the sharp one- and two-dimensional inequalities,

\[
\mathcal P(K*L)
\ge
\frac{3125}{15552}\cdot4\cdot\frac{27}{4}
=\frac{3125}{576}.
\]

Equality forces \(K\) to be a segment and \(L\) a triangle; their join is a
4-simplex. Therefore:

> **Every four-dimensional affine join satisfies the sharp non-symmetric
> Mahler conjecture, with equality only for a simplex.**

This is a non-pyramidal infinite-family theorem. In particular, it closes
the affinely decomposable branch arising from a disconnected
facet-circuit graph.

Products and free sums are separated from equality by a strict margin:

\[
\mathcal P(K^2\times L^2),\ \mathcal P(K^2\oplus L^2)
\ge\frac{243}{32},
\]

and

\[
\mathcal P(K^1\times L^3),\ \mathcal P(K^1\oplus L^3)
\ge\frac{64}{9}.
\]

Both exceed \(3125/576\).

## Covariance-trace calculus

For a bi-centered \(m\)-body \(K\), write

\[
T(K)=\operatorname{tr}\bigl(
\operatorname{cov}(K)\operatorname{cov}(K^\circ)
\bigr).
\]

The same beta integrations, now with second moments, give

\[
\boxed{
T(K\times L)=T(K\oplus L)
=
\frac{
(p+1)(p+2)T(K)+(q+1)(q+2)T(L)
}{
(p+q+1)(p+q+2)
}.
}
\]

For example, the \(K^\circ\) covariance block in
\((K\times L)^\circ\) is

\[
\frac{(p+1)(p+2)}
{(p+q+1)(p+q+2)}
\operatorname{cov}(K^\circ);
\]

this follows by inserting the extra squared radial factor into the beta
integral. The other blocks and the free-sum identity follow symmetrically.

For the Santaló-centered affine join,

\[
\boxed{
T(K*L)
=
\frac{
1+(p+2)^2T(K)+(q+2)^2T(L)
}{
(p+q+3)^2
}.
}
\]

Here the horizontal blocks follow from beta second moments of the join
height and its polar height. Their one-dimensional height blocks contribute
the constant \(1\). Cross blocks vanish because both factors are
bi-centered.

These formulas pressure-test the connected trace-gap conjecture. A
segment--triangle join is a simplex and has \(T=1/9\), while the exact
segment--square join has

\[
T=\frac{17}{162}<\frac19.
\]

The formulas also show why decomposable bodies cannot be controlled by a
connected-circuit argument: the join height carries an independent harmonic
mode.

The normalized defect

\[
\delta_d(K)=(d+2)^2T(K)-d
\]

linearizes the join formula:

\[
\boxed{
\delta_{p+q+1}(K*L)=\delta_p(K)+\delta_q(L).
}
\]

Thus the trace ceiling is closed under joins and strictness is additive.
For products and free sums, with \(d=p+q\),

\[
\begin{aligned}
\delta_d(K\times L)=\delta_d(K\oplus L)
={}&-\frac{pq(d+4)}
{(d+1)(p+2)(q+2)}\\
&+\frac{d+2}{d+1}
\left(
\frac{p+1}{p+2}\delta_p(K)
+\frac{q+1}{q+2}\delta_q(L)
\right).
\end{aligned}
\]

So factors satisfying their trace ceilings give a strict product/free-sum
gap. In dimension four this conditional calculation gives
\(T\le23/225\) for a \(1+3\) split and \(T\le1/10\) for a \(2+2\) split.

## Exact checks

`harness/test_polytope.py` checks all factors as rational numbers. It also
constructs the Santaló-centered join of a segment and square and verifies
independently that

\[
\mathcal P([-1,1]*[-1,1]^2)=\frac{3125}{486},
\]

matching the factorization exactly. Its exact covariance matrices
independently reproduce \(T=17/162\).
