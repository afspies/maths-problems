# Priority audit: the critical \(\sigma\)-bridge

**Audit date:** 2026-07-24
**Verdict:** no explicit prior rectangular-peg statement with the
Antonelli--Young dyadic quadratic-diameter hypothesis was found.  The safe
description is **an apparently unstated critical corollary/synthesis**, not
an independent signed-area theorem.

## Exact published inputs

### Antonelli--Young

Antonelli--Young, arXiv:2605.15987v1 (15 May 2026), Theorem 1.2, define
polygonal signed area using a limit over **all** partitions whose mesh tends
to zero.  For a \(1/2\)-Hölder path \(\gamma:[0,1]\to\mathbb R^2\), they
prove that this limit exists if
\[
 \sum_{i\geq0}\sum_{j<2^i}
 \operatorname {diam}\{\gamma(j2^{-i}),
 \gamma((2j+1)2^{-i-1}),\gamma((j+1)2^{-i})\}^2<\infty.
\]
They also prove that the trace has zero \(\mathcal H^2\)-measure and identify
the signed area with the integral of winding number.  Proposition B.1 gives
a more flexible approximation theorem.

The paper's beta numbers belong to its ambient Heisenberg-map/fibre
analysis.  The directly used planar hypothesis is the dyadic
diameter-square sum above.  It should not be renamed a planar beta-number
criterion.

Appendix B also shows why mere convergence of dyadic polygon areas is too
weak: at the critical exponent a path can have convergent dyadic areas while
the all-partitions area fails to exist.

### Boedihardjo--Geng

Boedihardjo--Geng, arXiv:1309.1576v2, Theorem 2.2, give arbitrarily fine
parameter-respecting affine interpolants of a Jordan curve which are
themselves Jordan.  This is the embeddedness input; arbitrary secant
polygons or mollifications would not suffice.

### Asano--Ike

Asano--Ike, arXiv:2412.21057v3, Theorem 1.1 and Remark 5.6, turn
parameter-aligned regular \(C^1\) Jordan approximation with locally uniformly
convergent Liouville primitives into every prescribed rectangle.

## What is new in the synthesis

Antonelli--Young state a total signed-area theorem.  The missing local step is
short but not vacuous: because their convergence quantifies over every fine
partition, two prefix partitions at an arbitrary endpoint can be extended
by the same fine tail.  The tail cancels, yielding a Cauchy bound uniform in
the endpoint.  This produces the entire primitive, not just its period.

Boedihardjo--Geng then supplies embedded polygons among the partitions
already controlled by Antonelli--Young.  A diagonal fixed-parameter
\(C^1\) rounding preserves both embeddedness and the primitives.  This is
exactly Asano--Ike's criterion.

The explicit spiral-comb witness is also material: it satisfies the critical
hypothesis but has infinite \(p\)-variation for every \(p<2\), infinite
length, and no locally monotone neighborhood at its accumulation point.
Thus the corollary is not contained in the campaign's earlier
finite-\(p<2\) theorem or Asano--Ike's two named geometric corollaries.

## Searches and limitations

Searches through 2026-07-24 combined:

- `"2605.15987" "square peg"`;
- `"Antonelli" "Young" "rectangular peg"`;
- `"sigma(gamma)" "rectangular peg" Hölder Jordan`; and
- `"1/2-Hölder" "rectangular peg" Jordan`.

They returned no relevant mathematical statement combining the papers.
The source is only two months old, indexing is incomplete, and an immediate
corollary may circulate without searchable text.  Absence from these searches
is not proof of priority.  Author or expert confirmation should precede an
unqualified novelty claim.

## Recommended language

Use:

> We record an apparently unstated critical consequence of
> Antonelli--Young's all-partitions signed-area theorem, the
> Boedihardjo--Geng embedded interpolation theorem, and the Asano--Ike
> approximation criterion.

Avoid:

- “a new beta-number theorem for square pegs”;
- “the first critical rough-path solution”;
- any suggestion that all finite-\(2\)-variation Jordan curves are covered;
  or
- any suggestion that the unrestricted Square Peg conjecture is solved.
