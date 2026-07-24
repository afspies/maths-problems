# Configuration-space degeneration audit

## Exact special-trapezoid reduction

Matschke's Theorem 2.8 gives a useful contrapositive.  Fix
\(\varepsilon\in(0,1)\) and take the generator
\[
 \omega_\varepsilon(t)=(t,t+\varepsilon)
\]
of the deleted product of the parameter circle.  If a Jordan curve has no
inscribed square, its mod-two intersection number with the special
trapezoid locus is one.  Consequently it contains, for **every**
\(\varepsilon\), four cyclically ordered vertices \(A,B,C,D\) satisfying
\[
 AB=BC=CD=a>AD=b,\qquad AC=BD.                            \tag{1}
\]
Thus a hypothetical Square Peg counterexample has exact special
trapezoids at arbitrarily small parameter scales.  This is stronger than
the existence of approximate squares on smooth approximants.

## Classification of the collision screens

The metric equations (1) force an elementary two-type classification.
Place
\[
 A=(-b/2,0),\qquad D=(b/2,0),\qquad B=(u,h).
\]
The equal-diagonal equation and the three equal-side equations force
\(C=(-u,h)\) or \(C=(u,-h)\).  The latter alternative is incompatible
with \(a>b\).  In the former, \(|u|=a/2\), with two possible label orders:
\[
\begin{array}{ll}
\text{normal:}&
 h^2=a^2-\dfrac{(a-b)^2}{4},\\[1.2ex]
\text{crossed:}&
 h^2=a^2-\dfrac{(a+b)^2}{4}.
\end{array}                                                \tag{2}
\]
After scaling \(b=1\), a shrinking sequence therefore has only the
following screens:

- \(a/b\to1\), normal type: a square screen;
- \(a/b\to1\), crossed type: pair coalescence;
- \(a/b\to k\in(1,\infty)\): a genuine isosceles-trapezoid screen;
- \(a/b\to\infty\): an equilateral-triangle screen with \(A=D\).

The reduction does not exclude any of these screens.

## The tangent-free degree that survives

For fixed \(\varepsilon\), define
\[
 u_\varepsilon(t)=
 \frac{c(t+\varepsilon)-c(t)}
 {|c(t+\varepsilon)-c(t)|}\in S^1.                        \tag{3}
\]
If \(c\) is positively oriented, then
\[
 \deg u_\varepsilon=1.                                    \tag{4}
\]
Indeed, a Schoenflies ambient isotopy carries \(c\) to the standard
circle, never allowing the two endpoints of the secant to meet.  Degree is
therefore invariant, and the circle calculation gives one.

Equation (4) is genuine tangent-free information, but it recovers the
special-trapezoid obstruction rather than excluding its collision
screens.

## Scale-continuation strengthening

Assume the curve has no square and fix
\(0<\delta<\varepsilon_0<1\).  The exact special-trapezoid locus contains
a compact connected subset whose scale projection covers
\([\delta,\varepsilon_0]\).  It can be chosen to have one fixed geometric
type, normal or crossed.

To see this, trivialize the four-dimensional configuration domain with
the distinguished parameter gap equal to
\(\varepsilon\in[\delta,\varepsilon_0]\).  Matschke's test map is uniformly
separated from its codimension-three target ray on collision facets and,
under the no-square assumption, from the endpoint \(a=b\).  Make one
arbitrarily small relative-transverse perturbation over the entire compact
domain.  The inverse image of the ray is a compact one-manifold.
Matschke's fiber intersection is odd at both endpoint scales.  Components
with both endpoints on the same fiber contribute an even number there, so
an odd number of interval components join the two endpoint fibers.

Let the perturbation tend to zero.  Hausdorff compactness of continua gives
a connected limit of exact special trapezoids meeting both fibers.  On the
compact positive-scale interval the short side \(b\) is uniformly positive,
and the normal/crossed coordinate classification is locally constant.
Hence the spanning continuum has a fixed type.  Letting
\(\delta\downarrow0\) yields a continuum meeting the total-collision
stratum and every positive scale up to \(\varepsilon_0\).

This appears implicit in Matschke's generic path picture, so no priority
claim is made.  It is stronger than choosing unrelated trapezoids at each
scale, but the continuum need not be a path or graph.

## Why the ordinary compactification cannot finish the proof

The Fulton--MacPherson/cyclohedral proof for \(C^1\) curves extends a
rescaled test map to collision strata using the limiting tangent vector.
An arbitrary Jordan arc has no curve-independent normalized collision
screen.  By inserting disjoint near-square \(U\)-motifs at scales tending
to zero, one obtains an embedded continuous arc whose normalized
four-point blow-ups contain an exact square screen.

Therefore the ordinary compactification cannot have a universal
nowhere-zero boundary test map for all Jordan curves.  Any successful
topological compactification must retain additional planar-side or collar
data, or must be coupled to an action/persistence filtration that decides
which collision screens survive.

Nor can prime-end ordering eliminate any one of the three non-square
screens.  In disjoint disks accumulating at one endpoint of an embedded
arc, insert successively similarity copies with
\[
 a/b=1+1/n\ \text{(crossed)},\qquad a/b=2,\qquad a/b=n.
\]
An ambient isotopy routes a simple subarc through each ordered quadruple.
Serially joining the disk pieces and closing outside produces one Jordan
curve with pair-coalescent, finite-trapezoid, and equilateral screens at
the same one-sided prime end.  The example may have squares elsewhere; it
proves that no *local* Jordan-separation rule forbids these screens.

## Verdict

Configuration topology gives a fixed-type spanning continuum, not a proof
of Square Peg.  The remaining possible use of (1) is global: extract an
invariant from that continuum which cannot be reproduced by isolated
nested motifs, then connect it to the conformal action-concentration or
diagonal-persistence class.

There is now one such exact invariant for a genuine path.  If
\(a,b\) are the two outer vertices of a moving square and
\(c=a+J(b-a),d=b+J(b-a)\) the inner vertices, the two closed ribbons have
signed-area difference
\[
 \mathcal A_{\rm in}-\mathcal A_{\rm out}
 =\frac{|b(s)-a(s)|^2-|b(t)-a(t)|^2}{2}.
\]
Hence a compactified finite-\(p<2\) envelope with simple nested ribbons is
impossible.  The calculation and its exact hypotheses are in
`square-envelope-area.md`.

The continuation theorem does not yet supply those hypotheses.  Its
carrier can be a topologist's sine continuum, and even a spanning path can
have infinite variation and multiply-wound ribbons.  Homologically it
records only the vertical generator of
\(H_1(S^1\times I,S^1\times\partial I;\mathbb F_2)\); two such generators
need not intersect.

## Primary sources

- B. Matschke, *On the Square Peg Problem and Its Relatives*,
  arXiv:1001.0186v2, Definition 2.7, Theorem 2.8, and its corollaries.
- S. Vrećica and R. Živaljević, *Fulton--MacPherson compactification,
  cyclohedra, and the polygonal peg problem*, arXiv:0810.1439,
  Proposition 6.
