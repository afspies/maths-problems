# Literature audit through 2026-07-24

## Status boundary

The unrestricted Square Peg conjecture remains open: a general Jordan curve is
not yet known to inscribe a nondegenerate square.  The regularity boundary
changed materially after the older surveys:

- Greene--Lobb prove the prescribed-rectangle theorem for smooth curves and
  develop Jordan Floer homology and action spectral invariants.  Their
  shrink-out paper gives only an interval of aspect angles for a rectifiable
  curve, with the square following under an area/diameter inequality
  [GL-floer].
- Their graph paper, now published online in 2026, proves a square for a union
  of two graphs of Lipschitz constant below \(1+\sqrt2\), and every rectangle
  at Lipschitz constant at most \(1\) [GL-graphs].
- Asano--Ike v3 remove the area/diameter condition: every rectifiable Jordan
  curve and every locally monotone Jordan curve inscribes every prescribed
  rectangle [AI].  Rectifiable curves therefore are **not open territory**.

The official arXiv record labels Asano--Ike v3 as submitted 2026-01-05 and the
downloadable v3 PDF is headed 2026-01-06.  A secondary experimental HTML
rendering retrieved during this audit displayed 2026-03-22, matching the date
reported in the campaign prompt, but that date is not on the official v3
record.  The mathematical audit below uses the downloadable v3 PDF.

## Asano--Ike Theorem 1.1, with quantifiers

Identify \(\mathbb R^2\) with \(T^*\mathbb R\), and let \(\lambda\) be the
Liouville form (the paper uses \(\lambda=\xi\,dx\); reversing the contact sign
only reverses all primitives).  Let
\(e:\mathbb R\to\mathbb R/2\pi\mathbb Z\simeq S^1\) be the quotient.

For a *parametrized* Jordan curve \(c:S^1\to\mathbb R^2\), Theorem 1.1 assumes
there are smooth Jordan embeddings \(c_n:S^1\to\mathbb R^2\) such that:

1. \(c_n\to c\) uniformly as maps on this same parameter circle; and
2. after choosing primitives
   \(df_n=(c_n\circ e)^*\lambda\), the functions \(f_n:\mathbb R\to\mathbb R\)
   converge locally uniformly to a continuous \(f\).

The additive constants are not specified in the theorem.  Equivalently one may
normalize all \(f_n(0)=0\).  Since the pullbacks are \(2\pi\)-periodic,
\[
 f_n(t+2\pi)=f_n(t)+\int_0^{2\pi}(c_n\circ e)^*\lambda.
\]
Thus uniform convergence on one period plus convergence of the period
integrals is exactly local-uniform convergence on \(\mathbb R\).  The
parametrizations are not disposable: unparametrized Hausdorff convergence is
not the stated hypothesis.  Remark 5.6 allows \(C^1\), rather than smooth,
Jordan approximants.

No area-\(\pi\) normalization appears in the statement.  In the proof the
limit curve is first scaled to enclose area \(\pi\); the approximants are then
scaled by factors tending to \(1\).  The limiting primitive forces the conic
microsupport of the limiting sheaf quantization to have no nonintegral
\(\pi\)-translate self-intersections.  Theorem 4.1 converts that disjointness
into a non-diagonal intersection with the rotated torus, hence a
\(\theta\)-rectangle.  The ingredients actually used after Theorem 1.1 are:

- completeness and microsupport semicontinuity for the Tamarkin interleaving
  metric;
- a compactly supported area-preserving/Hamiltonian homeomorphism taking the
  standard circle to the measure-zero Jordan curve;
- the critical value \(a(\theta,C)\in(0,\pi)\) in the persistence object; and
- the fact that diagonal intersections can occur only at action shifts in
  \(\pi\mathbb Z\).

For positive-area Jordan images the paper gives a separate density argument.

### Where rectifiability enters

Proposition 5.8 (Corollary 5.9 in v3) takes a Riemann map
\(\varphi:\mathbb D\to D\), extends it to the closed disk by Carathéodory, and
uses the inner level curves
\(c_n=\varphi|_{\partial\mathbb D_{1-1/n}}\).  They are smooth Jordan curves.
Riesz--Privalov supplies convergence of their lengths to the boundary length;
the rectifiable Green-theorem lemmas then give convergence of the primitives.
Rectifiability enters at precisely this length/Green-theorem step, not in the
sheaf criterion itself.

## Greene--Lobb shrink-out and its relation to Asano--Ike

For a smooth/analytic curve \(\gamma\),
\[
 L_0=\gamma\times\gamma,\qquad L_1=R_\theta(L_0)\subset\mathbb C^2.
\]
Off the clean diagonal \(\Delta(\gamma)\), intersections correspond to
nondegenerate \(\theta\)-rectangles.  Greene--Lobb build a two-dimensional
Jordan Floer homology using strips that avoid the diagonal divisor.  The
top-class spectral invariant \(\ell(\gamma,\theta)\) is an action value,
monotone in \(\theta\), tends from \(0\) to the enclosed area as
\(\theta:0\to\pi\), and has derivative bounded above by
\(\operatorname{Rad}(\gamma)^2\).  The resulting action window selects
rectangles whose action cannot shrink to zero.  For rectifiable limits, a
uniform length bound converts this action lower bound into geometric
nondegeneracy.

The sheaf proof retains the same Lagrangian rotation and action filtration, but
packages them as \(F_C\), \(R_\theta F_C\), and a persistence object in the
Tamarkin category.  Primitive convergence rules out unwanted action
translations on the diagonal; a critical value strictly between \(0\) and
\(\pi\) must therefore be realized off the diagonal.  For the present bridge,
the Floer construction need not be reproved: after verifying the hypotheses of
Asano--Ike Theorem 1.1, their sheaf-theoretic implication can be cited.

## Rough/Young approximation already in the literature

Boedihardjo--Geng prove two facts that are decisive here [BG]:

1. every parametrized Jordan curve admits arbitrarily fine polygonal
   interpolants that are themselves Jordan; prescribed parameter times may be
   included; and
2. if the original path has finite \(p\)-variation, its polygonal
   interpolants converge to it in \(q\)-variation for every \(q>p\).

They use these facts to prove Green's theorem for finite-\(p\)-variation Jordan
curves when \(p<2\).  This is much stronger than merely knowing that some
unparametrized polygon lies nearby, and it is exactly what prevents the
embedded-approximation step below from being a hidden assumption.

Targeted searches for combinations of “2412.21057”, “finite p-variation”,
“Young integral”, “rough path”, and “rectangular/square peg” found no paper
through 2026-07-24 stating the corollary proved in the accompanying
`angles/p-variation/README.md`.  This is a novelty check, not a proof of
priority: the result is a short synthesis of published theorems and may be
regarded by experts as an immediate corollary once pointed out.

## July 2026 addendum

### Greene--Lobb, arXiv:2604.17116

Greene--Lobb prove that every Jordan curve inscribes rectangles for a set of
diagonal angles of measure at least \(A/R^2\), where \(A\) is enclosed area
and \(R\) is half the diameter. This is a major arbitrary-Jordan result but
does not guarantee any prescribed angle, including \(\pi/2\). It therefore
neither subsumes the finite-\(p<2\) prescribed-rectangle consequence nor
solves the Square Peg conjecture.

### Unrestricted null-trace reduction

Asano--Ike Remark 5.5 separately proves every positive-planar-measure Jordan
trace has every prescribed rectangle by Lebesgue density.  Thus the
unrestricted problem reduces to null traces.  Remarks 4.2 and 5.7 identify
diagonal \(\mu hom\)-cohomology vanishing as the missing universal step.

The explicit interleaved \(r=\theta^{-1/2}\) spiral in
`../results/null-spiral-no-primitive.md` shows that the stronger
primitive-approximation hypothesis in their Theorem 1.1 is not universal,
even among null traces.  A local tubular-crosscut lemma excludes every
parameter-aligned \(C^1\) approximation with convergent primitives.  This is
a new obstruction to the sufficient criterion, not a counterexample to
Square Peg and not a refutation of the weaker Remark 4.2 condition.

### Antonelli--Young, arXiv:2605.15987

Antonelli--Young define signed area for critical \(1/2\)-Hölder curves
through convergence over all fine polygonal partitions. Their planar
Theorem 1.2 assumes the dyadic quadratic-diameter sum
\[
\sum_{i,j}\operatorname {diam}\{\gamma(j2^{-i}),
\gamma((2j+1)2^{-i-1}),\gamma((j+1)2^{-i})\}^2<\infty.
\]
Under this hypothesis the signed area exists, the trace is
\(\mathcal H^2\)-null, and the area is the integral of winding number.
The paper's beta numbers enter its ambient Heisenberg-map/fibre argument;
they are not the stated hypothesis of the directly used planar theorem.

The all-partitions quantifier gives uniform prefix-area convergence by
extending two prefix partitions with the same tail.  Together with
Boedihardjo--Geng embedded polygons and Asano--Ike, this yields the critical
peg theorem in `angles/critical-p2/antonelli-young-bridge.md`.

### Universal conformal \(L^2\) compactness

For a Riemann map \(f(z)=\sum a_nz^n\) of any bounded Jordan domain, the
area identity \(\sum n|a_n|^2=|\Omega|/\pi\) gives strong \(L^2\)
convergence of the mean-centered Liouville primitives on the analytic level
curves \(f(re^{it})\).  The Fourier proof and the resulting exhaustive
tame/action-concentration dichotomy are in
`../angles/conformal-l2/README.md`.

Targeted searches found no primary source stating this exact primitive
theorem in the peg context.  It is elementary enough that the safe
description is “apparently unstated in this context,” not a priority claim.
It does not imply Asano--Ike Remark 4.2 because point-supported action
concentration is invisible in \(L^2\).

### Configuration and microlocal boundary audit

Matschke's Theorem 2.8 implies that a square-free Jordan curve has a special
trapezoid at every fixed parameter scale.  This supplies exact collision
screens but does not exclude them.  Vrećica--Živaljević's
Fulton--MacPherson extension uses the tangent screen of a \(C^1\) curve;
arbitrary Jordan arcs admit square collision screens and do not provide a
curve-independent boundary test map.

The exact Asano--Ike target was reconstructed as derived global sections of
the diagonal restriction, rather than pointwise support vanishing.  The
required new result is a \(C^0\) clean-intersection theorem at the
persistence-bar level.  Small Hamiltonian/interleaving size does not control
individual action branches, and `../results/shrinking-square-action-injection.md`
constructs exact collapsing squares with arbitrary prescribed limiting
action.

### Wider configuration and barcode checks

Hugelmeyer proves that a square-free Jordan curve would admit a square
envelope, another exact global continuation object.  This does not rule out
the collision screens above; it reinforces that an obstruction must control a
whole continuum rather than one local blow-up.

A relative-transversality refinement of Matschke's parity argument gives a
connected, fixed-type continuum of exact special trapezoids spanning every
compact positive scale interval.  Conversely, disjoint local insertions show
that pair-coalescent, finite-trapezoid, and equilateral screens can all occur
at the same one-sided prime end of one Jordan curve.  These are recorded as
campaign deductions, with no priority claim.

Buhovsky--Humili{\`e}re--Seyfaddini and Kislev--Shelukhin give \(C^0\)
continuity of Hamiltonian and Lagrangian Floer barcodes in appropriate
aspherical/monotone settings, up to overall shift.  This does not localize a
global barcode at the collapsed diagonal; Hamiltonian homeomorphisms can
carry multiple spectral values on a very small fixed set.  The null spiral
makes the local failure explicit: finite truncations vanish at interior
diagonal action, while the limit has full projected action microsupport and
a vanishing-width two-sheet eye.  The corrected action-retaining toy model
shows that the \(!\)-versus-\(*\) cone has \(\tau_t=0\); it is not the
obstruction.  What is strictly stronger than global bottleneck continuity is
excluding an exact-action Milnor/ephemeral term in the continuation
telescope.  The interval
\(\mathbb k_{[a,a+\varepsilon)}\) is the exact persistence countermodel:
its lifetime vanishes while its left-end microstalk remains non-zero.

### Fixed-input localization and wild boundary audit

Oh's localization theorem for engulfable Hamiltonian paths
[OhLocalization] replaces \(C^2\)-smallness by \(C^0\)-smallness of the
time-one map plus a full engulfable isotopy. Under the full cotangent
hypotheses, its maximum-principle construction identifies the relevant local
and global complexes and fundamental-class spectral invariant. It does not
identify Asano--Ike's twisted \(v\)-complex or compare the original relative
rotation with the cutoff. The source also warns that thin trajectories may
have large area and that there is no uniform action or filtration control.

This does not control Asano--Ike's critical \(v\).  Their microlocalization
maps
\[
v\longmapsto v\otimes1+1\otimes v,
\]
which restricts to zero on the clean diagonal over \(\mathbb F_2\).  It is
also a class in their twisted quantization with endomorphism algebra
\(H^*(S^1)\), not the ordinary top class of \(C_0\times C_0\).

Fixing the first input does not make microlocal Hom continuous under the
completeness telescope. For bounded finite-stalk constructible sheaves
\[
F=\mathbb k_{(0,1)},\qquad G_n=\mathbb k_{(1/n,1)},
\]
every finite \(\mu hom(F,G_n)\) vanishes over \(T^*_0\mathbb R\), but
\(\operatorname{hocolim}G_n=F\) and \(\mu hom(F,F)\) is rank one on the
negative conormal. The composite \(\mu hom(F,-)\) is therefore not
cocontinuous: the fixed sheaf remains a contravariant internal-Hom test
object, while microlocal specialization also contains an open-embedding
\(Rj_*\). The left fronts are literal translates with a fixed right cutoff.
The failure remains after external product with a positive-\(\tau\) Tamarkin
factor.

Hugelmeyer's full cross-time relation also gives no winding sign.  The exact
square path
\[
z(t)=e^{-t+(i/20)\sin(\pi t/\log2)},\qquad
(a,b,c,d)=(z,2z,(1+i)z,(2+i)z)
\]
avoids every outer--inner cross-time collision and admits strict
exterior/interior separation by a triangular Jordan domain, but its
synchronized outer strands form alternating positive and negative lenses.
See `../results/envelope-cross-time-no-go.md`.

Finally, an explicit square-test zero with Jacobian determinant \(-2\) can
be scaled into a shrinking bump on a locally square-free \(1/4\)-Lipschitz
Jordan graph.  The regular local mod-two degree one collapses to the unique
total-collision orbit of the cyclic gap simplex while retaining an exact
square screen and fixed prime-end side.  See
`../angles/wild-configuration-degree/README.md`.  This is a local
configuration no-go, not a global parity computation.

### July 2026 unrestricted boundary refinements

The generic GKS-continuation repair is false even for smooth exact graphs.
The telescope in `../angles/gks-positive-telescope/README.md` consists of
invertible compactly supported GKS images of one simple object, has summable
Hamiltonian amplitudes, and uses canonical positive epigraph maps.  Every
finite microlocal restriction at one fixed reduced covector vanishes, while
the homotopy colimit is the original object and has a rank-one restriction.
Thus positivity, invertibility, and summable interleaving size do not imply
no-ephemeral rigidity.  Any surviving microlocal theorem must use the
conjugated quarter-rotation and its four-sheet cap maps.

Hugelmeyer's envelope does carry a canonical integer.  If \(A,B\) are
argument lifts of the two exterior strands about an interior point, their
relative lift tends to integers \(n_-\) and \(n_+\) at the two collapsed
ends, and total outer winding gives
\[
 n_- - n_+=1.
\]
This is an end-order reversal in the ordered configuration cylinder.  Two
disjoint proper cylinder arcs can realize that reversal, so ordinary
linking, Maslov, or ruled-ribbon intersection theory does not contradict it.
The exact missing statement is an end-order rigidity theorem for compatible
boundary-crossing carriers in the full admissible-square space; local
polygonal notches realize either end order.

Resolving total collision likewise supplies no integral refinement of the
usual parity.  The cyclic configuration quotient is nonorientable and its
degree-zero intersection group with orientation coefficients is
\(\mathbb Z/2\).  The resolved collision boundary carries an integer, but
its inclusion reduces that integer modulo two.  The explicit wild motif has
equivariant square-test determinant \(-8\) and realizes one boundary unit;
two disjoint motifs change the resolved integer by two without changing the
global class.  See `../angles/global-collision-charge/README.md`.

An unrefereed six-page manuscript circulated on 2026-07-15 claiming a
conormal-Floer proof of Tao's Conjecture 5.6.  The public version is false as
written: it defines \(\mathcal A=-\int y\,dx\) but subsequently uses the
opposite sign in the Liouville-period normalization.  Replacing that
definition by Tao's convention \(\mathcal A=+\int y\,dx\) repairs the
calculation.  After that repair, the square--conormal shear, exact-circle
Hamiltonian lemma, compact-support cutoff, conormal PSS step, and embedded
polygonal rounding passed two independent audits.  The safe status is
therefore “apparently sound after a mandatory sign repair, but unreviewed,”
not established literature.  The detailed claim audit is
`TAO56_CLAIM_AUDIT.md`.

Even the corrected four-curve result does not prove unrestricted Square Peg.
Tao's closed square locus includes the degenerate diagonal, and its
zero-section/conormal Floer class is precisely \(H_*(S^1;\mathbb F_2)\).
An unrestricted bridge must essentialize four pieces of a planar Jordan
curve with balanced alternating action while preventing both Floer classes
from collapsing to the diagonal or escaping through the artificial pieces.
