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
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
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
