# Quadratic slack flexes and the exact cofactor cancellation

The full four-dimensional Mahler conjecture remains open. This note
identifies the intrinsic geometric meaning of quadratic circuit coupling,
proves a new lower bound on its one-sided rank for terminal polytopes, and
shows that the displayed uniform oriented cofactor residues cancel in the
simplex moment energy.

## 1. Quadratic Hilbert rank

Let \(P\subset\mathbb R^4\) have vertices \(x_v\), and put

\[
U=\begin{pmatrix}1&x_v^{\mathsf T}\end{pmatrix}_{v\in V},
\qquad
\mathcal G_P=\ker U^{\mathsf T}.
\]

The global quadratic circuit map is

\[
\mathcal Q_P:\mathcal G_P\longrightarrow\operatorname{Sym}_4,
\qquad
\mathcal Q_P(\gamma)=\sum_v\gamma_vx_vx_v^{\mathsf T}.
\]

Its transpose sends a quadratic form \(A\) to the evaluation class

\[
\bigl(x_v^{\mathsf T}Ax_v\bigr)_v
\pmod{\operatorname{col}U}.
\]

Consequently

\[
\boxed{
\rho(P):=\operatorname{rank}\mathcal Q_P=h_{V(P)}(2)-5,
}
\]

where \(h_{V(P)}(2)\) is the quadratic Hilbert function of the homogenized
vertex configuration in \(\mathbb P^4\). For a terminal polytope,
facet-supported circuits span \(\mathcal G_P\), so this global rank is
exactly the rank computed from all facet circuit blocks.

The elementary bounds

\[
\rho(P)\le f_0(P)-5,\qquad
\rho(P^\circ)\le f_3(P)-5
\]

show an important limitation of the former sufficient target:

\[
\rho(P)+\rho(P^\circ)>10
\]

is impossible whenever \(f_0+f_3\le20\). The existing terminal flag
inequalities do not exclude this range.

## 2. Coupling is a Hadamard-square slack obstruction

Let \(y_F\) be the vertices of \(P^\circ\), let

\[
N_{vF}=x_v\cdot y_F,
\qquad
S_{vF}=1-N_{vF},
\]

and write

\[
S=UH\,W^{\mathsf T},
\qquad
H=\operatorname{diag}(1,-I_4),
\qquad
W=\begin{pmatrix}1&y_F^{\mathsf T}\end{pmatrix}_{F}.
\]

Thus \(S\) has rank five. If \(D_P,D_{P^\circ}\) are bases of the complete
left and right affine-dependency spaces, then the tangent space at \(S\) to
the rank-at-most-five determinantal variety is

\[
T_S\mathcal R_5
=
\left\{
Z:D_PZD_{P^\circ}^{\mathsf T}=0
\right\}.
\]

Since the dependency matrices annihilate both the constant and bilinear
parts,

\[
D_P(S\circ S)D_{P^\circ}^{\mathsf T}
=D_P(N\circ N)D_{P^\circ}^{\mathsf T}.
\]

Therefore:

> **Hadamard-square slack theorem.**
> \[
> \boxed{
> D_P(N\circ N)D_{P^\circ}^{\mathsf T}=0
> \iff
> S\circ S\in T_S\mathcal R_5.
> }
> \]

Because \(S\circ S\) is zero on every incidence, vanishing quadratic
coupling is exactly the existence of the special fixed-support
Zariski-tangent slack flex

\[
\boxed{\dot S=S\circ S.}
\]

This is only a first-order determinantal statement: no integrating
rank-five fixed-support curve is asserted.

Every two-level polytope is a necessary boundary case. In offset-one facet
normalization, each slack column takes values in \(\{0,c_F\}\), so

\[
S\circ S=S\operatorname{diag}(c_F)
\]

and the quadratic coupling vanishes identically. Thus any proof of robust
nonzero coupling must, at minimum, exclude terminal non-simplex two-level
polytopes or treat them separately.

There is also a useful conditional certificate. If the fixed-support
rank-five slack realization is infinitesimally projectively unique, every
allowed tangent is a row/column scaling. Hence \(S\circ S\in T_S\mathcal
R_5\) would force

\[
s_{vF}=a_v+b_F
\]

on all nonincidences. Any even nonincidence cycle with nonzero alternating
slack sum then certifies nonzero coupling.

## 3. A new terminal rank bound

> **Theorem.** Every terminal non-simplex four-polytope satisfies
> \[
> \boxed{\rho(P)\ge3.}
> \]
> In particular, every terminal non-simplex has at least eight vertices,
> and every pair-terminal non-simplex has
> \[
> \boxed{f_0\ge8,\qquad f_3\ge8.}
> \]

### Nonzero local tensors

For a nonsimplicial facet \(F\), the space
\(\mathcal Q_F(\operatorname{Rel}(F))\) is nonzero. Otherwise every
quadratic function on its vertices would be affine there. By polarization,
the four-dimensional space of affine evaluations on \(F\) would be a
unital algebra separating the vertices. A separating unital algebra on a
finite set is the full function algebra, forcing \(F\) to have only four
vertices.

Every \(A\in\mathcal Q_F(\operatorname{Rel}(F))\) kills the facet normal:

\[
Ay_F
=
\sum_{v\in F}\gamma_vx_v(x_v\cdot y_F)
=
\sum_{v\in F}\gamma_vx_v
=0.
\]

If \(\rho(P)=1\), every nonzero local image is a multiple of one matrix
\(A\). The nonsimplicial-facet normals span \(\mathbb R^4\) by
terminality, so \(A\) kills a spanning set and is zero, a contradiction.

### Excluding a symmetric pencil

Suppose \(\rho(P)=2\), and write the image as the symmetric pencil

\[
R=\operatorname{span}(A,B).
\]

Robust terminality says that after erasing all facet blocks whose normals
lie in any rank-at-most-three flat, the remaining local quadratic images
still span \(R\).

First suppose \(\det(sA+tB)\not\equiv0\). A two-dimensional local image
would put its facet normal in \(\ker A\cap\ker B\), making the pencil
identically singular. Thus each local image is the line of a singular
pencil member \(M_p\), and its facet normal belongs to \(\ker M_p\). If
\(k_p=\dim\ker M_p\), then

\[
\sum_p k_p\le4,
\]

because corank is at most the vanishing order of the homogeneous
determinant at each projective root, including infinity. Fix one realized
root \(p_0\), and span all normal groups at the other roots. That span has
rank at most \(4-k_{p_0}\le3\). Erasing it leaves only the single pencil
line \(\mathbb RM_{p_0}\), contradicting robust spanning of \(R\).

It remains to treat an identically singular pencil. Quotient first by the
common kernel. We use the following elementary lemma.

> **Small symmetric singular-pencil lemma.** A real, common-kernel-free,
> identically singular symmetric \(n\times n\) pencil with \(n\le4\) has
> all its real kernel directions in a subspace of dimension at most
> \(n-1\).

Choose a member of maximal rank \(r\) and, by congruence, write

\[
A=\begin{pmatrix}H&0\\0&0\end{pmatrix},
\qquad
B=\begin{pmatrix}C&D\\D^{\mathsf T}&E\end{pmatrix},
\]

with \(H\) nonsingular. Maximality and the Schur complement give

\[
E=0,\qquad
D^{\mathsf T}(H+tC)^{-1}D=0.
\]

If \(r\le n-2\), the columns of \(D\) form a totally isotropic subspace for
\(H^{-1}\), so

\[
\operatorname{rank}D\le\lfloor r/2\rfloor.
\]

For \(n\le4\), a nonzero vector remains in \(\ker D\), producing a common
kernel vector. Hence \(r=n-1\).

Now \(D=d\) is one column. Put \(v=H^{-1}d\) and \(T=H^{-1}C\). Expanding
the Schur identity shows

\[
\langle T^iv,T^jv\rangle_H=0
\qquad(i,j\ge0).
\]

The cyclic span of \(v\) is totally isotropic. Common-kernel-freeness gives
\(d\ne0\), hence \(v\ne0\). A one-dimensional \(H\) admits no such vector.
In dimensions two and three the Witt index of \(H\) is at most one, so the
cyclic span is one-dimensional and \(Tv=\alpha v\). With

\[
e=(0,1),\qquad u=(-v,\alpha),
\]

one has

\[
Ae=0,\qquad Au+Be=0,\qquad Bu=0.
\]

Indeed, \(C v=\alpha H v=\alpha d\) and
\(d^{\mathsf T}v=0\). Therefore

\[
P(s,t)(se+tu)=0.
\]

The vectors \(e,u\) are independent, so
\(k(s,t)=se+tu\) is a primitive homogeneous linear kernel vector.

Every column of \(\operatorname{adj}P\) lies in the polynomial kernel.
Primitivity of \(k\), followed by symmetry of the adjugate, gives

\[
\operatorname{adj}P(s,t)=p(s,t)k(s,t)k(s,t)^{\mathsf T},
\qquad \deg p=n-3.
\]

For \(n=3\),

\[
\operatorname{adj}P(s,t)=c\,k(s,t)k(s,t)^{\mathsf T},
\]

so all kernels lie in \(\operatorname{span}(e,u)\). For \(n=4\),

\[
\operatorname{adj}P(s,t)=\ell(s,t)\,
k(s,t)k(s,t)^{\mathsf T}
\]

with \(\ell\) linear. There is at most one exceptional member \(E\). It has
rank two. To see this, choose a rank-three member \(N\), with
\(\ker N=\mathbb Rz\). Since the determinant vanishes identically,

\[
0=\left.\frac d{d\epsilon}\det(N+\epsilon E)\right|_{\epsilon=0}
=\operatorname{tr}(\operatorname{adj}N\,E)
=c\,z^{\mathsf T}Ez.
\]

If \(E\) had rank one, real symmetry would write
\(E=\sigma aa^{\mathsf T}\), forcing \(Ez=0\); rank zero is immediate.
As \(E,N\) span the pencil, either case produces a common kernel, a
contradiction. Thus the exceptional kernel adds at most one direction, and
all kernel directions span at most three dimensions.

Finally restore the common kernel \(K\), put \(c=\dim K\), and let
\(n=4-c\). If the quotient pencil remains singular, the inverse image of
its kernel-direction span has dimension at most

\[
c+(n-1)=3
\]

and contains every nonsimplicial-facet normal. Erasing that flat removes
every nonzero local block. If the quotient pencil is regular and no local
root line survives outside \(K\), erasing \(K\) already removes every
block. Otherwise choose a realized root \(p_0\) and set

\[
W=K+\operatorname{span}\{y_F:\text{the local block has root }p\ne p_0\}.
\]

Root multiplicities in the degree-\(n\) quotient determinant give

\[
\dim W\le c+n-\operatorname{mult}(p_0)\le3.
\]

Two-dimensional local blocks have normals in \(K\); after erasing \(W\),
only the line \(M_{p_0}\) survives. Both cases contradict robust
terminality. Hence \(\rho(P)\ne2\), proving the theorem.

## 4. Why rank robustness cannot prove six

The bound three is sharp for the currently available abstract data. For
each \(\rho\in\{3,4,5\}\), put \(d=\rho-3\),

\[
B(z)=
\begin{pmatrix}
-z&1&0&0\\
0&-z&1&0\\
0&0&-z&1
\end{pmatrix},
\quad
p_d(z)=1+z+\cdots+z^d,
\]

\[
C_d(z)=\operatorname{diag}(1,-1,-p_d(z)),
\qquad
A_d(z)=B(z)^{\mathsf T}C_d(z)B(z).
\]

Then

\[
A_d(z)(1,z,z^2,z^3)^{\mathsf T}=0,
\]

and \(A_d(z)\) has one positive, two negative, and one zero eigenvalue for
\(z\ge0\). Its coefficient matrices in
\(1,z,\ldots,z^{\rho-1}\) are independent.

Take \(m=\rho+3\), \(z_i=i\),

\[
y_i=(-1)^i(1,i,i^2,i^3),
\qquad
R_i=\mathbb RA_d(i).
\]

The normal matroid is \(U_{4,m}\), and any rank-three flat erases at most
three blocks. Any \(\rho\) remaining \(A_d(i)\)'s span the
\(\rho\)-dimensional space. Moreover,

\[
\sum_{i=0}^{m-1}\binom{m-1}{i}y_i=0,
\]

so the normals positively span \(\mathbb R^4\). The inertia
\((1,2,1)\) is exactly that of a five-vertex triangular-bipyramid facet
circuit tensor.

These are exact abstract countermodels, not asserted polytope
realizations. They prove that normal-flat erasure, positive spanning,
kernel incidence, local convex-facet inertia, and uniform matroids cannot
yield \(\rho>3\). A stronger theorem must use simultaneous global gluing.

After projectively normalizing five vertices to

\[
0,e_1,e_2,e_3,e_4,
\]

the remaining vertices \(z\) give a canonical dependency basis with

\[
\boxed{
\mathcal Q_z=zz^{\mathsf T}-\operatorname{diag}(z).
}
\]

Thus the next algebraic attack surface is the common
Veronese-defect span of the extra vertices together with the requirement
that all facet tensors arise from this one configuration.

## 5. The exact oriented cofactor response

Take primal and polar affine circuits
\(x_0,\ldots,x_5\) and \(y_0,\ldots,y_5\). Let \(U,W\) be their
homogeneous \(6\times5\) evaluation matrices, and define

\[
\gamma_i=(-1)^i\det U_{\widehat i},
\qquad
\delta_j=(-1)^j\det W_{\widehat j}.
\]

For their \(6\times6\) slack block

\[
S=UHW^{\mathsf T},
\]

Cauchy--Binet gives

\[
\operatorname{Cof}_{ij}(S)=\gamma_i\delta_j.
\]

Therefore:

> **Oriented response identity.**
> \[
> \boxed{
> \left.\frac d{dt}
> \det\bigl(S+t(S\circ S)\bigr)
> \right|_{t=0}
> =
> \left.\frac d{dt}
> \det\bigl(S+t(N\circ N)\bigr)
> \right|_{t=0}
> =
> \gamma^{\mathsf T}(N\circ N)\delta
> =
> \operatorname{tr}
> \bigl(\mathcal Q_X(\gamma)\mathcal Q_Y(\delta)\bigr).
> }
> \]

The equality of the two derivatives follows because affine circuits
annihilate the constant and bilinear terms in
\(S\circ S=1-2N+N\circ N\). Thus quadratic circuit coupling is precisely
the first oriented cofactor response of a rank-five slack determinant to
the fixed-incidence deformation

\[
s\longmapsto s+ts^2.
\]

This is the clean oriented meaning that was missing from the previous
note.

## 6. Why ordinary cofactor transport still cancels

For a pair of 4-simplices, the exact \(900\)-scaled moment energy is

\[
E=T_0+T_r+T_c+T_e,
\]

where the four terms are the square of the total pairing sum, the sum of
row-sum squares, the sum of column-sum squares, and the sum of entry
squares.

Across the two affine circuits above, exact expansion gives

\[
\sum_{i,j}\gamma_i\delta_jT_0(\widehat i,\widehat j)=C,
\]

\[
\sum_{i,j}\gamma_i\delta_jT_r(\widehat i,\widehat j)=-C,
\qquad
\sum_{i,j}\gamma_i\delta_jT_c(\widehat i,\widehat j)=-C,
\]

\[
\sum_{i,j}\gamma_i\delta_jT_e(\widehat i,\widehat j)=C,
\]

where

\[
C=\gamma^{\mathsf T}(N\circ N)\delta.
\]

Hence the actual barycentric combination cancels:

\[
\boxed{C-C-C+C=0.}
\]

Equivalently, for one primal circuit, every fixed polar simplex \(T\), and
every constant \(c\),

\[
\sum_i(-1)^i\det S_{\widehat i,T}
\bigl(E(\widehat i,T)-c\bigr)=0,
\]

and the analogous double-circuit identity also holds.

The displayed ordinary one- and two-circuit cofactor residues therefore
cancel identically. Summing these uniform barycentric residues cannot prove
the trace sign. Geometry-dependent, nonlinear, or nonlocal
cofactor/Plücker weights are not excluded.

It does **not** rule out a terminality-dependent nonlocal Hodge or Green
operator. Such an operator would have to redistribute the four cofactor
residues before their uniform barycentric coefficients cancel.

## 7. Exact checks and surviving route

The harness verifies:

- regular 24-cell global slack obstruction rank \(9\);
- generic Paffenholz obstruction rank \(9\);
- zero obstruction for the segment--square join, centered
  \(\Delta(2,5)\), and cube/cross-polytope pair;
- on the regular-24-cell circuit pair
  \[
  I=(0,1,2,4,8,15),\qquad
  J=(0,1,2,3,6,12),
  \]
  the exact response is
  \[
  C=-16,
  \]
  the determinant derivative is \(-16\), and the four residues are
  \[
  (-16,16,16,-16);
  \]
- all \(\rho=3,4,5\) Vandermonde countermodels over
  \(\mathbb Q\), including every robust-erasure minor.

The rank-sum shortcut is therefore demoted from primary gate to a possible
large-cardinality corollary. The credible next routes are:

1. classify globally realizable low-Hilbert configurations using the
   common tensors \(zz^{\mathsf T}-\operatorname{diag}(z)\), beginning with
   \(f_0+f_3\le20\);
2. exclude terminal non-simplex two-level polytopes;
3. construct a terminality-dependent nonlocal Hodge/Green weighting before
   the four cofactor residues cancel;
4. at a constrained-critical candidate, use the stress-corrected
   semidefinite Schur complement rather than unconditional rank.

None of these final steps is proved here.
