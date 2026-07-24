# Exact negative realization Hessian at the regular 24-cell

## Theorem

Let \(P_a\), \(a\in(-1,1)^4\), be Paffenholz's four-parameter realization
family of the 24-cell, with \(P_0\) the regular member, and set

\[
M(a)=|P_a|\,|(P_a-s(P_a))^\circ|.
\]

Then

\[
\nabla\log M(0)=0,\qquad
\nabla^2\log M(0)=-\frac{61}{234}I_4.
\]

In particular, \(P_0\) is a strict local maximum inside this
four-dimensional realization slice, and there is an open
neighborhood \(U\) of \(0\) such that no \(P_a\), \(a\in U\), is a local
minimizer of Mahler volume.

This excludes an open infinite family of non-pyramidal 4-polytopes. It is not
a proof for all 24-cell realizations or all non-pyramidal polytopes.

## Santaló-envelope calculation

For an integrable fixed-chamber path \(K_t\), write

\[
V(t)=|K_t|,\quad L_t=K_t^\circ,\quad
W(t)=|L_t|,\quad m(t)=\int_{L_t}y\,dy.
\]

At a bi-centered base body in dimension four, eliminating the moving
Santaló point gives

\[
\bar W''=
W''-\frac5{6W}
\langle m',\operatorname{cov}(K^\circ)^{-1}m'\rangle.
\]

Equivalently, for the logarithm,

\[
(\log\mathcal P)''_{\rm reduced}
=(\log V)''+(\log W)''
-\frac56\left\langle
c'(K^\circ),
\operatorname{cov}(K^\circ)^{-1}c'(K^\circ)
\right\rangle.
\]

The exact implementation uses second-order rational jets. A fixed pulling
triangulation differentiates primal volume. For every polar vertex, four
affinely independent incident primal vertices solve
\(y_F(t)\cdot x_v(t)=1\); every remaining incidence is then checked through
second order. Thus the computation differentiates an actual integrable
realization path, not an arbitrary vector in a singular Zariski tangent
space.

## Exact matrix certificate

For each coordinate direction \(e_i\),

\[
D^2\log M(0)[e_i,e_i]=-\frac{61}{234}.
\]

For each \(i<j\),

\[
D^2\log M(0)[e_i+e_j,e_i+e_j]=-\frac{61}{117}.
\]

Polarization therefore gives zero off-diagonal entries and the displayed
negative-definite Hessian. The same verifier also obtains zero curvature for
affine scaling and the independently known reduced projective curvature
\(-31/13\), providing normalization checks.

Since the face-lattice chamber and Santaló minimizer vary smoothly near
\(a=0\), the reduced Hessian is continuous. It remains negative definite on
some open neighborhood \(U\). A differentiable function with
negative-definite Hessian cannot have a local minimum there, proving the
open-family exclusion.

## Verification

Run:

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
```

`test_santalo_reduced_second_variation_sanity_checks` checks the four diagonal
and six polarized values as exact `Fraction` objects.
