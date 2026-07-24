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
parameter-level conditions below the critical exponent, and one genuinely
critical condition:

1. finite \(p\)-variation for some \(p<2\); or
2. coordinate moduli satisfying the critical Dini--Young integral
   \(\int_0^1\omega_x(r)\omega_y(r)r^{-2}\,dr<\infty\); or
3. \(1/2\)-Hölder regularity together with Antonelli--Young's finite dyadic
   quadratic-diameter sum \(\sigma(c)<\infty\).

The first class contains explicit nonrectifiable, non-locally-monotone double
spirals (`results/spiral-family.md`).  The proof is a short synthesis of
Asano--Ike, Boedihardjo--Geng's embedded polygonal interpolation, a controlled
corner rounding, and Young integration.  It is a partial result; the
unrestricted conjecture remains open.

The third class reaches finite \(2\)-variation beyond every
finite-\(p<2\) class.  The explicit critical spiral comb in
`results/critical-spiral-comb.md` has infinite \(p\)-variation for every
\(p<2\), infinite length, and is not locally monotone, but still inscribes
every prescribed rectangle.  The proof is in
`angles/critical-p2/antonelli-young-bridge.md`.

The unrestricted campaign now has a sharp negative result about the present
bridge.  Asano--Ike already handle positive-measure traces by density, so the
remaining case is a planar-null trace.  Nevertheless,
`results/null-spiral-no-primitive.md` constructs an explicit null double
spiral for which **no** parameter-aligned \(C^1\) Jordan approximants can have
locally uniformly convergent Liouville primitives.  Thus their Theorem 1.1
criterion is not universal.  This does not refute their weaker Remark 4.2
diagonal-cohomology route or the Square Peg conjecture.

Every Jordan domain nevertheless has a canonical weaker lift.  For the
analytic level curves of its Riemann map, the mean-centered Liouville
primitives converge strongly in \(L^2\) in harmonic-measure parameter.  Either
this convergence upgrades to uniform convergence, giving every prescribed
rectangle by Asano--Ike, or order-one action concentrates on shrinking
prime-end intervals with winding multiplicity \(\gtrsim\rho^{-2}\).
Details are in `angles/conformal-l2/README.md`.

This dichotomy is sharp.  The null double spiral carries fixed action across
conformal cells whose harmonic measure is \(\exp(-\Theta(V^2))\), while
their area is \(O(V^{-1})\) and critical trace capacity is \(O(V^{-2})\).
Thus classical conformal energy and capacity cannot remove the exceptional
prime end.  See `results/null-spiral-conformal-concentration.md`.

The remaining microlocal step must work at the persistence-bar level.
`results/shrinking-square-action-injection.md` shows that exact shrinking
squares can carry any prescribed limiting action, even under conservative
perturbations converging to the identity.  Hence neither square symmetry nor
Jordan separation can bound individual collapsing actions or the sum of the
two projected capping areas.

For finite smooth truncations of the null spiral, the diagonal complex is
concentrated at action \(0\pmod\pi\).  In the limit, however, the reduced
microsupport contains the full action circle over the collapsed point while
the two phase sheets have gap \(\pi/(2\theta)+O(\theta^{-2})\).
`results/null-spiral-microlocal-eye.md` identifies the exact missing datum:
after retaining the action circle, the \(!\)-versus-\(*\) difference has
\(\tau_t=0\) and the deep eye is arbitrarily torsion.  The exact missing
datum is instead a possible exact-action Milnor defect in the metric
completion's continuation telescope.

At the critical exponent, `angles/critical-p2/osgood-area-anomaly.md` proves
that finite \(2\)-variation plus parameter-aligned embedded \(C^0\)
approximation does not force primitive convergence. A positive-area,
\(1/2\)-Hölder Jordan curve has inner and outer smooth Jordan approximations
whose limiting Liouville periods differ by the area of the trace. This is an
approximation-stability counterexample, not a counterexample to Square Peg or
to the existential Asano--Ike criterion.

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
- Positive-area Jordan traces admit inner and outer conformal level
  approximations with incompatible limiting periods. For a zero-area trace,
  total periods are stable.
- Total-period stability for null traces does not imply a local primitive.
  The interleaved \(r=\theta^{-1/2}\) double spiral has finite total enclosed
  area but logarithmically divergent action along one smooth arm.  A tubular
  crosscut lemma proves that any uniformly convergent approximating primitive
  would have to reproduce that divergence.
- Conformal inner curves always have strongly \(L^2\)-convergent centered
  primitives.  Failure of the continuous lift is equivalent to unbounded
  winding concentration on intervals shrinking to a prime end.
- Matschke's obstruction implies that a square-free Jordan curve has an exact
  special trapezoid at every parameter scale.  Over each compact positive
  scale interval, a fixed-type connected continuum spans the interval.  Its
  possible blow-up screens are classified in
  `angles/configuration-degeneration/README.md`.
- Fixed-vertex Hamiltonian twists can assign arbitrary action to an exact
  shrinking square while remaining \(C^0\)-small.  The missing theorem must
  pair such generators into persistence bars of vanishing length.
- Antonelli--Young's all-partitions signed-area theorem turns
  \(1/2\)-Hölder regularity plus \(\sigma(c)<\infty\) into a
  partition-independent local primitive. Combined with embedded Jordan
  polygons, this resolves a strict critical subclass.

## Angle-of-attack menu

- **Young/rough integration:** completed finite-\(p<2\) and Dini--Young
  criteria in `angles/p-variation/` and `angles/critical-p2/`.
- **Geometric rough paths at \(p=2\):** the positive-area period anomaly is
  complete, and the Antonelli--Young \(\sigma\)-class is complete; seek a
  weaker local lift theorem or a counterexample outside that class.
- **Sheaf criterion:** prove Asano--Ike Remark 4.2's diagonal
  \(\mu hom\)-cohomology vanishing at \(\theta=\pi/2\), in the persistent
  diagonal-locality form in `angles/diagonal-microlocal/README.md`.
- **Square envelopes:** combine Hugelmeyer's outer/inner envelope with the
  exact ribbon-area identity in
  `angles/configuration-degeneration/square-envelope-area.md`; it remains to
  obtain simple ribbons or the required outer/inner winding bounds.
- **Conformal concentration:** compute the diagonal \(\mu hom\) of the null
  double spiral by identifying the metric-limit extension of its
  vanishing-width eye.
- **Configuration degeneration:** combine the all-scales special trapezoids
  with the conformal tame/concentration dichotomy.
- **Planar topology:** find quantitative tubular/one-sided conditions that
  force primitive compactness for embedded approximants.
- **Counterexample pressure test:** localize an embedded anomaly to a
  zero-area trace outside the \(\sigma\)-class, or prove a weaker
  tubular/rough-lift compactness condition.

## First steps for the next session

1. Compute the derived inverse-limit/Milnor term of the explicit
   null-spiral continuation telescope.  The \(!\)-versus-\(*\) distinction is
   not the obstruction in the positive-\(\tau\) category.
2. Prove a no-ephemeral theorem for restricted diagonal \(\mu hom\), or show
   directly that the spiral's cross-stage tower is pro-zero away from
   \(\pi\mathbb Z\).
3. Do not try to bound individual shrinking-square actions: fixed-vertex
   Hamiltonian twists make them arbitrary.  Do not spend time on numerical
   square searches.
