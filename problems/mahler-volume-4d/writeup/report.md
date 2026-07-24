# Four-dimensional Mahler volume conjecture: terminality fails, second variation survives

**Status:** partial results · **Date:** 2026-07-24

**Problem:** Prove \(\mathcal P(K)=|K|\,|(K-s(K))^\circ|\ge3125/576\)
for every \(K\subset\mathbb R^4\), with equality only for simplices.

## Abstract

We independently audited the 2026 three-dimensional shadow-flow proof and
proved that bounded-vertex 4D Mahler minimizers and their Santaló polars are
terminal. The proposed classification bridge is nevertheless false: an
exact rational non-simplex 24-cell and its genuine Santaló polar are both
terminal in every direction. We replace terminality by a stronger
variational stack. Rational interval Newton isolates a unique bi-centered
representative in a nonregular 24-cell chart, and an exact covariance bound
proves it is a projective saddle. This excludes an open critical branch of
non-pyramidal 24-cells. The earlier sharp theorem for all 4-pyramids remains.
The full four-dimensional conjecture is not proved.

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

## Result

### Theorem 1: all 4-pyramids

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

### Theorem 2: terminal subclasses

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

## Verification

Run:

```text
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
```

Expected: ten tests pass. The harness uses rational arithmetic only. It checks
the centered simplex's polar, incidences, speed dimension, and exact product
\(3125/576\); verifies cube/cross-polytope polarity; and supplies negative
speed controls for the cross-polytope, cube, and pyramid over a cube.

The two substantive certificates are:

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/verify_bridge_counterexample.py

PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The first uses exact fractions. The second uses outward-rounded dyadic
rational intervals; its Krawczyk inclusion and negative covariance bound are
checked, not inferred from the floating-point discovery run.

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
projective polar sign, and the covariance pivot. The reviewer caught that
terminality at nearby rational points does not certify terminality at the
exact bi-centering root; no such claim is made here.

## What we tried that didn't work

Generic-direction rigidity is misleading: the 4-cube has only five admissible
speeds generically but gains nontrivial speeds in facet-parallel directions.
More decisively, even exact every-direction pair-terminality does not imply a
simplex. Incidence alone is insufficient because affine-dependence
coefficients vary with the realization. The next route must study the full
Mahler Hessian on realization-space variations, not enumerate terminal face
lattices.

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
