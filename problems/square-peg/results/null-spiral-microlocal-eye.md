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

## Why support closure does not decide cohomology

A one-dimensional toy model makes the extension ambiguity explicit.
Compactify
\[
 X^\circ=(0,\varepsilon)_r\times(\mathbb R/\pi\mathbb Z)_t
\]
by collapsing \(\{0\}\times S^1\) to one point \(p\).  Let \(g(r)\) wind
unboundedly modulo \(\pi\), let \(\delta(r)\to0\), and set
\[
 U=\{0<r<\varepsilon:
 0<(t-g(r))\bmod\pi<\delta(r)\}.
\]
For every fixed \(a\notin\pi\mathbb Z\), \(U\) and \(T_aU\) are disjoint
near \(p\), although both closures contain \(p\).  The extensions
\[
 E_!=j_!\mathbb k_U,\qquad E_*=Rj_*\mathbb k_U
\]
have the same punctured helical eye.  But \(E_!\) has zero boundary stalk,
whereas \(E_*\) has a non-zero stalk at \(p\); the latter admits a
point-supported translated morphism that the former does not.  Punctured
finite data and the projected support closure therefore do not determine
the boundary \(\mu hom\).

The actual metric-limit quantization \(F_C\) selects a specific derived
extension.  Computing that extension—rather than another finite truncation
or a support intersection—is the exact local problem for the null spiral.
