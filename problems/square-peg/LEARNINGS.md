# Learnings — Square Peg conjecture

## What the next session should do first

- Obtain human/expert priority and soundness feedback on both the packaged
  finite-\(p<2\) synthesis and the critical Antonelli--Young bridge.
- For the unrestricted problem, work directly on Asano--Ike Remark 4.2's
  diagonal cohomology at \(\theta=\pi/2\).  Do not assume every null trace has
  a continuous area primitive: the explicit double spiral disproves that.

## Results

- Boedihardjo--Geng already solve the topological approximation problem that
  initially looked dangerous: their parameter-respecting polygonal
  interpolants can be chosen Jordan, and a separate lemma gives
  \(q\)-variation convergence for every \(q>p\).
- Fixed-parameter cyclic corner rounding can be made arbitrarily small in
  both uniform and \(1\)-variation norms.  Collinear speed jumps must be
  retained and smoothed; deleting their vertices loses parameter data.
- Young--Loeve stability then gives Asano--Ike primitive convergence for every
  finite-\(p\)-variation Jordan parametrization with \(p<2\).
- A Dini coordinate modulus
  \(\int\omega_x\omega_y/r^2<\infty\) gives a critical-scale extension via a
  quantitative sewing estimate.
- For every positive-area Jordan trace, inner and outer conformal level
  curves converge with the same boundary parameter but their Liouville
  periods differ in the limit by exactly the trace area.
- A four-corner Hilbert--Osgood routing with summable gaps gives a
  positive-area \(1/2\)-Hölder Jordan curve, hence the embedded period anomaly
  occurs within finite \(2\)-variation.
- For a zero-area Jordan trace, winding-number stability forces convergence
  of total enclosed areas under uniform oriented Jordan approximation. This
  does not by itself control local subarc primitives.
- Antonelli--Young's all-partitions signed-area convergence has a hidden
  uniform-local consequence: extend two prefix partitions by the same tail.
  The common tail cancels, giving a Cauchy estimate uniform in the endpoint.
- Therefore every \(1/2\)-Hölder Jordan parametrization with finite dyadic
  quadratic-diameter sum \(\sigma(c)\) satisfies Asano--Ike and gets every
  prescribed rectangle.
- A disjoint many-turn spiral comb can have
  \(\sigma(c)<\infty\) but infinite \(p\)-variation for every \(p<2\):
  choose radius \(a_n=2^{-n-20}\), turn count
  \(N_n\asymp4^n/n^2\), and time \(w_n=N_na_n^2\).
- The two-arm spiral \(r=\theta^{-1/d}\), \(1<d<2\), is Jordan,
  nonrectifiable, finite \(p\)-variation for every \(p>d\), and not locally
  monotone.  It proves the new class is strictly outside Asano--Ike's two
  named corollaries.
- Asano--Ike Remark 5.5 already solves every positive-planar-measure Jordan
  trace by density.  The unrestricted problem therefore reduces to null
  traces.
- A null trace still need not satisfy Asano--Ike Theorem 1.1.  Interleave
  \(a(\theta)=\theta^{-1/2}\) with
  \(b(\theta)=(a(\theta)+a(\theta+2\pi))/2\).  The logarithmically divergent
  arm actions cancel in the full period to an integrable
  \(O(\theta^{-2})\) remainder.
- Local action rigidity: on every regular smooth subarc of the limit, uniform
  convergence of both parametrized Jordan curves and their primitives forces
  the limiting primitive to equal the classical line integral.  The proof
  extracts a proper crosscut in a shrinking tubular rectangle and applies
  Green's theorem; uniform primitive convergence removes the moving-endpoint
  errors.
- Consequently the null double spiral admits no parameter-aligned regular
  \(C^1\) approximants with convergent primitives.  This excludes every
  possible Asano--Ike Theorem 1.1 sequence, not just conformal or polygonal
  approximants.

## Dead ends and cautions

- Do not describe rectifiable curves as open: Asano--Ike v3 prove every
  prescribed rectangle for them.
- Bare mollification is not an embedded approximation argument.
- Uniform convergence plus bounded \(2\)-variation does not control area.
  The repeated shrinking circle demonstrates the analytic anomaly but is not
  Jordan. The positive-area Osgood construction now supplies a genuinely
  embedded approximation anomaly, but only for a supplied sequence: it does
  not show failure of Asano--Ike's existential condition.
- That last limitation does not apply to the new null double spiral: local
  action rigidity proves failure of the existential primitive criterion
  itself.  The curve has infinite \(2\)-variation, so it does not weaken the
  positive finite-\(2\)-variation results.
- Conservative \(C^0\) smoothing controls maps, not action potentials.
  Shrinking high-turn radial twists have vanishing displacement and
  order-one action oscillation.
- Square-angle Floer symmetry does not pin the top action at half the area.
  Duality exchanges degrees \(1\) and \(2\), while the available triangle
  inequality is only for degree \(2\).  The axioms permit the two actions to
  tend to \(0\) and the full enclosed area.
- The finite-\(p\) theorem is likely a short, nearly formal synthesis rather
  than deep novelty.  Targeted search found no explicit statement, but that
  does not establish priority. The independent audit recommends “apparently
  unstated consequence,” not “new rough-integration theorem.”
- Do not call Antonelli--Young Theorem 1.2 a planar beta-number criterion.
  Its directly usable planar hypothesis is the dyadic diameter-square sum;
  beta numbers occur in the ambient Heisenberg-map/fibre argument.
- Convergence of dyadic polygon areas alone is not enough at \(1/2\)-Hölder
  regularity. The essential Antonelli--Young input is convergence over all
  fine partitions.
