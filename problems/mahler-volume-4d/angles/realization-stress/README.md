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

The next go/no-go target is a smooth full-rank realization chart at a
bi-centered pair-terminal candidate. Quotient its exact Hessian by the
24-dimensional projective orbit and compress any negative eigenvector into a
coordinate-free stress/Gale certificate.
