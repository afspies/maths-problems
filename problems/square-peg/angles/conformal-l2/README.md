# Universal conformal \(L^2\) area primitives

## Status

For every bounded Jordan domain, the analytic level curves of its Riemann
map have centered Liouville primitives which converge strongly in \(L^2\)
in the harmonic-measure parameter.  This is a universal compactness theorem,
but it is not yet enough to verify the diagonal cohomology vanishing in
Asano--Ike Remark 4.2.

The result identifies the remaining obstruction more sharply: non-zero
shrink-out action can only be carried by exceptional parameter sets which
vanish in harmonic measure.  Microlocal sheaf cohomology can nevertheless
detect such sets, so a capacity or persistence argument is still needed.

## Theorem

Let \(\Omega\subset\mathbb C\) be a bounded Jordan domain and let
\[
  f(z)=\sum_{n=0}^{\infty}a_nz^n:\mathbb D\longrightarrow\Omega
\]
be conformal.  By Carathéodory, \(f\) extends homeomorphically to the closed
disk.  For \(0<r<1\), put
\[
  c_r(t)=f(re^{it}),\qquad 0\leq t\leq2\pi .
\]
Then \(c_r\) is a regular analytic Jordan parametrization and
\(c_r\to c_1\) uniformly.

Let
\[
  \alpha=\frac12(x\,dy-y\,dx)
\]
and let \(A_r\) be the area enclosed by \(c_r\).  There is a unique
mean-zero periodic function \(P_r\) satisfying
\[
  P_r'(t)=\alpha(c_r'(t))-\frac{A_r}{2\pi}.               \tag{1}
\]
There is a mean-zero \(P\in L^2(S^1)\) such that
\[
  P_r\longrightarrow P\quad\text{strongly in }L^2(S^1)
  \quad(r\uparrow1).                                      \tag{2}
\]
The same conclusion holds for \(\lambda=y\,dx\), after subtracting its
period and centering the primitive.

## Fourier proof

Use normalized Lebesgue measure \(dt/(2\pi)\) on \(S^1\).  Write
\[
  Df_r(t)=\sum_{n\geq0}n a_nr^ne^{int}.
\]
The density of \(c_r^*\alpha\) is
\[
  q_r(t)
  =\frac12\operatorname{Im}\bigl(\overline{f_r(t)}
     \partial_tf_r(t)\bigr)
  =\frac12\operatorname{Re}\bigl(\overline{f_r(t)}Df_r(t)\bigr).
                                                               \tag{3}
\]
For \(k\geq1\), define
\[
  C_{r,k}
   :=\sum_{m\geq0}\overline{a_m}a_{m+k}r^{2m+k},
\qquad
  D_{r,k}
   :=\sum_{m\geq0}m\,\overline{a_m}a_{m+k}r^{2m+k}.          \tag{4}
\]
Here \(C_{r,k}\) is the \(k\)-th Fourier coefficient of
\(\lvert f_r\rvert^2\).  Expanding (3) gives
\[
  \widehat q_r(k)=\frac14\bigl(kC_{r,k}+2D_{r,k}\bigr),
\qquad
  \widehat P_r(k)
  =\frac{C_{r,k}}{4i}+\frac{D_{r,k}}{2ik}.                  \tag{5}
\]
The negative coefficients are the complex conjugates and the zero
coefficient of \(P_r\) is zero.  Also
\[
  2\pi\widehat q_r(0)
  =\pi\sum_{n\geq1}n|a_n|^2r^{2n}=A_r,                    \tag{6}
\]
so (5) indeed describes (1).

The area formula for the univalent map \(f\) gives
\[
  E:=\sum_{n\geq1}n|a_n|^2=\frac{|\Omega|}{\pi}<\infty.    \tag{7}
\]
Consequently,
\[
\begin{aligned}
 |D_{r,k}|
 &\leq\sum_{m\geq1}m|a_m||a_{m+k}|\\
 &=\sum_{m\geq1}
   \sqrt{\frac m{m+k}}\,
   \bigl(\sqrt m|a_m|\bigr)
   \bigl(\sqrt{m+k}|a_{m+k}|\bigr)
 \leq E.                                                   \tag{8}
\end{aligned}
\]
For fixed \(k\), the absolutely convergent series in (4) therefore gives
\(D_{r,k}\to D_{1,k}\).  The uniform majorant
\[
  \left|\frac{D_{r,k}}k\right|\leq\frac Ek
\]
is square-summable over \(k\geq1\).  Hence
\[
  \left(\frac{D_{r,k}}k\right)_{k\geq1}
  \longrightarrow
  \left(\frac{D_{1,k}}k\right)_{k\geq1}
  \quad\text{in }\ell^2.                                  \tag{9}
\]

Carathéodory convergence is uniform on the closed disk, so
\[
  |f_r|^2\longrightarrow|f_1|^2
  \quad\text{uniformly on }S^1.
\]
Parseval therefore gives
\[
  (C_{r,k})_{k\in\mathbb Z}
  \longrightarrow(C_{1,k})_{k\in\mathbb Z}
  \quad\text{in }\ell^2.                                  \tag{10}
\]
Equations (5), (9), and (10), followed by Parseval once more, prove (2).

Finally,
\[
  y\,dx=\frac12d(xy)-\alpha.                               \tag{11}
\]
The exact-term primitives \(\frac12x_r(t)y_r(t)\) converge uniformly,
so (2) transfers to the Asano--Ike convention.

## Uniform convergence in measure of local increments

Strong \(L^2\) convergence gives a useful quantitative consequence.  If
\(\tau_hP(t)=P(t+h)\), then
\[
\begin{aligned}
 \|\tau_hP_r-P_r\|_2
 &\leq2\|P_r-P\|_2+\|\tau_hP-P\|_2 .
                                                               \tag{12}
\end{aligned}
\]
Thus, after taking \(r\) sufficiently close to \(1\), the right-hand side
tends to zero uniformly as \(h\to0\).  Chebyshev gives, for every
\(\varepsilon>0\),
\[
 \left|\left\{t:
 |P_r(t+h)-P_r(t)|>\varepsilon\right\}\right|
 \leq\varepsilon^{-2}\|\tau_hP_r-P_r\|_2^2\longrightarrow0. \tag{13}
\]
Therefore an order-one action carried by a shrinking boundary interval
must concentrate on a set of harmonic parameters of vanishing measure.

## An exhaustive conformal dichotomy

Let \(H_r\) be the mean-centered, non-periodic primitive on one period:
\[
 H_r(t)=\frac{A_r}{2\pi}(t-\pi)+P_r(t),\qquad0\leq t\leq2\pi. \tag{14}
\]
Define its asymptotic local oscillation by
\[
 \eta=\lim_{\delta\downarrow0}\limsup_{r\uparrow1}
 \sup_{\substack{s,t\in[0,2\pi]\\|s-t|\leq\delta}}
 |H_r(t)-H_r(s)|.                                        \tag{15}
\]
Exactly one of the following holds.

### Tame branch: \(\eta=0\)

The family \(H_r\), for \(r\) close to \(1\), is asymptotically
equicontinuous.  Its \(L^2\) convergence supplies a uniform bound at
least one point, and a finite \(\delta\)-chain then supplies a uniform
supremum bound.  Arzelà--Ascoli and uniqueness of the \(L^2\) limit show
that \(H_r\) converges uniformly to a continuous function.

By (11), the same is true for the \(\lambda=y\,dx\) primitives.  Hence the
analytic level curves satisfy Asano--Ike Theorem 1.1, and the boundary
inscribes every prescribed rectangle.

### Concentration branch: \(\eta>0\)

There are \(\varepsilon>0\), radii \(r_n\uparrow1\), and intervals
\(I_n=[s_n,t_n]\) with \(|I_n|\to0\) such that
\[
 \left|\int_{s_n}^{t_n}c_{r_n}^*\alpha\right|
 \geq\varepsilon.                                        \tag{16}
\]
Uniform convergence \(c_r\to c_1\) and uniform continuity of \(c_1\)
place the image arc \(c_{r_n}(I_n)\) in a disk of radius
\(\rho_n\to0\).  Close the arc by its straight chord.  The chord
contribution is \(o(1)\), so the resulting loop \(L_n\) has
\[
 \left|\int_{L_n}\alpha\right|\geq\varepsilon/2.           \tag{17}
\]
The area--winding formula and support in a disk of area
\(\pi\rho_n^2\) give
\[
 \|\operatorname{Wind}(L_n,\cdot)\|_\infty
 \geq\frac{\varepsilon}{2\pi\rho_n^2}\longrightarrow\infty.
                                                               \tag{18}
\]
After translating the disk to the origin,
\(\left|\int\alpha\right|\leq\rho_n\operatorname{length}(L_n)/2\);
thus also
\[
 \operatorname{length}(L_n)\geq\frac{\varepsilon}{\rho_n}. \tag{19}
\]

Consequently, failure of the Asano--Ike bridge for conformal level curves
is equivalent to concentration of unbounded winding multiplicity at a
prime end.  The null double spiral realizes this second branch
quantitatively: `../../results/null-spiral-conformal-concentration.md`
exhibits fixed action on cells whose harmonic measure is
\(\exp(-\Theta(V^2))\), while their area, Dirichlet energy, and critical
trace capacity tend to zero.

## Why this does not finish Square Peg

The diagonal object in Asano--Ike Remark 4.2 is a sheaf-cohomological
localization, not an \(L^2\) or almost-everywhere invariant.  A skyscraper
supported at one exceptional parameter can have non-zero cohomology.  The
null double spiral in
`../../results/null-spiral-no-primitive.md` has a logarithmically divergent
classical primitive at one parameter.  The theorem above says that its
conformal level primitives still converge strongly in \(L^2\); hence the
gap between \(L^2\) compactness and uniform primitive convergence is real.
The quantitative calculation in
`../../results/null-spiral-conformal-concentration.md` further shows that
ordinary harmonic-measure, \(W^{1,2}\), and critical capacity bounds cannot
close that gap.

The next required statement is one of the following:

1. a persistence lemma saying that diagonal classes supported on
   harmonic-measure-null parameter sets cannot carry the critical
   \(H^1(S^1)\) class used to define \(a(\theta,C)\); or
2. a counterexample showing that such a zero-measure diagonal class can
   survive with positive persistence.

Either statement would decisively settle the conformal route to
Asano--Ike Remark 4.2.
