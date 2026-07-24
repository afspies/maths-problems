# Conormal tail splicing: a rank-two reduction

## Verdict

**KILL action/rank/detour alone; HOLD one sharply conditional geometric
lemma.**

After the global action-sign repair recorded in
[the Tao 5.6 claim audit](../../literature/TAO56_CLAIM_AUDIT.md), the
conormal argument gives more than non-displacement.  For a transverse
zero-alternating-action quadruple of smooth essential cylinder curves, its
Floer complex has one generator for each ordered joint square and homology
of rank two.  Hence there are at least two ordered joint squares.

This makes the following unrestricted strategy logically exact:

1. splice four selected arcs of a planar Jordan curve \(C\) into four
   essential cylinder circles;
2. balance their alternating actions using only artificial tails;
3. arrange that there is exactly one transverse joint square involving a
   tail; and
4. arrange that every other joint square has all four vertices on the
   retained \(C\)-arcs.

The rank-two Floer group would then force a second square, and that square
would lie on \(C\).  The conditional reduction survives polygonal
approximation of an arbitrary Jordan curve and does not require a line
integral along \(C\).  It is not evidence that suitable tails exist.

The unresolved point is now sharply geometric:

> **Odd artificial splice lemma.**  Can the tails and their four connector
> corridors be chosen so that the artificial/mixed joint-square locus
> consists of exactly one uniformly transverse ordered square?

An independent Sol xhigh review killed the weaker hope that action balance,
rank two, and a local area detour might themselves localize a generator near
\(C\).  Parallel balanced tails carry a clean \(S^1\)-family whose
perturbation has at least two generators, while splices retaining a common
part of \(C\) carry Tao's degenerate diagonal.  The whole rank-two group can
remain on full-winding artificial collars.  There is an explicit
two-generator graph model in which one baseline generator can be put inside
a splice window, but this is only a target for an exclusion theorem:
replacing that window by four \(C\)-excursions may create new mixed
generators or move both surviving classes to artificial collars.

The July 2026 conormal manuscript is unrefereed and false under its printed
action convention.  Every statement below using it means the corrected
convention
\[
 {\cal A}(\sigma)=\int_\sigma y\,dx
\]
and is conditional on the corrected conormal proof passing expert review.

## 1. Cylinder square equations without lift ambiguity

Fix \(L>0\) and
\[
 \operatorname {Cyl}_L=(\mathbb R/L\mathbb Z)\times\mathbb R.
\]
An essential circle is oriented so that its projection to
\(\mathbb R/L\mathbb Z\) has degree one.  Four points
\(z_i=(q_i,y_i)\) form an ordered joint square precisely when there are
\(x\in\mathbb R/L\mathbb Z\) and \(a,b\in\mathbb R\) such that
\[
\begin{aligned}
 z_1&=(x,y),&
 z_2&=(x+a,y+b),\\
 z_3&=(x+a-b,y+a+b),&
 z_4&=(x-b,y+a).
\end{aligned}                                                    \tag{1}
\]
The base coordinates in (1) are read modulo \(L\), but \(a,b\) are real.
Equivalently,
\[
\begin{aligned}
 y_1-y_2+y_3-y_4&=0,\\
 q_2-q_1&\equiv y_4-y_1,\\
 q_3-q_2&\equiv y_1-y_2,\\
 q_4-q_3&\equiv y_1-y_4
 \pmod L .
\end{aligned}                                                    \tag{2}
\]
The fourth cyclic base congruence follows from these equations.

Put
\[
 Q=(\mathbb R/L\mathbb Z)^4,\qquad
 p=(y_1,-y_2,y_3,-y_4),\qquad e=(1,1,1,1),
\]
and
\[
 K=\begin{pmatrix}
 0&-1&0&1\\
 -1&-1&0&0\\
 0&0&0&0\\
 1&0&0&1
 \end{pmatrix},\qquad
 \Psi(q,p)=(q-Kp,p).                                      \tag{3}
\]
Then (1) is equivalent to
\[
 \Psi(q,p)\in N^*\Delta,\qquad
 \Delta=\{te:t\in\mathbb R/L\mathbb Z\}.                  \tag{4}
\]
Conversely, an intersection point in (4) recovers
\[
 x=q_1,\qquad y=p_1,\qquad
 b=-p_2-p_1,\qquad a=-p_4-p_1.                            \tag{5}
\]
Thus one ordered geometric square gives exactly one conormal intersection.
There is no extra generator indexed by a lift of \(q\): the real values of
\(a,b\) are already fixed by \(p\), and the base equations are congruences.
Cyclic relabellings count separately only when they are genuinely different
ordered quadruples on the four labelled curves.

## 2. The rank-two joint-square lemma

Let \(\sigma_1,\ldots,\sigma_4\) be smooth embedded essential circles and
assume
\[
 {\cal A}(\sigma_1)-{\cal A}(\sigma_2)
 +{\cal A}(\sigma_3)-{\cal A}(\sigma_4)=0.                \tag{6}
\]
After the four vertical normalizations in the corrected conormal proof, the
product of the four cotangent circles is a compactly supported Hamiltonian
image of the zero section \(O_Q\).  The translations change \(\Delta\) to an
affine diagonal \(\Delta_v\cong S^1\), and the shear (3) gives an exact
bijection between squares on the **original** curves and
\[
 \phi(O_Q)\cap N^*\Delta_v .                              \tag{7}
\]

Suppose (7) is transverse.  The conormal Floer complex over
\(\mathbb F_2\) is freely generated by its intersection points, and
\[
 HF_*(\phi(O_Q),N^*\Delta_v;\mathbb F_2)
 \cong H_*(\Delta_v;\mathbb F_2)
 \cong \mathbb F_2\oplus\mathbb F_2.                     \tag{8}
\]
Consequently
\[
 \#\{\text{ordered joint squares}\}
 =\dim CF_*\ \geq\ \dim HF_*=2.                          \tag{9}
\]

No assertion about the differential is needed: the rank of homology cannot
exceed the dimension of its chain group.  In particular, one transverse
geometric square cannot support both classes in (8).

Transversality is essential.  For a nontransverse limiting quadruple, two
perturbed generators may converge to the same geometric square.  The
non-displacement argument then proves only one unperturbed intersection.
Any splice proof using (9) must keep the artificial square uniformly
transverse and isolate it in a fixed neighborhood.

## 3. Essential splicing and the cylinder wrap

Choose \(L\) large enough to embed \(C\) in an open disk
\(D\subset\operatorname {Cyl}_L\) with a lift
\(\widetilde D\subset\mathbb R^2\) satisfying
\[
 \operatorname {diam}_x(\widetilde D)
 +\operatorname {diam}_y(\widetilde D)<L.               \tag{9a}
\]
This is the no-wrap margin needed to decode a cylinder square on retained
pieces as a Euclidean square. Let \(\alpha_i\subset C\) be a closed Jordan
arc with endpoints \(u_i,v_i\). In the universal cover, choose a tail
\(\widetilde\tau_i\) from a lift of \(v_i\) to the translate
\(\widetilde u_i+(L,0)\). If
\[
 \widetilde\alpha_i\cup\widetilde\tau_i
\]
is an embedded arc and its interior is disjoint from all nonzero
\((L,0)\)-translates of itself, its projection
\[
 \sigma_i=\alpha_i\cup\tau_i                              \tag{10}
\]
is an embedded essential circle of degree one.  This translation-separation
condition, not merely planar simplicity in one fundamental rectangle, is
the correct embedding test.

The tails can be routed outside \(D\), so (10) is topologically available
for every selected arc.  But an essential simple circle cannot contain all
of \(C\).  Indeed, a subset of a topological circle which is itself a
topological circle must be the entire circle.  If \(C\subset\sigma_i\), then
\(C=\sigma_i\), contradicting that \(C\subset D\) is null-homotopic while
\(\sigma_i\) is essential.  Every essential splice must delete a nonempty
part of \(C\).

There is a second immediate obstruction.  Tao's square locus includes
\(a=b=0\).  Hence every point in
\[
 \sigma_1\cap\sigma_2\cap\sigma_3\cap\sigma_4             \tag{11}
\]
is a degenerate joint square.  If all four splices retain the same large
arc of \(C\), (11) contains a continuum.  A perturbation can realize both
classes in (8) near this diagonal, giving no nondegenerate square on \(C\).
A viable choice of retained arcs must at least satisfy
\[
 \alpha_1\cap\alpha_2\cap\alpha_3\cap\alpha_4=\varnothing.
                                                                    \tag{12}
\]
Equivalently, the four deleted \(C\)-arcs must cover \(C\).

Pairwise overlap is not itself fatal.  Condition (12) is the exact
requirement preventing four vertices of a limiting genuine square from
collapsing to one point.

It also gives a uniform quantitative gap.  Compactness and (12) imply
\[
 \inf_{z_i\in\alpha_i}
 \operatorname {diam}\{z_1,z_2,z_3,z_4\}>0.              \tag{12a}
\]
Otherwise a sequence of diameters tending to zero would have a subsequence
converging to one point in all four \(\alpha_i\).  Thus retained-only
squares cannot collapse once (12) holds.  This says nothing about a square
with even one artificial vertex.

## 4. Action balance is not the wild-curve obstruction

For a piecewise smooth splice,
\[
 {\cal A}(\sigma_i)
 =\int_{\alpha_i}y\,dx+\int_{\tau_i}y\,dx.                \tag{13}
\]
Replacing a short tail segment by a detour around a rectangle changes
(13) by the signed area enclosed between the old and new segments.  A free
tail chamber can therefore enforce the one scalar equation (6) without
moving the retained \(C\)-arcs.  A whole-curve vertical translation also
changes the action by \(hL\), but is useless here because it moves the
purported vertices away from \(C\).

For an arbitrary Jordan curve, (13) need not be defined on the limiting
arc.  This does not block a polygonal approximation argument.  If an
embedded essential polygonal circle \(\sigma\) lies in
\[
 (\mathbb R/L\mathbb Z)\times[m,M],
\]
choose a horizontal core \(c_-\) below it.  The two circles bound a compact
annulus \(B_\sigma\).  Stokes' theorem gives, up to the fixed orientation
sign,
\[
 {\cal A}(\sigma)-{\cal A}(c_-)
 =\operatorname {area}(B_\sigma).                        \tag{14}
\]
Therefore the actions of **all** simple essential approximants in one
compact strip are uniformly bounded:
\[
 |{\cal A}(\sigma)|
 \leq |{\cal A}(c_-)|+L(M-m+1).                          \tag{15}
\]
No variation bound and no convergence of the individual actions is used.

Approximate the marked \(C\)-arcs by embedded polygonal arcs and attach
polygonal tails in a common strip.  The alternating defects are bounded by
(15).  Pass to a subsequence of the defects and use a fixed compact tail
chamber of sufficiently large area to correct each defect exactly.  Thus
even an area anomaly on a wild Jordan boundary does not make the correction
escape to infinity.

The delicate issue is instead that an area-correction ear may create new
mixed joint squares.  The chamber must be included in the artificial-square
control lemma; action balance alone is cheap.

## 5. A precise splice-to-square theorem

The following proposition isolates everything still needed.

**Proposition (one artificial generator implies a square on \(C\)).**
Let \(C\) be a planar Jordan curve.  Suppose there are smooth embedded
essential quadruples
\[
 (\sigma_{1,n},\ldots,\sigma_{4,n})
\]
in a common compact cylinder strip, decomposed into retained pieces
\(P_{i,n}\) and artificial tails \(T_{i,n}\), with:

1. the alternating action is zero for every \(n\);
2. the four-curve product is transverse to Tao's square locus;
3. every \(P_{i,n}\) has a lift \(\widetilde P_{i,n}\subset\widetilde D\)
   for one fixed disk satisfying (9a), and these lifted compact sets converge
   in Hausdorff distance to a compact arc \(\alpha_i\subset C\);
4. \(\bigcap_i\alpha_i=\varnothing\);
5. for every sufficiently large \(n\), there is exactly one ordered joint
   square having at least one vertex in \(T_{i,n}\);
6. that artificial square lies in a fixed neighborhood \(U\), is uniformly
   transverse, and no other square meets \(\overline U\).

Then \(C\) contains a nondegenerate square.

**Proof.**
By (9), every approximating quadruple has at least two ordered squares.
Exactly one is artificial, so choose a second square
\((z_{1,n},\ldots,z_{4,n})\) with \(z_{i,n}\in P_{i,n}\) for every \(i\).
Lift its vertices into \(\widetilde D\). Compactness and Hausdorff
convergence give a subsequence converging to
\((z_1,\ldots,z_4)\in\alpha_1\times\cdots\times\alpha_4\).

The cylinder congruences (2) are closed. For example, on the lifted limit
\[
 (x_2-x_1)-(y_4-y_1)\in L\mathbb Z,
\]
while its absolute value is at most
\(\operatorname {diam}_x(\widetilde D)+
\operatorname {diam}_y(\widetilde D)<L\). It is therefore zero. The same
argument applies to the other two independent base congruences, so the
limit is a genuine Euclidean square, not merely a wrapped cylinder square.
If it were degenerate, all four vertices would equal a point of
\(\bigcap_i\alpha_i\), contradicting (4).
\(\square\)

Small generic Hamiltonian perturbations of the four factors preserve their
Liouville periods, so they preserve (6), and can make (7) transverse.
They may be chosen fixed near the already transverse artificial square.
This is the right way to obtain transversality: an arbitrary perturbation
followed by vertical action correction may disturb the retained arcs and
the artificial-square count.

## 6. Why parallel tails consume both generators

The simplest artificial model explains the main trap.  Take four horizontal
essential graphs
\[
 \sigma_i=\{(q,h_i):q\in\mathbb R/L\mathbb Z\}.
\]
Their alternating action vanishes exactly when
\[
 h_1-h_2+h_3-h_4=0.                                     \tag{16}
\]
Under (16), every \(x\in\mathbb R/L\mathbb Z\) gives a square with
\[
 a=h_4-h_1,\qquad b=h_2-h_1.                             \tag{17}
\]
Thus the tails carry a clean \(S^1\)-family of artificial squares.  Its
Floer homology is already \(H_*(S^1)\); a generic Morse--Bott perturbation
has at least a minimum and a maximum.  Both rank-two generators can remain
entirely artificial.

This also shows why “make the tails nearly parallel and argue there is only
one obvious square” is not valid.  Exact action balance is precisely the
height relation which creates the full family.

The Sol review supplied the particularly useful one-parameter countermodel
\[
 (h_1,h_2,h_3,h_4)=(0,s,3s,2s),\qquad s>0.               \tag{17a}
\]
Its alternating action is identically zero.  Equations (17) give
\[
 a=2s,\qquad b=s,
\]
so the clean artificial \(S^1\) carries the entire group
\(HF\cong H_*(S^1)\).  This family defeats both common limiting arguments:

- as \(s\to0\), all its squares collapse to Tao's degenerate diagonal;
- as \(s\to\infty\), their Tao-cylinder (equivalently universal-cover) side
  length
  \(\sqrt{a^2+b^2}=\sqrt5\,s\) escapes every compact set, even though the
  alternating action remains exactly zero.

Thus zero action supplies neither a diameter lower bound nor compactness of
the selected Floer generators.  The compact-strip and empty-fourfold-
intersection hypotheses in Proposition 5 are substantive, not cosmetic.

There is also no localization hidden in the vertical normalization
\(c_i=-{\cal A}(\sigma_i)/L\).  It makes each factor exact, but the resulting
affine conormal can intersect preferentially along the full-winding
artificial collars.  Adding a rectangular action detour changes the affine
translation data; it does not mark the associated Floer class as “central.”
Consequently action/rank/detour alone is a dead route.  Only a direct
geometric exclusion of every other artificial and mixed square can revive
the argument.

## 7. The swallowed-zero model

There is an exact model which reduces the desired construction to connector
control.  Keep the first three horizontal curves and put
\[
 \sigma_4=\{(q,h_4+\varepsilon g(q)):q\in\mathbb R/L\mathbb Z\},       \tag{18}
\]
where
\[
 h_1-h_2+h_3-h_4=0,\qquad
 \int_0^L g(q)\,dq=0.                                   \tag{19}
\]
Equations (18)--(19) retain zero alternating action.  From (2), a joint
square must satisfy
\[
 g(q_4)=0.                                               \tag{20}
\]
Conversely, every zero \(t\) of \(g\) gives exactly one ordered square:
\[
\begin{aligned}
 q_4&=t,\\
 q_1&=t+b,\\
 q_2&=t+a+b,\\
 q_3&=t+a
\end{aligned}
\pmod L,\qquad
 a=h_4-h_1,\quad b=h_2-h_1.                             \tag{21}
\]
If \(g'(t)\ne0\), this intersection is transverse: the three base
congruences solve the other three \(q\)-variables, and the remaining normal
equation has derivative \(-\varepsilon g'(t)\).

Choose a zero-mean periodic \(g\) with exactly two simple zeros, for example
a phase shift of \(\sin(2\pi q/L)\).  The model then has exactly two
transverse artificial squares, as predicted by (9).

Choose \(a,b\) generically so that the two zeros' four-point base sets in
(21) are disjoint. Now choose four small splice windows, one around each
base position for one zero, avoiding every base position for the other zero.
Replace the relevant horizontal pieces in the four windows by excursions
through selected arcs of \(C\). The second zero remains as one uniformly
transverse artificial square. If all mixed squares created by the four
excursions and the action-correction chamber can be excluded, Proposition 5
proves the Square Peg conjecture.

This is the sharpest surviving construction.  It does not ask for a
mysterious “single tail square” from scratch: it starts with the forced
two-generator model and tries to swallow exactly one generator into the
\(C\)-sector.

## 8. The exact unresolved lemma

The remaining statement should be attacked directly in the elementary
coordinates (2).

> **Odd artificial splice lemma (geometric form).**  For every planar Jordan
> curve \(C\), after choosing \(L\), four retained compact arcs
> \(\alpha_i\subset C\) satisfying (12), and the two-zero graph model
> (18)--(21), there are four translation-separated connector/tail systems
> which:
>
> 1. replace one of the two graph squares by excursions through the
>    \(\alpha_i\);
> 2. preserve the other graph square and its transversality;
> 3. have no other square with a vertex on a connector, tail, splice joint,
>    or action-correction ear;
> 4. admit embedded polygonal approximations in a common compact strip; and
> 5. permit exact alternating-action correction inside the controlled
>    artificial chamber.

This lemma is neither formal nor a genericity statement.  Joint squares are
zero-dimensional after transversality, but generic tails can create any
finite number of mixed intersections.  One needs a sign, monotonicity,
scale-separation, or interval-order argument proving **absence**.

The most promising concrete formulation is to put all four connector
corridors into very short, disjoint \(q\)-intervals and choose their heights
with distinct residues modulo \(L\).  Then every mixed square must satisfy
the four congruences (2).  The desired proof would show that the allowed
interval differences and height differences are disjoint for every one of
the \(2^4-1\) nonempty tail/core incidence patterns.  The connector portions
are not horizontal, so endpoints and monotone vertical runs must be included
explicitly; checking only the constant-height plateaux is insufficient.

## 9. Failed shortcuts and audit checklist

- **Attach a tail to the whole closed \(C\):** impossible for an embedded
  circle; it produces a lollipop, self-intersection, or an extra cycle.
- **Use four copies sharing most of \(C\):** their common points are
  degenerate squares in Tao's closed locus.
- **Vertically normalize whole curves:** this balances action but moves the
  retained vertices off \(C\).
- **Use four parallel tails:** zero alternating action creates an
  \(S^1\)-family and both Floer generators remain artificial.
- **Count one visible geometric square in a nontransverse limit:** two Floer
  generators may coalesce there.
- **Invoke a differential to remove the artificial generator:** backwards.
  A differential can lower homology rank; it cannot make a one-dimensional
  chain group have rank-two homology.
- **Count lift choices as the second generator:** wrong by (5).
- **Approximate \(C\) by arbitrary mollification:** embeddedness is not
  preserved.  Use marked simple polygonal approximations and local
  corner-rounding with positive separation from nonincident edges.
- **Assume action primitives converge on a wild arc:** unnecessary here and
  generally unsafe.  Use the strip bound (15), a subsequence, and a compact
  correction chamber.
- **Prove only that mixed squares are unlikely:** insufficient.  Proposition
  5 needs a uniform exclusion so that the second generators have a compact
  genuine limit separated from the artificial square.

## 10. Next attack

Work entirely with the explicit square equations (2) and a piecewise-linear
version of the swallowed-zero model.

1. Fix rational \(L,h_i\), take a rational triangular-wave \(g\) with two
   simple zeros, and verify the two baseline squares exactly.
2. Reserve one zero as the persistent artificial generator and open splice
   windows around the four coordinates of the other.
3. Parameterize each connector by monotone rational segments in a designated
   \(q\)-interval and height band.
4. For each of the fifteen nonempty artificial incidence patterns, turn (2)
   into interval constraints and seek a symbolic separation certificate.
5. Put the bounded area-correction ear inside one splice window and include
   its possible segments in the same case split.
6. Only after an exact separation pattern is found, replace the four core
   placeholders by marked polygonal approximations of an arbitrary \(C\).

Computation can discover a viable ordering of intervals and height residues,
but the deliverable must be a finite inequality certificate valid for every
point on every connector segment.  If no ordering survives, the resulting
finite obstruction should reveal whether the artificial sector has an
independent even-parity law, which would kill the splicing route.

## Sources and status

- [Tao, *An integration approach to the Toeplitz square peg problem*,
  Forum of Mathematics, Sigma 5 (2017), e30](https://doi.org/10.1017/fms.2017.23).
- [Djuretić, *Piunikhin--Salamon--Schwarz isomorphisms and spectral
  invariants for conormal bundle*, arXiv:1411.0852](https://arxiv.org/abs/1411.0852).
- [Abbondandolo--Portaluri--Schwarz, *The homology of path spaces and Floer
  homology with conormal boundary conditions*,
  arXiv:0810.1977](https://arxiv.org/abs/0810.1977).
- July 2026 public manuscript: *A Conormal Proof of Tao's Alternating-Area
  Conjecture for Jointly Inscribed Squares*, version 1.2.  This is an
  unrefereed public claim, not established literature.  The circulated
  version has the global sign error described in the repository audit.

The repository-required Sol xhigh second opinion returned:

> **KILL action/rank/detour as a localization argument.**  The exact
> horizontal family (17a) supports the full rank-two group on artificial
> collars; its squares collapse as \(s\to0\) and escape as \(s\to\infty\)
> while alternating action stays zero.  Empty fourfold intersection of the
> retained arcs gives the useful diameter gap (12a), but it does not stop
> artificial collars from carrying all Floer homology.

Accordingly the only held statement is the conditional Proposition 5.  The
odd artificial splice lemma has not been proved, and without a finite mixed-
square exclusion certificate this angle does not advance the unrestricted
conjecture.
