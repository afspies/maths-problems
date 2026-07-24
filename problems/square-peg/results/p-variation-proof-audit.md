# Adversarial audit of the finite-\(p\)-variation bridge

**Audit date:** 2026-07-24  
**Audited claim:** every Jordan parametrization of finite \(p\)-variation,
\(1\leq p<2\), satisfies Asano--Ike Theorem 1.1 and hence inscribes every
prescribed rectangle.  
**Verdict:** **MERGE.**  After the narrowly scoped \(C^1\)-rounding repair
described below, I found no remaining proof gap.

## Primary sources checked

1. T. Asano and Y. Ike, *The rectifiable rectangular peg problem*,
   [arXiv:2412.21057v3](https://arxiv.org/pdf/2412.21057v3), especially
   Theorem 1.1 (PDF pp. 2--3), its proof and Remark 5.6 (PDF p. 25).
2. H. Boedihardjo and X. Geng, *Simple Piecewise Geodesic Interpolation of
   Simple and Jordan Curves with Applications*,
   [arXiv:1309.1576v2](https://arxiv.org/pdf/1309.1576v2), especially
   Theorem 2.2 (PDF pp. 7--11), Theorem 3.1 and Lemma 3.1
   (PDF pp. 12--13).

The audit uses the theorem statements and proofs in those versions, not a
secondary summary.

## Checkpoint verdicts

### 1. Asano--Ike hypotheses and conclusion: PASS

Asano--Ike Theorem 1.1 starts with a Jordan map
\(c:S^1\to\mathbb R^2\) and a sequence
\(c_n:S^1\to\mathbb R^2\) of smooth Jordan curves.  Its two assumptions are:

1. \(c_n\to c\) in the \(C^0\) sense; and
2. for a primitive \(f_n\) of
   \((c_n\circ e)^*\lambda\) on the universal cover
   \(e:\mathbb R\to S^1\), the \(f_n\) converge locally uniformly on
   \(\mathbb R\) to a continuous function.

The theorem concludes that the image inscribes a \(\theta\)-rectangle for
every \(\theta\in(0,\pi)\).  The paper's Lagrangian-intersection formulation
uses four distinct points for an off-diagonal intersection, so
\(\theta=\pi/2\) gives a nondegenerate square, not merely a collapsed one.

The bridge proves the stronger, parameter-aligned form of \(C^0\) convergence:
the approximants converge uniformly as maps on the original parameter circle.
No inference from Hausdorff convergence is used.  Asano--Ike Remark 5.6
explicitly permits \(C^1\), rather than smooth, approximating Jordan curves.

### 2. Embedded polygonal interpolation and parameter alignment: PASS

Boedihardjo--Geng Theorem 2.2 applies to a parametrized Jordan curve on a
closed interval.  For every requested mesh bound it produces a partition for
which the piecewise minimizing-geodesic interpolation is itself Jordan; in
\(\mathbb R^2\) this is the affine polygonal interpolant.  The vertices occur
at the original parameter times.  The theorem also permits finitely many
parameter times to be prescribed in advance, although that strengthening is
not needed here.

Their Lemma 3.1(2), applied with the identity Lipschitz map, says that for a
finite-\(p\)-variation path and any \(q>p\),
\[
 \|c^{P}-c\|_{q\text{-var}}\longrightarrow0
 \quad\text{as }\operatorname{mesh}(P)\longrightarrow0.
\]
It applies to the particular embedded partitions supplied by Theorem 2.2,
not only to a separately selected interpolation sequence.  Thus
lines 32--40 of the bridge correctly give embedded, parameter-aligned
polygons and convergence in \(q\)-variation.

For \(p=1\), the text's reduction to any \(p_0\in(1,q)\) is valid because
finite \(1\)-variation implies finite \(p_0\)-variation.  Alternatively this
case is already Asano--Ike's rectifiable corollary.

### 3. Cyclic smoothing while retaining embeddedness: PASS AFTER REPAIR

The original version claimed a relative \(C^\infty\) corner rounding but only
sketched the jet-matching construction.  That claim is unnecessary because
Asano--Ike Remark 5.6 accepts \(C^1\) approximants.  The proof has therefore
been narrowed to a relative regular-\(C^1\) rounding:

- all vertex neighborhoods, including the cyclic seam, are pairwise disjoint
  disks meeting the polygon only in the two incident terminal subsegments;
- a noncollinear corner is replaced by a tangential fillet in the empty local
  sector, parameterized on the same preimage interval with matching endpoint
  velocities;
- a positive-collinear speed jump is repaired on the same straight image by a
  positive \(C^1\) speed with the prescribed endpoint speeds and integral;
- negative-collinear incident directions would retrace an interval and cannot
  occur in a Jordan polygon; and
- if \(\ell_j\) is the length removed at vertex \(j\), the local bound
  \[
  \operatorname{Var}(b-a;I_j)
  \leq \operatorname{len}(b|_{I_j})+
       \operatorname{len}(a|_{I_j})
  \leq (K+1)\ell_j
  \]
  makes the total \(1\)-variation error arbitrarily small.

Because there are finitely many vertices for each polygon, the disks can be
shrunk until both their maximum diameter and
\(\sum_j\ell_j\) are arbitrarily small.  The local replacements are simple,
lie in disjoint disks, and meet the unchanged polygon only at their endpoints;
therefore embeddedness is preserved.  Matching endpoint velocities, including
at the seam, makes the result a regular \(C^1\) embedding on \(S^1\).

This repair appears at lines 46--110 of
`angles/p-variation/README.md`.  It removes the only under-justified step I
found; it does not change the theorem or the analytic argument.

### 4. Passage from \(1\)-variation error to \(q\)-variation: PASS

For every path \(h\) and \(q\geq1\),
\(\|h\|_{q\text{-var}}\leq\|h\|_{1\text{-var}}\).
Consequently the repaired rounding gives
\(\|b_n-a_n\|_{q\text{-var}}\to0\).  The triangle inequality for the
\(q\)-variation seminorm and the Boedihardjo--Geng convergence then give
\[
 \|b_n-c\|_{q\text{-var}}\to0
\]
and a uniform bound on the coordinate \(q\)-variation norms.  Uniform
convergence also follows (and is independently included in the rounding
bound).

### 5. Young-integral stability estimate: PASS

Take \(p<q<2\).  The Young condition is \(2/q>1\).  Subtracting the two
Liouville integrals gives
\[
 \int_0^t(u^2-v^2)\,du^1+
 \int_0^t v^2\,d(u^1-v^1).
\]
The Young--Loeve estimate for each term, with the basepoint increments retained,
is exactly the four-term bound in lines 122--142 of the bridge, with the safe
constant \(2\zeta(2/q)\) used by Boedihardjo--Geng.  Restricting a
\(q\)-variation norm to \([0,t]\) cannot increase it, so the estimate is
uniform in \(t\in[0,T]\).

Since \(b_n\to c\) in \(q\)-variation, the coordinate variation differences
and basepoint differences tend to zero while the other variation norms remain
bounded.  Hence
\[
 \sup_{0\leq t\leq T}\left|
 \int_0^t y_n\,dx_n-\int_0^t y\,dx
 \right|\longrightarrow0.
\]
For a \(C^1\) approximant, its ordinary pullback primitive agrees with this
Young integral, so these are the primitives required by Asano--Ike.

### 6. Additive normalization and local-uniform extension: PASS

Primitives on \(\mathbb R\) are determined up to constants.  Choosing
\(F_n(0)=0\) is allowed and supplies a convergent normalization.  Periodicity
of \(b_n\) gives
\[
 F_n(t+kT)=F_n(t)+kF_n(T)
\]
for every integer \(k\), and the same identity holds for the Young primitive
of \(c\).  Uniform convergence on \([0,T]\), including convergence of the
period integrals \(F_n(T)\), therefore gives uniform convergence on every
compact interval of \(\mathbb R\).  This is exactly condition (2), not merely
convergence of total enclosed areas.

No area-\(\pi\) normalization is missing from the theorem's hypotheses.
Asano--Ike introduce that scaling inside their proof; their proof observes
that the approximating enclosed areas converge and rescales by factors tending
to one.

### 7. Final implication: PASS

The repaired \(b_n\) satisfy the \(C^1\) version of both Asano--Ike hypotheses.
Theorem 1.1 therefore supplies a \(\theta\)-rectangle for every
\(\theta\in(0,\pi)\); selecting \(\theta=\pi/2\) supplies a nondegenerate
square.  Nothing from the Greene--Lobb shrink-out argument is additionally
required for this implication.

## Remaining gaps and claim boundary

**Proof gaps:** none found.

**Not established by this audit:** publication priority or expert-community
novelty.  The result is a short corollary obtained by composing two published
theorems with an elementary relative \(C^1\)-rounding and Young stability
argument.  It should continue to be described as a concise synthesis unless a
separate priority review supports a stronger claim.

## Blunt gate verdict

**MERGE.**  The finite-\(p\)-variation theorem is logically complete under the
cited primary-source results.  The former \(C^\infty\)-rounding sketch has
been replaced by the sufficient and justified \(C^1\) construction.  There
are no remaining mathematical blockers in the bridge itself.
