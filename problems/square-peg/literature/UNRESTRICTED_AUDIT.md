# Unrestricted Square Peg audit — 2026-07-24

## Current boundary

The unrestricted Square Peg conjecture remains open as of 2026-07-24.
Greene--Lobb explicitly say so in arXiv:2604.17116.  Their new result gives a
positive-measure set of rectangle angles for every Jordan curve, but does not
force the square angle.

Asano--Ike v3, arXiv:2412.21057, contains a sharper reduction than the
earlier campaign notes recorded:

- Remark 5.5 proves every positive-planar-measure Jordan trace inscribes every
  prescribed rectangle by Lebesgue density.
- For a null trace, the proof of Theorem 1.1 uses Schoenflies and
  Oxtoby--Ulam to obtain a compactly supported area-preserving/Hamiltonian
  homeomorphism taking the circle to the curve.
- Remark 5.7 says the universal rectangular-peg problem would follow from
  the diagonal cohomology vanishing in Remark 4.2 for null traces.

Therefore the unrestricted problem reduces to null traces, but null trace is
not itself the missing microlocal vanishing statement.

## Floer midpoint audit

For a smooth curve of enclosed area \(A\), Greene--Lobb have two spectral
invariants \(\ell_1,\ell_2\).  Their duality is
\[
\ell_1(\gamma,\theta)+\ell_2(\gamma,\pi-\theta)=A.
\]
The 2026 triangle inequality is for the top invariant \(\ell_2\):
\[
\ell_2(\theta_1+\theta_2)
\leq\ell_2(\theta_1)+\ell_2(\theta_2).
\]
At the square angle this gives only
\[
\ell_2(\pi/2)\geq A/2,\qquad
\ell_1(\pi/2)=A-\ell_2(\pi/2)\leq A/2.
\]
The self-duality at \(\pi/2\) exchanges degrees \(1\) and \(2\); it does not
identify them.  There is no corresponding \(\ell_1*\ell_1\) triangle
inequality.  Thus the available axioms permit
\(\ell_2(\pi/2)\to A\) and \(\ell_1(\pi/2)\to0\), exactly the two action
endpoints compatible with shrink-out.

Greene--Lobb's no-shrinkout Lemma 5.1 controls projected capping loops modulo
\(A\).  Those loops may be self-intersecting.  Bounded length controls their
signed areas; null support measure does not, since
\[
\int_Lx\,dy=\int_{\mathbb R^2}\operatorname{Wind}(L,z)\,dz
\]
and the winding multiplicity can diverge inside a shrinking disk.

## Approximation audit

Oh (arXiv:math/0601183) and Sikorav show that area-preserving homeomorphisms
of a surface can be approximated uniformly by area-preserving
diffeomorphisms.  In the plane, compactly supported symplectic
diffeomorphisms are Hamiltonian.  These results control maps, not their
action potentials.

The shrinking radial twist
\[
(r,\theta)\mapsto(r,\theta+\alpha_n(r))
\]
with \(N_n\asymp\rho_n^{-2}\) turns in a disk of radius \(\rho_n\) is
\(C^0\)-small but has order-one action oscillation.  The explicit null double
spiral in `../results/null-spiral-no-primitive.md` strengthens this from a
full-disk warning to a boundary theorem: for that Jordan curve no
parameter-aligned smooth approximation can have convergent boundary
primitives.

Accordingly, a universal “action-controlled conservative smoothing” theorem
strong enough to imply Asano--Ike Theorem 1.1 is false.

## Novelty boundary

Targeted searches for combinations of Jordan curves, Liouville/area
primitives, smooth approximation, and spiral obstructions found no explicit
version of the local action-rigidity lemma or the null double-spiral
counterexample.  Search indexing is incomplete, and no priority claim is
made.  The safe description is:

> an explicit campaign counterexample showing that Asano--Ike's
> primitive-approximation sufficient condition is not universal.

It does not disprove their weaker Remark 4.2 criterion and does not provide a
counterexample to Square Peg.

## Primary sources

- T. Asano and Y. Ike, *The rectifiable rectangular peg problem*,
  arXiv:2412.21057v3, especially Theorem 4.1 and Remarks 4.2, 5.5--5.7.
- J. E. Greene and A. Lobb, *Floer homology and square pegs*,
  arXiv:2404.05179v2, especially Lemma 5.1.
- J. E. Greene and A. Lobb, *Square pegs between two graphs*,
  arXiv:2407.07798, Theorem 1.1 and Proposition 2.4.
- J. E. Greene and A. Lobb, *Jordan curves inscribe a positive measure of
  rectangles*, arXiv:2604.17116, Theorem A and Section 2.
- Y.-G. Oh, *\(C^0\)-coerciveness of Moser's problem and smoothing area
  preserving homeomorphisms*, arXiv:math/0601183.
