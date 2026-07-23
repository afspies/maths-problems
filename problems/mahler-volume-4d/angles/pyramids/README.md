# Terminality descent for pyramids

**Status:** sharp Mahler inequality proved for the entire infinite family;
terminality descent independently gives the requested classification route.

## Direct volume-product factorization

For a \(d\)-pyramid, affine invariance allows
\[
P=\operatorname{conv}(K\times\{0\},(0,1)),
\]
where the Santaló point of the \((d-1)\)-body \(K\) is the origin. Put
\(z=(0,\tau)\). The polar of \(P-z\) has height coordinate
\[
-1/\tau\le r\le1/(1-\tau)
\]
and horizontal section
\[
\{y:h_K(y)\le1+r\tau\}=(1+r\tau)K^\circ.
\]
Because \(c(K^\circ)=0\), the horizontal centroid of this polar is zero. Its
vertical centroid is zero exactly at \(\tau=1/(d+1)\), as follows from
\[
\int_0^{(d+1)/d}(u-1)u^{d-1}\,du=0.
\]
The centroid--Santaló duality therefore identifies
\[
s(P)=(0,1/(d+1)).
\]
Now
\[
|P|=\frac{|K|}{d},\qquad
|(P-s(P))^\circ|
=\frac{|K^\circ|}{d\,\tau(1-\tau)^d},
\]
and hence
\[
\mathcal P(P)
=\frac{(d+1)^{d+1}}{d^{d+2}}\mathcal P(K). \tag{V}
\]

Taking \(d=4\) and applying the audited three-dimensional theorem gives
\[
\mathcal P(P)\ge
\frac{5^5}{4^6}\frac{4^4}{(3!)^2}
=\frac{3125}{576},
\]
with equality exactly when \(K\) is a tetrahedron, equivalently when \(P\) is
a 4-simplex.

This proof is stronger than an exclusion from minimization and does not use
the four-dimensional terminal reduction.

## Terminality descent

Let \(P=\operatorname{pyr}(Q)\) be a 4-polytope with 3-dimensional base \(Q\).
After an affine normalization, put the base in
\(\mathbb R^3\times\{0\}\) and the apex outside that hyperplane. For a tangent
direction \(\theta=(u,0)\):

- the base facet is parallel to \(\theta\) and imposes no equation;
- a side facet \(\operatorname{pyr}(H)\) is parallel to \(\theta\) exactly
  when the base facet \(H\) is parallel to \(u\); and
- on a constrained side facet, an affine speed consists exactly of an affine
  speed on \(H\) plus an independently chosen apex value.

Consequently there are natural identifications
\[
A_{(u,0)}(P)\cong A_u(Q)\oplus\mathbb R,\qquad
T(P)\cong T(Q)\oplus\mathbb R. \tag{1}
\]
Thus terminality of \(P\) in all directions implies terminality of \(Q\).

The face-lattice dual of a pyramid is again a pyramid: the facet dual to the
apex contains every dual vertex except the vertex dual to the base. Therefore
if a dual \(P^\ast\) is also terminal, its 3-dimensional base \(R\), whose
face lattice is dual to that of \(Q\), is terminal by the same argument.

The counting proof of Chen--Li--Xi--Xu's 3D terminal lemma only uses that the
two terminal 3-polytopes have dual face lattices. It does not require \(R\) to
be the Santaló polar of this particular realization of \(Q\). Applied to
\((Q,R)\), it forces \(Q\) and \(R\) to be tetrahedra. Hence:

> **Pyramid theorem.** If a 4-dimensional pyramid and a face-lattice dual
> realization both admit only globally affine admissible speeds in every
> direction, then the pyramid is a 4-simplex.

Combining this theorem with the audited minimizer-to-terminal reduction gives
an independent proof that every non-simplex 4-dimensional pyramid is excluded
from minimization. This is an infinite-family proof, not an enumeration.

The exact harness checks the descent pattern on the pyramid over a cube:
a generic tangent direction has dimension five, while a direction parallel
to a side of the base produces a nontrivial speed. This calculation is a
sanity check only; the theorem above is the certificate.
