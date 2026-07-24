# The terminal trace gap as cone-duality superharmonicity

The full connected non-pyramidal Mahler problem remains open. This note
identifies the facet-boundary deficit with an intrinsic Laplacian of
Klartag's cone-duality defect and proves that cone-volume subspace
concentration, by itself, cannot establish the required sign.

## 1. Exact cone/Laplace reduction

Let \(K\subset\mathbb R^n\) be bi-centered, and let

\[
V=\{(t,tx):t\geq0,\ x\in K\}\subset\mathbb R^{n+1}
\]

be its homogenizing cone. Write \(\Phi_V\) for the logarithmic Laplace
transform of \(V\), \(\Phi_V^*\) for its Legendre transform, and
\(\Phi_{V^*}\) for the logarithmic Laplace transform of the dual cone. Put

\[
J=\Phi_{V^*}-\Phi_V^*.
\]

At the section point \(e=(1,0)\), bi-centering is exactly the critical-point
condition for \(J\). If

\[
A=\operatorname{cov}(K),\qquad
B=\operatorname{cov}(K^\circ),
\]

Klartag's derivative formulas give, on the \(n\)-dimensional section
directions,

\[
\frac1{n+1}\nabla^2J(e)
=(n+2)B-\frac1{n+2}A^{-1}.
\]

The entropic Hessian metric is

\[
g=\nabla^2\Phi_V^*(e)
=\frac{n+1}{n+2}A^{-1}.
\]

Taking the metric trace proves the exact identity

\[
\boxed{
\Delta_gJ(e)
=(n+2)^2\operatorname{tr}(AB)-n.
}
\]

No smoothness of \(K\) is used: the logarithmic Laplace transforms are
smooth on the interiors of the proper cones.

In dimension four,

\[
\boxed{
\Delta_gJ(e)
=36\operatorname{tr}(AB)-4.
}
\]

Thus the connected terminal trace-gap conjecture is precisely:

> Every bi-centered connected pair-terminal non-simplex section of a
> five-dimensional polyhedral cone satisfies \(\Delta_gJ(e)<0\).

A local Mahler minimum requires \(\nabla^2J(e)\succeq0\), and hence
\(\Delta_gJ(e)\geq0\). Strict superharmonicity would therefore exclude the
entire connected non-simplex branch.

The simplex has trace \(1/9\) and Laplacian zero. For the regular 24-cell,

\[
\operatorname{tr}(AB)=\frac{169}{1800},
\qquad
\Delta_gJ(e)=-\frac{31}{50}.
\]

## 2. The boundary deficit is the same invariant

The previously derived facet-boundary identity has left-hand side

\[
D_\partial
=\frac14-\frac94\operatorname{tr}(AB).
\]

Consequently,

\[
\boxed{
\Delta_gJ(e)=-16D_\partial.
}
\]

The proposed boundary transport inequality and the cone-duality
superharmonicity theorem are not two routes: they are exactly the same
scalar inequality in boundary and interior coordinates, respectively.

This normalization supplies independent checks. At the regular 24-cell,
\(D_\partial=31/800\), so \(-16D_\partial=-31/50\), agreeing with the
Laplace-transform calculation.

There is also an exact probabilistic warning. Choose \(F,v\) independently
with cone-volume probabilities \(r_F,s_v\), then choose \(U,W\) uniformly
from the primal facet \(F\) and the polar facet dual to \(v\). Put

\[
N=x_v\cdot y_F,\qquad Z=U\cdot W.
\]

Conditioning on \(F,v\) in the boundary formula gives

\[
\boxed{
D_\partial=\mathbb E[Z(N-Z)].
}
\]

The two summands factor globally:

\[
\mathbb E[NZ]=\frac14,\qquad
\mathbb E[Z^2]=\frac94\operatorname{tr}(AB).
\]

Thus an incidence/nonincidence rearrangement is only a repartition of the
desired scalar unless it imports a genuinely new terminal inequality.
For an incidence \(v\in F\), write \(U=x_v+a\), \(W=y_F+b\). Then
\(Z=1+a\cdot b\), \(a\cdot b\leq0\), and the local bracket is

\[
\mathbb E[-a\cdot b-(a\cdot b)^2],
\]

which need not be positive if \(U\cdot W<0\).

## 3. The exact information supplied by terminality

For a vertex function \(\alpha\), let \(R_F(\alpha)\) denote its restriction
to a facet \(F\), modulo affine functions on \(F\), and set

\[
S(\alpha)=\{F:R_F(\alpha)\neq0\}.
\]

Then

\[
\boxed{
P\text{ is terminal}
\quad\Longleftrightarrow\quad
\operatorname{span}\{y_F:F\in S(\alpha)\}=\mathbb R^4
\text{ for every nonaffine }\alpha.
}
\]

Indeed, if this normal span is proper, choose a nonzero direction
\(\theta\) orthogonal to it. Every facet on which \(\alpha\) violates an
affine circuit is then parallel to \(\theta\) and waived, so \(\alpha\) is
a nonaffine admissible speed. Conversely, a nonaffine admissible speed in
direction \(\theta\) can violate circuits only on facets with
\(y_F\in\theta^\perp\), whose normals span a proper subspace.

Equivalently, after quotienting global affine functions, the circuit
operator formed from facets outside every rank-at-most-three normal flat is
injective. This **robust-support lemma** is stronger than circuit-support
connectivity and is the precise every-direction content of terminality.

It still acts trivially on degree-one polarity columns, which are global
affine functions. The first features on which it can carry new information
are the circuit second-moment tensors

\[
Q_{F,\alpha}=\sum_{v\in F}\alpha_vx_vx_v^\mathsf T.
\]

These tensors are generally indefinite. The remaining missing lemma must
therefore be a coupled primal--dual positivity statement, not an ordinary
Markov or convex-order argument.

## 4. Why subspace concentration alone cannot work

Henk and Linke prove that the cone-volume measure of every centroid-zero
polytope satisfies the subspace concentration condition

\[
\mu(L\cap S^{n-1})
\leq\frac{\dim L}{n}\mu(S^{n-1})
\]

for every linear subspace \(L\), with equality characterized by a split
of the normal support into complementary subspaces.

This condition cannot imply

\[
\operatorname{tr}(\operatorname{cov}K\operatorname{cov}K^\circ)
\leq\frac{n}{(n+2)^2}.
\]

Indeed, the displayed covariance inequality is Kuperberg's conjectured
bound for

\[
\phi(K)=\mathbb E\langle X,Y\rangle^2,
\]

where \(X,Y\) are independent uniform points of \(K,K^\circ\). Klartag
proved this bound false in sufficiently high dimension. There is also a
small exact polytopal witness inside the present harness.

Let

\[
K_m=\Delta(2,m)-\frac2m\mathbf1
\subset\left\{x\in\mathbb R^m:\sum_i x_i=0\right\}.
\]

For \(m=11\), this is a ten-dimensional centered hypersimplex. Exact slice
integration and a Weyl-chamber triangulation of its polar give

\[
\boxed{
\phi(K_{11})
=\frac{51389}{738477}
=\frac5{72}+\frac{847}{5907816}
>\frac{10}{12^2}.
}
\]

Here is the general exact calculation used by the verifier. The
Irwin--Hall density of the sum of \(m\) independent uniforms at \(2\) is

\[
f_m(2)=\frac{2^{m-1}-m}{(m-1)!}.
\]

Writing \(p=m-2\), put

\[
\begin{aligned}
A_m={}&
\frac{4(2^{p+1}-1)}{p+1}
-\frac{4(2^{p+2}-1)}{p+2}
+\frac{2^{p+3}-1}{p+3},\\
B_m={}&\frac2{(m-1)m(m+1)},\\
R_m={}&
\frac{m-1}{2^{m-1}-m}\bigl(A_m-(m-1)B_m\bigr).
\end{aligned}
\]

The covariance of \(K_m\) is scalar on the sum-zero hyperplane, with
eigenvalue

\[
\lambda_m=\frac{m}{m-1}\left(R_m-\frac4{m^2}\right).
\]

For the polar, order a Weyl chamber by
\(y_1\geq\cdots\geq y_m\). Its extreme rays are the fundamental weights

\[
(w_j)_i=
\begin{cases}
(m-j)/m,&i\leq j,\\
-j/m,&i>j,
\end{cases}
\]

and the polar constraint is \(y_1+y_2\leq1\). Thus the chamber is the
simplex with vertices \(0,v_1,\ldots,v_{m-1}\), where

\[
v_j=\frac{w_j}{\ell_j},\qquad
\ell_1=\frac{m-2}{m},\qquad
\ell_j=\frac{2(m-j)}m\quad(j\geq2).
\]

The simplex second-moment formula yields

\[
\rho_m=\mathbb E_{K_m^\circ}|Y|^2
=\frac{\left|\sum_jv_j\right|^2+\sum_j|v_j|^2}{m(m+1)},
\qquad
\phi(K_m)=\lambda_m\rho_m.
\]

Substitution at \(m=11\) reduces to the boxed rational value. Since
\(K_{11}\) is itself a centered polytope, Henk--Linke subspace
concentration holds for this exact counterexample.

In dimension four the same family supplies a useful negative control:
\(K_5=\Delta(2,5)-2\mathbf1/5\) has

\[
\phi(K_5)=\frac{667}{7128}<\frac19,\qquad
\Delta_gJ=-\frac{125}{198}.
\]

Exact enumeration of all facet-normal flats nevertheless finds admissible
speed dimensions five and six on both \(K_5\) and its polar, so this
bi-centered trace-gap example is not pair-terminal.

Therefore neither subspace concentration nor its equality case contains
enough metric information to determine the sign of \(\Delta_gJ\). Any
successful proof must use the additional terminal circuit equations (or a
genuinely equivalent property), not merely centered cone-volume data.

## 5. Homogeneous polyhedral equality is already classified

A full-dimensional pointed homogeneous polyhedral cone is simplicial.
Here is a short proof that also identifies the desired equality case.

Let \(C\subset\mathbb R^m\) be such a cone. Its automorphism group permutes
the finite set of extreme rays. Hence the identity component \(G^0\) fixes
every extreme ray. Since the full automorphism group is transitive on the
connected manifold \(\operatorname{int}C\), its orbit has dimension \(m\).
The full group and \(G^0\) have the same Lie algebra, so every \(G^0\)-orbit
also has dimension \(m\) and is open. The connected interior cannot be a
disjoint union of multiple open \(G^0\)-orbits, hence \(G^0\) is transitive.

Choose \(m\) linearly independent extreme rays as a basis. Every member of
\(G^0\) is diagonal in this basis. Transitivity on an \(m\)-dimensional
open set forces this diagonal group to have dimension \(m\), so it contains
the full connected group of positive coordinate scalings. An additional
extreme ray with two nonzero coordinates could not be fixed by all these
scalings. Thus the chosen \(m\) rays are all the extreme rays, and \(C\) is
simplicial.

Consequently a homogeneous five-dimensional polyhedral cone has a
4-simplex as any bounded transverse section. If a future Bochner or
maximum-principle proof yields

\[
\Delta_gJ\leq0
\]

with equality only in the homogeneous case, its equality analysis needs no
further polytope classification.

## 6. Remaining proof target

The reduction suggests a dimension-specific maximum-principle statement:

\[
\boxed{
\text{For a nonhomogeneous pair-terminal polyhedral five-cone, }
\Delta_g(\Phi_{V^*}-\Phi_V^*)<0
\text{ at every bi-centered section.}
}
\]

The word *pair-terminal* is essential. A dimension-free version is false,
and even centered polytopes with the strongest available subspace
concentration do not suffice. The next proof attempt should express the
metric Laplacian as a nonnegative quadratic form in coupled primal and dual
circuit second-moment tensors, with vanishing forcing an affine join. It
should be abandoned unless the missing positivity is proved; the boundary
repartition and first-degree circuit identities alone are tautological.
Alternatively, falsify the statement with an exact connected pair-terminal
trace counterexample.

## References

- Bo'az Klartag, *Isotropic Constants and Mahler Volumes*, Advances in
  Mathematics 330 (2018), 74--108, arXiv:1710.08084.
- Martin Henk and Eva Linke, *Cone-volume measures of polytopes*,
  Advances in Mathematics 253 (2014), 50--62, arXiv:1305.5335.
