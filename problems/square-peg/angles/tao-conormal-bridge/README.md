# Tao-conormal bridge to unrestricted Square Peg

**Session:** 2026-07-24
**Status:** exact bridge criterion plus no-go theorems for the natural
four-copy, graph, affine-perturbation, cyclic-cover, and unfiltered-rank
constructions. No unrestricted proof.

## 1. Input theorem and objective

Use the corrected form of the conormal theorem audited in
`../../literature/TAO56_CLAIM_AUDIT.md`:

> If four embedded essential polygonal circles
> \(\sigma_i\subset\operatorname{Cyl}_L\) satisfy
> \[
> \int_{\sigma_1}y\,dx-\int_{\sigma_2}y\,dx+
> \int_{\sigma_3}y\,dx-\int_{\sigma_4}y\,dx=0,
> \tag{1.1}
> \]
> then they jointly inscribe a square in Tao's closed square locus.

The square may be degenerate. The goal of a bridge would be to construct the
four cylinder circles from an arbitrary planar Jordan curve \(C\) so that a
joint cylinder square decodes to a **nondegenerate** square on \(C\).

This note tests the most direct constructions:

1. encode a Jordan parametrization as one or more graphs over the cylinder;
2. take four small vertical/horizontal/normal perturbations;
3. essentialize a planar copy by winding through a seam;
4. pass to a finite cyclic cover to hide the seam; or
5. use the rank-two conormal Floer group to demand a second, nonlocal
   intersection.

All five fail for exact reasons below.

## 2. An exact sufficient bridge criterion

Let \(\mathcal S\subset(\mathbb R^2)^4\) be the closed linear subspace of
ordered, possibly degenerate squares:
\[
(z_1,z_2,z_3,z_4)\in\mathcal S
\quad\Longleftrightarrow\quad
z_3=z_2+z_4-z_1,\qquad z_4-z_1=R_{\pi/2}(z_2-z_1).
\tag{2.1}
\]
Its degenerate stratum is
\[
\mathcal D=\{(p,p,p,p):p\in\mathbb R^2\}.
\tag{2.2}
\]

The following formulation isolates exactly what a successful use of (1.1)
must add.

### Proposition 2.1 (uniform decoding bridge)

Let \(C\subset\mathbb R^2\) be a Jordan curve. Suppose that for a sequence
\(n\to\infty\) there are four embedded essential polygonal circles
\(\sigma_{i,n}\subset\operatorname{Cyl}_{L_n}\) and continuous decoding maps
\[
\pi_{i,n}:\sigma_{i,n}\longrightarrow C
\]
such that:

1. the alternating action (1.1) is zero for every \(n\);
2. if \(\mathcal Q_n\) is the set of jointly inscribed cylinder squares, then
   \[
   \sup_{(z_1,\ldots,z_4)\in\mathcal Q_n}
   \operatorname{dist}\!\left(
   (\pi_{1,n}z_1,\ldots,\pi_{4,n}z_4),\mathcal S\right)
   \longrightarrow0;
   \tag{2.3}
   \]
3. there is an \(\eta>0\) such that every decoded joint square satisfies
   \[
   \operatorname{diam}\{\pi_{1,n}z_1,\ldots,\pi_{4,n}z_4\}\geq\eta.
   \tag{2.4}
   \]

Then \(C\) inscribes a nondegenerate square.

#### Proof

The corrected Tao theorem makes \(\mathcal Q_n\) nonempty. Choose one element
of each \(\mathcal Q_n\). Compactness of \(C^4\) gives a convergent subsequence
of its decoded quadruples. Equation (2.3) and closedness of \(\mathcal S\)
put the limit in \(\mathcal S\). Equation (2.4) puts it outside
\(\mathcal D\). Thus it is a nondegenerate square on \(C\). \(\square\)

No smoothing of \(C\) is hidden here. The proposition is a compactness
reduction, and (2.4) is exactly the missing total-collision exclusion.

The rest of the note shows that the natural four-copy constructions fail
(2.4), while unfiltered conormal Floer homology cannot supply a replacement.

## 3. Balanced parallel graphs create exact screen squares

The first obstruction is already present on four horizontal core circles.

### Proposition 3.1 (balanced-level countermodel)

Fix \(0<\varepsilon<1/16\) and work in
\(\operatorname{Cyl}_1=(\mathbb R/\mathbb Z)\times\mathbb R\). Let
\[
h_1=0,\qquad h_2=\varepsilon,\qquad
h_3=3\varepsilon,\qquad h_4=2\varepsilon
\tag{3.1}
\]
and
\[
\sigma_i=\{(q,h_i):q\in\mathbb R/\mathbb Z\}.
\]
Then:

1. the four circles are pairwise disjoint, embedded, essential, and satisfy
   zero alternating action;
2. for every \(x\in\mathbb R/\mathbb Z\), the four points
   \[
   \begin{aligned}
   z_1&=(x,0),&
   z_2&=(x+2\varepsilon,\varepsilon),\\
   z_3&=(x+\varepsilon,3\varepsilon),&
   z_4&=(x-\varepsilon,2\varepsilon)
   \end{aligned}
   \tag{3.2}
   \]
   form a nondegenerate ordered square; and
3. under the natural parameter decoding
   \[
   \pi_i(q,h_i)=
   c(q):=(\cos 2\pi q,\sin 2\pi q)
   \tag{3.3}
   \]
   to the unit circle, the four decoded points do not form a
   nondegenerate square and converge totally to \(c(x)\) as
   \(\varepsilon\to0\).

#### Proof

The action of \(\sigma_i\) is \(h_i\), so
\[
h_1-h_2+h_3-h_4=0-\varepsilon+3\varepsilon-2\varepsilon=0.
\]
In Tao's square coordinates, (3.2) has
\[
a=2\varepsilon,\qquad b=\varepsilon,
\]
and hence side vectors \((2\varepsilon,\varepsilon)\) and
\((-\varepsilon,2\varepsilon)\). It is nondegenerate.

All four parameters in (3.2) lie in an arc of parameter length
\(3\varepsilon<1/4\). A nondegenerate square inscribed in the unit circle has
the unit circle as its circumcircle, so its four parameters differ by
successive quarter-turns. It cannot lie in an arc of length less than
\(1/4\). Finally, all four parameters tend to \(x\). \(\square\)

This is not a numerical example. It is an exact one-parameter continuum of
spurious joint squares. The same construction works on
\(\operatorname{Cyl}_L\): constant height \(h_i\) has action \(Lh_i\), and
the square (3.2) is unchanged whenever its horizontal scale is smaller than
the injectivity radius.

### Corollary 3.2 (finite cyclic covers do not help)

Passing to any finite cyclic cover of the cylinder does not remove the
countermodel. Choose \(\varepsilon\) smaller than one sixteenth of the new
period. The square (3.2) lies in one evenly covered interval, and the
alternating action remains
\(L(h_1-h_2+h_3-h_4)=0\).

Thus a finite cover can move a seam but cannot change the local collision
screen.

## 4. The same screen occurs on a straight collar

Proposition 3.1 is local. It does not depend on the four curves being
horizontal everywhere.

### Proposition 4.1 (local flat-collar no-go)

Suppose four essential cylinder circles contain the segments
\[
J_i=\{(q,h_i):q\in I\},
\]
with the balanced heights (3.1). If \(I\) contains
\([x-\varepsilon,x+2\varepsilon]\), then the four circles jointly inscribe
the square (3.2) entirely inside the \(J_i\).

Consequently, any four-copy essentialization which:

1. preserves a straight subarc of a Jordan curve;
2. separates its copies by the balanced normal offsets (3.1); and
3. decodes by normal projection back to that subarc,

has a joint square whose four decoded vertices are collinear. As the offsets
shrink, that square totally collides.

#### Proof

All four points in (3.2) lie in the stated segments, and the calculation in
Proposition 3.1 is local. Normal projection sends them to one straight line,
which cannot contain a nondegenerate square. \(\square\)

This gives a countermodel even for polygonal Jordan curves, so no appeal to
Jordan smoothing can repair the construction. Rounding the four cylinder
curves would instead destroy the exact flat calculation and would require a
new proof that the screen disappears; no such conclusion follows from
embeddedness or \(C^0\) closeness.

## 5. Why fixed translated copies cannot preserve squares and remove the diagonal

The preceding countermodel reflects a linear obstruction.

### Proposition 5.1 (translation dichotomy)

Let \(\delta=(\delta_1,\ldots,\delta_4)\in(\mathbb R^2)^4\). Suppose fixed
translations \(z_i\mapsto z_i+\delta_i\) have the universal implication
\[
(z_1+\delta_1,\ldots,z_4+\delta_4)\in\mathcal S
\quad\Longrightarrow\quad
(z_1,\ldots,z_4)\in\mathcal S
\tag{5.1}
\]
for every \(z\in(\mathbb R^2)^4\). Then \(\delta\in\mathcal S\).
Consequently, for every \(p\in\mathbb R^2\),
\[
(p+\delta_1,\ldots,p+\delta_4)\in\mathcal S.
\tag{5.2}
\]
Thus fixed translated copies which preserve the square equation always
carry every common source point to a tautological joint square.

#### Proof

The preimage of \(\mathcal S\) under translation by \(\delta\) is the affine
four-plane \(\mathcal S-\delta\). Condition (5.1) says
\(\mathcal S-\delta\subseteq\mathcal S\). The two affine spaces have the same
dimension, hence they are equal, which is equivalent to
\(\delta\in\mathcal S\). Since the diagonal \(\mathcal D\) is contained in
\(\mathcal S\), (5.2) follows. \(\square\)

If \(\delta\) is a nondegenerate square, (5.2) is a nondegenerate square on
the four translated copies but decodes to the degenerate source quadruple
\((p,p,p,p)\). If \(\delta\) is degenerate, the copies retain exact common
points. Either way, fixed translations cannot both intertwine the square
relation and remove its diagonal.

### Proposition 5.2 (affine version)

Let
\[
T(z_1,\ldots,z_4)=(T_1z_1,\ldots,T_4z_4)
\]
be an invertible product affine map. If
\[
T^{-1}(\mathcal S)\subseteq\mathcal S,
\tag{5.3}
\]
then \(T^{-1}(\mathcal S)=\mathcal S\), and therefore
\[
T(\mathcal D)\subseteq\mathcal S.
\tag{5.4}
\]
Hence any fixed per-copy affine construction which universally decodes
joint squares to source squares also produces a tautological joint square
from every common source point.

#### Proof

\(T^{-1}(\mathcal S)\) is an affine four-plane contained in the linear
four-plane \(\mathcal S\), so equality holds. Apply \(T\) to
\(\mathcal D\subset\mathcal S\). \(\square\)

This rules out fixed combinations of translations, rotations, similarities,
and nonsingular affine changes as an exact four-copy bridge. A nonlinear or
parameter-dependent perturbation must break the exact intertwining and then
prove the uniform approximation and collision bounds (2.3)--(2.4) by other
means.

## 6. Essentiality itself forces a seam or parameter distortion

There is also a basic topological obstruction to inserting the planar curve
unchanged.

### Lemma 6.1 (lifted planar copies are inessential)

Let \(C\cong S^1\) and let
\[
F:C\longrightarrow\operatorname{Cyl}_L
\]
admit a continuous lift \(\widetilde F:C\to\mathbb R^2\). Then the projection
of \(F\) to \(\mathbb R/L\mathbb Z\) has degree zero. In particular, the
quotient of any single-valued affine or Euclidean image of a bounded planar
Jordan curve is not an essential cylinder curve.

#### Proof

The first coordinate of \(\widetilde F\) is a real-valued lift of the circle
map \(\operatorname{pr}_1F\). A circle map admitting a real-valued lift has
degree zero. \(\square\)

Thus an essentialization must do at least one of the following:

- cut the planar copy and insert a winding connector;
- use the curve parameter itself as the cylinder coordinate; or
- identify through a seam after a non-Euclidean distortion.

The first option creates a region in which a forced square may live and
collapse; a finite cyclic cover only moves that region. The second and third
do not preserve Euclidean squares. Proposition 3.1 shows that even the
cleanest parameter graph can satisfy the exact action identity while its
joint squares decode to total collisions.

This is not a theorem that every conceivable essentialization fails. It is
the precise reason a successful construction needs additional global data
beyond four nearby copies.

## 7. The conormal Floer rank is completely local to the diagonal

The corrected proof uses
\[
HF_*(\phi(O_Q),N^*\Delta_v;\mathbb F_2)
\cong H_*(\Delta_v;\mathbb F_2),
\qquad \Delta_v\cong S^1.
\tag{7.1}
\]
It is tempting to argue that rank two should give one intersection near the
degenerate diagonal and another away from it. The following exact model
refutes that inference.

### Proposition 7.1 (two local generators exhaust Floer homology)

Let \(Q=(\mathbb R/L\mathbb Z)^4\), let
\[
\Delta_v=\{te-Kv:t\in\mathbb R/L\mathbb Z\}\subset Q,
\]
and let \(U\) be any neighborhood of the zero conormal
\[
O_{\Delta_v}=\{(q,0):q\in\Delta_v\}\subset T^*Q.
\]
There is a compactly supported Hamiltonian image \(L_U\) of the zero section
such that:

1. \(L_U\) intersects \(N^*\Delta_v\) transversely in exactly two points;
2. both intersection points lie in \(O_{\Delta_v}\subset U\); and
3. these two points generate the full rank-two group (7.1).

#### Proof

Write \(c=(Kv)_1\) and define
\[
f(q)=\cos\!\left(\frac{2\pi(q_1+c)}L\right).
\tag{7.2}
\]
On \(\Delta_v\), where \(q_1=t-c\), its restriction is
\[
f|_{\Delta_v}(t)=\cos(2\pi t/L),
\]
a perfect Morse function with exactly two critical points.

For sufficiently small \(\eta>0\), let \(L_U=\operatorname{graph}(\eta\,df)\).
The graph is a Hamiltonian image of the zero section. Although the
fiber-independent Hamiltonian is not compactly supported on all of \(T^*Q\),
one may multiply it by a fiber cutoff which is identically one on a
neighborhood of the compact trace; this preserves the image of the zero
section and makes the Hamiltonian compactly supported.

A point \((q,\eta df_q)\) lies in \(N^*\Delta_v\) precisely when
\[
q\in\Delta_v,\qquad df_q|_{T_q\Delta_v}=0.
\]
These are exactly the two critical points of \(f|_{\Delta_v}\). At both,
\(df_q=0\), so both intersections lie in \(O_{\Delta_v}\). Morse
nondegeneracy of \(f|_{\Delta_v}\) is exactly transversality of the two
Lagrangians there. Thus the entire intersection set, though not the whole
graph over \(Q\), lies in the prescribed neighborhood \(U\). Taking
\(\eta\to0\) also makes the Hamiltonian image arbitrarily close to the zero
section.

The conormal PSS isomorphism identifies the resulting complex with the Morse
complex of the perfect Morse function \(f|_{\Delta_v}\), whose two
generators realize \(H_*(S^1;\mathbb F_2)\). \(\square\)

### Consequences

1. Full Floer rank gives no intersection outside a neighborhood of the
   degenerate affine diagonal.
2. A relative or localization argument cannot be obtained merely by
   subtracting the rank of the obvious degenerate class: the local clean
   intersection already carries all of \(H_*(\Delta_v)\).
3. The two local action values in the model differ by \(O(\eta)\). Hence the
   unfiltered theorem, or a filtered theorem with no uniform spectral gap,
   cannot prevent both classes from collapsing to the diagonal.
4. When \(v\to0\), the affine diagonal \(\Delta_v\) itself converges to the
   degenerate diagonal. In the original square coordinates, the local
   generators are precisely the kind of vanishing-scale screens exhibited
   in Proposition 3.1.

The last statement has an exact formula. At either local intersection in
Proposition 7.1 the translated momentum is \(p'=0\). Undoing the four
vertical normalizations gives original momentum \(p=-v\). The converse
calculation in the square-conormal dictionary therefore gives
\[
a=-p_4-p_1=v_4+v_1,\qquad
b=-p_2-p_1=v_2+v_1,
\tag{7.3}
\]
and hence square sidelength
\[
\sqrt{(v_1+v_4)^2+(v_1+v_2)^2}.
\tag{7.4}
\]
Thus this entire rank-two model collapses at a rate controlled linearly by
the normalization vector \(v\). For the balanced levels (3.1),
\[
v=(0,\varepsilon,-3\varepsilon,2\varepsilon),
\]
so (7.3) recovers exactly \(a=2\varepsilon\), \(b=\varepsilon\).

### Proposition 7.2 (ordinary action does not detect screen size)

For \(s>0\), take horizontal levels
\[
(h_1,h_2,h_3,h_4)=(0,s,3s,2s).
\tag{7.5}
\]
The exactness translations \(c_i=-h_i\) make all four cotangent factors the
zero section and give \(v=(0,s,-3s,2s)\). Hence
\[
O_Q\cap N^*\Delta_v=O_{\Delta_v}.
\tag{7.6}
\]
Both exact primitives vanish on this clean intersection, so it lies at one
action value, normalized to zero. But (7.3) gives
\((a,b)=(2s,s)\), hence sidelength \(\sqrt5\,s\).

Thus \(s\to0\) collapses the screen and \(s\to\infty\) gives arbitrarily
large screens at the same action. A small Morse perturbation splits the clean
circle into the two generators of Proposition 7.1 with arbitrarily small
action difference. Ordinary action filtration, without a new calibration to
the decoded planar geometry, cannot supply the noncollision bound.

Therefore a successful Floer upgrade must introduce genuinely nonlocal
information: for example, a class relative to the complement of a fixed
diagonal neighborhood, a spectral lower bound uniform under the proposed
essentialization and geometrically calibrated to the decoder, or an external
linking condition. None is present in the corrected Tao 5.6 argument.

## 8. What remains viable

The conormal theorem is a real new forcing module, but it cannot select where
its intersection occurs. The following routes are not ruled out by the
countermodels:

1. **Nonlocal relative class.** Construct four strands for which a class in a
   Floer theory relative to a fixed diagonal neighborhood is nonzero. Full
   \(HF\cong H_*(S^1)\) is insufficient by Proposition 7.1.
2. **Uniform spectral gap.** Attach an action normalization to the decoded
   planar geometry and prove that every diagonal-screen generator has action
   in a shrinking interval while a distinguished class stays a fixed
   positive distance away. The local model shows this gap cannot follow from
   rank alone.
3. **Global seam linking.** Essentialize through four coupled seams carrying
   a nonzero linking number which no local flat-collar square can realize.
   A finite cyclic cover without such a class does nothing.
4. **A decoder satisfying Proposition 2.1.** This is the direct route, but
   (2.4) must be proved geometrically; embeddedness, disjointness of the four
   copies, and exact action balance do not imply it.

Any claimed unrestricted bridge should be tested first against the exact
balanced-level family (3.1)--(3.3) and the local Floer model (7.2).

## 9. Independent adversarial second opinion

GPT-5.6 Sol at xhigh independently checked Propositions 3.1, 5.1--5.2, and
7.1--7.2. Its verdict was **KILL for the four-copy action/rank/cyclic-cover
bridge**: the balanced-level family exhausts the clean
\(HF\cong H_*(S^1)\), finite covers retain the local screen, and neither
unfiltered rank nor ordinary action filtration distinguishes collision scale.
It agreed that only a new uniform localization or noncollision invariant
leaves a positive route.

## 10. Verdict

**NO-GO for the proposed natural bridge family.**

- Four balanced vertical/normal copies have exact small joint squares that
  collapse under decoding.
- Fixed affine perturbations which preserve the square equation necessarily
  preserve its diagonal as a source of tautological squares.
- A planar Euclidean copy is inessential; winding, parameterization, or a
  seam is unavoidable.
- Finite cyclic covers do not alter the local screen.
- The entire rank-two conormal Floer group can be realized in an arbitrarily
  small neighborhood of the degenerate affine diagonal.

This does not prove that corrected Tao 5.6 is irrelevant to unrestricted
Square Peg. It proves that the missing ingredient must be a **nonlocal
relative or spectrally separated class**, not four-copy action balancing by
itself.
