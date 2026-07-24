# Four-dimensional Mahler volume conjecture: sharp reducible families and exact realization descent

**Status:** partial results · **Date:** 2026-07-24

**Problem:** Prove \(\mathcal P(K)=|K|\,|(K-s(K))^\circ|\ge3125/576\)
for every \(K\subset\mathbb R^4\), with equality only for simplices.

## Abstract

We independently audited the 2026 three-dimensional shadow-flow proof and
proved that bounded-vertex 4D Mahler minimizers and their Santaló polars are
terminal. The proposed classification bridge is nevertheless false: an
exact rational non-simplex 24-cell and its genuine Santaló polar are both
terminal in every direction. We prove exact Mahler factorizations for
products, free sums, and affine joins. These settle every 4D affine join,
including the non-pyramidal \(1+2\) split, and give strict gaps for all
products and free sums. An exact Santaló-envelope Hessian is
\(-61I_4/234\) on the Paffenholz realization chart at the regular 24-cell;
an independent interval certificate excludes a second nonregular critical
branch. Exact covariance formulas now exclude eight full-rank signed
24-cell curves, while a q-regular stress-cone velocity integrates the
singular pair-terminal counterexample into an open smooth family whose
bi-centered representatives remain projective saddles. The full
four-dimensional conjecture is not proved.

## Principal negative result

### Theorem 0: the terminal-pair bridge is false

There exists a rational non-simplex 4-polytope \(Q\) with \(s(Q)=0\) such
that both \(Q\) and \(Q^\circ\) admit only globally affine admissible shadow
speeds in every direction.

Take the Paffenholz 24-cell realization with
\(a=(1/5,2/5,3/5,4/5)\), set \(g=c(P_0^\circ)\), and define
\[
Q=\{x/(1-g\cdot x):x\in P_0\}.
\]
Then \(Q^\circ=P_0^\circ-g\), so the ordinary polar is exactly the Santaló
polar. Exhausting all facet-normal flats gives 1,941 primal cases and 580
polar cases; every speed space has dimension five. Pulling moments are
independently reproduced by a boundary-facet cone triangulation.

This does not contradict Mahler: \(c(Q)\ne0\), so \(Q\) fails a first-order
necessary condition for local minimality.

### Theorem 0.1: a certified 24-cell projective saddle

A local minimizer in Santaló position is bi-centered. Moreover, in dimension
four it satisfies the Klartag projective second-order inequality
\[
\operatorname{cov}(K^\circ)\succeq
\frac1{36}\operatorname{cov}(K)^{-1}.
\]

For the Paffenholz realization above, a rational interval Krawczyk
certificate isolates a unique bi-centering translation in a box of radius
\(10^{-10}\). Throughout that box,
\[
e_1^\mathsf T\left(
\operatorname{cov}(K^\circ)-\frac1{36}\operatorname{cov}(K)^{-1}
\right)e_1<-0.0075809.
\]
Thus the exact critical representative is a saddle. Nonsingularity of the
centroid Jacobian and strictness of the inequality exclude an open
four-parameter critical branch of nonregular 24-cells from local minimality.

### Theorem 0.2: smooth full-rank 24-cell exclusions

For each of Rastanawi--Sinn--Ziegler's eight signed 24-cell families, put
\(r=x^2\), \(0\le x<1\). Direct pyramid/cap integration gives
\[
\mathcal P(K_x)=\frac{16(3+r)}{3(1+r)}
\]
and scalar covariances
\[
a(r)=\frac{13+22r+5r^2}{30(1+r)^2},\qquad
b(r)=\frac{39+27r-3r^2+r^3}{240(3+r)}.
\]
The exact factorization
\[
\frac1{36}-a(r)b(r)
=\frac{
93+191r+250r^2+118r^3-7r^4-5r^5
}{7200(1+r)^2(3+r)}
>0
\]
excludes every parameter by projective second variation. For
\(0<x<1\), the incidence Jacobian has full rank 144, so continuity excludes
open subsets of the smooth 48-dimensional realization stratum.

## Sharp infinite families

### Theorem 1: every four-dimensional affine join

Every four-dimensional affine join \(K*L\) satisfies
\[
\mathcal P(K*L)\ge\frac{3125}{576},
\]
with equality if and only if it is a 4-simplex.

For \(K\subset\mathbb R^p\), \(L\subset\mathbb R^q\), and
\(d=p+q+1\), two beta integrals and the Santaló height
\(\tau=(q+1)/(d+1)\) give
\[
\mathcal P(K*L)=
\left(\frac{p!q!}{d!}\right)^2
\frac{(d+1)^{d+1}}
{(p+1)^{p+1}(q+1)^{q+1}}
\mathcal P(K)\mathcal P(L).
\]
The factor exactly transports sharp simplex constants. The only
non-pyramidal four-dimensional split is \(1+2\); equality forces a segment
and a triangle, whose join is a simplex.

Likewise,
\[
\mathcal P(K\times L)=\mathcal P(K\oplus L)
=\frac{p!q!}{(p+q)!}\mathcal P(K)\mathcal P(L).
\]
Thus all \(2+2\) products and free sums have product at least \(243/32\),
and all \(1+3\) examples at least \(64/9\), both strictly above the
four-dimensional sharp constant.

### Theorem 2: all 4-pyramids

Every 4-dimensional pyramid \(P\) satisfies
\[
\mathcal P(P)\ge\frac{3125}{576},
\]
with equality if and only if \(P\) is a 4-simplex.

For a \(d\)-pyramid over a \((d-1)\)-body \(K\), polar cross-sections and the
centroid characterization of the Santaló point give the exact identity
\[
\mathcal P(\operatorname{pyr}_dK)
=\frac{(d+1)^{d+1}}{d^{d+2}}\mathcal P(K).
\]
At \(d=4\), the audited three-dimensional theorem yields the claim.

### Theorem 3: terminal subclasses

If a simplicial 4-polytope is terminal, it is a 4-simplex. If a simple
4-polytope and its dual realization are terminal, both are simplices. If a
4-pyramid and its dual realization are terminal, both are simplices.

The pyramid proof is dimensional descent:
\[
A_{(u,0)}(\operatorname{pyr}Q)
\cong A_u(Q)\oplus\mathbb R.
\]
Terminality therefore descends to the 3D base on both sides, where the audited
3D dual counting lemma forces a tetrahedron.

### Necessary incidence inequality

Every pair-terminal 4-polytope satisfies
\[
2f_{03}\ge5(f_0+f_3)-10.
\]
More precisely,
\[
\Delta\le f_{03}-f_0-4f_3+9,\qquad
\delta\le f_{03}-f_3-4f_0+9.
\]
These are necessary conditions, not a complete classification.

## Realization-space structure and second variation

Normalize paired primal/polar coordinates by
\(x_v\cdot y_F=1\) on every incidence. The linearized incidence equations
have tangent dimension
\[
4(f_0+f_3)-f_{03}+\omega,
\]
where \(\omega\) is the incidence-stress dimension. Terminality makes
facet-supported circuit spaces span the global Gale kernel. A disconnected
circuit-support graph gives an affine join, settled by Theorem 1. In the
connected branch the labeled projective stabilizer is scalar, so the
projective orbit has dimension 24 and the quotient tangent dimension is
\[
4(f_0+f_3)-f_{03}+\omega-24.
\]
This is a realization-moduli quotient. Mahler volume is invariant only under
the 20-dimensional affine subgroup; the other four projective directions
carry the covariance Hessian and cannot be discarded.

At a singular realization, a tangent \(u=(a_v,b_F)\) has a second-order lift
exactly when every incidence stress \(\lambda\) satisfies
\[
q_\lambda(u)=
\sum_{v\in F}\lambda_{vF}a_v\cdot b_F=0.
\]
If \(Dq_u\) surjects onto the stress cokernel, a blow-up
implicit-function argument integrates \(u\) to a real-analytic arc.
For the exact pair-terminal 24-cell, the harness proves
\[
u=\tau_0+\frac{659}{667}\tau_1,\qquad
q(u)=0,\qquad \operatorname{rank}Dq_u=2.
\]
This new nonprojective, non-Paffenholz arc enters the rank-144 smooth
stratum. Combining openness of terminality with the certified nonsingular
bi-centering branch and strict covariance violation excludes an open
24-dimensional moduli family of smooth pair-terminal 24-cells.

For an integrable fixed-chamber path at a bi-centered body, eliminating the
moving Santaló point subtracts
\[
\frac56\langle c'(K^\circ),
\operatorname{cov}(K^\circ)^{-1}c'(K^\circ)\rangle
\]
from the unreduced logarithmic Hessian. Exact rational second-order jets
give, on Paffenholz's four realization parameters at the regular 24-cell,
\[
\nabla^2\log\mathcal P=-\frac{61}{234}I_4.
\]
Continuity excludes an open neighborhood of the regular realization from
local Mahler minimality. This is a genuine nonprojective realization-space
descent, not merely the earlier projective covariance direction.

## Verification

Run:

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
```

Expected: fifteen tests pass. The harness uses rational arithmetic only. It checks
the centered simplex's polar, incidences, speed dimension, and exact product
\(3125/576\); verifies cube/cross-polytope polarity; and supplies negative
speed controls for the cross-polytope, cube, and pyramid over a cube.

The two standalone certificates are:

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py

PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The first uses exact fractions. The second uses outward-rounded dyadic
rational intervals; its Krawczyk inclusion and negative covariance bound are
checked, not inferred from the floating-point discovery run.

The unit suite also checks the exact product/join factors, a centered
segment--square join, the incidence tangent ranks, all 24 projective tangent
vectors, the four diagonal plus six polarized entries of the Paffenholz
realization Hessian, the smooth signed-family covariance formulas, and the
q-regular analytic-arc rank certificate.

This computation verifies the finite linear-algebra interfaces. The
infinite-family results are proofs, not extrapolations from tested examples.

## Method

For a facet \(F\), form the evaluation matrix \(E_F\) with rows \((1,x_v)\).
Admissibility is expressed intrinsically as
\[
\lambda^\mathsf T\alpha|_F=0
\quad\text{for every }\lambda\in\ker E_F^\mathsf T
\]
whenever \(F\) is not parallel to the shadow direction. This separates
combinatorial support from realization-dependent affine coefficients.

Choosing a direction parallel to a largest facet and counting the maximum
rank of these blocks gives the inequalities above. The 4D flag identity
\[
f_{03}-f_{02}+2f_2=2f_3
\]
comes from summing Euler over 3-facets and using polygonal edge links.

Independent GPT-5.6 Sol xhigh reviews checked the algebra, the repaired
dimension-free persistence proof, the exact 24-cell counterexample, the
projective polar sign, the covariance pivot, both beta factorizations, and
the realization-Hessian normalization. The reviewer caught that
terminality at nearby rational points does not certify terminality at the
exact bi-centering root; no such claim is made here.

## What we tried that didn't work

Generic-direction rigidity is misleading: the 4-cube has only five admissible
speeds generically but gains nontrivial speeds in facet-parallel directions.
More decisively, even exact every-direction pair-terminality does not imply a
simplex. Incidence alone is insufficient because affine-dependence
coefficients vary with the realization. Raw incidence-kernel vectors at a
singular realization also need not integrate. The remaining route must build
smooth realization charts and study the constrained Santaló Hessian, not
enumerate terminal face lattices.

## Relation to prior work

Chen--Li--Xi--Xu (arXiv:2605.09334v3) prove the dimension-three conjecture
using Meyer--Reisner shadow-system convexity and a specifically 3D terminal
count. Our audit verifies that the minimizer-to-terminal part extends to 4D
after replacing the printed 3D face-intersection paragraph.
Rastanawi--Sinn--Ziegler provide the 24-cell realization family. Klartag and
Balacheff--Solanes--Tzanev provide the projective covariance condition.
References and the detailed source audit are in `../literature/`.

## Cite as

See CITATION.cff in this folder (DOI is added by tools/release.py on release).
