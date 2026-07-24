# Journal — Four-dimensional Mahler volume conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-23 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-23 — shadow-flow audit and terminal subclasses

### Scope and source audit

Worked on branch
`problem/mahler-volume-4d/2026-07-23-terminal-polytopes`, touching only this
problem folder and the generated root board. No `AGENTS.local.md` was present.

Audited Chen--Li--Xi--Xu, *The Mahler Conjecture in Three Dimensions*,
arXiv:2605.09334v3, against Meyer--Reisner's dimension-\(n\) shadow-system
theorem and the Fradelizi--Meyer--Zvavitch restatement. The step map is in
`literature/shadow-flow-audit.md`.

The minimizer-to-terminal reduction is valid in dimension four, but not merely
by copying the preprint. Its printed persistence proof uses a specifically 3D
intersection argument. Replacing it with an independent-active-facets
subsequence argument gives short-time face-lattice persistence in every
dimension. Facet triangulation and the one-direction determinant argument make
volume affine in every dimension. The bounded-vertex minimization and polar
chain then prove terminality of both a minimizer and its Santaló polar.

### Exact harness

Built `harness/polytope.py` before any computational search. It uses exact
`Fraction` arithmetic for rational rank/nullspaces, supporting facets, polar
vertices, incidence summaries, admissible-speed matrices, and simplex volume.
The speed equations are affine dependencies indexed by vertex--facet
incidence; the audit explicitly records that incidence alone does not
determine realization-dependent coefficients.

Commands:

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
python3 -m py_compile problems/mahler-volume-4d/harness/polytope.py problems/mahler-volume-4d/harness/test_polytope.py
```

Final outcome: 6 tests passed in 0.494 seconds; byte-compilation passed. The
centered 4-simplex has exact product \(3125/576\) and speed dimension five.
The cross-polytope, cube in a facet-parallel direction, and pyramid over a
cube certify nontrivial speeds. No floats, seeds, solver search, or bulk
face-lattice enumeration were used.

### Incidence inequalities and subclass proofs

For \(V=f_0\), \(F=f_3\), \(I=f_{03}\), maximum facet size \(\Delta\), and
maximum vertex--facet degree \(\delta\), exact rank subadditivity gives
\[
\dim A_\theta(P)\ge V-I+4F+\Delta-4
\]
when \(\theta\) is parallel to a largest facet. Pair-terminality therefore
implies
\[
\Delta\le I-V-4F+9,\quad
\delta\le I-F-4V+9,\quad
2I\ge5(V+F)-10.
\]

Summing Euler over all 3-facets and using polygonal 2-faces and edge links
gave the flag/Dehn--Sommerville identities
\[
f_{03}-f_{02}+2f_2=2f_3,\qquad
f_{03}=f_{02}-2f_1+2f_0.
\]

Every simplicial 4-polytope has unconstrained speed space
\(\mathbb R^{f_0}\), so terminality forces \(f_0=5\). Duality handles the
simple pair-terminal class.

For \(P=\operatorname{pyr}(Q)\) and tangent direction \((u,0)\), proved
\[
A_{(u,0)}(P)\cong A_u(Q)\oplus\mathbb R,\qquad
T(P)\cong T(Q)\oplus\mathbb R.
\]
The polar is again a pyramid over a face-lattice dual of \(Q\). The 3D
dual-pair counting lemma then forces a pair-terminal 4-pyramid to be a
simplex.

Finally derived directly from polar cross-sections and the
centroid--Santaló characterization:
\[
\mathcal P(\operatorname{pyr}_d K)
=\frac{(d+1)^{d+1}}{d^{d+2}}\mathcal P(K).
\]
The audited three-dimensional theorem therefore proves
\(\mathcal P(P)\ge3125/576\) for every 4-pyramid, with equality only for a
4-simplex. This is the strongest first-session result and passes the
two-session continuation gate.

### Mandatory independent review

Consulted GPT-5.6 Sol at xhigh effort once the incidence/pyramid route was
selected. Its adversarial verdict:

- all rank, duality, and flag identities were correct;
- the simple/simplicial and pyramid terminality reductions were sound;
- the printed 3D persistence paragraph was a real citation gap, and the
  independent-active-facets repair closes it;
- the full terminal classification does **not** follow from the current
  inequalities; and
- the pyramid volume-product factorization supplies the stronger direct
  infinite-family theorem.

The reviewer required no correction to the stated partial theorems. Its
warning against presenting the flag inequality as a global classification is
reflected throughout the write-up.

### Compute and verdict

Local exact tests used under one CPU-second in the final run. External work
was one xhigh independent-review turn and source retrieval; there was no
search compute. Verdict: **continue**. The gate is met by both a new
incidence/dimension inequality and nontrivial infinite-family theorems.

## 2026-07-24 — the terminal bridge fails; projective second variation

### Exact all-direction harness

Worked on branch
`problem/mahler-volume-4d/2026-07-24-24cell-rigidity`, within the problem
folder plus the generated board.

Extended the rational harness with exact enumeration of every
facet-normal-arrangement flat; Paffenholz's rational 24-cell realization;
exact pulling triangulations, volumes, centroids and covariance matrices; an
independent boundary-facet cone integration for 24-cell centroids; and exact
projective Santaló normalization.

The regular 24-cell is not terminal: twelve rank-three direction flats have
speed dimension six. A generic projective deformation removes those extra
speeds, exposing realization dependence missed by pure incidence counts.

### Counterexample to the proposed bridge

For \(a=(1/5,2/5,3/5,4/5)\), let \(P_0\) be the Paffenholz 24-cell and
\(g=c(P_0^\circ)\). The rational projective image
\[
Q=\{x/(1-g\cdot x):x\in P_0\}
\]
satisfies \(Q^\circ=P_0^\circ-g\), hence \(s(Q)=0\).

The exact exhaustive check found 1,941 primal direction flats and 580 polar
direction flats. Every admissible-speed space has dimension five on both
sides. The labeled incidence agrees with the regular \(a=0\) family member,
and two independent exact centroid integrations agree. Thus \(Q\) is a
rational non-simplex whose genuine Santaló polar is also terminal. The
primary bridge lemma is false.

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py

labelled-24-cell-incidence True
santalo-polar-centroid-zero True
primal-centroid-zero False
primal-direction-flats 1941
polar-direction-flats 580
all-speed-dimensions 5
terminal-pair-implies-simplex False
```

Wall clock was approximately 13 seconds in the final parallel verification.

### Bi-centering and the covariance saddle

Independently derived the first projective variation. If \(s(K)=0\), local
minimality under \(x\mapsto x/(1+t\,u\cdot x)\) forces \(c(K)=0\); hence a
minimizer is bi-centered.

A floating-point Newton discovery run located the bi-centering translation
near
\[
(0.065348617243,\ 0.127816191744,\ 0.153467113574,\ 0.022269205148).
\]
No theorem relies on that run. `bicenter_certificate.py` reconstructs the
claim using outward-rounded dyadic rational intervals. A Krawczyk inclusion
proves a unique exact centroid root in the radius-\(10^{-10}\) box. On the
whole box it proves
\[
e_1^\mathsf T\left(\operatorname{cov}(K^\circ)
-\frac1{36}\operatorname{cov}(K)^{-1}\right)e_1<0.
\]
The exact root therefore violates the Klartag/Balacheff--Solanes--Tzanev
projective second-order condition and is a saddle. The centroid Jacobian is
nonsingular and the violation strict, so the implicit-function theorem
excludes an open four-parameter critical branch of nonregular 24-cells.

The final interval command completed in 7.1 seconds:

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/explore_bicenter.py
```

The certified covariance-gap upper bound was

```text
-2769897430741000129485066521703178181068461843
 /365375409332725729550921208179070754913983135744
```

### Verification and independent review

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
Ran 10 tests in 4.201s
OK
```

Consulted GPT-5.6 Sol at xhigh effort at the classification pivot and on the
proposed proof. It independently reran the rational bridge counterexample,
checked the sign in \(Q^\circ=P_0^\circ-g\), validated the bi-centering
lemma, and identified the covariance Hessian as the correct next condition.
It also caught two proof-quality issues: nearby rational terminal points do
not certify terminality at the exact centroid root, and the pulling centroid
needed an independent integration. The report makes no terminality claim at
that root, and the facet-cone calculation supplies the independent check.

### Verdict

The full four-dimensional conjecture remains open. The session nevertheless
passes the continuation gate twice: it decisively falsifies the campaign's
central bridge with an exact certificate, and it excludes an open
non-pyramidal 24-cell critical branch by a rigorous second variation.
Terminal face-lattice classification is now a dead route. The next proof
campaign must use full realization-space variations.

## 2026-07-24 — join closure and realization-space Hessian

### Parallel proof attacks

Worked on branch
`problem/mahler-volume-4d/2026-07-24-realization-hessian`, within the problem
folder plus the generated board. Three independent agents attacked
realization rigidity, global covariance inequalities, and adversarial route
selection. GPT-5.6 Sol at xhigh effort reviewed every theorem-shaped claim.

The stress/Gale attack produced paired incidence coordinates
\(x_v\cdot y_F=1\), with tangent dimension
\[
4(f_0+f_3)-f_{03}+\omega,
\]
where \(\omega=\dim\ker J^\mathsf T\). Exact ranks for the regular and
nonregular Paffenholz 24-cells give tangent dimensions 52 and 50,
respectively; the standard projective subspace has rank 24.

Terminality makes the facet-supported circuit spaces span the global Gale
kernel. If their support graph is disconnected, the homogeneous
configuration splits and the polytope is an affine join. Otherwise circuit
connectivity forces the labeled projective stabilizer to be scalar. Thus a
terminal non-join has projective orbit dimension 24 and quotient tangent
dimension
\[
4(f_0+f_3)-f_{03}+\omega-24.
\]

### Exact join, product, and free-sum theorems

Two beta-integral calculations proved
\[
\mathcal P(K\times L)=\mathcal P(K\oplus L)
=\frac{p!q!}{(p+q)!}\mathcal P(K)\mathcal P(L)
\]
and, for \(d=p+q+1\),
\[
\mathcal P(K*L)=
\left(\frac{p!q!}{d!}\right)^2
\frac{(d+1)^{d+1}}
{(p+1)^{p+1}(q+1)^{q+1}}
\mathcal P(K)\mathcal P(L).
\]
The Santaló height in the join proof is
\(\tau=(q+1)/(d+1)\). Consequently the sharp conjecture is closed under
joins. In dimension four, the non-pyramidal split is \(1+2\); the known sharp
one- and two-dimensional theorems give \(3125/576\), with equality only for
the segment--triangle join, a 4-simplex.

Products and free sums have strict lower bounds \(243/32\) in the \(2+2\)
split and \(64/9\) in the \(1+3\) split. The harness independently verifies
the Santaló-centered segment--square join product \(3125/486\).

### Exact Santaló-envelope Hessian

Implemented `harness/variation.py` using exact second-order rational jets.
It differentiates volumes on fixed pulling triangulations, reconstructs every
polar-vertex jet from four incident primal vertices, and checks all remaining
incidences through second order. At a bi-centered base body, eliminating the
moving Santaló point subtracts the Schur term
\[
\frac56\langle c'(K^\circ),
\operatorname{cov}(K^\circ)^{-1}c'(K^\circ)\rangle
\]
from the unreduced log-volume Hessian.

Sanity checks give zero for affine scaling and reduced projective curvature
\(-31/13\) at the regular 24-cell. On all four Paffenholz parameter
directions, polarization gives the complete exact matrix
\[
\nabla^2\log M(0)=-\frac{61}{234}I_4.
\]
The regular 24-cell is therefore a strict local maximum inside this
four-parameter realization slice. Continuity excludes an open neighborhood
of the chart from local Mahler minimality.

### Independent review and route verdict

The xhigh Sol reviewer independently rederived both beta factors, the
Santaló height, the equality cases, the circuit-graph/projective-orbit
argument, and the two Hessian normalizations. Its verdict required no
correction. It emphasized two limitations now recorded in the angle notes:
vectors in a singular incidence tangent space need not integrate, and the
correct constrained Hessian includes incidence-stress terms.

The covariance agent derived the exact sufficient target
\[
L_KL_{K^\circ}\le L_{\Delta_4}^2
\]
for pair-terminal minimizer candidates, but current sharp isotropic-constant
knowledge does not prove it in dimension four. A trace ceiling is a possible
stronger separator only with extra terminal/minimality structure.

### Commands, compute, and verdict

```text
python3 -m py_compile problems/mahler-volume-4d/harness/*.py
python3 -m unittest discover -s problems/mahler-volume-4d/harness -q
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
```

Byte-compilation passed. The final unit run passed 13 tests in 24.616
seconds. The terminal-bridge certificate completed in 12.8 seconds and
reproduced all 1,941 primal and 580 polar direction-flat checks. The interval
certificate completed in 7.5 seconds, again proving Krawczyk inclusion and a
strictly negative covariance-gap upper bound. No randomized search or
floating-point assertion entered a proof. The refactored floating discovery
aid completed in 2.0 seconds and only guided the covariance route.
The full non-pyramidal conjecture remains open. The session nevertheless
passes the continuation gate with a sharp infinite-family theorem, a new
incidence/stress dimension formula, and a second open non-pyramidal
realization-family exclusion. The remaining proof problem is the connected,
integrable realization-space branch, not face-lattice enumeration.

## 2026-07-24 — smooth stress cone and full-rank 24-cell exclusions

### Push and scope

Pushed the previously merged local `main` through commit `e4c79f9` to
`origin/main`, then opened branch
`problem/mahler-volume-4d/2026-07-24-connected-hessian-rigidity`.
Work remained inside this problem folder plus the generated board.

Three independent agents attacked the connected case: exact
slack-variety integrability, a covariance/slack-concentration route, and an
xhigh Sol adversarial synthesis. No agent edited repository files.

### Primary-source audit and smooth signed families

Inspected Proposition 5.8(3) of Rastanawi--Sinn--Ziegler directly from the
primary paper. It gives eight centrally symmetric one-parameter 24-cell
families with incidence Jacobian rank 144 for \(0<x<1\). Transcribed the
displayed coordinates and checked them independently with the rational
harness.

Writing \(r=x^2\), direct cube-pyramid and cross-polytope-cap integration
gave
\[
|K_x|=\frac{32}{1+r},\qquad
|K_x^\circ|=\frac{3+r}{6},
\qquad
\mathcal P(K_x)=\frac{16(3+r)}{3(1+r)}.
\]
The order-24 symmetry and exact second moments give
\[
\operatorname{cov}(K_x)=
\frac{13+22r+5r^2}{30(1+r)^2}I,
\]
\[
\operatorname{cov}(K_x^\circ)=
\frac{39+27r-3r^2+r^3}{240(3+r)}I.
\]
Their scalar product is strictly below \(1/36\), because the numerator of
the difference is
\[
93+191r+250r^2+106r^3+r^3(1-r)(5r+12)>0.
\]
Thus every parameter in all eight signed families violates the projective
local-minimum condition. Continuous Santaló normalization excludes open
subsets of the full smooth 48-dimensional realization stratum.

### Exact q-regular analytic arc

For the paired incidence equations
\[
F_{vF}=x_v\cdot y_F-1,
\]
defined the stress quadrics
\[
q_\lambda(u)=
\sum_{v\in F}\lambda_{vF}a_v\cdot b_F,
\qquad \lambda\in\ker J^\mathsf T.
\]
A tangent has a formal second-order lift exactly when every stress quadric
vanishes. More strongly, Lyapunov--Schmidt reduction followed by the blow-up
\(r^{-2}\Phi(ru)\) proves that
\[
q(u)=0,\qquad Dq_u\text{ surjective}
\]
integrates to a two-sided real-analytic incidence arc, even when the base
realization is singular.

At the rational Paffenholz member, exact nullspace arithmetic gives
\[
\operatorname{rank}J=142,\quad \dim\ker J=50,\quad
\dim\ker J^\mathsf T=2.
\]
The deterministic witness
\[
u=\tau_0+\frac{659}{667}\tau_1
\]
satisfies both quadrics and has \(\operatorname{rank}Dq_u=2\).
The augmented second-order system has rank 142. Adjoining \(u\) raises the
PGL tangent rank from 24 to 25 and the PGL-plus-Paffenholz rank from 28 to
29, proving this is a genuinely new realization direction. Nearby nonzero
arc points have Jacobian rank 144.

Transport to the exact pair-terminal Santaló-normalized counterexample,
openness of its finite speed-rank minors, the nonsingular bi-centering
certificate, and the strict covariance violation together exclude an open
24-dimensional moduli family of smooth pair-terminal 24-cells.

### Mandatory correction and new global target

The xhigh Sol reviewer caught an error in the previous handoff language:
only the 20-dimensional affine subgroup is a Mahler gauge. The four
denominator-projective directions are genuine and carry the covariance
Hessian. After quotienting affine motion, the correct block test is
\[
\begin{pmatrix}A&B\\B^\mathsf T&C\end{pmatrix}\succeq0,
\]
which requires
\[
A\succeq0,\qquad
\ker A\subseteq\ker B^\mathsf T,\qquad
C-B^\mathsf T A^\dagger B\succeq0.
\]
All current documents now distinguish PGL realization moduli from affine
Mahler gauges.

The global exploratory route rewrites the trace target as slack
concentration. For independent uniform \(X\in K\), \(Y\in K^\circ\),
bi-centering gives
\[
\operatorname{tr}(
\operatorname{cov}K\operatorname{cov}K^\circ)
=\operatorname{Var}(1-\langle X,Y\rangle).
\]
Vertex triangulations turn the desired connected-terminal ceiling \(<1/9\)
into an explicit volume-weighted quadratic energy of normalized slack
submatrices. This is now the cleanest theorem-shaped global target, but it
remains a conjecture.

### Verification and verdict

Commands:

```text
python3 -m py_compile problems/mahler-volume-4d/harness/*.py
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
python3 tools/board.py
```

Byte-compilation passed; the final isolated run passed all 15 exact tests in
32.161 seconds. The exhaustive terminal-pair certificate completed in 12.6
seconds, and the interval bi-centering/covariance certificate completed in
7.6 seconds with the same strict rational bounds. Exploratory floating
sampling and rational interpolation only suggested formulas; every recorded
formula was rederived geometrically and checked with exact fractions.

The full connected non-pyramidal conjecture remains open. This session
nevertheless advances the hard case in three ways: it excludes open sets in
the smooth full-dimensional 24-cell stratum, proves a singular
pair-terminal point has a q-regular analytic deformation into that stratum,
and replaces an invalid 24-direction Hessian quotient by the correct
affine/projective Schur test.

## 2026-07-24 — harmonic slack obstruction and projective-radical stress

### Scope and independent review

Worked on branch
`problem/mahler-volume-4d/2026-07-24-slack-stress-gap`, inside this problem
folder plus the generated board. Three independent agents attacked the
slack/Hodge route, the constrained incidence Hessian, and route selection.
GPT-5.6 Sol at xhigh effort selected the global trace route over a
sign-free stress-dimension argument and independently audited the exact
mass and KKT formulas. No agent edited repository files.

### Exact constrained Hessian and projective-radical lemma

For paired incidences \(F_{vF}=x_v\cdot y_F-1\), implemented the exact
paired volume gradient and solved

\[
\nabla(\log|P|+\log|P^\circ|)=J^\mathsf T\lambda.
\]

If \(H_0\) is the straight ambient Santaló-envelope Hessian, the actual
second derivative on a second-liftable tangent is

\[
Q_\lambda(u)=H_0(u)-2q_\lambda(u).
\]

The acceleration disappears through \(Jz''=-2c(u,u)\), and multiplier
ambiguity disappears on the stress cone. A new coordinate-free lemma proves
that every self-stress quadric has the full 24-dimensional PGL tangent in
its bilinear radical. Thus integrability descends modulo PGL, even though
only 20 affine directions are Mahler gauges.

At the regular 24-cell, the deterministic exact multiplier has 120 nonzero
entries, global sum four, and range \([-7/48,7/48]\). Exact polarization on
the four denominator-projective and four Paffenholz directions gives

\[
A=-31I_4/13,\qquad B=-31I_4/78,\qquad C=-61I_4/234.
\]

The nonzero mixed block is a concrete certificate that discarding all 24
projective directions changes the realization Hessian.

### Spanning the singular stress cone

Derived the second-fundamental spanning criterion for a homogeneous
quadratic map \(q:V\to W\). At a regular zero \(u\), if

\[
\operatorname{span}\{q(v):v\in\ker Dq_u\}=W,
\]

then the local regular zero germ spans \(V\). At the rational singular
Paffenholz cell, \(\dim V=50\), \(\dim W=2\),
\(\dim\ker Dq_u=48\), and the exact quadratic outputs have rank two.
Therefore nearby q-regular integrable directions span all 50 tangent
dimensions. This closes the KKT-existence gap at that singularity for a
hypothetical local minimizer.

### Harmonic obstruction and corrected trace target

The naive circuit-Poincare plan fails identically. Facet-supported affine
circuits annihilate the entire polarity pairing \(N_{vF}=x_v\cdot y_F\) and
the slack matrix. At a terminal polytope these matrices are wholly in the
five-dimensional affine harmonic space, so their circuit Dirichlet energy
is zero.

The corrected exact barycentric mass identity is

\[
900\operatorname{tr}(\operatorname{cov}P\operatorname{cov}P^\circ)
=
\operatorname{tr}(\mathsf M_PN\mathsf M_{P^\circ}N^\mathsf T).
\]

For simplex cells,

\[
|\det(1-x_i\cdot y_j)|=(4!)^2|S||T|.
\]

Thus the trace gap is a global determinant-weighted energy inequality,
independent of triangulation. Pointwise control is false: in the canonical
regular-24-cell pulling triangulations, 1,784 of 5,184 blocks exceed 100
and the maximum is 344, while the weighted average is \(169/2\).

Cone-measure divergence gives the sharper boundary identity

\[
\frac14-\frac94\operatorname{tr}(
\operatorname{cov}P\operatorname{cov}P^\circ)
=
\sum_{F,v}r_Fs_v\left[
(x_v\cdot y_F)(c_F\cdot d_v)-\operatorname{tr}(H_FH_v^\circ)
\right].
\]

For the regular 24-cell the total is \(31/800\); among 576 facet pairs,
288 brackets are \(-11/100\) and 288 are \(3/16\). All 144 incidences are
positive. Hence the remaining trace theorem is a genuinely global
circuit-network transport inequality, not local facet positivity.

Beta second moments also give exact covariance-trace recursions under
products, free sums, and joins. The normalized trace defect is additive
under joins, and the segment--square join has trace \(17/162\).

### Certified trace interval and failed terminal-root attempt

Extended the rational Krawczyk certificate to the full covariance trace on
the nonregular Paffenholz bi-centering box:

\[
0.0999343391445795
<
\operatorname{tr}(\operatorname{cov}P\operatorname{cov}P^\circ)
<
0.0999343606091986
<
1/9.
\]

This remains supporting evidence because pair-terminality at the exact
irrational root is not certified. An exact terminality check at the rational
box center was attempted, but the \(10^{12}\)-scale coordinate
denominators caused rational RREF denominator explosion before the
direction-flat enumeration completed. The run was interrupted after about
90 seconds. A future certificate must transport preselected rank minors
with intervals rather than reconstruct all exact direction flats at the
large-denominator center.

### Commands and compute

```text
python3 -m py_compile problems/mahler-volume-4d/harness/*.py
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
python3 tools/board.py
```

The first full intermediate suite passed 18 exact tests in 58.394 seconds;
after caching paired geometry and Hessian values, the final suite was rerun
as recorded below. The interval certificate completed in 7.5 seconds.
Exploratory floating Paffenholz samples were used only to pressure-test the
trace conjecture; every committed identity and numerical enclosure is exact.

The full connected non-pyramidal conjecture remains open. This session
passes the continuation gate with two new general lemmas, a full
50-dimensional singular-germ classification at the Paffenholz cell, exact
join/product trace recursions, and a sharper global boundary formulation of
the remaining trace inequality.

### Same-session correction: the exact root is pair-terminal

The failed large-denominator RREF attempt above diagnosed an implementation
problem, not a mathematical obstruction. The xhigh reviewer found the
correct certificate and the main harness reproduced it exactly.

For a projective image
\(\widehat{T(x_v)}=H\hat x_v/d_v\), affine circuit coefficients transform as
\(\lambda_v=d_v\mu_v\). Hence every fixed-active-facet circuit matrix changes
only by an invertible diagonal column scaling. Terminality can fail only if
an independent set of four facet normals becomes dependent.

At the rational center of the Krawczyk box, exact normal-flat enumeration
using the transformed normals but the small-denominator reference circuit
matrices gives 1,941 primal flats and 1,911 polar flats, all of speed
dimension five. Minimal facet-circuit supports are connected on both sides:
120 primal circuits of sizes four and five, and 72 polar circuits of size
four.

Outward-rounded interval determinants over the entire radius-\(10^{-10}\)
box certify:

```text
                         nonzero   zero   unresolved
primal four-normal sets    10498    128       0
polar four-normal sets     10488    138       0
```

Both projective denominator families have strictly positive lower bounds.
Therefore no new four-normal dependency appears anywhere in the box, and
the unique Krawczyk root is an exact bi-centered connected pair-terminal
non-simplex. Its certified covariance trace is strictly below \(1/9\), so it
becomes the canonical exact test object for the remaining terminal trace
conjecture. The upgraded certificate completed successfully in about 60
seconds without any interval RREF.

Final verification after all edits: byte-compilation passed; all 18 exact
unit tests passed in 54.344 seconds; the strengthened bi-centering,
connectivity, terminality, trace, and covariance certificate passed in about
60 seconds; and the independent terminal-bridge certificate again checked
1,941 primal and 580 polar flats in 26.3 seconds.

## 2026-07-24 — cone-duality Laplacian and a degree-two terminal target

### Exact Laplace/boundary identification

For the homogenizing cone \(V\subset\mathbb R^{n+1}\), set
\[
J=\Phi_{V^*}-\Phi_V^*.
\]
Klartag's Hessian identities at a bi-centered section give
\[
\frac1{n+1}\nabla^2J
=(n+2)B-\frac1{n+2}A^{-1},
\qquad
g=\nabla^2\Phi_V^*
=\frac{n+1}{n+2}A^{-1}.
\]
Taking the entropic-metric trace yields
\[
\Delta_gJ=(n+2)^2\operatorname{tr}(AB)-n.
\]
In dimension four,
\[
\Delta_gJ=36\operatorname{tr}(AB)-4=-16D_\partial.
\]
Thus the determinant-weighted slack sum, facet-boundary deficit, and
cone-duality superharmonicity are exactly the same scalar target. The
simplex has Laplacian zero; the regular 24-cell gives \(-31/50\), matching
\(-16(31/800)\).

Conditioning the boundary formula gives a further no-go. If \(F,v\) have
independent cone-volume laws and \(U,W\) are uniform on the corresponding
facets, then with \(N=x_v\cdot y_F\) and \(Z=U\cdot W\),
\[
D_\partial=\mathbb E[Z(N-Z)].
\]
The two terms already factor to \(1/4\) and
\((9/4)\operatorname{tr}(AB)\). Merely transporting incidence and
nonincidence terms is therefore a tautological repartition unless a new
terminal inequality is supplied.

### Exact robust-support characterization

For a vertex function \(\alpha\), let \(S(\alpha)\) be the facets on which
its restriction is nonaffine. Proved
\[
P\text{ terminal}
\iff
\operatorname{span}\{y_F:F\in S(\alpha)\}=\mathbb R^4
\quad\text{for every nonaffine }\alpha.
\]
If the span is proper, a direction orthogonal to it waives every violated
facet and makes \(\alpha\) a nonaffine admissible speed. The converse is
immediate from the violated facets of an admissible speed. This is the
precise every-direction strengthening of circuit connectivity.

It still annihilates the degree-one polarity columns. The first plausible
variables are the circuit second-moment tensors
\[
Q_{F,\alpha}
=\sum_{v\in F}\alpha_vx_vx_v^\mathsf T.
\]
They are individually indefinite, so the surviving theorem must be a
coupled primal--dual Bochner positivity identity.

### Exact hypersimplex falsification

For
\[
K_m=\Delta(2,m)-\frac2m\mathbf1
\subset\{\sum_i x_i=0\},
\]
derived a closed exact trace formula. The primal covariance is obtained by
conditioning \(m\) independent uniforms on sum \(2\), using the
Irwin--Hall density
\[
f_m(2)=\frac{2^{m-1}-m}{(m-1)!}.
\]
On the polar, each \(A_{m-1}\) Weyl chamber is the simplex cut from the
fundamental-weight cone by \(y_1+y_2\leq1\). The simplex second-moment
formula then gives the polar scalar covariance exactly.

At \(m=11\), dimension ten, the result is
\[
\operatorname{tr}(
\operatorname{cov}K_{11}\operatorname{cov}K_{11}^\circ)
=\frac{51389}{738477}
=\frac5{72}+\frac{847}{5907816}
>\frac{10}{12^2}.
\]
This is an exact centered polytope satisfying Henk--Linke subspace
concentration, so concentration alone cannot prove the covariance ceiling.

At \(m=5\), the closed formula matches a completely independent exact
four-dimensional facet enumeration:
\[
\operatorname{tr}(AB)=\frac{667}{7128},\qquad
\Delta_gJ=-\frac{125}{198}.
\]
All 26 primal and 101 polar normal flats have speed dimensions in
\(\{5,6\}\), with six occurring on both sides, so the centered
hypersimplex is a nonterminal negative control.

A short Lie-group argument also proves every homogeneous pointed
polyhedral cone is simplicial. Hence equality in a future superharmonicity
theorem would already force the simplex section, provided the analytic
equality case upgrades zero Laplacian to homogeneity.

### Independent source audit and xhigh verdict

Primary sources checked:

- Klartag, arXiv:1710.08084, for the cone/Laplace Hessian formulas and the
  high-dimensional failure of Kuperberg's covariance conjecture;
- Henk--Linke, arXiv:1305.5335, for centroid-zero polytopal cone-volume
  subspace concentration and its equality case.

The GPT-5.6 Sol xhigh reviewer independently rederived the Irwin--Hall
moment, Weyl-chamber vertices and heights, simplex moment normalization,
the exact \(m=11\) fraction, both Laplacian checks, the robust-support
lemma, and the homogeneous-cone argument. It required one clarification:
the identity component is transitive because it has the same Lie algebra
orbit dimension as the full transitive automorphism group, hence open
orbits in a connected interior.

Its blunt route verdict was:

- **STOP** pairwise boundary repartition, first-degree circuits, ordinary
  Markov mixing, and subspace concentration as proof mechanisms;
- **GO** only for a degree-two terminal Bochner identity expressing
  \(-\Delta_gJ\) as a nonnegative coupled quadratic form in primal and dual
  circuit second-moment tensors, with zero forcing an affine join.

No terminality-to-superharmonicity proof was found. The full conjecture
remains open.

### Commands and compute

```text
python3 -m py_compile \
  problems/mahler-volume-4d/harness/polytope.py \
  problems/mahler-volume-4d/harness/test_polytope.py
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness \
  -p test_polytope.py -k cone_duality_defect_laplacian -v
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness \
  -p test_polytope.py -k hypersimplex -v
```

Both focused exact tests passed in under one second. An initial direct
module invocation failed with `ModuleNotFoundError: polytope` because the
harness is intentionally imported via discovery/PYTHONPATH; rerunning with
the documented discovery form passed. The full exact suite then passed:
`Ran 20 tests in 46.496s — OK`. The terminal-bridge certificate again
returned `terminal-pair-implies-simplex False`. The independent interval
certificate completed in about 95 seconds and returned
`unique-bicenter-root True`, `covariance-trace-below-one-ninth True`,
`bi-centered-root-pair-terminal True`, and
`projective-local-minimum False`.

## 2026-07-24 — robust terminal excess and exact quadratic no-go tests

The full conjecture remains open. This session attacked the connected
pair-terminal branch at the first unsolved combinatorial and analytic
gates. It produced one new infinite-subclass classification and three exact
falsifications of overly local curvature ansatzes.

### Weighted terminal-excess theorem

For a terminal non-simplex \(P\), write
\[
E=f_{03}-4f_3=\sum_F(|V(F)|-4)
\]
and let \(\beta_3\) be the maximum total excess on three nonsimplicial
facets with independent normals. The robust-support characterization of
terminality implies
\[
E\ge f_0-5+\beta_3.
\]
Indeed, erase the rank-three normal flat containing a maximizing triple.
The circuit rows outside that flat must still have rank \(f_0-5\), while
the erased flat has row capacity at least \(\beta_3\). Since the
nonsimplicial-facet normals span \(\mathbb R^4\), \(\beta_3\ge3\), and
\[
f_{03}\ge4f_3+f_0-2.
\]
Applying this to both members of a pair-terminal polar pair gives
\[
2f_{03}\ge5(f_0+f_3)-4,
\]
improving the previous constant \(-10\) to \(-4\).

Equality has rigid matroidal consequences. If
\(E=f_0-2\), every nonsimplicial facet has five vertices, its normal
matroid is \(U_{4,f_0-2}\), and the corresponding one-row circuit matroid
is \(U_{f_0-5,f_0-2}\). Equality on both sides forces
\[
f_0=f_3=n,\qquad f_{03}=5n-2,
\]
with exactly two tetrahedral facets and two simple vertices.

### Six-nonsimplicial-facet theorem

A coloop in the rank-four matroid of nonsimplicial-facet normals forces the
remaining blocks to lie in a rank-three flat. Robust erasure then makes the
coloop facet contain \(f_0-1\) vertices, so \(P\) is a pyramid.

If a terminal non-pyramid had exactly five nonsimplicial facets, their
normal matroid would be \(U_{4,5}\). Let \(\mathcal G\) be the global Gale
dependency space and \(D_i\) its subspace supported on facet \(F_i\).
Erasing any other three facets gives \(D_i+D_j=\mathcal G\). Therefore the
five vertex complements \(C_i=V(P)\setminus V(F_i)\) are pairwise
disjoint: a common vertex would give a nonzero Gale coordinate in
\(D_i^\perp\cap D_j^\perp\). Non-pyramidality gives \(|C_i|\ge2\).
Pairwise disjointness makes every vertex of \(C_i\) lie on the other four
facet hyperplanes; their normals are independent, so their common
intersection contains at most one point. Thus \(|C_i|\le1\), a
contradiction.

Hence every terminal non-pyramid has at least six nonsimplicial facets.
Dually, every pair-terminal non-pyramid also has at least six nonsimple
vertices. Together with the earlier pyramid theorem, this classifies every
terminal four-polytope with at most five nonsimplicial facets without
enumerating face lattices.

### Intrinsic quadratic data and exact falsifications

The earlier notation \(Q_{F,\alpha}\) was not intrinsic. A shadow-speed
residual is a covector in \(\operatorname{Rel}(F)^*\), whereas the
intrinsic circuit second moment is
\[
\mathcal Q_F(\gamma)=\sum_{v\in F}\gamma_vx_vx_v^\mathsf T,
\qquad\gamma\in\operatorname{Rel}(F).
\]
A positive identification between these two spaces is additional Hodge
data, not a consequence of terminality.

The direct mixed contraction is
\[
C=D_P(N\circ N)D_{P^\circ}^{\mathsf T},
\qquad
C_{\gamma,\delta}=\operatorname{tr}
(\mathcal Q_P(\gamma)\mathcal Q_{P^\circ}(\delta)).
\]
Exact ranks (primal, polar, mixed) are \(9,9,9\) for the regular 24-cell,
\(10,9,9\) for a generic Paffenholz cell, \(1,1,0\) for the
segment--square join, \(5,5,0\) for centered \(\Delta(2,5)\), and
\(6,0,0\) for the cube/cross-polytope pair. The first two zero-mixed-rank
controls have positive boundary deficits, \(1/72\) and \(125/3168\).
They are nonterminal, so this rules out only a universal identity based
solely on the unweighted mixed contractions. A terminality-dependent Hodge
operator, separate primal/dual Gram data, or a terminal-only identity
remains possible.

For a bi-centered pair, exact least-squares decomposition gives
\[
\mathbb E N^2
=\frac1{256}\operatorname{tr}((H^\circ)^{-1}H^{-1})
 \mathbb E(N-N_{\rm lin})^2,
\]
while \(N-N_{\rm lin}\) is orthogonal to every bilinear
\(U^\mathsf TTW\), including the target \(Z=U\cdot W\). Thus the raw
nonlinear regression residual cancels from the boundary deficit. At the
regular 24-cell the exact data are
\[
\operatorname{tr}(HH^\circ)=\frac{169}{800},\quad
\mathbb E N^2=\frac12,\quad
\frac1{256}\operatorname{tr}((H^\circ)^{-1}H^{-1})=\frac{50}{169},\quad
\mathbb E(N-N_{\rm lin})^2=\frac{69}{338}.
\]
This leaves the concrete sufficient target
\[
\operatorname{tr}((H^{1/2}H^\circ H^{1/2})^{-1})>64
\]
at any hypothetical non-simplex minimum.

Finally, retriangulating one fixed facet across a five-point bistellar
circuit, while holding the opposite tetrahedron and geometry fixed, leaves
the signed volume-weighted local boundary bracket unchanged. This kills
that fixed-geometry one-sided flip energy, but does not exclude geometric
or oriented two-sided flips.

### Exploratory sweeps

Exact rational evaluations were used to check candidate identities; floats
were used only to rank search directions. Twenty random centrally symmetric
rational 12-vertex examples and sixteen sampled Paffenholz parameters all
had covariance trace below \(1/9\). The best observed floating values were
approximately \(0.09188\) and \(0.10036\), respectively. These finite
samples are discovery evidence only and support no exclusion claim.

### GPT-5.6 Sol xhigh reviews

Two independent xhigh reviews were run at the classification and analytic
decision points.

- The terminal-rigidity audit returned **GO** on the weighted inequality,
  coloop lemma, five-facet contradiction, and equality matroids.
- The quadratic audit returned **STOP** on a universal unweighted
  contraction, raw residual energy, and fixed-geometry one-sided flips;
  **GO** on the robust coupling rank gate and global oriented cofactor
  transport.
- The final adversarial audit required the scope corrections now present in
  the result: the zero-coupling examples are nonterminal; regression needs
  bi-centering; a fixed-facet flip calculation does not exclude geometric
  two-sided flips; and no claim about unoriented singular values was
  justified.

The next finite gate is therefore
\[
D_P(N\circ N)D_{P^\circ}^{\mathsf T}\ne0
\]
for every connected pair-terminal non-simplex, with the sufficient
rank-sum target \(\rho(P)+\rho(P^\circ)>10\). Even that would establish
coupling, not the required sign; the full proof still needs oriented
cofactor transport.

### Commands and compute

```text
python3 -m py_compile \
  problems/mahler-volume-4d/harness/polytope.py \
  problems/mahler-volume-4d/harness/variation.py \
  problems/mahler-volume-4d/harness/test_polytope.py
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness -v
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness \
  -p test_polytope.py \
  -k terminal_excess_and_quadratic_coupling_diagnostics -v
python3 problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
python3 problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The exact suite passed `Ran 22 tests in 61.083s — OK`; after adding the
simplex and cube/cross quadratic-rank sanity assertions, the focused test
passed again in 7.095 seconds. The bridge verifier returned
`all-speed-dimensions 5` and
`terminal-pair-implies-simplex False`. The interval certificate returned
`unique-bicenter-root True`, `covariance-trace-below-one-ninth True`,
`circuit-support-connected True`, `bi-centered-root-pair-terminal True`,
and `projective-local-minimum False`. The two standalone certificates took
about 28 and 95 seconds.

## 2026-07-24 — quadratic slack flex and oriented cofactor cancellation

The full conjecture remains open. This session attacked the robust
quadratic-coupling and oriented-transport gates selected in the previous
handoff. It produced a new terminal Hilbert-rank theorem, an exact
realization-space interpretation of coupling, and a two-sided no-go for
pure cofactor transport.

### Quadratic Hilbert rank and slack tangent

For a vertex configuration \(X=(x_v)\), let
\[
\mathcal G_X=\ker[1\ X]^\mathsf T,\qquad
\mathcal Q_X(\gamma)=\sum_v\gamma_vx_vx_v^\mathsf T.
\]
Quadratic evaluation modulo affine functions is the transpose map, so
\[
\rho(P):=\operatorname{rank}\mathcal Q_X=h_{V(P)}(2)-5.
\]
For terminal \(P\), facet circuits span \(\mathcal G_X\).

The former sufficient target
\(\rho(P)+\rho(P^\circ)>10\) has the cardinality obstruction
\[
\rho(P)+\rho(P^\circ)\le f_0+f_3-10.
\]
It cannot hold when \(f_0+f_3\le20\), a range not excluded by the current
flag inequalities.

With normalized slack
\[
S=1-N=[1\ X]\operatorname{diag}(1,-I_4)[1\ Y]^\mathsf T,
\]
the rank is five. Determinantal tangent-space linear algebra gives
\[
\boxed{
D_P(N\circ N)D_{P^\circ}^\mathsf T=0
\iff
S\circ S\in T_S\{\operatorname{rank}\le5\}.
}
\]
Because \(S\circ S\) vanishes on incidences, zero coupling is exactly the
fixed-incidence infinitesimal slack flex \(\dot S=S\circ S\).

Every two-level polytope has zero coupling: each slack column takes values
\(\{0,c_F\}\), so \(S\circ S=S\operatorname{diag}(c_F)\). Terminal
non-simplex two-level exclusion is therefore a mandatory boundary case.

### Terminal quadratic rank is at least three

For each nonsimplicial facet \(F\), its quadratic circuit image is nonzero.
Otherwise all products of affine functions would again be affine on its
vertices, making the four-dimensional affine evaluation space a separating
unital algebra and hence the full function algebra.

Every local tensor kills its facet normal. Rank one is impossible because
the nonsimplicial-facet normals span \(\mathbb R^4\).

Rank two reduces to a symmetric \(4\times4\) pencil. For a regular pencil,
group normals by projective determinant roots. Corank is bounded by root
multiplicity, whose total is four. Erasing the span of every root group
except one removes a rank-at-most-three normal flat and leaves only one
pencil line, contradicting robust terminal spanning.

The identically singular case was independently audited at xhigh effort.
After quotienting the common kernel, a self-contained Schur-complement
argument shows that a common-kernel-free singular symmetric pencil in
dimension at most four has all kernel directions in a subspace of
codimension at least one. Maximal rank is \(n-1\); the Schur identity makes
one cyclic span totally isotropic; Witt index one gives a linear polynomial
kernel; and the adjugate has at most one exceptional member in dimension
four. Restoring a common kernel either puts all normals in a rank-three
flat or reduces to the regular root-erasure argument.

Consequently
\[
\boxed{\rho(P)\ge3}
\]
for every terminal non-simplex. Hence \(f_0(P)\ge8\), and a pair-terminal
non-simplex has \(f_0,f_3\ge8\).

### Exact sharpness of abstract rank data

The normal-flat axioms alone cannot improve three. For
\(\rho=3,4,5\), exact rational Vandermonde models were built from
\[
y_i=(-1)^i(1,i,i^2,i^3)
\]
and
\[
A_d(z)=B(z)^\mathsf T
\operatorname{diag}(1,-1,-(1+\cdots+z^d))B(z),
\quad d=\rho-3,
\]
where
\[
B(z)=
\begin{pmatrix}
-z&1&0&0\\
0&-z&1&0\\
0&0&-z&1
\end{pmatrix}.
\]
They have normal matroid \(U_{4,\rho+3}\), survive every rank-three-flat
erasure with full block rank, positively span by a finite-difference
identity, and have inertia \((1,2,1)\), matching a convex
triangular-bipyramid facet circuit.

These are abstract local models, not globally glued polytopes. They prove
that a stronger theorem must use the common vertex configuration. After
normalizing five vertices to \(0,e_1,\ldots,e_4\), the remaining vertices
\(z\) generate
\[
\mathcal Q_z=zz^\mathsf T-\operatorname{diag}(z).
\]

### Oriented cofactor atom and cancellation

For two six-point affine circuits,
\[
\gamma_i=(-1)^i\det U_{\widehat i},\qquad
\delta_j=(-1)^j\det W_{\widehat j}.
\]
Cauchy--Binet gives \(\operatorname{Cof}_{ij}(S)=\gamma_i\delta_j\), hence
\[
\boxed{
\left.\frac d{dt}\det(S+t(N\circ N))\right|_{t=0}
=\gamma^\mathsf T(N\circ N)\delta.
}
\]
Quadratic coupling is the first oriented cofactor response of the
rank-five slack determinant.

However, the four pieces of the \(900\)-scaled simplex moment energy have
double-circuit residues
\[
C,\quad-C,\quad-C,\quad C.
\]
Thus the full energy cancels as
\[
\boxed{C-C-C+C=0.}
\]
Pure one-sided or simultaneous Cauchy--Binet/Plucker retriangulation is a
valuation tautology. A successful Hodge/Green operator must introduce
terminality-dependent nonlocal weights before these terms are combined.

At the regular 24-cell, the exact circuit pair
\[
I=(0,1,2,4,8,15),\qquad J=(0,1,2,3,6,12)
\]
gives coupling and determinant derivative \(-16\), component residues
\((-16,16,16,-16)\), and total energy residue zero.

### Exploratory falsification

An exact Gale search sampled 50,000 rational seven-vertex configurations.
Only one passed the necessary six-nonsimplicial-facet and six-nonsimple-
vertex screen; its primal maximum shadow-speed dimension was six while its
polar maximum was five. This is finite discovery evidence only; the
theorem \(f_0\ge8\) comes from the pencil proof.

A possible inverse-covariance trace inequality was pressure-tested but not
adopted. Ten exact centrally symmetric rational ten-vertex bodies had
\[
\operatorname{tr}
\bigl((\operatorname{cov}P\operatorname{cov}P^\circ)^{-1}\bigr)
\in[176.53,177.86],
\]
above the homogeneous value \(144\). No proof or counterexample was found,
and this observation supports no claim.

### GPT-5.6 Sol xhigh verdict

The independent reviewer approved the Hilbert-function and slack-tangent
identities, identified the small-cardinality obstruction to rank-sum,
audited the regular-pencil proof, and replaced an initial Kronecker appeal
with the self-contained singular-pencil lemma above. Its route verdict was:

- **STOP** rank-sum as a prerequisite and pure oriented Plucker transport;
- **GO** global low-Hilbert/Veronese gluing, terminal two-level exclusion,
  and terminality-dependent nonlocal Hodge/Green weighting.

### Commands and compute

```text
python3 -m py_compile \
  problems/mahler-volume-4d/harness/variation.py \
  problems/mahler-volume-4d/harness/test_polytope.py
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness \
  -p test_polytope.py -k quadratic -v
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness -v
python3 problems/mahler-volume-4d/harness/verify_bridge_counterexample.py
python3 problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The three focused quadratic tests passed in 9.064 seconds. The full exact
suite passed `Ran 24 tests in 64.719s — OK`. The bridge certificate again
returned `all-speed-dimensions 5` and
`terminal-pair-implies-simplex False`. The interval certificate returned
`unique-bicenter-root True`, `covariance-trace-below-one-ninth True`,
`circuit-support-connected True`, `bi-centered-root-pair-terminal True`,
and `projective-local-minimum False`.

### Final xhigh proof audit and scope correction

A second GPT-5.6 Sol xhigh pass returned **STOP as written / GO after
narrow corrections**. The reviewer found no counterexample to
\(\rho(P)\ge3\), but required the singular-pencil proof to expose:

- the explicit kernel vector
  \(k(s,t)=se+tu\), with \(e=(0,1)\), \(u=(-H^{-1}d,\alpha)\);
- the primitive polynomial-kernel argument
  \(\operatorname{adj}P=p\,kk^\mathsf T\);
- the rank-one exceptional-member derivative certificate; and
- the dimension count after restoring the common kernel.

Those details are now written out in
`results/quadratic-slack-cofactor.md`. The audit also caught two
overstatements. First, \(\dot S=S\circ S\) is only a fixed-support
Zariski tangent; no integrating rank-five slack curve is claimed. Second,
the exact \(C-C-C+C\) calculation kills the displayed uniform barycentric
cofactor residues, not every possible geometry-dependent, nonlinear, or
nonlocal Plucker weighting. The result note, report, handoff, and
learnings were narrowed accordingly.

An independent exploratory pass identified the next concrete two-level
target:

> If \(P\) is a connected terminal non-simplex two-level four-polytope,
> then \(\rho(P)=6\).

This Boolean--Veronese saturation lemma survives the simplex, join,
cube/cross-polytope, regular-24-cell, and \(\Delta(2,5)\) pressure tests.
On both sides it would contradict the ten-dimensional trace pairing under
zero coupling, forcing every pair-terminal two-level body into the solved
join branch. It remains a conjectural next lemma, not a result of this
session.

The final exact rerun passed `Ran 24 tests in 64.401s — OK`; both standalone
certificates and Python compilation also passed. After the corrections, the
same xhigh reviewer returned **GO — no remaining exact issue**.

## 2026-07-24 — complete two-level boundary and cone-volume Green diagnostic

### Boolean saturation falsified, then replaced

The proposed next lemma
\[
P\text{ terminal, connected, two-level, non-simplex}
\Longrightarrow \rho(P)=6
\]
is false. The exact counterexample is
\(\Delta_2\times\Delta_2\): it is terminal, has connected rectangle-circuit
support, and has \(\rho=4\). Its polar is simplicial and nonsimplex, hence
nonterminal, and its Mahler product is the already-separated
\(243/32>3125/576\).

The matrix proof generalizes: for \(p,q\ge2\), a speed on
\(\Delta_p\times\Delta_q\) is a \((p+1)\times(q+1)\) matrix. Global affine
speeds are exactly row-plus-column matrices. Every nonadditive matrix
violates enough delete-row and delete-column facets to span the two
complementary normal factors. Thus
\[
\Delta_p\times\Delta_q\text{ is terminal},\qquad
\rho(\Delta_p\times\Delta_q)=pq.
\]

### Structural simple-vertex theorem

If a terminal two-level 4-polytope has a simple vertex, its incident-facet
slacks give Boolean coordinates containing \(0,e_1,\ldots,e_4\). Every
remaining facet is a clique inequality, so the polytope is the stable-set
polytope of a graph \(G\) on four vertices.

For a nonedge \(ij\), the globally nonaffine speed \(x_ix_j\) and the
robust-support criterion force both
\[
N(i)\setminus N(j)\ne\varnothing,\qquad
N(j)\setminus N(i)\ne\varnothing.
\]
A direct four-vertex graph argument gives only \(G=K_4\) or \(G=2K_2\).
Hence the only terminal simple-vertex two-level types are
\(\Delta_4\) and \(\Delta_2\times\Delta_2\).

### Exact completion of all two-level types

Bohn--Faenza--Fiorini--Fisikopoulos--Macchia--Pashkovich prove that affine
and combinatorial equivalence agree for two-level polytopes and that there
are exactly nineteen affine types in dimension four, eleven with a simple
vertex. An independent exact Boolean audit reproduced the boundary:

```text
nonempty Boolean subsets                 65535
cube-symmetry orbits                       401
full-dimensional representatives           347
two-level presentations                     100
distinct strong incidence signatures         19
simple-vertex types                           11
no-simple-vertex types                         8
```

For each of the remaining eight types, the harness records a Boolean
representative, a squarefree quadratic speed \(x_ix_j\), and a nonzero
rational direction perpendicular to every violated facet normal. The
violated-normal ranks are \(1,0,1,2,3,0,0,1\), respectively; every speed
is exactly globally nonaffine and admissible in its displayed direction.
Therefore
\[
\boxed{P\text{ terminal and two-level}
\Longrightarrow P\simeq\Delta_4\text{ or }\Delta_2\times\Delta_2.}
\]
Since the latter polar is nonterminal, every pair-terminal two-level
4-polytope is a simplex. This closes the full two-level minimizer branch.

### Cone-volume Green energy

For normalized dual/primal cone-volume laws \(\mu,\nu\), complete
affine-dependency bases \(D,E\), and
\[
K=D\operatorname{diag}(\mu)^{-1}D^\mathsf T,\quad
L=E\operatorname{diag}(\nu)^{-1}E^\mathsf T,\quad
C=D(S\circ S)E^\mathsf T,
\]
define
\[
\mathcal G_{\rm cv}
=\operatorname{tr}(K^{-1}CL^{-1}C^\mathsf T).
\]
Exact algebra identifies this with the product-weighted squared norm of
the doubly affine-regressed \(S\circ S\), or the Hilbert--Schmidt overlap
of primal and polar residual-quadratic covariance operators. It is
basis-, relabeling-, and \(GL(4)\)-invariant, nonnegative, and zero exactly
when the mixed quadratic coupling vanishes.

The harness gives
\[
\mathcal G_{\rm cv}(\text{regular 24-cell})=\frac14,\qquad
D_\partial=\frac{31}{800},\qquad
\frac{D_\partial}{\mathcal G_{\rm cv}}=\frac{31}{200},
\]
and \(\mathcal G_{\rm cv}=0\) on the segment--square join and centered
\(\Delta(2,5)\). High-precision bi-centered Paffenholz tests numerically
violate the candidate constants \(31/200,1/8,1/10\), with a smallest
recorded ratio about \(0.096765\). These are discovery-level witnesses,
not interval certificates. The scalar energy is therefore retained only
as a diagnostic; the proof route needs signed/anisotropic or
configuration-dependent terminal data.

### Independent xhigh audits

GPT-5.6 Sol at xhigh effort returned **GO** on the simple-vertex theorem and
on the classification-backed completion, conditional on the exact
representative matching and speed certificates supplied by the harness.
It independently checked the graph witnesses and the terminality proof for
\(\Delta_2\times\Delta_2\).

A separate xhigh audit returned **GO** on every Green identity, verified
the weighted-projection expansion and a nonorthogonal rational
\(GL(4)\)-transform, and reproduced the numerical Paffenholz ratio. Its
route verdict was **STOP** for a universal positive scalar comparison and
conditional **GO** only as a secondary mixed-coupling diagnostic.

### Commands and compute

```text
python3 -m unittest discover \
  -s problems/mahler-volume-4d/harness -v
```

The final full exact suite passed `Ran 27 tests in 61.527s — OK`. Focused
two-level and Green tests had already passed independently. The Boolean
orbit sweep used exact rational affine ranks and incidence signatures; it
was a certificate-discovery and completeness cross-check, not a substitute
for the published nineteen-type theorem. No face-lattice enumeration was
used in the proof of the simple-vertex subclass.

The full four-dimensional conjecture remains open. The surviving connected
pair-terminal branch is necessarily non-two-level. Its two concrete proof
surfaces are global simultaneous Veronese gluing for
\(zz^\mathsf T-\operatorname{diag}(z)\), especially when
\(f_0+f_3\le20\), and a terminality-dependent signed/anisotropic transport
operator that retains information lost by the scalar Green energy.
