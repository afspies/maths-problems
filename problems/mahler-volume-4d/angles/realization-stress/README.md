# Realization-space stress and the Santaló-reduced Hessian

## Paired incidence coordinates

Normalize primal vertices \(x_v\) and polar vertices \(y_F\) by

\[
x_v\cdot y_F=1\qquad(v\in F).
\]

The fixed-incidence Jacobian is

\[
J_{vF}(\dot x,\dot y)
=y_F\cdot\dot x_v+x_v\cdot\dot y_F.
\]

Thus \(T=\ker J\) is the combined realization tangent space. If
\(\omega=\dim\ker J^\mathsf T\) is the incidence-stress dimension, then

\[
\dim T=4(f_0+f_3)-f_{03}+\omega.
\]

The 24 standard infinitesimal \(\operatorname{PGL}_5\) motions lie in this
kernel. Exact harness calculations give:

```text
regular 24-cell:     rank J = 140, dim T = 52
Paffenholz member:   rank J = 142, dim T = 50
projective subspace: rank = 24
```

## Projective-orbit lemma

For a terminal 4-polytope, the facet-supported affine circuit spaces span
the global Gale kernel. Form the graph joining two vertices when they occur
in a common facet-supported circuit.

If this graph is disconnected, the homogeneous vertex configuration is a
direct sum, so the polytope is an affine join. The sharp join theorem in
`../../results/join-product-exclusion.md` settles its Mahler inequality.

Otherwise the circuit graph is connected. An infinitesimal labeled
projective stabilizer scales each vertex ray. Circuit preservation forces
the scaling factors to agree on every circuit support, hence everywhere.
The transformation is scalar and therefore zero in
\(\mathfrak{pgl}_5\). Consequently every terminal non-join has projective
orbit dimension exactly 24, and

\[
\boxed{
\dim(T/T_{\rm proj})
=4(f_0+f_3)-f_{03}+\omega-24.
}
\]

This is a structural reduction, not yet a descent theorem.

It is a quotient for realization moduli, not for Mahler volume. Only the
20-dimensional affine subgroup is a Mahler gauge. The other four projective
directions are genuine variations governed by the covariance Hessian.

After quotienting the affine gauges, split the constrained Hessian into the
four denominator-projective directions and the remaining realization
directions:

\[
H=\begin{pmatrix}A&B\\B^\mathsf T&C\end{pmatrix}.
\]

Here \(A\) is the covariance block. If \(A\) has a negative direction, the
candidate is excluded. If \(A\succeq0\), positivity of \(H\) additionally
requires

\[
\ker A\subseteq\ker B^\mathsf T,\qquad
C-B^\mathsf T A^\dagger B\succeq0.
\]

Thus even a semidefinite projective block cannot simply be removed.

## Exact Santaló-envelope Hessian

For an integrable \(C^2\) fixed-chamber path \(K_t\), put

\[
V(t)=|K_t|,\quad L_t=K_t^\circ,\quad
W(t)=|L_t|,\quad m(t)=\int_{L_t}y\,dy.
\]

At a bi-centered base body in dimension four, eliminating the moving
Santaló point gives

\[
\bar W''=W''-\frac5{6W}
\langle m',\operatorname{cov}(K^\circ)^{-1}m'\rangle.
\]

Therefore

\[
\mathcal P''=
WV''+2V'W'
+V\left(
W''-\frac5{6W}
\langle m',\operatorname{cov}(K^\circ)^{-1}m'\rangle
\right).
\]

`harness/variation.py` implements this with exact second-order jets, solves
facet-normal jets from four incident vertices, and checks every remaining
incidence. It reproduces:

- zero curvature for affine scaling;
- reduced projective curvature \(-31/13\) for the regular 24-cell; and
- reduced curvature \(-61/234\) in each of the four nonprojective
  Paffenholz parameter directions at the regular member.

## Remaining obstruction

At singular realization points, not every element of \(\ker J\) integrates.
Moreover, the constrained Hessian is the Lagrangian Hessian, including the
incidence-stress cross term, not the raw ambient volume Hessian.

At a constrained-critical pair, choose

\[
\nabla(\log|P|+\log|P^\circ|)=J^\mathsf T\lambda.
\]

If \(H_0\) is the straight ambient Santaló-envelope Hessian, the exact
Lagrangian form on every second-liftable tangent is

\[
Q_\lambda(u)=H_0(u)-2q_\lambda(u).
\]

The acceleration drops out because
\(Jz''=-2c(u,u)\). Multiplier ambiguity also drops out on the common
stress cone.

More strongly, the polarization of every self-stress quadric has the entire
24-dimensional PGL tangent space in its radical. Thus q-regularity descends
to realization moduli and is unaffected by optimizing the four genuine
denominator-projective directions. This is the precise compatibility
between the 24-dimensional projective realization quotient and the
20-dimensional affine Mahler gauge quotient.

At the regular 24-cell, the exact KKT multiplier and the four projective
plus four Paffenholz directions give

\[
A=-\frac{31}{13}I_4,\qquad
B=-\frac{31}{78}I_4,\qquad
C=-\frac{61}{234}I_4.
\]

The nonzero mixed block \(B\) is an exact warning that discarding all 24
projective directions changes the realization Hessian.

The q-regular arc lemma in `../../results/24cell-stress-arc.md` removes the
need for base-point smoothness. But stress-cone dimension and spanning alone
cannot force a quadratic form to be negative. The next go/no-go target is a
volume-specific sign identity for the Schur complement on
\(q^{-1}(0)\), not a purely incidence-theoretic dimension argument.
