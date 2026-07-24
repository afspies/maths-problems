# A q-regular analytic arc through the pair-terminal 24-cell

## Stress-lifting lemma

Use paired incidence coordinates

\[
F_{vF}(x,y)=x_v\cdot y_F-1=0.
\]

Let \(J=DF\), \(T=\ker J\), and
\(\Omega=\ker J^\mathsf T\). Write a tangent as
\(u=(a_v,b_F)\). Every incidence stress
\(\lambda\in\Omega\) defines

\[
q_\lambda(u)
=\sum_{v\in F}\lambda_{vF}\,a_v\cdot b_F.
\]

Then:

1. \(u\) admits a second-order formal lift if and only if
   \(q_\lambda(u)=0\) for every \(\lambda\in\Omega\).
2. If, additionally,
   \[
   Dq_u:T\longrightarrow\Omega^\ast
   \]
   is surjective, then \(u\) is the velocity of a real-analytic
   incidence-preserving arc.
3. The nearby nonzero points on that arc have full Jacobian rank whenever
   the rank deficit at the base equals \(\dim\Omega\).

The first statement follows by differentiating twice. With the ordinary
series convention

\[
z(t)=z_0+t u+t^2w+\cdots,
\]

the second coefficient must solve

\[
Jw=-c(u,u),\qquad
c(u,u)_{vF}=a_v\cdot b_F.
\]

Fredholm solvability is precisely the family \(q_\lambda(u)=0\).

For the analytic statement, split the domain into \(T\) and a complement,
and the codomain into \(\operatorname{im}J\) and a cokernel identified with
\(\Omega^\ast\). The implicit-function theorem solves the image component.
The reduced obstruction has the form

\[
\Phi(t)=q(t)+O(\|t\|^3).
\]

The blow-up

\[
H(r,v)=r^{-2}\Phi(rv),\qquad H(0,v)=q(v),
\]

is analytic. Surjectivity of \(Dq_u\) lets the implicit-function theorem
solve \(H(r,u+\ell(r))=0\), producing the desired arc. At nonzero points its
reduced derivative has rank \(\dim\Omega\), restoring the missing Jacobian
rank.

## Exact 24-cell certificate

Take the rational Paffenholz realization

\[
P_0=P_{(1/5,\,2/5,\,3/5,\,4/5)}.
\]

With the deterministic exact nullspace bases \(\tau_i\) and \(\lambda_s\)
returned by the harness,

\[
\operatorname{rank}J=142,\qquad
\dim T=50,\qquad
\dim\Omega=2.
\]

Set

\[
u=\tau_0+\frac{659}{667}\tau_1.
\]

Exact rational arithmetic verifies

\[
q_{\lambda_0}(u)=q_{\lambda_1}(u)=0,
\qquad
\operatorname{rank}Dq_u=2.
\]

It also verifies

\[
\operatorname{rank}(J\mid -c(u,u))=\operatorname{rank}J=142,
\]

so the second-order coefficient exists directly.

The 24 infinitesimal PGL directions have rank 24; adjoining \(u\) raises the
rank to 25. The PGL directions together with the four Paffenholz parameter
directions have rank 28; adjoining \(u\) raises it to 29. Thus the arc is
both nonprojective and outside the known four-parameter Paffenholz slice.

The fixed rational projective map \(P_0\to Q\) transports this incidence
germ to the exact Santaló-normalized pair-terminal counterexample
`terminal-bridge-counterexample.md`. Hence:

> The pair-terminal 24-cell lies in the closure of a smooth
> 48-dimensional realization stratum, and admits a genuinely new
> nonprojective analytic deformation into that stratum.

Pair-terminality and the strict chamber inequalities persist in a
sufficiently small neighborhood. This supplies an open family of smooth
pair-terminal 24-cell realizations.

The openness assertion is finite: within a fixed normal-dependence chamber,
terminality is certified by finitely many nonzero speed-rank minors.
Perturbation preserves those minors, while a disappearing normal dependence
only activates additional facet equations. This is stronger than merely
approximating a terminal point by nearby realizations.

## Smooth pair-terminal projective saddles

The interval certificate in `24cell-projective-saddle.md` proves that the
base projective class has a unique nearby bi-centered representative, that
the centering Jacobian is nonsingular, and that its covariance gap has a
strict negative direction. Apply the implicit-function theorem to the
nearby full-rank classes furnished by the q-regular arc. Their bi-centered
representatives vary continuously, pair-terminality persists, and the
negative covariance direction remains strict.

Therefore an open subset of the smooth rank-144 stratum consists of
pair-terminal 24-cell projective classes that are not local Mahler minima.
The stratum has dimension 48 in paired coordinates and dimension 24 modulo
PGL. This is substantially larger than the four-parameter Paffenholz slice.

## Correction to the Hessian route

The 24 PGL directions are gauges for the realization space, but not for
Mahler volume. Only the 20-dimensional affine subgroup (four translations
and 16 linear directions) is a Mahler gauge. The remaining four projective
denominator directions carry the covariance Hessian and must be retained.

At a candidate passing the projective covariance condition, the correct
reduction first quotients the 20 affine directions and then eliminates any
positive projective block by a Schur complement. It is incorrect to discard
all 24 PGL directions from the Mahler Hessian.

For a singular candidate, the realization part of the second-order test
must be imposed on the regular stress cone

\[
Z_{\rm reg}
=\{u\in T:q(u)=0,\ \operatorname{rank}Dq_u=\dim\Omega\}.
\]

Every direction in \(Z_{\rm reg}\) integrates with both signs. A
classification proof can therefore avoid global smoothness if it proves
that \(Z_{\rm reg}\) spans the non-affine tangent quotient and contains a
negative direction of the correctly reduced Mahler Hessian.

## Verification

The unit test `test_24_cell_has_q_regular_integrable_tangent` checks all
displayed dimensions, quadratic equations, ranks, and second-order
solvability over exact rational arithmetic.
