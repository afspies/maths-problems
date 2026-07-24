# The null spiral's vanishing-width microlocal eye

## Finite truncations

Let \(C_N\) be a smooth rounded finite truncation of the null double
spiral, scaled to enclose area \(\pi\), and let \(F_N\) be its torus
quantization.  The diagonal is a clean Morse--Bott component.  Its local
Floer cohomology is
\[
 H^*(S^1;\mathbb F_2)
\]
entirely at action \(0\pmod\pi\).  Consequently,
\[
 R\Gamma\!\left(\rho^{-1}\Delta_{C_N};
 \mu hom(F_N,T_aR_\theta F_N)|_{\rho^{-1}\Delta_{C_N}}\right)=0
 \quad(a\notin\pi\mathbb Z).                             \tag{1}
\]
Thus no finite truncation contains an interior-action diagonal term.

## Full action support in the limit

On the inward arm
\[
 A(\theta)=\theta^{-1/2}e^{i\theta},
\]
the \(\lambda=y\,dx\) primitive, up to an additive constant, is
\[
 f_A(\theta)
 =\frac{\sin(2\theta)}{4\theta}
  -\frac12\log\frac{\theta}{\theta_0}.                   \tag{2}
\]
If \(s^2=\pi/|\Omega|\) is the area-normalizing scale, the product
diagonal phase is therefore
\[
 t_{AA}(\theta)
 =s^2\left(
 \log\frac{\theta}{\theta_0}
 -\frac{\sin(2\theta)}{2\theta}\right)+t_0
 \pmod\pi .                                              \tag{3}
\]
It is continuous and unbounded.  Every action phase is consequently a
limit of phases above points \((A(\theta),A(\theta))\) tending to the
collapsed spiral point.  Closedness of the reduced microsupport projection
gives the whole \(t\)-circle over that point:
\[
 \{((0,0),t):t\in\mathbb R/\pi\mathbb Z\}
 \subset SS^\bullet(F_C).                               \tag{4}
\]
Since relative rotation fixes the diagonal with zero action, (4) says
that the stronger support-separation hypothesis in Asano--Ike Theorem 4.1
fails at every interior translate.  Only their cohomological Remark 4.2
can still vanish.

## Vanishing eye width

Use the rotational primitive
\(\alpha=(x\,dy-y\,dx)/2\).  Orient the inward arm \(A\) toward the origin
and the interleaved arm \(B\) away from it.  The phase separation of the
two sheets at the same angle is exactly the remaining strip area
\[
 \delta(\theta)
 =\frac12\int_\theta^\infty(a(u)^2-b(u)^2)\,du.           \tag{5}
\]
Here
\[
 a(\theta)^2-b(\theta)^2
 =\frac{\pi}{\theta^2}+O(\theta^{-3}),
\]
so
\[
 \delta(\theta)=\frac{\pi}{2\theta}+O(\theta^{-2}).       \tag{6}
\]
For the product torus, the four \(AA,AB,BA,BB\) sheets lie in an eye of
total phase width
\[
 2\delta(\theta)=\frac{\pi}{\theta}+O(\theta^{-2}),       \tag{7}
\]
while their common center grows as \(\log\theta+O(\theta^{-1})\) and winds
through the full action circle.

Equations (1), (4), and (7) are the exact limiting puzzle: every finite
diagonal complex vanishes at interior action, the limiting support is
maximal, and the sheet separation tends to zero.

## Corrected action-retaining toy model

The action circle must not be collapsed.  The correct local space is
\[
 Y=[0,\varepsilon)_r\times(\mathbb R/\pi\mathbb Z)_t,\qquad
 B=\{0\}\times(\mathbb R/\pi\mathbb Z)_t.                 \tag{8}
\]
This matches \(\rho^{-1}\Delta_C\), which retains every \(t\)-phase over the
collapsed spatial point.

There are two corrections to the earlier \(!\)-versus-\(*\) model.  First,
\(j_!\mathbb k_U\) and \(Rj_*\mathbb k_U\) already differ along the
punctured side boundary of the ribbon; they are not two extensions of one
fixed punctured sheaf.  Second, a common endpoint stalk does not define a
translated sheaf morphism.  Naturality along the translated arm forces the
putative scalar to vanish.

Fix instead one punctured eye sheaf \(F\) on
\((0,\varepsilon)\times S^1_t\), including its side-boundary convention, and
compare its two extensions across \(B\).  Recollement gives
\[
 k_!F\longrightarrow Rk_*F\longrightarrow i_*Q
 \xrightarrow{+1}.                                      \tag{9}
\]
For a monotone infinitely winding constant ribbon,
\[
 Q_t\simeq
 \frac{\prod_{n\ge0}\mathbb k}{\bigoplus_{n\ge0}\mathbb k},              \tag{10}
\]
with shift monodromy.  It is locally constant along \(S^1_t\), so
\[
 SS(i_*Q)\subset\{\tau_t=0\}.                            \tag{11}
\]
Consequently \(k_!F\) and \(Rk_*F\) are canonically isomorphic after
Tamarkin localization to \(\tau_t>0\).  The proposed \(!\)-versus-\(*\)
ambiguity is invisible in the category relevant to Asano--Ike.

Moreover, a half-open eye of fiber width at most \(w\) is \(w\)-torsion:
its canonical forward-translation map vanishes after translating farther
than \(w\).  By (7), every sufficiently deep null-spiral tail is arbitrarily
torsion.  Infinite winding and full support closure alone therefore cannot
create a positive-length boundary bar.

## What remains

The metric completion is a telescope
\[
 F_C\simeq\operatorname*{hocolim}_n
 T_{-\varepsilon_{\ge n}}F_{C_n},                        \tag{12}
\]
not an ordinary \(!\), \(*\), or middle extension.  To finish the null-eye
calculation one must construct the continuation triangle between successive
truncations and prove that its cone is confined to the narrow eye.  A cap
could otherwise create an exact-action, zero-lifetime Milnor boundary term.
The four-sheet geometry alone does not determine the transition maps.

The precise general failure of a zero-Hofer argument is recorded in
`metric-germ-cutoff-no-go.md`.
