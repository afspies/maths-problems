# Rectangular pegs on Jordan curves of subcritical variation

## Abstract

Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization of finite
\(p\)-variation for some \(p<2\). We record the apparently unstated
consequence that \(c\) satisfies the
smooth-approximation and Liouville-primitive convergence criterion of
Asano--Ike. It follows that \(c(S^1)\) inscribes a rectangle of every
prescribed aspect, and in particular a nondegenerate square. The proof
combines the parameter-respecting embedded polygonal interpolation theorem of
Boedihardjo--Geng with a fixed-parameter regular-\(C^1\) rounding lemma and an
explicit Young integral stability estimate. We also give a double-spiral Jordan curve of
infinite length that is not locally monotone but lies in the resulting class.
At the critical exponent \(p=2\), bounded variation and uniform convergence
do not determine the area primitive; the missing datum is a second-level
area lift. The unrestricted Square Peg conjecture remains open.

## 1. Introduction

For \(\theta\in(0,\pi)\), a \(\theta\)-rectangle means a rectangle whose
diagonals meet at angle \(\theta\); prescribing \(\theta\) is equivalent, up
to exchanging the sides, to prescribing its aspect ratio. The Rectangular
Peg problem asks whether every Jordan curve in the plane contains the four
vertices of a \(\theta\)-rectangle for every \(\theta\). The special case
\(\theta=\pi/2\) is the Square Peg conjecture.

Asano and Ike prove the prescribed-rectangle conclusion under the following
approximation criterion [AI, Theorem 1.1 and Remark 5.6]. Write
\(e:\mathbb R\to S^1=\mathbb R/T\mathbb Z\) for the quotient map and identify
\(\mathbb R^2\) with \(T^*\mathbb R\), with Liouville form
\(\lambda=y\,dx\). A parametrized Jordan curve \(c:S^1\to\mathbb R^2\)
satisfies their criterion if there are regular \(C^1\) Jordan embeddings
\(c_n:S^1\to\mathbb R^2\) such that

\[
 c_n\longrightarrow c\quad\text{uniformly on the same parameter circle},
 \tag{1.1}
\]

and primitives \(F_n:\mathbb R\to\mathbb R\) satisfying

\[
 dF_n=(c_n\circ e)^*\lambda
 \tag{1.2}
\]

converge locally uniformly. The additive constants may be fixed by
\(F_n(0)=0\). In particular, the criterion requires more than Hausdorff
convergence of unparametrized images.

Asano--Ike already deduce their criterion for every rectifiable Jordan curve
and every locally monotone Jordan curve [AI]. The purpose of this note is not
to reprove either result. Instead, we observe that published rough-path
approximation results supply their criterion for a different geometric
regularity class, including explicit curves of infinite length outside both
named corollaries.

For a continuous path \(z:[0,T]\to\mathbb R^m\), write

\[
 \|z\|_{p\text{-var};[0,T]}
 =
 \left(
 \sup_{\mathcal P}\sum_{[u,v]\in\mathcal P}|z_v-z_u|^p
 \right)^{1/p},
 \tag{1.3}
\]

where the supremum is over finite partitions. Finite \(p\)-variation is
unchanged by orientation-preserving reparametrization, so the class in the
following theorem is geometric.

## 2. Main theorem

**Theorem 2.1.**  
Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization. If \(c\) has finite
\(p\)-variation for some \(1\le p<2\), then \(c\) satisfies the Asano--Ike
criterion (1.1)--(1.2). Consequently \(c(S^1)\) inscribes a
\(\theta\)-rectangle for every \(\theta\in(0,\pi)\), and in particular a
nondegenerate square.

The proof uses two approximation facts. The first is due to
Boedihardjo--Geng.

**Theorem 2.2 (embedded polygonal approximation [BG]).**  
Let \(c:[0,T]\to\mathbb R^2\) parametrize a Jordan curve. There are
partitions \(\mathcal P_n\) with mesh tending to zero such that the affine
interpolants \(a_n=c^{\mathcal P_n}\), using the original parameter values,
are Jordan polygons. If, in addition, \(c\) has finite \(p\)-variation, the
partitions can be chosen so that, for every \(q>p\),

\[
 \|a_n-c\|_{q\text{-var};[0,T]}\longrightarrow0.
 \tag{2.1}
\]

Here the embedded interpolation is [BG, Theorem 2.2], and the variation
convergence is [BG, Lemma 3.1]. The embeddedness statement is essential: an
arbitrary polygonal approximation, and a fortiori an arbitrary mollification,
need not remain Jordan.

The second fact records the parameter control needed to pass from polygons to
smooth curves.

**Lemma 2.3 (fixed-parameter regular-\(C^1\) rounding).**  
Let \(a:S^1\to\mathbb R^2\) be a finite Jordan polygon, with its given
piecewise-affine parametrization. For every \(\varepsilon>0\), there is a
regular \(C^1\) Jordan embedding \(b:S^1\to\mathbb R^2\), on the same parameter
circle, such that

\[
 \|b-a\|_\infty<\varepsilon,
 \qquad
 \|b-a\|_{1\text{-var}}<\varepsilon.
 \tag{2.2}
\]

**Proof.**  
Retain every breakpoint of \(a\), including the cyclic seam. Choose pairwise
disjoint vertex disks \(D_j\), each meeting the polygon only in terminal
subsegments of its two incident edges. Let \(I_j\) be the original preimage
interval and let
\(\ell_j=\operatorname{len}(a(I_j))\).

At a noncollinear vertex, replace \(a|_{I_j}\) by a tangential fillet in the
empty local sector between the incident subsegments. Parametrize it regularly
on the same interval, matching the two constant endpoint velocities of
\(a\); an orientation-preserving \(C^1\) change of speed supplies the
prescribed positive endpoint speeds. If the incident directions are
positively collinear, retain the straight image and replace its
piecewise-constant positive speed by a positive \(C^1\) speed with the same
endpoint speeds and integral. Negative-collinear directions would retrace a
segment and cannot occur in a Jordan polygon.

The replacements lie in disjoint disks, meet the unchanged polygon only at
their endpoints, and are simple, so global injectivity is preserved. For a
fillet profile of length at most \(K_j\ell_j\),

\[
 \operatorname{Var}(b-a;I_j)
 \le
 \operatorname{len}(b|_{I_j})+\operatorname{len}(a|_{I_j})
 \le (K_j+1)\ell_j.
 \tag{2.3}
\]

With \(K=\max_jK_j\), shrink the disks until
\(\sum_j\ell_j<\varepsilon/(K+1)\) and
\(\max_j\operatorname{diam}D_j<\varepsilon\). This gives (2.2). Matching
endpoint values and velocities, including at the cyclic seam, makes the
result a regular \(C^1\) embedding. This regularity is sufficient by
[AI, Remark 5.6]. \(\square\)

## 3. Young stability and proof of Theorem 2.1

Fix

\[
 p<q<2.
 \tag{3.1}
\]

Apply Theorem 2.2 to obtain Jordan polygons \(a_n\) satisfying (2.1). Apply
Lemma 2.3 with errors tending to zero to obtain regular \(C^1\) Jordan embeddings
\(b_n=(x_n,y_n)\) such that

\[
 \|b_n-a_n\|_\infty+\|b_n-a_n\|_{1\text{-var}}\longrightarrow0.
 \tag{3.2}
\]

Since \(q\)-variation is bounded by \(1\)-variation, (2.1)--(3.2) imply

\[
 \|b_n-c\|_{q\text{-var};[0,T]}\longrightarrow0.
 \tag{3.3}
\]

In particular, \(b_n\to c=(x,y)\) uniformly and the \(q\)-variation norms of
the coordinates of \(b_n\) are uniformly bounded.

We next make the primitive convergence explicit. With the normalization
\(F_n(0)=F(0)=0\), set

\[
 F_n(t)=\int_0^t y_n\,dx_n,
 \qquad
 F(t)=\int_0^t y\,dx.
 \tag{3.4}
\]

All integrals exist as Young integrals because \(2/q>1\). We use the
Young--Loeve estimate in the following convenient, nonoptimal normalization:
if \(f,g\) have finite \(q\)-variation, then

\[
 \left|
 \int_s^t f\,dg-f_s(g_t-g_s)
 \right|
 \le C_q
 \|f\|_{q\text{-var};[s,t]}
 \|g\|_{q\text{-var};[s,t]},
 \qquad
 C_q=2\zeta(2/q).
 \tag{3.5}
\]

Subtracting two integrals as

\[
 \int_0^t y_n\,dx_n-\int_0^t y\,dx
 =
 \int_0^t (y_n-y)\,dx_n
 +
 \int_0^t y\,d(x_n-x)
 \tag{3.6}
\]

and applying (3.5) twice gives, uniformly in \(t\in[0,T]\),

\[
\begin{aligned}
 |F_n(t)-F(t)|
 &\le
 |y_n(0)-y(0)|\,\|x_n\|_{q\text{-var}}
 +C_q\|y_n-y\|_{q\text{-var}}\|x_n\|_{q\text{-var}}
 \\
 &\quad+
 |y(0)|\,\|x_n-x\|_{q\text{-var}}
 +C_q\|y\|_{q\text{-var}}\|x_n-x\|_{q\text{-var}}.
 \tag{3.7}
\end{aligned}
\]

By (3.3), the right-hand side tends to zero. Thus

\[
 \|F_n-F\|_{\infty;[0,T]}\longrightarrow0.
 \tag{3.8}
\]

The pulled-back one-forms are \(T\)-periodic and therefore

\[
 F_n(t+kT)=F_n(t)+kF_n(T),\qquad k\in\mathbb Z.
 \tag{3.9}
\]

Convergence in (3.8), including at \(T\), now implies local-uniform
convergence of \(F_n\) to \(F\) on the universal cover \(\mathbb R\).
Equations (3.3) and (3.8)--(3.9) are precisely the two hypotheses in the
Asano--Ike criterion. Their theorem supplies every prescribed rectangle,
which proves Theorem 2.1. \(\square\)

The normalization \(F_n(0)=0\) is only a choice of additive constants.
Translating the curve in the \(y\)-direction adds a constant multiple of
\(x(t)-x(0)\), which converges by (3.3). Reversing orientation changes the
sign of the period integral but not the existence of rectangles. No
area normalization is an additional hypothesis of Theorem 2.1.

## 4. A strict nonrectifiable example

Fix \(1<d<2\) and \(0<\delta<2\pi\). For \(\theta\ge1\), define

\[
 \gamma_0(\theta)=\theta^{-1/d}e^{i\theta},
 \qquad
 \gamma_1(\theta)=e^{i\delta}\gamma_0(\theta).
 \tag{4.1}
\]

Traverse \(\gamma_0\) from its limiting point \(0\) out to \(e^i\), join
\(e^i\) to \(e^{i(1+\delta)}\) along the corresponding unit-circle arc, and
traverse \(\gamma_1\) back to \(0\). Denote the resulting closed curve by
\(C_{d,\delta}\).

**Proposition 4.1.**  
\(C_{d,\delta}\) is a Jordan curve of infinite length, is not locally
monotone, and has finite \(p\)-variation for every \(p>d\). Consequently it
inscribes every prescribed rectangle.

**Proof.**  
The radius \(\theta^{-1/d}\) is strictly decreasing, so each spiral is
injective. Points on the two spirals having equal radius have equal
\(\theta\) and their arguments differ by \(\delta\notin2\pi\mathbb Z\);
hence the arms are disjoint away from \(0\). The unit-circle arc meets them
only at its endpoints. Parametrizing a tail by \(\theta=1/t\) and assigning
the value \(0\) at \(t=0\) produces an explicit continuous compactification.
Thus the closed parametrization is injective on the parameter circle.

Moreover,

\[
 |\gamma_0'(\theta)|
 =
 \sqrt{\theta^{-2/d}+d^{-2}\theta^{-2/d-2}}
 \ge \theta^{-1/d}.
 \tag{4.2}
\]

The length therefore dominates a constant multiple of
\(\sum_{n\ge1}n^{-1/d}\), which diverges.

To estimate variation, divide a spiral into full-turn blocks
\(I_n=[2\pi n,2\pi(n+1)]\). Its length on \(I_n\) is
\(L_n=O(n^{-1/d})\). Given any partition, increments lying inside one block
contribute at most \(L_n^p\). Assign each increment that crosses a block
boundary to its starting block. At most one such increment is assigned to a
given block, and radial monotonicity bounds it by \(O(n^{-1/d})\). Hence

\[
 \sum |\Delta\gamma_j|^p
 \le C_p\sum_{n\ge1}n^{-p/d}<\infty
 \qquad(p>d).
 \tag{4.3}
\]

The joining arc has finite variation. Since \(d<2\), one can choose
\(p\in(d,2)\), and Theorem 2.1 applies.

Finally, the projection of either spiral onto a line making angle \(\phi\)
with the positive real axis is

\[
 \theta^{-1/d}\cos(\theta-\phi).
 \tag{4.4}
\]

It changes sign infinitely often on every tail at \(0\). No linear
projection is therefore monotone on a one-sided neighborhood of that point,
so the curve is not locally monotone in the sense used by Stromquist and
Asano--Ike. \(\square\)

This example is outside both the rectifiable and locally monotone classes
named in [AI]; it is not merely a different parametrization of a rectifiable
curve.

## 5. The critical \(p=2\) boundary

The proof above requires \(q<2\), equivalently \(2/q>1\). At \(q=2\), the
Young constant diverges, and this reflects a genuine area instability. For
\(0\le t\le1\), let

\[
 z_n(t)=n^{-1/2}\bigl(e^{2\pi int}-1\bigr).
 \tag{5.1}
\]

Then \(z_n\to0\) uniformly and
\(\sup_n\|z_n\|_{2\text{-var}}<\infty\), but the signed area, counted with
multiplicity, is independent of \(n\). Equivalently, the Liouville integrals
\(\int z_n^2\,dz_n^1\) do not converge to the primitive of the zero path.
These \(z_n\) retrace the same small circle and are not Jordan curves; thus
(5.1) is not a counterexample to the Asano--Ike approximation criterion for
Jordan curves. It shows only that uniform convergence plus bounded
\(2\)-variation cannot determine the primitive. At this exponent one must
control an antisymmetric second-level, or Lévy-area, lift.

A useful positive condition at the threshold is the Dini--Young hypothesis.

**Proposition 5.1 (Dini--Young extension).**  
Suppose that a Jordan parametrization \(c=(x,y)\) has coordinate moduli

\[
 |x_t-x_s|\le\omega_x(|t-s|),\qquad
 |y_t-y_s|\le\omega_y(|t-s|)
 \tag{5.2}
\]

and that

\[
 \int_0^T\frac{\omega_x(r)\omega_y(r)}{r^2}\,dr<\infty,
 \tag{5.3}
\]

Then \(c\) satisfies the Asano--Ike criterion and hence inscribes every
prescribed rectangle.

**Proof.**  
Put \(\phi(r)=\omega_x(r)\omega_y(r)\) and

\[
 J(h)=\int_0^{\min(2h,T)}\frac{\phi(r)}{r^2}\,dr.
 \tag{5.4}
\]

On an interval \([s,t]\) of length \(h\), compare successive dyadic left
Riemann sums for \(\int_s^t y\,dx\). Inserting one midpoint changes the
corresponding summand by a product of one \(x\)-increment and one
\(y\)-increment. Summation over all intervals and scales, followed by the
integral comparison for the increasing function \(\phi\), gives a limit
\(I_{s,t}\) with

\[
 |I_{s,t}-y_s(x_t-x_s)|\le C hJ(h).
 \tag{5.5}
\]

The dyadic construction gives
\(I_{s,t}=I_{s,u}+I_{u,t}\) first at dyadic split points and then at every
\(u\), by continuity from (5.5). Hence, for every partition \(\pi\) of mesh
\(\delta\),

\[
 \left|
 I_{0,T}-\sum_{[u,v]\in\pi}y_u(x_v-x_u)
 \right|
 \le CTJ(\delta)\longrightarrow0.
 \tag{5.6}
\]

The same holds uniformly on terminal subintervals. The difference between
the left sum and the trapezoidal sum is at most

\[
 \frac12\sum_{[u,v]\in\pi}|y_v-y_u|\,|x_v-x_u|
 \le
 \frac T2\sup_{0<h\le\delta}\frac{\phi(h)}h
 \longrightarrow0,
 \tag{5.7}
\]

where (5.3) implies \(\phi(h)/h\to0\). The trapezoidal sums are exactly the
Liouville integrals of the affine interpolants at partition vertices;
uniform convergence between vertices follows from

\[
 \left|\int_{t_i}^t y^\pi\,dx^\pi\right|
 \le \|y\|_\infty\omega_x(\delta)+\phi(\delta).
 \tag{5.8}
\]

Choose the embedded affine interpolants supplied by Theorem 2.2. For the
\(n\)-th polygon \(a_n\), use Lemma 2.3 to choose a regular \(C^1\) Jordan embedding
\(b_n\) so close in uniform and \(1\)-variation norms that

\[
\begin{aligned}
\sup_t\left|
\int_0^t y_{b_n}\,dx_{b_n}
-
\int_0^t y_{a_n}\,dx_{a_n}
\right|
&\le
\|y_{b_n}-y_{a_n}\|_\infty\,
\operatorname{Var}(x_{b_n})
\\
&\quad+
\|y_{a_n}\|_\infty\,
\operatorname{Var}(x_{b_n}-x_{a_n})
<\frac1n.
\tag{5.9}
\end{aligned}
\]

This diagonal choice is possible for each fixed polygon, even if their
lengths are not uniformly bounded. Equations (5.6)--(5.9) give the required
uniform primitive convergence on one period, and periodicity promotes it to
local-uniform convergence on \(\mathbb R\), as in (3.9). \(\square\)

Condition (5.3) includes the critical modulus

\[
 \omega(r)=\frac{\sqrt r}{(\log(eT/r))^\beta},
 \qquad \beta>\frac12,
 \tag{5.10}
\]

which is not bounded by \(Cr^\alpha\) for any \(\alpha>1/2\).

The unresolved critical question is geometric:

> Which finite-\(2\)-variation Jordan curves possess a canonical area lift
> realizable as the limit of smooth embedded approximations on the same
> parameter circle?

A negative answer for the full class would require two embedded approximation
sequences of the same parametrized Jordan curve whose normalized Liouville
primitives have incompatible limits. Example (5.1) does not provide this.

## 6. Attribution and publication status

The two principal inputs are published or publicly available results:
Boedihardjo--Geng prove the embedded polygonal approximation and
\(q\)-variation convergence, while Asano--Ike prove that smooth embedded
approximation with locally uniform primitive convergence implies the
rectangular-peg conclusion. The contribution isolated here is their short
combination through Young stability, together with Lemma 2.3 and the strict
double-spiral witness.

A targeted literature search through 24 July 2026 found no prior paper
stating Theorem 2.1 in finite-\(p\)-variation language. That search is not a
proof of priority. Before submission, the attribution and novelty claim
should be confirmed with the authors or another specialist, and Lemma 2.3
should receive an independent referee-style check. No claim is made here to
settle the unrestricted Square Peg conjecture.

## References

**[AI]** T. Asano and Y. Ike, *The rectifiable rectangular peg problem*,
arXiv:2412.21057v3 (2026).

**[BG]** H. Boedihardjo and X. Geng, *Simple piecewise geodesic interpolation
of simple and Jordan curves with applications*, Constructive Approximation
**42** (2015), 161--180. DOI:
[10.1007/s00365-014-9257-z](https://doi.org/10.1007/s00365-014-9257-z).

**[St]** W. Stromquist, *Inscribed squares and square-like quadrilaterals in
closed curves*, Mathematika **36** (1989), 187--197.

**[Y]** L. C. Young, *An inequality of the Hölder type, connected with
Stieltjes integration*, Acta Mathematica **67** (1936), 251--282. DOI:
[10.1007/BF02401743](https://doi.org/10.1007/BF02401743).
