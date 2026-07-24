# Slack concentration and a terminal trace gap

## The theorem-shaped target

Let \(P\subset\mathbb R^4\) be bi-centered and pair-terminal. If its
facet-circuit support graph is connected, conjecturally

\[
\boxed{
\operatorname{tr}\!\left(
\operatorname{cov}(P)\operatorname{cov}(P^\circ)
\right)<\frac19.
}
\]

This would finish the connected non-join branch. A local Mahler minimum must
satisfy

\[
\operatorname{cov}(P^\circ)
\succeq\frac1{36}\operatorname{cov}(P)^{-1},
\]

which implies the opposite trace inequality.

The simplex has trace \(1/9\), but its facet-circuit graph is disconnected.
Ellipsoids also attain equality, but are nonpolyhedral. The regular 24-cell
has trace \(169/1800<1/9\). Projectively critical pentagons do not falsify
the target: polygon edges have no affine circuit equations, so nontriangles
are not terminal.

The interval-certified nonregular Paffenholz root is bi-centered,
pair-terminal, and connected on both primal and polar circuit supports. It
satisfies

\[
0.0999343391<
\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)
<0.0999343607<1/9.
\]

Thus the target survives its strongest exact nonregular pressure test.

## Probabilistic identity

Let \(X\) and \(Y\) be independent uniform points of \(P\) and \(P^\circ\),
respectively, and put

\[
Z=1-\langle X,Y\rangle.
\]

Polarity gives \(Z\ge0\). Bi-centering gives

\[
\mathbb E Z=1,
\]

and independence gives the exact identity

\[
\operatorname{Var}(Z)
=\mathbb E\langle X,Y\rangle^2
=\operatorname{tr}\!\left(
\operatorname{cov}(P)\operatorname{cov}(P^\circ)
\right).
\]

Thus the target is a sharp slack-concentration inequality
\(\operatorname{Var}(Z)<1/9\) on the connected terminal branch.

## Finite weighted slack energy

Choose vertex triangulations of \(P\) and \(P^\circ\). For a pair of
4-simplices \(S=\operatorname{conv}(x_0,\ldots,x_4)\) and
\(T=\operatorname{conv}(y_0,\ldots,y_4)\), put

\[
L_{ij}=1-x_i\cdot y_j\ge0.
\]

Write \(L_{i+}\), \(L_{+j}\), and \(L_{++}\) for row, column, and total
sums. The pair's contribution to
\(900\operatorname{tr}(\operatorname{cov}P\operatorname{cov}P^\circ)\)
is

\[
\begin{aligned}
E(S,T)={}&(25-L_{++})^2
+\sum_i(5-L_{i+})^2\\
&+\sum_j(5-L_{+j})^2
+\sum_{i,j}(1-L_{ij})^2.
\end{aligned}
\]

This follows directly from the second moment of a uniform 4-simplex:

\[
\mathbb E_S[XX^\mathsf T]
=\frac{
(\sum_i x_i)(\sum_i x_i)^\mathsf T+\sum_i x_ix_i^\mathsf T
}{30}.
\]

The desired trace ceiling is exactly that the primal/polar
volume-weighted average of \(E(S,T)\) is at most \(100\), with strictness in
the connected non-simplex case. A simplex has diagonal normalized slack
entries five and attains \(100\).

Equivalently, if \(X,Y\) are the global vertex matrices,
\(N=X^\mathsf TY\), \(R_S\) selects the vertices of a simplex, and
\(G=I_5+\mathbf1\mathbf1^\mathsf T\), put

\[
\mathsf M_P=\sum_S\frac{|S|}{|P|}R_SGR_S^\mathsf T.
\]

Then the exact global identity is

\[
900\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)
=
\operatorname{tr}(
\mathsf M_PN\mathsf M_{P^\circ}N^\mathsf T).
\]

For the simplex slack minor \(L_{ST}=(1-x_i\cdot y_j)\),

\[
|\det L_{ST}|=(4!)^2|S||T|.
\]

Thus the target is also

\[
\sum_{S,T}|\det L_{ST}|(E(S,T)-100)<0.
\]

This expression is independent of the chosen triangulations, although its
individual summands are not.

The divergence theorem gives an even more terminality-facing boundary form.
With cone-volume facet weights \(r_F,s_v\), facet centroids \(c_F,d_v\),
and uncentered facet second moments \(H_F,H_v^\circ\),

\[
\frac14-\frac94\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)
=
\sum_{F,v}r_Fs_v
\left[
(x_v\cdot y_F)(c_F\cdot d_v)
-\operatorname{tr}(H_FH_v^\circ)
\right].
\]

At the regular 24-cell all 144 incidence brackets equal \(3/16\), while the
nonincidences contribute another 144 positive brackets and 288 negative
brackets \(-11/100\). Their total is \(31/800\). The remaining theorem is
therefore a global circuit-network transport inequality, not local facet
positivity.

## A dead Hodge route

Let \(D_P\) stack all facet-supported affine circuit rows. Every such row
annihilates constants and all coordinate functions. Therefore, for
\(N_{vF}=x_v\cdot y_F\) and \(L=\mathbf1\mathbf1^\mathsf T-N\),

\[
D_PN=D_PL=0,\qquad
ND_{P^\circ}^\mathsf T=LD_{P^\circ}^\mathsf T=0.
\]

At a terminal realization, \(\ker D_P\) is exactly the five-dimensional
space of affine vertex functions. Hence the polarity matrix is entirely
harmonic. A conventional circuit-Poincare inequality has zero Dirichlet
energy on the very matrix it is meant to control and cannot prove the
trace gap.

The corrected Hodge target compares the two geometry-dependent volume mass
forms on the four-dimensional nonconstant affine harmonic spaces. Support
connectivity identifies these spaces and kills projective stabilizers, but
does not quantitatively compare their mass forms.

## Pointwise control is false

Arbitrary nonincidence slacks can be large, so positivity and incidence
counts alone cannot prove this energy bound. In the canonical pulling
triangulations of the regular 24-cell, 1,784 of 5,184 simplex pairs have
\(E>100\), and the maximum is \(344\), even though the determinant-weighted
average is

\[
900\cdot\frac{169}{1800}=\frac{169}{2}<100.
\]

So neither a blockwise estimate nor an unsigned circuit spectral gap can
work. The route remains **GO** only for a genuinely global
determinant-weighted flip/divergence identity, or an equivalent comparison
of the two volume Hodge stars. It should be abandoned upon finding an exact
bi-centered connected pair-terminal example with trace above \(1/9\).

## Cone-duality form and a concentration no-go

Let \(V\subset\mathbb R^5\) be the homogenizing cone and put
\(J=\Phi_{V^*}-\Phi_V^*\). At a bi-centered section, the entropic Hessian
metric satisfies

\[
\Delta_gJ
=36\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)-4
=-16D_\partial.
\]

Thus the determinant, boundary-transport, and cone/Laplace formulations
are the same scalar target. The connected theorem can be restated as strict
superharmonicity of \(J\) at every pair-terminal nonhomogeneous
five-dimensional polyhedral cone section.

Do not try to derive this sign from cone-volume subspace concentration
alone. Henk--Linke concentration holds for every centered polytope, whereas
Klartag's high-dimensional counterexamples to Kuperberg's covariance
functional persist under symmetric polytopal approximation. Terminal
circuit geometry must enter essentially.

The exact terminal input is the robust-support lemma: for every nonaffine
vertex function \(\alpha\), the normals of facets on which
\(\alpha|_F\) is nonaffine must span \(\mathbb R^4\). Equivalently, after
quotienting global affine functions, facets outside every proper normal flat
give an injective circuit operator.

This cannot act on the degree-one polarity columns, since they are global
affine functions. The next viable object is the degree-two tensor

\[
Q_F(\gamma)=\sum_{v\in F}\gamma_vx_vx_v^\mathsf T,
\qquad\gamma\in\operatorname{Rel}(F).
\]

The universal unweighted version of this proposal is now exactly ruled out
on nonterminal controls.  The
intrinsic tensor is indexed by a facet relation
\(\gamma\in\operatorname{Rel}(F)\), while a speed residual is a covector in
\(\operatorname{Rel}(F)^*\); there is no canonical positive identification.
Moreover, boundary-normal regression makes the nonlinear residual
orthogonal to the bilinear target, and a fixed-geometry one-sided
bistellar flip energy cancels. A terminality-dependent Hodge operator,
separate primal/dual Gram data, and geometric two-sided flips remain open.

The finite surviving gate is
\[
D_P(N\circ N)D_{P^\circ}^{\mathsf T}\ne0
\]
for connected pair-terminal non-simplices.  A sufficient dimension target
is \(\rho(P)+\rho(P^\circ)>10\).  Even this would prove only nonzero
quadratic coupling, not the trace sign.  A completion must use a global
oriented determinant/cofactor transport operator, not a local tensor norm.
