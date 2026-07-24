# Robust terminal rigidity and exact limits of two local ansatzes

The full four-dimensional Mahler conjecture remains open.  This note proves
a stronger flag theorem for terminal polytopes, classifies another infinite
subclass, and records exact obstructions to the universal unweighted
degree-two contraction and fixed-geometry one-sided flip ansatzes.

## 1. A weighted terminal-excess inequality

Let \(P\) be a terminal non-simplex four-polytope.  Write

\[
V=f_0(P),\qquad F=f_3(P),\qquad I=f_{03}(P),
\]

and, for a facet \(G\), put

\[
e_G=|V(G)|-4,\qquad E(P)=\sum_Ge_G=I-4F.
\]

Only nonsimplicial facets have positive excess.  Let

\[
\beta_3(P)=
\max\left\{
e_{G_1}+e_{G_2}+e_{G_3}:
y_{G_1},y_{G_2},y_{G_3}\text{ are linearly independent}
\right\},
\]

where the maximum is over nonsimplicial facets.

Then

\[
\boxed{
E(P)\ge V-5+\beta_3(P).
}
\]

In particular, the nonsimplicial-facet normals span \(\mathbb R^4\), so
\(\beta_3(P)\ge3\), and

\[
\boxed{
f_{03}\ge4f_3+f_0-2.
}
\]

### Proof

For a facet \(G\), its affine-relation space has dimension

\[
\dim\operatorname{Rel}(G)=|V(G)|-4=e_G.
\]

The robust-support characterization of terminality says that, for every
normal flat \(W\) of rank at most three, the circuit rows belonging to
facets with \(y_G\notin W\) still have rank \(V-5\).

The nonsimplicial-facet normals span \(\mathbb R^4\).  Indeed, take any
nonaffine vertex function.  Its restriction is automatically affine on
every tetrahedral facet, while terminality says the normals of the facets
where affinity fails span all of \(\mathbb R^4\).

Now take an independent triple attaining \(\beta_3(P)\), and let \(W\) be
the rank-three flat spanned by its normals.  The rows outside \(W\) have
rank \(V-5\), hence row capacity at least \(V-5\).  The erased flat contains
the chosen triple, hence has capacity at least \(\beta_3(P)\).  Therefore

\[
E(P)\ge(V-5)+\beta_3(P),
\]

as claimed.

If \(P^\circ\) is terminal, applying the same theorem to \(P^\circ\) gives

\[
f_{03}\ge4f_0+f_3-2.
\]

Consequently every pair-terminal non-simplex satisfies the new flag
inequality

\[
\boxed{
2f_{03}\ge5(f_0+f_3)-4.
}
\]

The previous campaign bound had \(-10\) in place of \(-4\).

## 2. At least six nonsimplicial facets

There is a structural strengthening which does not enumerate face
lattices.

> **Six-facet theorem.** A terminal non-pyramid four-polytope has at least
> six nonsimplicial facets.  Dually, a pair-terminal non-pyramid has at
> least six nonsimplicial facets and at least six nonsimple vertices.

### Coloops force pyramids

Consider the rank-four linear matroid of the nonsimplicial-facet normals.
If \(G\) is a coloop, the other nonsimplicial normals span a flat of rank at
most three.  Erase that flat.  Robust terminality says the single remaining
block \(\operatorname{Rel}(G)\) has rank at least \(V-5\).  Hence

\[
|V(G)|-4\ge V-5.
\]

Since \(G\) is a proper facet, equality holds and \(|V(G)|=V-1\).  Thus
\(P\) is a pyramid with base \(G\).

It follows that a terminal non-pyramid has a coloop-free rank-four
nonsimplicial-normal matroid, and therefore has at least five elements.

### Five elements are impossible

Suppose there are exactly five nonsimplicial facets
\(G_1,\ldots,G_5\).  A coloop-free rank-four matroid on five nonzero
elements is \(U_{4,5}\): any four normals are independent.

Let \(\mathcal G\) be the \(V-5\)-dimensional global affine-dependency
space, and let

\[
D_i=\mathcal G\cap\mathbb R^{V(G_i)}
\]

be the dependencies supported on \(G_i\).  Erasing the normal flat spanned
by any other three facets gives

\[
D_i+D_j=\mathcal G
\qquad(i\ne j).
\]

Put \(C_i=V(P)\setminus V(G_i)\).  The annihilator \(D_i^\perp\subset
\mathcal G^*\) is spanned by the coordinate restrictions indexed by
\(C_i\).  If \(C_i\cap C_j\) contained a vertex \(v\), its coordinate
functional would lie in both annihilators.  It is nonzero because a zero
Gale coordinate would make \(P\) a pyramid.  This contradicts

\[
(D_i+D_j)^\perp=D_i^\perp\cap D_j^\perp=0.
\]

Thus the five complements \(C_i\) are pairwise disjoint.  Each contains at
least two vertices, since a facet missing exactly one vertex is the base of
a pyramid.  On the other hand, every vertex is absent from at most one
\(G_i\), so every vertex in \(C_i\) lies on the other four facet
hyperplanes.  Their normals are independent, and therefore their common
intersection contains at most one point.  Hence \(|C_i|\le1\), a direct
contradiction.

This proves the six-facet theorem.  Together with the already proved
pyramid theorem, it classifies every terminal four-polytope with at most
five nonsimplicial facets.

## 3. Equality rigidity

Suppose

\[
E(P)=V-2.
\]

The weighted inequality forces every nonsimplicial facet to have excess
one.  Indeed, every such facet belongs to an independent normal triple,
and any triple of total excess at least four would give
\(E(P)\ge V-1\).

No rank-three normal flat can contain four nonsimplicial normals.  Hence,
if \(m\) is the number of nonsimplicial facets,

\[
m=E(P)=V-2
\]

and their normal matroid is \(U_{4,V-2}\).  Erasing any three normal blocks
leaves \(V-5\) one-row blocks of rank \(V-5\).  Thus their circuit-row
matroid is

\[
U_{V-5,V-2}.
\]

If equality holds for both \(P\) and \(P^\circ\), then

\[
\boxed{
f_0=f_3=n,\qquad f_{03}=5n-2.
}
\]

Exactly two facets are tetrahedra and exactly two vertices are simple.
This reduces the extremal flag case to two uniform-matroid realization
problems rather than a face-lattice enumeration.

## 4. The intrinsic quadratic circuit object

The previous note used an ambiguous notation for a circuit second moment.
For a shadow speed \(\alpha\), its facet residual is intrinsically a
covector

\[
R_G(\alpha)\in\operatorname{Rel}(G)^*,
\qquad
R_G(\alpha)(\gamma)=\sum_{v\in G}\gamma_v\alpha_v.
\]

There is no canonical identification of this covector with a circuit
relation.  The intrinsic second-moment map is instead

\[
\boxed{
\mathcal Q_G:\operatorname{Rel}(G)\longrightarrow
\operatorname{Sym}^2(\mathbb R^4),\qquad
\mathcal Q_G(\gamma)=\sum_{v\in G}\gamma_vx_vx_v^{\mathsf T}.
}
\]

A genuine Bochner formula would first need a positive, intrinsic Hodge
operator

\[
\operatorname{Rel}(G)^*\longrightarrow\operatorname{Rel}(G).
\]

Terminality supplies injectivity after every rank-three normal-flat
erasure, but it does not supply this metric.

There is nevertheless a qualitative degree-two consequence.  For

\[
q_u(v)=(u\cdot x_v)^2,
\]

a generic \(u\) makes \(q_u\) nonaffine on every nonsimplicial facet.  If
all such squares were affine on the vertices of one facet, polarization
would make the four-dimensional space of affine evaluations a unital
algebra which separates the facet vertices.  A separating unital algebra
on a finite set is the full function algebra, forcing the facet to have
only four vertices.  The exceptional \(u\)'s for each nonsimplicial facet
form a proper algebraic set, so one generic \(u\) works for all facets.

After choosing any finite-dimensional norms, this injectivity gives a
realization-dependent lower singular value for the resulting quadratic
evaluation operator.  No intrinsic or volume-normalized metric has been
identified, so this qualitative fact gives no trace sign by itself.

## 5. Exact failure of a universal unweighted quadratic identity

Let \(D_P,D_{P^\circ}\) stack facet-supported circuit relations and put

\[
N_{vG}=x_v\cdot y_G.
\]

For primal and dual circuit rows \(\gamma,\delta\),

\[
\boxed{
\gamma^{\mathsf T}(N\circ N)\delta
=\operatorname{tr}\left(
\mathcal Q_P(\gamma)\mathcal Q_{P^\circ}(\delta)
\right).
}
\]

Therefore the complete direct mixed quadratic datum is

\[
C=D_P(N\circ N)D_{P^\circ}^{\mathsf T}
 =D_P(L\circ L)D_{P^\circ}^{\mathsf T}.
\]

Exact rational calculations give:

| pair | primal quadratic rank | polar quadratic rank | \(\operatorname{rank}C\) |
|---|---:|---:|---:|
| regular 24-cell | 9 | 9 | 9 |
| generic Paffenholz 24-cell | 10 | 9 | 9 |
| segment--square join | 1 | 1 | 0 |
| centered \(\Delta(2,5)\) | 5 | 5 | 0 |
| cube/cross-polytope | 6 | 0 | 0 |

The segment--square join and centered hypersimplex have nonzero boundary
deficits,

\[
D_\partial=\frac1{72},\qquad
D_\partial=\frac{125}{3168},
\]

respectively, but \(C=0\).  Both sides still have full all-facet circuit
rank \(f_0-5\).  These controls are not terminal.  They therefore rule out
only a universal identity, valid for all polytopes, which expresses
\(D_\partial\) solely as a quadratic form in the unweighted direct
contractions \(\operatorname{tr}(\mathcal Q\mathcal Q^\circ)\).  They do
not rule out a terminality-dependent Hodge operator, separate primal and
dual Gram data, or an identity restricted to terminal pairs.

The hypersimplex also checks the weighted terminal theorem without
enumerating direction flats.  Its five octahedral facets have

\[
V=10,\qquad E=10,\qquad\beta_3=6,
\]

whereas terminality would require

\[
E\ge V-5+\beta_3=11.
\]

## 6. Regression cancellation

Assume \(P\) and \(P^\circ\) are bi-centered.  There is then a basis-free
reason the raw nonlinear regression residual cannot by itself be the
desired energy.  Draw a primal cone-boundary point \(U\) with its scaled
facet normal \(Y\), and independently draw a polar cone-boundary point
\(W\) with its scaled normal \(X\).  Put

\[
H=\mathbb E UU^{\mathsf T},\qquad
H^\circ=\mathbb E WW^{\mathsf T}.
\]

The dual-frame identities are

\[
\mathbb E UY^{\mathsf T}
=\mathbb E WX^{\mathsf T}
=\frac14I.
\]

Define the regression residuals

\[
a=Y-\frac14H^{-1}U,\qquad
b=X-\frac14(H^\circ)^{-1}W.
\]

Then

\[
\mathbb E[aU^{\mathsf T}]
=\mathbb E[bW^{\mathsf T}]
=0.
\]

Writing

\[
N=X\cdot Y,\qquad Z=U\cdot W,\qquad
N_{\rm lin}
=\frac1{16}U^{\mathsf T}H^{-1}(H^\circ)^{-1}W,
\]

one obtains

\[
N-N_{\rm lin}
=b\cdot a
+b\cdot\frac14H^{-1}U
+\frac14(H^\circ)^{-1}W\cdot a.
\]

Independence and the two orthogonality relations show that
\(N-N_{\rm lin}\) is orthogonal in \(L^2\) to every bilinear function
\(U^{\mathsf T}TW\).  In particular,

\[
\langle Z,N-N_{\rm lin}\rangle=0.
\]

Consequently the proposed nonlinear Bochner term cancels exactly:

\[
\boxed{
D_\partial
=\langle Z,N_{\rm lin}-Z\rangle
=\frac14-\operatorname{tr}(HH^\circ).
}
\]

The corresponding Pythagorean identity is

\[
\boxed{
\mathbb E N^2
=\frac1{256}\operatorname{tr}\bigl((H^\circ)^{-1}H^{-1}\bigr)
+\mathbb E(N-N_{\rm lin})^2.
}
\]

At a hypothetical local Mahler minimum,

\[
H^{1/2}H^\circ H^{1/2}\succeq\frac1{16}I.
\]

Thus a sufficient, but still unproved, terminal contradiction is

\[
\boxed{
\operatorname{tr}\left(
(H^{1/2}H^\circ H^{1/2})^{-1}
\right)>64.
}
\]

For the regular 24-cell the exact regression data are

\[
\operatorname{tr}(HH^\circ)=\frac{169}{800},\qquad
\mathbb E N^2=\frac12,
\]

\[
\frac1{256}\operatorname{tr}((H^\circ)^{-1}H^{-1})
=\frac{50}{169},\qquad
\mathbb E(N-N_{\rm lin})^2=\frac{69}{338}.
\]

In particular, the inverse trace is \(12800/169>64\).

## 7. Flip cancellation and the surviving gate

For a primal boundary tetrahedron \(T=(u_i)_{i=1}^4\), a polar boundary
tetrahedron \(S=(w_j)_{j=1}^4\), and

\[
A_{ij}=u_i\cdot w_j,\qquad
\sigma=\mathbf1^{\mathsf T}A\mathbf1,
\]

the exact local boundary bracket is

\[
\boxed{
\frac{
25N\sigma-\sigma^2-\|A\mathbf1\|^2
-\|A^{\mathsf T}\mathbf1\|^2-\|A\|_F^2
}{400}.
}
\]

When one retriangulates a fixed facet across a five-point bistellar circuit,
while keeping the opposite tetrahedron and \(N\) fixed, the signed
volume-weighted sum of this bracket is unchanged.  The potential
\(\mathcal Q_\gamma\) terms from the centroid square and the diagonal
second moment cancel.  Thus this fixed-geometry one-sided flip energy is
identically blind to the target.  This calculation does not exclude a
geometric or oriented two-sided flip argument.

The universal unweighted contraction, raw regression-residual energy, and
fixed-geometry one-sided flip routes must therefore stop.  A
terminality-dependent Hodge operator remains possible.  Two exact gates
survive:

1. Prove or falsify the **robust quadratic-coupling lemma**
   \[
   D_P(N\circ N)D_{P^\circ}^{\mathsf T}\ne0
   \]
   for every connected pair-terminal non-simplex.  A sufficient condition
   is
   \[
   \rho(P)+\rho(P^\circ)>10,
   \]
   where \(\rho(P)\) is the quadratic circuit-image rank.
2. Derive a global **oriented cofactor transport** operator.  It must retain
   determinant signs and distinguish regular-24-cell local brackets such
   as \(3/16\) and \(-11/100\); the unweighted contractions above do not
   provide that sign-sensitive transport.

Neither gate is presently proved.  The full conjecture remains open, but
these two specific local mechanisms are now exactly falsified and the
remaining terminal combinatorics are strictly narrower.
