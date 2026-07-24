# Square-envelope area conservation

## Exact ribbon identity

Let \(J\) be counterclockwise rotation by \(\pi/2\).  For paths
\(a,b:[s,t]\to\mathbb R^2\), put
\[
 v=b-a,\qquad c=a+Jv,\qquad d=b+Jv.
\]
Close \(a\) against \(b\) by straight end segments, orienting \(a\) forward
and \(b\) backward.  Close \(c\) against \(d\) in the same way.  Denote the
two closed ribbons by \(\Gamma_{\rm out}\) and \(\Gamma_{\rm in}\).

If the paths have finite \(p\)-variation for some \(p<2\), their Young signed
areas satisfy
\[
 \mathcal A(\Gamma_{\rm in})-\mathcal A(\Gamma_{\rm out})
 =\frac{|v(s)|^2-|v(t)|^2}{2}.                            \tag{1}
\]
Indeed, on the long sides,
\[
\begin{aligned}
 &c\times dc-d\times dd-(a\times da-b\times db)\\
 &\qquad=-(Jv)\times dv-v\times J\,dv
 =v\cdot dv-v\cdot dv=0.                                 \tag{2}
\end{aligned}
\]
Only the two straight connectors remain, giving (1).  The calculation is
also exact for every synchronized polygonal approximation; it is not a
formal integration-by-parts heuristic.

For a full square envelope with \(|v(x)|\to0\) at both ends, (1) gives
\[
 \mathcal A(\Gamma_{\rm in})=\mathcal A(\Gamma_{\rm out}) \tag{3}
\]
whenever the two improper areas exist.

## A rigorous conditional obstruction

Suppose a square envelope has finite \(p<2\) variation after compactification,
both ribbons are Jordan, the outer ribbon has index one on the Jordan domain
\(\Omega\), and the inner ribbon lies strictly inside \(\Omega\).  Then it
cannot exist.

The outer ribbon positively encloses \(\Omega\), and its Jordan trace
genuinely enters the exterior, so its bounded domain strictly contains
\(\Omega\).  The inner ribbon encloses a strict subset of \(\Omega\) (or is
negatively oriented).  Green's theorem for Young Jordan curves therefore
gives
\[
 \mathcal A(\Gamma_{\rm out})>|\Omega|>
 \mathcal A(\Gamma_{\rm in})
\]
in the positive case, contradicting (3).  Simplicity may be replaced by
the explicit winding bounds
\[
 n_{\rm out}\geq\mathbf1_\Omega
\]
and either \(n_{\rm in}\leq0\), or
\[
 0\leq n_{\rm in}\leq\mathbf1_\Omega,\qquad
 \int_\Omega(1-n_{\rm in})>0.                            \tag{4}
\]

The finite-variation hypothesis is not the conceptual boundary.  A
joint compatible geometric rough-path lift of \((a,b)\) gives the same
algebra at and above \(p=2\).  The obstruction there is the absence of a
canonical lift for arbitrary continuous paths.

## Why Hugelmeyer's theorem does not yet close the proof

Hugelmeyer's square envelope supplies continuous \(e_1,e_2:\mathbb R\to
\mathbb R^2\) with the outer vertices in the exterior, the inner vertices
in the interior, \(|e_2-e_1|\to0\) at both ends, and outer winding one on
\(\Omega\).  It does **not** assert that

- either ribbon is simple;
- the winding functions are one-sided;
- the paths have finite variation or a compatible rough lift; or
- the two ends converge to single boundary points.

Signed area can cancel between regions of opposite high winding.  Equality
(3) is therefore not inconsistent with the definition as presently stated.
As an abstract winding countermodel, around \(\Omega=[-1,1]^2\), take an
exterior loop which traverses
\(\partial[-2,2]^2\) counterclockwise and, along a retraced exterior bridge,
a disjoint \(5\times3\) rectangle clockwise.  It has index one on \(\Omega\)
but signed area \(16-15=1\), equal to the area of the inner loop
\(\partial[-1/2,1/2]^2\).  Conversely, a simple outer loop of area \(16\)
can match an inner unit square traversed sixteen times.  One-sided outer
winding alone or inner containment alone is insufficient.

Nor can one close the two long paths by a common exterior connector whose
quarter-turn translate stays inside.  Such a connector would have to lie in
\[
 X_v=\operatorname{Ext}(\gamma)\cap
 \bigl(\operatorname{Int}(\gamma)-v\bigr),\qquad v=J(b-a).                \tag{5}
\]
This set need not connect its two prescribed endpoints, even for a polygonal
domain.  Take the rectangle \([-2,2]\times[0,3]\) and remove the bottom notch
\([-1/5,1/5]\times[0,2]\).  With
\[
 b-a=(1/2,0),\quad v=(0,1/2),\quad
 a=(-1/4,-1/4),\quad b=(1/4,-1/4),
\]
both \(a,b\) are exterior and \(a+v,b+v\) lie in the two legs of the domain,
but \(a\) and \(b\) lie in different components of \(X_v\).  Scaled notches
give the same obstruction at arbitrarily small side length.  Schoenflies
and uniform local connectivity do not supply the paired closure.

The all-scales Matschke carrier is weaker still: it is only a connected
continuum.  A topologist's sine continuum shows that a connected carrier
which projects onto every scale need not contain a path spanning the scales.
Homologically the carrier records only the generator of
\[
 H_1(S^1\times I,S^1\times\partial I;\mathbb F_2)
 \simeq\mathbb F_2.
\]
Two such relative generators can be disjoint parallel vertical arcs, so
there is no self-intersection obstruction.

## Exact remaining topological lemma

A finite-dimensional route to Square Peg would be completed by either of:

1. every bad curve has a square envelope admitting a simple
   zero-anomaly compactification; or
2. its envelope has a joint geometric rough lift and the explicit winding
   bounds in (4).

The area identity then gives the contradiction immediately.  Neither
property follows from the present parity/continuation arguments.
