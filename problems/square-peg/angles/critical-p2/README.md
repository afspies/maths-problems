# The critical \(p=2\) frontier

**Status:** sharp analytic obstruction isolated; a Dini--Young positive
subclass is available.  No claim is made for all finite \(2\)-variation Jordan
curves.

The companion note `osgood-area-anomaly.md` proves a sharp embedded
counterexample to bare \(C^0\) primitive stability: a positive-area,
\(1/2\)-Hölder Jordan curve has inner and outer parameter-aligned smooth
Jordan approximations whose Liouville periods differ in the limit by exactly
the planar area of the trace. Thus the obstruction persists for finite
\(2\)-variation paths and does not rely on nonembedded repeated loops.

Antonelli--Young (arXiv:2605.15987, May 2026) independently develop a
geometric approximation criterion for signed area of \(1/2\)-Hölder planar
curves. Their beta-number framework is the most relevant published input for
the remaining **zero-area, local-primitive** frontier; the positive-area
inner/outer period anomaly below is logically separate.

## Why the proof stops at \(2\)

The estimate in the finite-\(p\) proof needs an exponent \(q<2\), so that
\(2/q>1\).  At \(q=2\), the Young constant diverges.  This is structural:
there are smooth closed paths \(z_n\) with
\[
             \|z_n\|_\infty\to0,\qquad
             \sup_n\|z_n\|_{2\text{-var}}<\infty
 \quad\text{but}\quad
             \int z_n^2\,dz_n^1\not\to0.             \tag{1}
\]
For example, set
\[
 z_n(t)=n^{-1/2}(e^{2\pi int}-1),\qquad 0\le t\le1.
\]
This traverses a circle of radius \(n^{-1/2}\) exactly \(n\) times with a
literal common basepoint.  Its image shrinks uniformly to a point, its
\(2\)-variation stays bounded, and its signed area with multiplicity is
constant.  Such examples are not Jordan curves; they show that uniform
convergence plus a critical variation bound does not control the primitive.
The missing datum is the antisymmetric second level (Lévy area).

Accordingly, a finite-\(2\)-variation Jordan path should be viewed as needing a
choice of geometric rough-path lift
\((c,\mathbb A)\).  Asano--Ike primitive convergence asks, in these terms, for
embedded smooth lifts whose \((x,y)\)-area component converges to
\(\mathbb A\).  Uniform convergence of the first level alone does not specify
that lift.

The displayed common-basepoint example is deliberately **not** offered as a
counterexample to Asano--Ike's embedded-approximation hypothesis.  Producing a
Jordan-specific area anomaly while retaining their fixed parametrization
would require an additional construction.

## A positive critical compactness lemma

The following classical Young--Dini condition gives a meaningful subclass at
the threshold.

**Lemma (Dini--Young primitive stability).**  Let \(c=(x,y):[0,T]\to\mathbb
R^2\) be continuous, and suppose
\[
 |x_t-x_s|\le\omega_x(|t-s|),\qquad
 |y_t-y_s|\le\omega_y(|t-s|)
\]
for increasing moduli with \(\omega_i(0)=0\) and
\[
       \int_0^T {\omega_x(r)\omega_y(r)\over r^2}\,dr<\infty. \tag{2}
\]
Then \(\int_0^t y\,dx\) exists as a Riemann--Stieltjes integral.  The
primitives of affine interpolants on any partitions of mesh tending to zero
converge uniformly to it.

**Proof with the quantitative tail.**  Put
\(\phi(r)=\omega_x(r)\omega_y(r)\) and
\[
                 J(h)=\int_0^{\min(2h,T)}{\phi(r)\over r^2}\,dr.
\]
Compare successive dyadic left Riemann sums on an interval \([s,t]\) of
length \(h\).  Inserting a midpoint changes the sum on each parent interval
by a product of one \(x\)-increment and one \(y\)-increment.  Summing the
geometric scales and using (2) gives a limit \(I_{s,t}\) satisfying
\[
 \left|I_{s,t}-y_s(x_t-x_s)\right|\le ChJ(h).          \tag{3}
\]
Additivity \(I_{s,t}=I_{s,u}+I_{u,t}\) holds first when \(u\) is a dyadic
split point, directly from the compatible sums, and then for arbitrary
\(u\in[s,t]\) by continuity from (3).
Consequently, for any partition \(\pi\) of mesh \(\delta\),
\[
 \left|I_{0,T}-\sum_{[u,v]\in\pi}y_u(x_v-x_u)\right|
 \le CTJ(\delta)\longrightarrow0.                     \tag{4}
\]
This proves convergence without appealing to a variation-increasing common
refinement.

At partition vertices, the integral of the affine interpolant is the
trapezoidal sum.  Its difference from the left sum is bounded by
\[
 {1\over2}\sum_{[u,v]\in\pi}|y_v-y_u|\,|x_v-x_u|
 \le {T\over2}\sup_{0<h\le\delta}{\phi(h)\over h}
 \longrightarrow0,                                   \tag{5}
\]
where Dini integrability implies \(\phi(h)/h\to0\).  Uniform convergence
between vertices follows from uniform continuity of \(t\mapsto I_{0,t}\) and
\[
 \left|\int_{t_i}^t y^\pi\,dx^\pi\right|
 \le\|y\|_\infty\omega_x(\delta)+\phi(\delta).         \tag{6}
\]
For arbitrary tagged sums, the tag change contributes at most
\[
 \sum_i|y_{\tau_i}-y_{t_i}|\,|x_{t_{i+1}}-x_{t_i}|
 \le T\sup_{0<h\le\delta}{\phi(h)\over h}\longrightarrow0. \tag{7}
\]
Thus the Riemann--Stieltjes integral is tag-independent and the
affine-interpolant primitives converge uniformly. \(\square\)

Combining this lemma with Boedihardjo--Geng's embedded polygonal
interpolation and the finite corner-rounding lemma proves the peg corollary.
For completeness, let \(a_n\) be the \(n\)-th Jordan polygon.  Since it has
finite variation, choose its smoothing \(b_n\) diagonally close enough that
\[
\begin{aligned}
\sup_t\left|\int_0^t y_{b_n}\,dx_{b_n}
             -\int_0^t y_{a_n}\,dx_{a_n}\right|
&\le \|y_{b_n}-y_{a_n}\|_\infty
       \operatorname{Var}(x_{b_n})\\
&\quad+\|y_{a_n}\|_\infty
       \operatorname{Var}(x_{b_n}-x_{a_n})<1/n.       \tag{8}
\end{aligned}
\]
The corner-rounding lemma permits arbitrarily small uniform and
\(1\)-variation errors for each fixed \(n\), so this diagonal choice is
available even when the polygonal lengths diverge.

**Critical rectangular-peg corollary.**  A Jordan parametrization satisfying
(2), with the moduli interpreted periodically using circular parameter
distance, meets Asano--Ike Theorem 1.1 and therefore inscribes every
prescribed rectangle.

This reaches a genuinely non-Hölder-above-\(1/2\) critical scale.  For example
the common modulus
\[
     \omega(r)={\sqrt r\over(\log(eT/r))^\beta},
     \qquad \beta>{1\over2},\quad 0<r\le T,            \tag{9}
\]
satisfies (2), while no estimate \(\omega(r)\le Cr^\alpha\) with
\(\alpha>1/2\) holds.  Thus (2) is not merely the finite-\(p<2\) theorem
rewritten with a Hölder exponent.

## Sharp formulation for future work

The next honest question is not “does finite \(2\)-variation imply a Young
integral?” (it does not).  It is:

> Which finite-\(2\)-variation Jordan curves possess a canonical geometric
> area lift that is the rough-path limit of *embedded* smooth
> approximations with the same parametrization?

Positive candidates include Dini--Young moduli, controlled paths with a
prescribed geometric \(2\)-rough lift and an embedded approximation theorem,
or curves with a quantitative one-sided/tubular geometry that forbids area
anomalies.  A decisive negative result would require two embedded
approximation sequences of the same parametrized Jordan curve with
incompatible primitive limits.
