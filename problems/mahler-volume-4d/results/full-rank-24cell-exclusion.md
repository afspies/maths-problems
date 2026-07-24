# Eight smooth 24-cell families are projective saddles

## Theorem

Fix \(s_1,s_2,s_3\in\{-1,1\}\) and \(0\le x<1\). Put

\[
r=x^2,\qquad
A=\frac2{1+r},\qquad
B_i=\frac{2s_i x}{1+r}.
\]

Let \(K_{x,s}\) be the convex hull of the 16 vertices of \([-1,1]^4\)
and the following eight points:

\[
\begin{array}{rrrr}
-A&-B_1&-B_2&-B_3\\
 A& B_1& B_2& B_3\\
 B_1&-A& B_3&-B_2\\
-B_1& A&-B_3& B_2\\
 B_2&-B_3&-A& B_1\\
-B_2& B_3& A&-B_1\\
 B_3& B_2&-B_1&-A\\
-B_3&-B_2& B_1& A .
\end{array}
\]

These are the eight one-parameter 24-cell families of
Rastanawi--Sinn--Ziegler. They are centrally symmetric and satisfy

\[
|K_{x,s}|=\frac{32}{1+r},\qquad
|K_{x,s}^\circ|=\frac{3+r}{6},
\]

so

\[
\boxed{\mathcal P(K_{x,s})
=\frac{16(3+r)}{3(1+r)}.}
\]

Their covariance matrices are scalar:

\[
\operatorname{cov}(K_{x,s})
=a(r)I_4,\qquad
a(r)=\frac{13+22r+5r^2}{30(1+r)^2},
\]

\[
\operatorname{cov}(K_{x,s}^\circ)
=b(r)I_4,\qquad
b(r)=\frac{39+27r-3r^2+r^3}{240(3+r)}.
\]

For every \(0\le r<1\),

\[
a(r)b(r)<\frac1{36}.
\]

Thus every member violates the necessary projective covariance condition for
a local Mahler minimum. For \(0<x<1\), the incidence Jacobian has full rank
144 [rastanawi-sinn-ziegler-2020]. Consequently these curves lie in the
smooth 48-dimensional stratum of the 24-cell realization space, and
continuity excludes an open neighborhood of every curve point from local
Mahler minimality.

For the last assertion, first apply the continuously varying Santaló
translation. Nearby bodies with nonzero primal centroid fail the first
projective variation. If that centroid vanishes, the strictly negative
covariance eigenvalue persists and fails the second variation.

This is an open-set exclusion inside a genuinely full-dimensional smooth
realization stratum, not a classification of all 24-cells.

## Exact geometric calculation

Each of the eight added vertices lies beyond one cube facet and beneath the
other seven. The corresponding eight pyramids have disjoint interiors.
Their base volume is \(8\), height \(A-1\), and four-dimensional volume
\(2(A-1)\). Hence

\[
|K_{x,s}|=16+16(A-1)=16A=\frac{32}{1+r}.
\]

The polar starts from the cross-polytope

\[
[-1,1]^{4\circ}=\{y:\|y\|_1\le1\}.
\]

The eight new inequalities cut disjoint caps at its eight vertices.
Triangulate each octahedral cap base into tetrahedra. The determinant and
second-moment simplex formulas give, after summing the eight sign-related
caps,

\[
\left|[-1,1]^{4\circ}\setminus K_{x,s}^\circ\right|
=\frac{1-r}{6}
\]

and, in each coordinate,

\[
\int_{[-1,1]^{4\circ}\setminus K_{x,s}^\circ} y_i^2\,dy
=\frac{(1-r)(r^2-2r+25)}{1440}.
\]

Since the cross-polytope has volume \(2/3\) and coordinate second moment
\(2/45\), this yields

\[
|K_{x,s}^\circ|=\frac{3+r}{6},
\qquad
\int_{K_{x,s}^\circ}y_i^2\,dy
=\frac{39+27r-3r^2+r^3}{1440}.
\]

The same tetrahedral decomposition of the eight primal pyramids gives

\[
\int_{K_{x,s}}y_i^2\,dy
=\frac{16(13+22r+5r^2)}{15(1+r)^3}.
\]

The order-24 symmetry makes all mixed moments zero and all diagonal moments
equal. Dividing the displayed moments by the volumes proves the covariance
formulas.

## Strict covariance obstruction

Direct multiplication gives

\[
\frac1{36}-a(r)b(r)
=
\frac{
93+191r+250r^2+118r^3-7r^4-5r^5
}{
7200(1+r)^2(3+r)
}.
\]

The numerator is strictly positive on \(0\le r\le1\), since it equals

\[
93+191r+250r^2+106r^3
+r^3(1-r)(5r+12).
\]

At a bi-centered local minimizer in dimension four one must have

\[
\operatorname{cov}(K^\circ)
\succeq \frac1{36}\operatorname{cov}(K)^{-1}.
\]

For scalar covariance matrices this requires \(a(r)b(r)\ge1/36\), the
opposite of the strict inequality above.

## Verification

`harness/polytope.py` constructs all eight signed families and records the
closed formulas. The unit test independently enumerates the facets, checks
144 incidences, verifies Jacobian rank 144 at \(x=1/2\), and reproduces both
volumes and covariance matrices with exact `Fraction` arithmetic.
