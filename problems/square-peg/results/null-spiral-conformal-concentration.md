# Vanishing-capacity conformal action concentration

## Result

The null double spiral in `null-spiral-no-primitive.md` realizes the
concentration branch of the universal conformal \(L^2\)-primitive theorem.
More precisely, it has prime-end boundary intervals \(I_V\), shrinking to
one point in harmonic measure, on which a fixed positive Liouville action
survives.  The corresponding spiral cells have simultaneously:

\[
\begin{array}{c|c}
\text{quantity}&\text{scale as }V\to\infty\\ \hline
\text{action}&\varepsilon\\
\text{Euclidean diameter}&\asymp V^{-1/2}\\
\text{winding multiplicity}&\asymp V\\
\text{length}&\asymp V^{1/2}\\
\text{area and Dirichlet energy}&\asymp V^{-1}\\
\text{condenser capacity}&\asymp V^{-2}\\
\text{harmonic measure}&\exp(-\Theta(V^2)).
\end{array}
\]

Thus neither finite conformal Dirichlet energy, harmonic-measure
absolute continuity, nor critical trace capacity can upgrade the universal
\(L^2\) lift to a continuous primitive.  The limiting exceptional prime end
has zero \(C_{1/2,2}\) trace capacity.

## The logarithmic strip

Put
\[
 a(v)=v^{-1/2},\qquad
 b(v)=\frac{a(v)+a(v+2\pi)}2 .
\]
The spiral portion of the enclosed domain lifts under the exponential map
to
\[
 {\cal S}=\{(u,v):\log b(v)<u<\log a(v),\ v>v_0\}.        \tag{1}
\]
The exponential map is injective on this strip.  Indeed,
\[
 a(v)>b(v)>a(v+2\pi),
\]
so the radial intervals in (1) for heights differing by a non-zero
multiple of \(2\pi\) are disjoint.

Write
\[
 h(v)=\log\frac{a(v)}{b(v)},\qquad
 m(v)=\frac{\log a(v)+\log b(v)}2 .
\]
Taylor expansion gives
\[
 h(v)=\frac{\pi}{2v}-\frac{5\pi^2}{8v^2}+O(v^{-3}),
 \qquad
 m'(v)=-\frac1{2v}+O(v^{-2}).                            \tag{2}
\]
Straighten (1) by
\[
 u=m(v)+h(v)X,\qquad
 s=\int_{v_0}^{v}\frac{d\xi}{h(\xi)},\qquad
 -\frac12<X<\frac12 .
\]
In \((X,s)\) coordinates the derivative is
\[
 h(v)
 \begin{pmatrix}
 1&m'(v)+Xh'(v)\\
 0&1
 \end{pmatrix}.                                          \tag{3}
\]
On every slab \(V\leq v\leq cV\), with fixed \(c>1\), (3) is
\((1+O(V^{-1}))\)-quasiconformal.  Its longitudinal extremal length is
therefore
\[
 M(V,cV)
  =(1+O(V^{-1}))\int_V^{cV}\frac{dv}{h(v)}
  =\frac{(c^2-1)V^2}{\pi}+O(V).                          \tag{4}
\]
With the reciprocal convention, the condenser capacity of the two ends
of the slab is
\[
 \operatorname {Cap}(V,cV)
 =\frac{\pi}{(c^2-1)V^2}\bigl(1+O(V^{-1})\bigr).         \tag{5}
\]

## Fixed action with vanishing energy

On the inward arm \(r=a(v)\), for
\(\alpha=(x\,dy-y\,dx)/2\),
\[
 \int_V^{cV}\alpha
 =\frac12\int_V^{cV}a(v)^2\,dv
 =\frac12\log c.                                         \tag{6}
\]
Given \(\varepsilon>0\), choose \(c=e^{2\varepsilon}\); then (6) is exactly
\(\varepsilon\).

The Euclidean area between the two arms over the same slab is
\[
 \frac12\int_V^{cV}(a(v)^2-b(v)^2)\,dv
 =\frac{\pi(1-c^{-1})}{2V}+O(V^{-2}).                    \tag{7}
\]
This is also the conformal Dirichlet energy divided by two.  Meanwhile the
cell lies in a disk of radius \(O(V^{-1/2})\), its inward side has length
\(\asymp V^{1/2}\), and it makes \(\asymp V\) turns.  Equations (5)--(7)
therefore give all the scales in the table above and saturate, up to
constants, the winding and length lower bounds from the conformal
concentration dichotomy.

## Harmonic-measure scale and the bad branch

The long-rectangle estimate applied to (4) says that, from any fixed
compact part of the domain, the harmonic measure of the boundary tail
beyond height \(V\) is
\[
 \exp(-\Theta(M(v_0,V)))=\exp(-\Theta(V^2)).              \tag{8}
\]
Equivalently, under the Carathéodory boundary parametrization, both
endpoints of the inward-arm segment \(V\leq v\leq cV\) approach the same
circle parameter and their separation tends to zero at the scale (8).

Let \(f:\mathbb D\to\Omega\) be the Riemann map and
\(c_r(t)=f(re^{it})\).  For each fixed \(V\), the relevant inward-arm
segment is analytic and separated from the spiral endpoint.  Schwarz
reflection across that compact segment gives \(C^1\) convergence of
\(c_r\) to the boundary there.  Choose \(V_n\to\infty\), then choose
\(r_n\uparrow1\) diagonally so that the primitive increment on the analytic
level arc differs from (6) by \(o(1)\).  The parameter intervals shrink by
(8), but their primitive increments tend to \(\varepsilon\).  Hence the
asymptotic local oscillation \(\eta\) in
`../angles/conformal-l2/README.md` is positive.

Finally, the boundary primitive on the inward arm grows as
\[
 \frac12\log V.
\]
Combining this with (8) shows that in harmonic parameter \(s\) its
singularity has the scale
\[
 \frac14\log\log\frac1{|s-s_0|}+O(1).                    \tag{9}
\]
It belongs locally to every finite \(L^p\), consistently with the
universal strong-\(L^2\) theorem, but is unbounded at \(s_0\).  In the
critical trace-capacity normalization,
\[
 C_{1/2,2}(J_V)\asymp\frac1{\log(1/|J_V|)}
 \asymp V^{-2},
\]
so the limiting singleton has zero capacity.  This does not assert that
the primitive lies in \(H^{1/2}\); it says that the boundary trace of the
Riemann map is permitted to ignore exactly the exceptional point.

## Consequence

The conformal route is now sharp at the level of classical analytic
compactness.  Any unrestricted proof must use information that survives
fixed action on vanishing-capacity sets—precisely the bar pairing or
diagonal \(\mu hom\) structure—not merely improve the integrability,
energy, harmonic-measure, or capacity estimate for the primitive.
