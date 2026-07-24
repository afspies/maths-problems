# Global collision charge: an integer boundary which only survives mod two

## Result

Resolving total collision by the cyclic gap simplex does produce an
integer-valued signed boundary charge.  It does **not** produce a new
global obstruction.

The cyclic configuration quotient is nonorientable: one cyclic
relabelling reverses its orientation.  Consequently its degree-zero
intersection group with the correct orientation coefficients is
\[
 H_0(\operatorname{Conf}^{\mathrm{cyc}}_4(S^1)/C_4;\mathcal O)
 \cong\mathbb Z/2.                                      \tag{1}
\]
In the resolved gap compactification, however, the four total-collision
sectors are freely permuted.  Their quotient is one copy of the Jordan
parameter circle, and the orientation system restricts trivially there:
\[
 H_0(B_{\mathrm{coll}};\mathcal O|_{B_{\mathrm{coll}}})
 \cong\mathbb Z.                                        \tag{2}
\]
The inclusion-induced map from (2) to (1) is reduction modulo two.

Thus a signed collision count exists on the resolved boundary, but the
global square degree sees only its parity.  The local model in
`../wild-configuration-degree/README.md` realizes a boundary charge
\(\pm1\).  Disjoint copies realize arbitrary finite local sums, while a
pair changes the resolved integer by \(2\) and is invisible to (1).
There is therefore no canonical mod-four refinement, nor any rule from
prime-end cyclic order forcing the boundary integer to vanish.

This is a no-go theorem for ordinary equivariant or Borel--Moore
intersection theory.  It is not a no-go for a genuinely filtered
one-dimensional carrier with additional action, winding, or area data.

## An equivariant square test

For an ordered quadruple \(z=(z_1,z_2,z_3,z_4)\), define
\[
 d_1=z_3-z_1,\qquad d_2=z_4-z_2
\]
and
\[
 \Phi(z)=\left(
 z_1+z_3-z_2-z_4,\;
 |d_1|^2-|d_2|^2,\;
 d_1\mathbin{\cdot}d_2
 \right)\in\mathbb R^2\oplus\mathbb R\oplus\mathbb R.
                                                               \tag{3}
\]
For four distinct points, \(\Phi=0\) precisely when they are the
vertices of a square in the displayed cyclic order.  The first component
makes a parallelogram; equal and perpendicular diagonals then make it a
square.

Let \(\sigma\) cyclically relabel the points:
\[
 \sigma(z_1,z_2,z_3,z_4)=(z_2,z_3,z_4,z_1).
\]
Then \(d_1\mapsto d_2\), \(d_2\mapsto-d_1\), and
\[
 \Phi(\sigma z)=-\Phi(z).                                \tag{4}
\]
The target representation \(V\) is therefore \(-I_4\), which is
orientation preserving:
\[
 \det(\sigma|_V)=+1.                                    \tag{5}
\]

## The global quotient has only a mod-two degree

The positively cyclically ordered parameter configurations form an open
four-manifold.  In a lifted chart,
\[
 t_1<t_2<t_3<t_4<t_1+1,
\]
and cyclic relabelling acts by
\[
 (t_1,t_2,t_3,t_4)\longmapsto
 (t_2,t_3,t_4,t_1+1).
\]
Its derivative is a four-cycle, hence
\[
 \det D\sigma=-1.                                       \tag{6}
\]
The quotient
\[
 Q=\operatorname{Conf}^{\mathrm{cyc}}_4(S^1)/C_4
\]
is consequently nonorientable.  The associated square-test bundle has
fiber \(V\); by (5), its orientation line is trivial.  Local intersection
indices therefore take values in the orientation local system
\(\mathcal O\) of \(Q\).

A loop in \(Q\) induced by one cyclic relabelling has monodromy \(-1\) on
\(\mathcal O\).  Since \(Q\) is connected,
\[
\begin{aligned}
H_0(Q;\mathcal O)
&=\mathbb Z/\langle a-(-a)\rangle\\
&\cong\mathbb Z/2,
\end{aligned}                                            \tag{7}
\]
which proves (1).

Equivalently, if one ordered representative of a regular square has
integer local index \(k\), its four cyclic representatives have indices
\[
 k,\ -k,\ k,\ -k.                                       \tag{8}
\]
The signed count on the ordered cover cancels, while the quotient retains
one mod-two orbit.

## Resolving total collision

Write a cyclic quadruple by a starting parameter \(t\) and positive gaps
\[
 (g_1,g_2,g_3,g_4),\qquad \sum g_i=1.
\]
The closed gap simplex separates total collision into four sectors:
\[
 (1,0,0,0),\ (0,1,0,0),\ (0,0,1,0),\ (0,0,0,1).
\]
Before quotienting, the resolved collision locus is therefore four
copies of \(S^1\).  The \(C_4\)-action freely permutes these copies and
does not move \(t\) at a vertex.  Its quotient is
\[
 B_{\mathrm{coll}}\cong S^1.                            \tag{9}
\]

This free action is important.  In the unresolved product
\((S^1)^4\), the total diagonal is fixed by relabelling and an orbifold
description directly records a \(\mathbb Z/2\).  In the resolved
gap/screen compactification the four approach sectors have instead been
separated, so there is no \(C_4\)-stabilizer at one sector.

The generator of \(\pi_1(B_{\mathrm{coll}})\) moves \(t\) once around the
same resolved sector.  It does not perform a cyclic relabelling.
Therefore \(\mathcal O\) restricts trivially to
\(B_{\mathrm{coll}}\), proving (2).

Choose one point of the boundary circle with its sector orientation.
Under inclusion into \(Q\), paths representing cyclic relabelling impose
the relation \(a=-a\).  Hence
\[
 i_*:
 H_0(B_{\mathrm{coll}};\mathcal O)\cong\mathbb Z
 \longrightarrow H_0(Q;\mathcal O)\cong\mathbb Z/2
\]
is
\[
 i_*(n)=n\bmod2.                                        \tag{10}
\]

Thus the resolved compactification has a signed integer boundary count,
but only its parity participates in the global square degree.

## The boundary generator is geometrically realizable

The construction in `../wild-configuration-degree/README.md` supplies a
regular local square of index \(\pm1\) whose vertices depend continuously
on a scale \(\varepsilon>0\) and meet total collision at
\(\varepsilon=0\).  In the compactified universal configuration space
over \([0,\varepsilon_0]\), its zero set gives a local bordism
\[
 \{\text{regular square at }\varepsilon_0\}
 \longleftrightarrow
 \{\text{resolved collision at }0\}.                     \tag{11}
\]
Both endpoints have odd multiplicity.  Consequently the collision
boundary realizes a generator of \(\mathbb Z\) in (2), whose image is the
generator of \(\mathbb Z/2\) in (1).

Regularity also holds for the equivariant test (3), not only for the test
used in the preceding note.  At its marked square, with tangents
\[
 (1,0),\ (1,1),\ (-1,1),\ (-1,0),
\]
the derivative of (3) is
\[
 \begin{pmatrix}
  1&-1&-1& 1\\
  0&-1& 1& 0\\
 -2& 0& 0&-2\\
  1&-2& 2&-1
 \end{pmatrix},
 \qquad\det=-8.                                         \tag{12}
\]
Thus the realized boundary charge is genuinely a unit local
intersection for the \(C_4\)-equivariant formulation.

The motif can be reflected to use the other local side.  It can also be
placed in finitely many pairwise disjoint graph neighbourhoods of one
Jordan curve.  The corresponding product boxes in configuration space
are disjoint, and each contains one regular local zero.  This realizes
any prescribed finite collection of local collision generators.  The
statement is deliberately local: other squares of the approximating
curves are not classified.

Two identical disjoint motifs change the resolved local boundary sum by
\(\pm2\), while (10) sees no change.  Therefore the integer in (2) cannot
be reconstructed from the global degree.  Reducing it modulo four does
not help: local paired insertions alter that residue by \(2\) without
altering the only globally conserved class.

## Global assembly and cancellation

On the connected collision circle, an unsigned finite collection of
collision points represents only its parity in
\(H_0(-;\mathbb F_2)\).  An even collection is the boundary of arcs
pairing the points, and an odd collection is homologous to one point.
With the resolved integer orientation, the signed total is defined, but
moving into the interior quotient adds the relation \(a=-a\), leaving
only parity.

This gives the complete conservation law available from ordinary
degree:
\[
 \text{interior square parity}
 +\text{total-collision parity}
 =\text{fixed global parity}.                            \tag{13}
\]
A hypothetical square-free limiting curve is compatible with its odd
class being carried by one total-collision point.  The local construction
shows that neither Jordan separation nor a one-sided prime-end label
forbids such a point.

This does not prove that the complete collision set of an arbitrary
approximating sequence can be prescribed independently: untracked
nonlocal squares may impose further relations.  It proves that the
equivariant topology and the resolved boundary groups impose no such
relation.

## Prime-end order and normalized screens

Orienting the Jordan parameter circle or remembering the location of a
collision does not change (10).  The collision in (11) may remain at one
fixed prime end while only its scale tends to zero, so there is no forced
winding of collision location.

Retaining a normalized finite screen also does not remove the boundary
generator.  In the local bordism, the normalized screen is a constant
exact square.  Reflecting the motif realizes the opposite geometric
orientation.  Thus screen orientation and prime-end side can split the
boundary into components, but at least one \(\mathbb Z\)-generator is
realized in each permitted local type and still maps to parity by (10).

## Why unfiltered persistence over scale also fails

The local bordism (11) is a degree-one class at positive scale whose
lifetime ends at scale zero.  Ordinary persistence records a half-open
interval and permits this endpoint.  Excluding scale zero loses the
class; adjoining scale zero records the boundary charge.

The integer resolved charge does not repair persistence, because a local
interval can end with charge \(1\), and pairs of intervals can change its
integer lift by \(2\) without changing global parity.

Any viable persistent formulation must add a quantity which prevents a
global class from ending through (11).  Possibilities include:

- a positive lower bound on the persistence length of the global class;
- a two-sided continuation law pairing total-collision generators;
- an action or winding filtration in which the local motif is null but
  the global class is not;
- a one-dimensional carrier over all scales whose allowed boundary is
  smaller than the full resolved collision circle.

None follows from ordinary configuration topology.

## Exact no-go and next target

The calculation rules out the following as standalone proofs:

1. summing ordinary signed indices on the ordered cover;
2. treating the resolved boundary integer as a canonical global degree;
3. reducing that integer modulo four;
4. correcting parity only by collision location, prime-end side, or a
   finite normalized screen;
5. using persistence with scale as its only filtration.

The next viable topological statement must be one dimension higher:

> **Filtered carrier target.** From a hypothetical square-free Jordan
> curve, construct a compact one-dimensional equivariant carrier whose
> projection has odd degree over a positive scale interval, and prove
> that every component meeting total collision contributes zero in a
> second filtration such as action, winding, or paired-ribbon area.

Matschke's fixed-type continuum of special trapezoids supplies a
topological carrier, but not the second filtration.  Equations (10)--(13)
show exactly why no degree-zero collision charge can substitute for it.
