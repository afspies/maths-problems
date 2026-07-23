# Four-dimensional Mahler volume conjecture: a proof-first first attack

**Status:** partial results · **Date:** 2026-07-23

**Problem:** Prove \(\mathcal P(K)=|K|\,|(K-s(K))^\circ|\ge3125/576\)
for every \(K\subset\mathbb R^4\), with equality only for simplices.

## Abstract

We independently audited the 2026 three-dimensional shadow-flow proof and
isolated its only dimension-specific bridge. A short replacement proves that
bounded-vertex 4D Mahler minimizers and their Santaló polars are terminal:
they admit only globally affine admissible speeds. We derive a necessary
pair-terminality inequality, classify the simple, simplicial, and pyramid
subclasses, and prove the sharp Mahler inequality directly for every
4-dimensional pyramid. Exact rational tests verify the incidence and
speed-space formulas on standard 4-polytopes. The full non-pyramidal terminal
classification, and hence the full 4D conjecture, remain open.

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

Expected: six tests pass. The harness uses rational arithmetic only. It checks
the centered simplex's polar, incidences, speed dimension, and exact product
\(3125/576\); verifies cube/cross-polytope polarity; and supplies negative
speed controls for the cross-polytope, cube, and pyramid over a cube.

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

An independent GPT-5.6 Sol xhigh review checked the algebra, the repaired
dimension-free persistence proof, and the pyramid descent. It agreed that the
partial theorems are sound and that the current flag inequalities do not
settle the general bridge.

## What we tried that didn't work

Generic-direction rigidity is misleading: the 4-cube has only five admissible
speeds generically but gains nontrivial speeds in facet-parallel directions.
Also, incidence alone is insufficient because affine-dependence coefficients
vary with the realization. The present rank count leaves substantial slack
for non-simple, non-simplicial, non-pyramidal 4-polytopes.

## Relation to prior work

Chen--Li--Xi--Xu (arXiv:2605.09334v3) prove the dimension-three conjecture
using Meyer--Reisner shadow-system convexity and a specifically 3D terminal
count. Our audit verifies that the minimizer-to-terminal part extends to 4D
after replacing the printed 3D face-intersection paragraph. The terminal
classification remains the new 4D obstacle. References and the detailed
source audit are in `../literature/`.

## Cite as

See CITATION.cff in this folder (DOI is added by tools/release.py on release).
