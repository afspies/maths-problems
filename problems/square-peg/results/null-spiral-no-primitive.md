# A null Jordan curve with no continuous approximating area primitive

## Theorem

There is a Jordan parametrization \(c:S^1\to\mathbb R^2\) whose trace has
planar measure zero and which admits no parameter-aligned sequence of regular
\(C^1\) Jordan embeddings with locally uniformly convergent Liouville
primitives.  In particular, this curve does not satisfy the hypotheses of
Asano--Ike Theorem 1.1.

This is an obstruction to that sufficient criterion, not a counterexample to
Square Peg.

## Construction

Let \(\theta_0=2\pi\).  For \(\theta\geq\theta_0\), set
\[
a(\theta)=\theta^{-1/2},\qquad
b(\theta)=\frac{a(\theta)+a(\theta+2\pi)}2,
\]
\[
A(\theta)=a(\theta)e^{i\theta},\qquad
B(\theta)=b(\theta)e^{i\theta}.                           \tag{1}
\]
On the parameter circle \([0,3]/(0\sim3)\), define
\[
c(t)=
\begin{cases}
A\!\left(\dfrac{\theta_0}{1-t}\right),&0\leq t<1,\\[1ex]
0,&t=1,\\[1ex]
B\!\left(\dfrac{\theta_0}{t-1}\right),&1<t\leq2,\\[1ex]
\left[b(\theta_0)+(t-2)(a(\theta_0)-b(\theta_0))\right]
e^{i\theta_0},&2\leq t\leq3.
\end{cases}                                               \tag{2}
\]

Thus the curve follows \(A\) inward, follows the interleaved arm \(B\)
outward, and closes across the outer radial gap.

## Jordan and measure checks

Strict decrease of \(a\) gives
\[
a(\theta)>b(\theta)>a(\theta+2\pi)>b(\theta+2\pi).         \tag{3}
\]
Each arm is injective.  Two polar points can agree only if their angles differ
by \(2\pi k\), and (3) rules out every intersection between the arms.  They
share only their limiting point \(0\).  The closing segment uses radii
\([b(\theta_0),a(\theta_0)]\); all later turns lie below
\(a(\theta_0+2\pi)<b(\theta_0)\).  Hence (2) is Jordan.

Each finite piece of either arm is a \(C^1\) rectifiable arc.  The trace is a
countable union of such pieces, a segment, and one point, so its planar
Lebesgue measure is zero.

The bounded component is the disjoint spiral strip
\[
\Omega=\{re^{i\theta}:\theta>\theta_0,\ b(\theta)<r<a(\theta)\}.
\]
Its area is
\[
|\Omega|
=\frac12\int_{\theta_0}^{\infty}
  \bigl(a(\theta)^2-b(\theta)^2\bigr)\,d\theta<\infty.      \tag{4}
\]
Indeed,
\[
a-b=O(\theta^{-3/2}),\qquad a+b=O(\theta^{-1/2}),
\]
so the integrand is \(O(\theta^{-2})\).

## Divergent local action

For
\[
\alpha=\frac12(x\,dy-y\,dx)=\frac12r^2\,d\theta,
\]
the inward arm satisfies
\[
\int_{\theta_0}^{\Theta}A^*\alpha
=\frac12\int_{\theta_0}^{\Theta}\frac{d\theta}{\theta}
=\frac12\log\frac{\Theta}{\theta_0}.                       \tag{5}
\]
For the Asano--Ike convention \(\lambda=y\,dx\),
\[
\lambda=\frac12d(xy)-\alpha.
\]
The exact term stays bounded and tends to zero at the origin, so the
\(\lambda\)-primitive tends to \(-\infty\) along \(A\).

Suppose regular \(C^1\) Jordan embeddings \(c_n\to c\) uniformly had
normalized \(\lambda\)-primitives converging locally uniformly to a continuous
function \(f\).  The local action-rigidity lemma proved in
`../angles/unrestricted-zero-trace/README.md` applies on the smooth interval
\((0,1)\), and gives
\[
f(t)-f(s)=\int_s^t c^*\lambda\qquad(0<s<t<1).
\]
Letting \(t\uparrow1\) contradicts (5) and continuity of \(f\) at the finite
parameter value \(1\).  Therefore no such approximation sequence exists.

## Explicit embedded approximation anomaly

Let \(\Theta_N=\theta_0+2\pi N\), and truncate the strip at
\(\theta=\Theta_N\).  Its boundary follows \(A\) inward, crosses radially to
\(B\), follows \(B\) outward, and closes at \(\theta_0\).  These are nested
Jordan domains whose parametrized boundaries converge uniformly to (2).

At the middle of the shrinking inner cap, the normalized primitives satisfy
\[
\int\alpha=\frac12\log\frac{\Theta_N}{\theta_0},\qquad
\int\lambda=-\frac12\log\frac{\Theta_N}{\theta_0}+O(1).    \tag{6}
\]
Their periods nevertheless converge:
\[
\oint_{\partial\Omega_N}\lambda
\longrightarrow-|\Omega|,                                \tag{7}
\]
by (4).  Rounding the finitely many corners inside disjoint disks changes
the local actions by the disks' areas.  Choosing the rounding scales
diagonally gives smooth embedded parameter-aligned approximants for which
(6) still diverges and (7) still converges.

Thus the obstruction is local, not a failure of total-area stability.

## Variation boundary

One full turn at radius \(\asymp k^{-1/2}\) contributes
\(\asymp k^{-p/2}\) to \(p\)-variation.  Hence this example has infinite
\(2\)-variation.  It does not contradict the finite-\(p<2\), Dini--Young, or
Antonelli--Young positive classes proved elsewhere in this folder.
