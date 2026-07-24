# Global linking of a square envelope

## Status

This angle does not prove the Square Peg conjecture.  It identifies the exact
two-ended integer carried by Hugelmeyer's envelope and shows why ordinary
braid, linking, Maslov, and ruled-ribbon intersection arguments do not force
it to vanish.

The useful reduction is an **end-order rigidity problem**.  The total outer
winding says that the two exterior strands reverse their order between the
two collapsed ends.  A contradiction would follow from a theorem saying that
the two parallel outside-to-inside square edges cannot induce such an end
reversal on the prime-end circle.  Neither Jordan separation nor local
smallness proves that theorem; polygonal notches realize both local end
orders, and in the wild case the boundary-intersection carriers need not be
paths.

## Envelope coordinates and the full relation

Let \(J\) be counterclockwise rotation by \(\pi/2\), and write an envelope as
\[
 a(t)=e_1(t),\qquad b(t)=e_2(t),\qquad w(t)=b(t)-a(t).
\]
The other two vertices are
\[
 c(t)=a(t)+Jw(t),\qquad d(t)=b(t)+Jw(t).                 \tag{1}
\]
Here \(a,b\) lie in the unbounded component \(E\) of
\(\mathbb R^2\setminus\Gamma\), \(c,d\) lie in the Jordan domain \(\Omega\),
and
\[
 w(t)\ne0,\qquad |w(t)|\longrightarrow0
 \quad(t\to\pm\infty).                                  \tag{2}
\]
The non-vanishing follows because \(w=0\) would make the same point both
exterior and interior.

For every two times \(s,t\), no member of \(\{a(s),b(s)\}\) equals a member
of \(\{c(t),d(t)\}\).  This is Hugelmeyer's cross-time relation avoidance,
but after the envelope has been separated by \(\Gamma\), it is exactly the
global set separation
\[
 \{a(t),b(t):t\in\mathbb R\}\subset E,\qquad
 \{c(t),d(t):t\in\mathbb R\}\subset\Omega.               \tag{3}
\]
Thus any extra invariant must use the square formula (1), not merely the
absence of cross-time collisions.

## The exact outer end defect

Fix \(p\in\Omega\).  Choose continuous argument lifts
\[
 A(t)=\arg(a(t)-p),\qquad B(t)=\arg(b(t)-p).
\]
This is possible because the parameter line is simply connected and both
paths avoid \(p\).  Since every exterior point has distance at least
\(\operatorname{dist}(p,\Gamma)>0\) from \(p\), (2) implies
\[
 \frac{b(t)-p}{a(t)-p}\longrightarrow1
 \quad(t\to\pm\infty).
\]
Consequently there are integers \(n_-,n_+\) such that
\[
 \frac{B(t)-A(t)}{2\pi}\longrightarrow n_\pm
 \quad(t\to\pm\infty).                                  \tag{4}
\]
The integer is constant on each sufficiently far tail: a continuous real
function which is eventually arbitrarily close to \(\mathbb Z\) cannot
move between two integers.

For a large truncation, follow \(a\) forward, close to \(b\), follow \(b\)
backward, and close to \(a\), as in Hugelmeyer's Definition 1.  The argument
changes along the two connectors tend to zero.  Hence its winding about
\(p\) tends to
\[
 \frac{A(+\infty)-A(-\infty)
       -B(+\infty)+B(-\infty)}{2\pi}
 =n_- -n_+.
\]
The winding is identically one for all sufficiently large truncations, so
\[
 \boxed{n_- -n_+=1.}                                    \tag{5}
\]
This is the canonical global integer.  It uses neither finite variation nor
endpoint convergence in the plane.

Equation (5) is not a contradiction.  It says that the ratio
\((b-p)/(a-p)\), although tending to \(1\) at both ends, approaches two
different lifts of \(1\).  In other words, one unit of braid escapes through
the collapsed ends.

## The two ruled ribbons in space-time

The two parallel square edges give maps
\[
\begin{aligned}
 R_1(t,s)&=(a(t)+sJw(t),t),\\
 R_2(t,s)&=(b(t)+sJw(t),t),
 \qquad (t,s)\in\mathbb R\times[0,1].
\end{aligned}                                           \tag{6}
\]
They are disjoint embedded strips in \(\mathbb R^2\times\mathbb R\).
Indeed, the time coordinate distinguishes different \(t\)'s; for fixed
\(t\), each edge is embedded and
\[
 R_2(t,s)-R_1(t,s)=w(t)\ne0.                             \tag{7}
\]
Their boundary strands are \(a,c\) and \(b,d\), respectively.

Let
\[
 \Sigma=\Gamma\times\mathbb R.
\]
Every vertical fiber of each strip joins \(E\) to \(\Omega\), so it meets
\(\Sigma\).  In a transverse polygonal or smooth model,
\[
 Z_j=R_j^{-1}(\Sigma)
\]
is a relative one-cycle in the parameter strip with odd intersection number
over each time fiber.  Its image is a boundary-crossing carrier on the
cylinder \(\Sigma\simeq S^1\times\mathbb R\).

If each square edge meets \(\Gamma\) exactly once and the intersection
depends continuously on \(t\), write the two intersections as
\[
 q_j(t)=\gamma(\theta_j(t)).
\]
They are distinct because the space-time strips are disjoint.  Moreover,
\[
 |q_2(t)-q_1(t)|
 \le \sqrt2\,|w(t)|\longrightarrow0.                    \tag{8}
\]
Uniform continuity of the inverse Jordan parametrization implies that the
circle distance between \(\theta_1(t)\) and \(\theta_2(t)\) tends to zero.
For continuous lifts, the separation
\[
 \delta(t)=\widetilde\theta_2(t)-\widetilde\theta_1(t)
 \pmod 1,\qquad 0<\delta(t)<1,
\]
therefore tends at each end to either face \(0\) or face \(1\) of the
compactified ordered configuration cylinder
\[
 \operatorname{Conf}_2(S^1)\simeq S^1\times(0,1).        \tag{9}
\]

The exterior portions of the two edge strips homotope \(a,b\) to
\(q_1,q_2\).  With consistent orientations, (5) says exactly that the two
ends land on opposite faces of (9).  Thus total outer winding one is an
**end-order reversal** of the two boundary-crossing carriers.

## Why the end-order reversal is topologically allowed

Two disjoint proper arcs on a cylinder can realize this defect without
intersecting.  In coordinates \(S^1\times\mathbb R\), take
\[
 C_1(t)=(0,t),\qquad
 C_2(t)=\left(\frac{1}{1+e^t},t\right).                 \tag{10}
\]
They are disjoint for every finite \(t\), while their ordered separation
tends to \(1\) at \(-\infty\) and to \(0\) at \(+\infty\).  After the two
coalescing ends are added, their union carries the essential relative
generator rather than forcing an interior crossing.

Therefore:

- an intersection pairing of the two strips in space-time is zero, because
  the strips are already disjoint by (7);
- a linking number is not canonical, because the four boundary strands are
  non-compact and changing an end closure changes the integer by precisely
  the braid in (10);
- relative homology on \(\Sigma\) permits two disjoint representatives with
  end defect one; and
- adding one point at each parameter end does not repair the problem unless
  the vertex paths have actual endpoint limits and a prescribed approach
  direction.

This is the same escape mechanism as total collision in configuration-space
degree arguments: the odd class exits through a boundary stratum rather
than meeting another finite configuration.

## Maslov and rotation indices are not defined at the ends

The relative normal framing of the two strips is \(w(t)\).  On a compact
truncation its rotation is the change of \(\arg w\), but (2) supplies no
limit for \(w/|w|\).  Even a smooth relation-avoiding shrinking square path
can have no limiting direction.  For example, on a half-tail take
\[
 z(t)=e^{-t+i\varepsilon\sin(t^2)},\qquad
 (a,b,c,d)=(z,2z,(1+i)z,(2+i)z),                        \tag{11}
\]
with \(0<\varepsilon<0.1\).  An outer--inner equality at two times would
require an angular change at least
\(\arctan(1/2)>0.4\), whereas every difference of the oscillatory angles in
(11) has absolute value below \(0.2\).  Thus the full cross-time avoidance
holds, but \(w/|w|\) oscillates without an end limit.

Any Maslov integer therefore requires an additional endpoint
trivialization.  Different trivializations change it arbitrarily, so it
cannot obstruct an envelope under the stated hypotheses.

## Cross-time difference maps and the cross-ratio

Cross-time avoidance defines four maps
\[
 F_{OI}(s,t)=O(s)-I(t)\in\mathbb C^*,
 \quad O\in\{a,b\},\ I\in\{c,d\}.                       \tag{12}
\]
Because \(\mathbb R^2\) is simply connected, every \(F_{OI}\) has a
continuous logarithm.  On the diagonal, (1) merely says that these
logarithms restrict to fixed nonzero multiples of \(w(t)\); it imposes no
closed-loop degree.

A symmetric version is the cross-ratio
\[
 K(s,t)=
 \frac{(a(s)-c(t))(b(s)-d(t))}
      {(a(s)-d(t))(b(s)-c(t))}
 \in\mathbb C\setminus\{0,1\}.                          \tag{13}
\]
The value \(1\) is excluded by
\[
 (a-c)(b-d)-(a-d)(b-c)=(a-b)(c-d)\ne0.
\]
At equal times, the square identities give the striking normalization
\[
 K(t,t)=\frac12.                                        \tag{14}
\]
Nevertheless (13) extends over the entire parameter plane, so every finite
boundary loop is null-homotopic.  A nontrivial limiting loop can only arise
if \(K\) approaches one of \(0,1,\infty\) at parameter infinity, and the
envelope hypotheses give no uniform cross-time separation preventing this.

The constant-shape model in (11) makes the failure explicit.  If
\(r=z(s)/z(t)\), then
\[
 K(s,t)=
 \frac{(r-(1+i))(2r-(2+i))}
      {(r-(2+i))(2r-(1+i))}.                            \tag{15}
\]
As both times tend to the collapsed end with \(t-s\) unrestricted, \(r\)
has no unique limit and neither does \(K\).  Thus the normalized diagonal
(14) does not compactify the two-parameter map.

## Local square geometry does not choose an end face

The strongest natural repair would choose, on each parallel edge, a
continuous first crossing with \(\Gamma\) and prove that both tails approach
the same face of (9).  This is not a local consequence of being a Jordan
curve.

Let \(\Omega\) be the polygonal \(\Pi\)-domain obtained from
\([-2,2]\times[0,3]\) by removing the bottom notch
\([-\tfrac15,\tfrac15]\times[0,2]\).  Put
\[
 w=(1/2,0),\quad Jw=(0,1/2),\quad
 a=(-1/4,-1/4),\quad b=(1/4,-1/4).
\]
Then \(a,b\) are exterior and \(a+Jw,b+Jw\) lie in the two legs of
\(\Omega\).  The two parallel edges cross two different bottom boundary
arcs.  Equivalently, the fixed-translation crossing set
\[
 E\cap(\Omega-Jw)
\]
has three components, and \(a,b\) lie in different ones.  Reflection of the
motif realizes the opposite local order.  Scaling and inserting such
notches makes either order occur at arbitrarily small side length.

For a wild Jordan curve an edge may meet the boundary infinitely many
times.  The sets \(Z_j\) in (6) are then closed separators or continua, not
necessarily graphs of continuous selections.  A topologist's sine carrier
shows that projection onto every time fiber does not itself produce a
proper crossing path.  Hence the unique-crossing reduction cannot be
silently imposed.

## Exact sufficient theorem

The global envelope route would close if one proved the following.

> **End-order rigidity lemma.**
> For the two parallel edge ribbons of every square envelope, the
> boundary-intersection carriers admit compatible proper prime-end
> representatives whose ordered separation approaches the same face of
> \(S^1\times[0,1]\) at \(t=-\infty\) and \(t=+\infty\).

Indeed, compatible representatives transfer the exterior pair to the
prime-end cylinder without changing its relative angular defect.  Equal end
faces give \(n_-=n_+\), contradicting (5).

A carrier-level formulation, avoiding path selection, would be stronger and
preferable: the two relative intersection classes of \(R_1,R_2\) with
\(\Gamma\times\mathbb R\) should have zero end-order defect.  The cylinder
model (10) shows that such vanishing is not formal intersection theory.  It
must come from the fact that the two strips are parallel sides of Euclidean
squares and from the same fixed Jordan separator at every time.

The polygonal notch shows that the lemma cannot be proved one tail at a
time.  Any valid proof must couple the two ends through the entire
four-dimensional admissible-square space
\[
 \{(a,w):a,a+w\in E,\ a+Jw,a+w+Jw\in\Omega\}.           \tag{16}
\]
Conversely, a path in (16) with end defect one would be an exact
counterexample to the lemma.  Constructing or excluding that path is the
remaining finite-dimensional global problem.

## Verdict

The wide-net linking attack finds no contradiction from existing envelope
data:

1. total outer winding is exactly the integer end defect (5);
2. in space-time it is an allowed order reversal of two disjoint
   boundary-crossing carriers;
3. Maslov and linking numbers lack canonical endpoint closures;
4. the normalized cross-ratio has no controlled extension at parameter
   infinity; and
5. local Jordan topology permits both end orders and may not supply crossing
   paths at all.

The sharp target is therefore end-order rigidity in the admissible-square
space (16), not another unsigned winding or area identity.
