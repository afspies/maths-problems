# Square Peg conjecture

## Statement

Does every Jordan curve \(C\subset\mathbb R^2\) contain four distinct points
that are the vertices of a nondegenerate Euclidean square?

The general conjecture remains open.  More strongly, one may ask whether a
curve inscribes a rectangle of every prescribed aspect angle
\(\theta\in(0,\pi)\).

## Status / context

Asano--Ike [AI] prove in v3 that every rectifiable Jordan curve and every
locally monotone Jordan curve inscribes every prescribed rectangle.  These
classes must not be described as open.  Their main theorem applies more
generally when a parametrized Jordan curve admits smooth Jordan approximants
whose Liouville primitives converge locally uniformly.

This campaign proves that the criterion holds under either of two
parameter-level conditions:

1. finite \(p\)-variation for some \(p<2\); or
2. coordinate moduli satisfying the critical Dini--Young integral
   \(\int_0^1\omega_x(r)\omega_y(r)r^{-2}\,dr<\infty\).

The first class contains explicit nonrectifiable, non-locally-monotone double
spirals (`results/spiral-family.md`).  The proof is a short synthesis of
Asano--Ike, Boedihardjo--Geng's embedded polygonal interpolation, a controlled
corner rounding, and Young integration.  It is a partial result; the
unrestricted conjecture remains open.

## Certificate + verifier

- **Finite certificate:** a rational polygon, together with four rational
  boundary points claimed to form a square.
- **Verifier:** `harness/geometry.py` checks polygonal simplicity, exact
  boundary membership, and the square equations using `fractions.Fraction`.
  It also checks exact shoelace/Liouville primitives and invariance under
  rational subdivision.
- **Limitation:** no finite candidate square, numerical search, or finite
  polygon experiment can certify the universal Jordan-curve theorem.  The
  harness is conjecture hygiene only.

## Known structure

- Smooth Jordan curves inscribe every prescribed rectangle [GL-smooth].
- Rectifiable and locally monotone curves do too [AI].
- For an analytic/smooth curve, rectangle inscriptions are off-diagonal
  intersections of \(\gamma\times\gamma\) with its Hamiltonian rotation.
- Shrink-out is the limiting obstruction: smooth approximants may have only
  rectangles whose four vertices coalesce.
- Asano--Ike's primitive convergence removes the diagonal action
  contribution; it is parametrization-sensitive and is not implied by bare
  Hausdorff convergence.
- Below variation exponent \(2\), Young integration controls the primitive.
  At \(2\), uniform convergence plus a bounded \(2\)-variation norm does not
  determine Lévy area; a second-level lift or a Dini improvement is needed.

## Angle-of-attack menu

- **Young/rough integration:** completed finite-\(p<2\) and Dini--Young
  criteria in `angles/p-variation/` and `angles/critical-p2/`.
- **Geometric rough paths at \(p=2\):** seek an embedded approximation theorem
  for a prescribed geometric area lift, or incompatible primitive limits.
- **Sheaf criterion:** weaken the no-translate microsupport condition without
  requiring a single-valued continuous primitive.
- **Planar topology:** find quantitative tubular/one-sided conditions that
  force primitive compactness for embedded approximants.
- **Counterexample pressure test:** construct area-anomalous embedded
  approximations with the same parametrization, if possible.

## First steps for the next session

1. Ask Asano--Ike and Boedihardjo--Geng for a priority/soundness check of the
   synthesis before claiming novelty.
2. Replace the proof-sketch form of the Dini--Young arbitrary-partition lemma
   by a fully cited or self-contained lemma with constants.
3. Attack the \(p=2\) embedded area-lift question; do not spend time on
   numerical square searches.
