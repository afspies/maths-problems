# Arbitrary action on a shrinking exact square

## Result

Jordan separation and the order-four symmetry of the square do not force
the two projected capping areas of a collapsing square to cancel.

More strongly, let \(a_*\) be any prescribed real number.  There are smooth
Jordan curves \(\gamma_n\), converging uniformly to a Jordan curve, and
exact inscribed squares \(Q_n\subset\gamma_n\) shrinking to one point such
that the capping-area contribution to the square action converges to
\(a_*\) modulo the total enclosed area.

This does not assert that \(Q_n\) are the squares selected by a spectral
invariant.  It refutes any no-shrinkout proof based only on embeddedness,
cyclic order, and square symmetry.

## Hamiltonian action-injection construction

Start with smooth Jordan curves \(\gamma_n^0\) carrying exact squares
\[
 Q_n=\{q_{1,n},q_{2,n},q_{3,n},q_{4,n}\}
\]
of diameter \(\rho_n\to0\).  Such a local square-shaped motif can be
inserted in a shrinking disk while the complementary arc converges to a
fixed Jordan curve.

Choose mutually disjoint disks
\[
 B(q_{j,n},\delta_n),\qquad\delta_n=o(\rho_n),
\]
and a smooth radial cutoff \(\beta\), equal to \(1\) near the origin and
\(0\) near the boundary of the unit disk.  On the four disks take
autonomous Hamiltonians
\[
 K_{j,n}(z)=\kappa_{j,n}
 \beta\!\left(\frac{|z-q_{j,n}|}{\delta_n}\right).         \tag{1}
\]
Their time-one maps have disjoint supports, so they commute.  Let
\(\chi_n\) be their product.  Then
\[
 \|\chi_n-\mathrm{id}\|_{C^0}
 +\|\chi_n^{-1}-\mathrm{id}\|_{C^0}\leq4\delta_n\to0,      \tag{2}
\]
and every vertex \(q_{j,n}\) is fixed.  Therefore
\[
 \gamma_n:=\chi_n(\gamma_n^0)
\]
is again a smooth Jordan curve, converges to the same limit, and contains
the same exact square \(Q_n\).

For \(\lambda=y\,dx\), normalize the action potential \(S_n\) by
\[
 dS_n=\chi_n^*\lambda-\lambda
\]
and \(S_n=0\) outside the four disks.  A constant fixed orbit at the center
of (1) has action \(-\kappa_{j,n}\), hence
\[
 S_n(q_{j,n})=-\kappa_{j,n}.                              \tag{3}
\]
Conjugating the two boundary factors changes the rectangle action by the
four-point second difference
\[
 \Delta_{Q_n}S_n
 =S_n(q_{\mathrm{out},1})+S_n(q_{\mathrm{out},2})
  -S_n(q_{\mathrm{in},1})-S_n(q_{\mathrm{in},2}).          \tag{4}
\]
The four constants \(\kappa_{j,n}\) may be chosen so that (4) equals
\(a_*\) for every \(n\).  Since the unmodified local square motif can be
chosen with action tending to zero, the modified square action tends to
\(a_*\).

The construction has uniform \(C^0\) control of both maps and inverses.
What diverges is the derivative and the local action potential.  Thus
equicontinuity of conservative approximating maps does not repair the
action problem.

## Geometric two-fjord model

The same obstruction can be seen directly in the projected capping loops.
Put a square of scale \(\rho\) in a disk and label it so that the
\(\pi/2\)-rotation trajectory projects to two quarter-circle arcs.  Arrange
the Jordan order so that the two product-capping projections close those
arcs using disjoint boundary subarcs \(\alpha,\beta\).

Near each of two opposite vertices use an \(N\)-turn spiral fjord with core
\[
 s(\theta)=q+d\left(1-\frac{\theta}{2\pi N}\right)e^{i\theta},
\qquad0\leq\theta\leq2\pi N,\qquad d=\kappa\rho.           \tag{5}
\]
For \(\alpha_0=(x\,dy-y\,dx)/2\), translation of the center contributes
only \(O(\rho^2)\), while
\[
 \int_s\alpha_0
 =\frac12\int_0^{2\pi N}
 d^2\left(1-\frac{\theta}{2\pi N}\right)^2\,d\theta
 +O(\rho^2)
 =\frac{\pi Nd^2}{3}+O(\rho^2).                           \tag{6}
\]
Take a tube of width \(\eta\ll d/N\) around the core.  A tube side changes
(6) by \(O(\eta Nd)\).  With
\[
 N\asymp\rho^{-2},\qquad \eta=\rho^5,                     \tag{7}
\]
the tube is embedded, the error tends to zero, and the integral tends to
an arbitrary prescribed constant.  Put identical-handed fjords in
disjoint disks at the two opposite vertices.  Then both selected capping
loops have the same non-zero limiting signed area; their winding
functions even have disjoint supports, so pointwise cancellation is
impossible.

The paired outward sides of the fjords occur in the two unselected
boundary arcs and carry the opposite action.  They keep the total Jordan
area small, but they do not enter the preferred cap.  This is exactly why
control of total enclosed area does not control the square action.

## Consequence for the microlocal route

For smooth conservative approximants \(\phi_n\), the conjugated relative
rotation
\[
 \psi_n^t=(\phi_n\times\phi_n)^{-1}R_t(\phi_n\times\phi_n)
\]
fixes the diagonal, and its Hamiltonian vanishes there.  Nevertheless,
near-diagonal off-diagonal chords can carry any fixed action by the
construction above.  Small Hamiltonian oscillation or small interleaving
distance can make the associated bars short; it does not control their
location in the action filtration.

Therefore a proof of Asano--Ike Remark 4.2 needs a genuinely new statement
about the *limit* diagonal \(\mu hom\), for example:

> Point-supported action-concentration bars created by uniformly
> convergent conservative approximations have zero global diagonal
> cohomology at the critical class \(a(\pi/2,C)\).

Neither ordinary \(C^0\) convergence nor square symmetry implies this
statement.
