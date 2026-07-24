# Rectangular pegs from Young-regular Jordan curves

**Status:** partial result; the unrestricted Square Peg conjecture remains
open.

## Abstract

We combine Asano--Ike's 2026 smooth-approximation criterion with
Boedihardjo--Geng's parameter-respecting Jordan polygon interpolation and
Young integration.  Every Jordan parametrization of finite \(p\)-variation
for some \(p<2\) satisfies the criterion and hence inscribes every prescribed
rectangle.  The same proof works at the critical scale under the coordinate
Dini condition
\[
\int_0^1\omega_x(r)\omega_y(r)r^{-2}\,dr<\infty.
\]
An explicit double-spiral family is nonrectifiable and not locally monotone,
yet has finite \(p\)-variation for some \(p<2\).  Thus the result gives
rectangular pegs for a class not contained in the two named Asano--Ike
corollaries. At the critical exponent we construct a positive-area,
\(1/2\)-Hölder Jordan curve whose inner and outer smooth embedded
approximations have incompatible Liouville-period limits. Thus finite
\(2\)-variation plus parameter-aligned embedded \(C^0\) approximation does
not force primitive convergence. The universal conjecture remains open.

## Main result

**Theorem.** Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization.  If
\(c\) has finite \(p\)-variation for some \(1\le p<2\), then \(c(S^1)\)
inscribes a \(\theta\)-rectangle for every \(\theta\in(0,\pi)\).

**Critical extension.** The same conclusion holds if the periodic coordinate
moduli satisfy
\[
\int_0^1\frac{\omega_x(r)\omega_y(r)}{r^2}\,dr<\infty.
\]

The complete argument, including the fixed-parameter embedded \(C^1\) rounding
lemma and explicit Young--Loeve estimate, is in
`../angles/p-variation/README.md`.  The Dini refinement and \(p=2\) boundary
are in `../angles/critical-p2/README.md`.

## Proof architecture

Choose \(p<q<2\).  Boedihardjo--Geng construct partitions of mesh tending to
zero whose affine interpolants are still Jordan; their separate variation
lemma gives convergence to \(c\) in \(q\)-variation.  Each finite Jordan
polygon can be rounded inside pairwise disjoint vertex disks so that the
result is a regular \(C^1\) Jordan embedding on the same parameter circle and
the \(1\)-variation of the change is arbitrarily small. Thus the approximants
also converge in \(q\)-variation. Asano--Ike Remark 5.6 explicitly permits
these \(C^1\) approximants.

Writing \(c=(x,y)\), normalize the primitives by
\[
F_n(t)=\int_0^t y_n\,dx_n,\qquad F_n(0)=0.
\]
Young's estimate for \(q<2\) makes \(F_n\) converge uniformly on one period.
The period increments converge as well, so the primitives converge locally
uniformly on the universal cover \(\mathbb R\).  These are exactly
Asano--Ike's hypotheses.  No mollified curve is silently assumed to remain
embedded.

For the Dini extension, dyadic refinement errors are summable with tail
bounded by
\[
C\int_0^\delta\omega_x(r)\omega_y(r)r^{-2}\,dr.
\]
This supplies primitive convergence directly; the same embedded polygons and
corner rounding then apply.

## Strict witness beyond rectifiability and local monotonicity

For \(1<d<2\), take two disjoint rotated spirals
\[
\gamma_0(\theta)=\theta^{-1/d}e^{i\theta},\qquad
\gamma_1(\theta)=e^{i\delta}\gamma_0(\theta),
\quad \theta\ge1,
\]
and join their radius-one endpoints by a circular arc.  Strictly monotone
radius proves embeddedness.  Its length dominates
\(\sum n^{-1/d}=\infty\), while its \(p\)-variation is finite for every
\(p>d\).  Every linear projection oscillates infinitely often at the common
origin, so the curve is not locally monotone.  Details are in
`../results/spiral-family.md`.

## Verification

The exact rational harness is deliberately limited to finite conjecture
hygiene:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
```

Five tests verify rational polygonal simplicity, reject crossings and
degeneracies, check the shoelace/Liouville sign, prove exact primitive
invariance under rational subdivision, and verify/reject candidate inscribed
squares.  These tests do not certify the universal theorem, whose proof is
analytic.

## Critical obstruction

The obstruction persists with every approximant embedded. For any Jordan
trace \(C=\partial\Omega\), inner conformal level curves converge with
parameter to \(C\) and have Liouville periods tending to \(-|\Omega|\).
Outer conformal level curves also converge with parameter to \(C\), but their
periods tend to
\[
                         -|\overline\Omega|
                         =-|\Omega|-|C|.
\]
If \(|C|>0\), interleaving the two smooth Jordan sequences destroys primitive
convergence.

A scale-controlled Hilbert--Osgood construction gives a positive-area
\(1/2\)-Hölder Jordan curve. Since
\[
 |c(t)-c(s)|\le H|t-s|^{1/2}
 \quad\Longrightarrow\quad
 \sup_P\sum_{[u,v]\in P}|c(v)-c(u)|^2\le H^2,
\]
this is a finite-\(2\)-variation counterexample to **automatic primitive
stability for a supplied embedded approximation sequence**. It does not show
that the curve fails Asano--Ike's existential criterion, and it is not a
counterexample to the Square Peg conjecture.

For zero-area Jordan traces, winding-number stability forces the total
periods of all uniformly convergent oriented Jordan approximants to converge.
Local subarc primitives can still carry a second-level anomaly. The remaining
frontier is therefore uniqueness or realizability of the local area lift for
zero-area finite-\(2\)-variation Jordan curves. Antonelli--Young's May 2026
beta-number criterion for signed area of \(1/2\)-Hölder curves is the most
relevant published input.

## Relation to prior work and novelty boundary

Asano--Ike already cover every rectifiable and every locally monotone Jordan
curve; this report does not rediscover those results.  Boedihardjo--Geng
already prove the hard embedded polygonal approximation and finite-\(p\)
Green theorem.  The contribution here is a concise synthesis with
Asano--Ike's newly available sheaf criterion, plus an explicit strict witness
and a Dini-critical formulation. An independent source-by-source audit found
no explicit prior peg theorem in these terms, but classified the result as an
apparently unstated immediate corollary/synthesis rather than a new
rough-integration theorem. Expert confirmation should precede a formal
priority claim.

## Cite as

See `CITATION.cff`.  No DOI has been minted.
