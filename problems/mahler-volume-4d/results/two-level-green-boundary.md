# The two-level boundary and an intrinsic cone-volume Green energy

The full four-dimensional Mahler conjecture remains open. This note closes
the two-level branch of the pair-terminal reduction and introduces a
nonlocal quadratic diagnostic which survives the uniform cofactor
cancellation. No positive comparison between that diagnostic and the
Mahler trace deficit is proved.

## 1. The first Boolean saturation target is false

The proposed implication

\[
P\text{ terminal, connected, two-level, non-simplex}
\Longrightarrow \rho(P)=6
\]

is false. The exact obstruction is

\[
P=\Delta _2\times\Delta _2.
\]

Use the Boolean realization

\[
X=\{(u_1,u_2,v_1,v_2):
u,v\in\{(0,0),(1,0),(0,1)\}\}.
\]

It has nine vertices and six facets, each containing six vertices. Its
rectangle circuits connect all nine vertices. Since
\(u_1u_2=v_1v_2=0\), while the four cross-products \(u_iv_j\) are
independent modulo affine functions,

\[
h_X(2)=9,\qquad \rho(P)=4.
\]

Nevertheless \(P\) is terminal. Write a speed as a \(3\times3\) matrix
\(\alpha\). Global affine speeds are precisely the additive matrices

\[
\alpha_{ij}=r_i+c_j.
\]

Declare two rows equivalent when their difference is constant across the
columns. A facet deleting row \(i\) has affine restriction exactly when all
remaining rows are equivalent. If \(\alpha\) is not additive, the rows have
at least two equivalence classes, so at most one delete-row facet is
affine. At least two row-facet normals are therefore violated and span the
first two-dimensional normal factor. The identical column argument spans
the complementary factor. Hence every nonaffine speed violates facets
whose normals span \(\mathbb R^4\), which is the intrinsic terminality
criterion.

The argument gives an infinite-family theorem.

> **Simplex-product terminality theorem.** For \(p,q\ge2\),
> \[
> \boxed{\Delta_p\times\Delta_q\text{ is terminal}.}
> \]
> Its rectangle-circuit support is connected and
> \[
> \boxed{\rho(\Delta_p\times\Delta_q)=pq.}
> \]

The polar of \(\Delta_2\times\Delta_2\) is a simplicial non-simplex with
six vertices, hence is not terminal. Its Mahler product is already
strictly separated in the solved product branch:

\[
\mathcal P(\Delta_2\times\Delta_2)
=\frac{2!2!}{4!}\left(\frac{27}{4}\right)^2
=\frac{243}{32}
>\frac{3125}{576}.
\]

## 2. Structural classification with one simple vertex

> **Theorem.** Let \(P\) be a terminal two-level four-polytope having a
> simple vertex. Then
> \[
> \boxed{P\simeq\Delta_4\quad\text{or}\quad
> P\simeq\Delta_2\times\Delta_2.}
> \]

Put the simple vertex at zero and use the normalized slacks of its four
incident facets as affine coordinates. The vertex set becomes

\[
X\subseteq\{0,1\}^4
\]

and contains \(0,e_1,\ldots,e_4\). A facet not containing zero has, after
normalization, equation \(a\cdot x=1\). Evaluating its two slack levels at
the \(e_i\)'s gives \(a_i\in\{0,1\}\). Thus every such facet is

\[
\sum_{i\in C}x_i=1
\]

for some \(C\subseteq[4]\).

Define a graph \(G\) on \([4]\) by declaring \(ij\) an edge when some
facet-set \(C\) contains both \(i,j\). The coordinate facets and the clique
inequalities above give

\[
X=\{\mathbf1_I:I\text{ is a stable set of }G\}.
\]

Indeed, the inclusion from left to right follows from the facet
inequalities. Conversely a Boolean stable-set vector satisfies every
facet inequality, hence lies in \(P\); a Boolean point in a convex hull of
Boolean points must itself be one of those points.

Fix a nonedge \(ij\) and take the nonaffine speed

\[
\alpha(x)=x_ix_j.
\]

On the two coordinate facets \(x_i=0,x_j=0\) it is zero. On each of the
other two coordinate facets it remains nonaffine, so their normals span
the coordinate complement of \(\operatorname{span}(e_i,e_j)\). A clique
facet avoiding \(i,j\) has no component in the missing two-plane. If a
clique facet \(C\) contains \(i\), but every
\(c\in C\setminus\{i\}\) is adjacent to \(j\), then on that facet

\[
x_ix_j=x_j,
\]

so the restriction is affine. Therefore terminality forces witnesses

\[
c\in N(i)\setminus N(j),\qquad
d\in N(j)\setminus N(i)
\]

for every nonedge \(ij\).

On four graph vertices this condition is decisive. Given a nonedge \(12\),
the other two vertices must supply the two witnesses; after relabeling,

\[
13,24\in E,\qquad 23,14\notin E.
\]

If \(34\in E\), then \(N(1)\subseteq N(4)\), contradicting the witness
condition for the nonedge \(14\). Hence \(34\notin E\) and \(G=2K_2\). If
there is no nonedge, \(G=K_4\). Their stable-set polytopes are respectively
\(\Delta_2\times\Delta_2\) and \(\Delta_4\).

## 3. Closing all two-level types in dimension four

Bohn--Faenza--Fiorini--Fisikopoulos--Macchia--Pashkovich prove that:

1. every two-level polytope is affinely equivalent to a Boolean polytope;
2. combinatorial and affine equivalence coincide for two-level polytopes;
3. there are exactly nineteen affine types in dimension four; and
4. exactly eleven of them have a simple vertex
   [Bohn et al., arXiv:1703.01943v2].

An independent exact Boolean audit reproduced this boundary:

- the \(384\)-element cube group reduces the \(65\,535\) nonempty Boolean
  subsets to \(401\) orbits;
- \(347\) representatives are full-dimensional;
- \(100\) presentations are two-level;
- their incidence signatures give exactly nineteen distinct classes,
  matching the proved count;
- eleven have a simple vertex and are covered by the structural theorem;
- the remaining eight have pairwise distinct incidence signatures and the
  exact squarefree-quadratic certificates below.

The Boolean cube is ordered lexicographically as in
`itertools.product((0,1), repeat=4)`. In every row, the speed is
\(\alpha=x_ix_j\). The displayed direction is perpendicular to every
facet normal on which \(\alpha\) is nonaffine, so the last column is an
explicit nonterminal admissible-speed dimension.

| Boolean vertex indices | \((i,j)\) | violated-normal rank | direction | speed dimension |
|---|---:|---:|---:|---:|
| 1,2,3,4,5,6,8 | 1,2 | 1 | (0,1,0,0) | 7 |
| 1,2,4,6,8,9 | 0,3 | 0 | (1,1,1,1) | 6 |
| 1,2,3,4,5,6,8,9 | 1,2 | 1 | (0,1,0,0) | 6 |
| 1,2,3,4,5,6,8,9,10 | 2,3 | 2 | (0,0,1,0) | 7 |
| 1,2,3,4,5,6,8,9,10,12 | 0,1 | 3 | (1,-1,0,0) | 6 |
| 3,5,6,7,8,9,10,12 | 0,1 | 0 | (1,1,1,1) | 8 |
| 3,4,5,6,7,8,9,10,11,12 | 0,1 | 0 | (1,1,1,1) | 6 |
| 2,3,4,5,6,7,8,9,10,11,12,13 | 0,1 | 1 | (1,0,0,0) | 7 |

The published completeness theorem plus these exact certificates proves:

> **Terminal two-level classification in dimension four.**
> \[
> \boxed{
> P\text{ terminal and two-level}
> \Longrightarrow
> P\simeq\Delta_4\text{ or }\Delta_2\times\Delta_2.
> }
> \]
> Consequently a pair-terminal two-level four-polytope is a simplex.

Thus no non-simplex two-level polytope can be a Mahler minimizer after the
pair-terminal shadow-flow reduction.

## 4. A cone-volume Green diagnostic

Let \(P\) be full-dimensional with \(0\in\operatorname{int}P\), use the
canonical support-one normalization
\(S_{vF}=1-\langle x_v,y_F\rangle\), and let \(Q=P^\circ\). Give each
vertex \(x_v\) of \(P\) the normalized
cone-volume weight of its dual facet in \(Q\), denoted \(\mu_v\), and give
each polar vertex \(y_F\) the normalized cone-volume weight \(\nu_F\) of
the corresponding facet of \(P\). Let the rows of \(D\) and \(E\) be any
bases of \(\ker(1,X)^{\mathsf T}\) and
\(\ker(1,Y)^{\mathsf T}\), respectively, and put

\[
K=D\operatorname{diag}(\mu)^{-1}D^{\mathsf T},\qquad
L=E\operatorname{diag}(\nu)^{-1}E^{\mathsf T},
\]

\[
C=D(S\circ S)E^{\mathsf T}=D(N\circ N)E^{\mathsf T}.
\]

Define

\[
\boxed{
\mathcal G_{\rm cv}(P)
=\operatorname{tr}(K^{-1}CL^{-1}C^{\mathsf T}).
}
\]

This number is independent of the choices of \(D,E\), invariant under
relabeling and \(GL(4)\), and nonnegative. Indeed,

\[
R_P=\operatorname{diag}(\mu)^{-1}
D^{\mathsf T}K^{-1}D
\]

is the \(\mu\)-orthogonal projection onto the complement of affine
evaluations, and similarly for \(R_Q\). Hence

\[
\mathcal G_{\rm cv}
=\|R_P(S\circ S)R_Q^{\mathsf T}\|_{\mu\otimes\nu}^2.
\]

Equivalently, regress \(x_vx_v^{\mathsf T}\) on affine functions under
\(\mu\), call the residual \(\widetilde q_v\), and define the polar
residuals similarly. Then

\[
\mathcal G_{\rm cv}
=\mathbb E_{\mu\otimes\nu}
\left[\left(
\operatorname{tr}(\widetilde q_v\widetilde q_F^\circ)
\right)^2\right]
=\operatorname{tr}(\Gamma_P\Gamma_Q),
\]

where the two \(\Gamma\)'s are positive semidefinite covariance operators
on the dual symmetric-tensor spaces, identified in coordinates by the
Hilbert--Schmidt pairing. The regression uses the product probability law
\(\mu\otimes\nu\). In particular,

\[
\mathcal G_{\rm cv}=0
\iff C=0.
\]

The construction projects before squaring, so it does not apply the
particular linear \(C-C-C+C\) functional. It does not retain the missing
orientation or control the signed boundary deficit. Bi-centering is
unnecessary for \(\mathcal G_{\rm cv}\) itself, but is required for the
displayed comparison with \(D_\partial\). Exact values include

\[
\mathcal G_{\rm cv}(\text{regular 24-cell})=\frac14,
\qquad
D_\partial=\frac{31}{800},
\qquad
\frac{D_\partial}{\mathcal G_{\rm cv}}=\frac{31}{200},
\]

and \(\mathcal G_{\rm cv}=0\) for the segment--square join and
\(\Delta(2,5)\).

No fixed comparison has survived pressure testing. The candidate
inequalities

\[
D_\partial\ge\frac{31}{200}\mathcal G_{\rm cv},\qquad
D_\partial\ge\frac18\mathcal G_{\rm cv},\qquad
D_\partial\ge\frac1{10}\mathcal G_{\rm cv}
\]

all fail high-precision tests on bi-centered Paffenholz 24-cell members.
The last ratio reaches approximately \(0.096765\) near the parameter ray
\(1.1(1/5,2/5,3/5,4/5)\). These are discovery-level counterexamples, not
interval certificates. The surviving question is whether terminality
supplies a configuration-dependent spectral coefficient or a signed
identity, not a universal scalar Poincaré constant.

An independent GPT-5.6 Sol xhigh audit returned **GO** on the identities,
**STOP** on any universal positive scalar comparison, and conditional
**GO** only as a secondary magnitude/conditioning diagnostic. It also
independently reproduced \(GL(4)\)-invariance on a nonorthogonal rational
transform and the numerical Paffenholz ratio above. The quantity is not
translation- or general-projective-invariant, so different projective
representatives must first be put in the chosen bi-centered normalization
before comparing them.
