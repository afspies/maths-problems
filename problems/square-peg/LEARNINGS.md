# Learnings — Square Peg conjecture

## What the next session should do first

- Obtain human/expert priority and soundness feedback on the packaged
  finite-\(p<2\) synthesis, especially from the authors of Asano--Ike and
  Boedihardjo--Geng.
- Compare Antonelli--Young's beta-number criterion with the zero-area local
  primitive needed by Asano--Ike. Seek either parameter-aligned embedded
  realizability or a zero-area local anomaly.

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
  does not yet control local subarc primitives.
- The two-arm spiral \(r=\theta^{-1/d}\), \(1<d<2\), is Jordan,
  nonrectifiable, finite \(p\)-variation for every \(p>d\), and not locally
  monotone.  It proves the new class is strictly outside Asano--Ike's two
  named corollaries.

## Dead ends and cautions

- Do not describe rectifiable curves as open: Asano--Ike v3 prove every
  prescribed rectangle for them.
- Bare mollification is not an embedded approximation argument.
- Uniform convergence plus bounded \(2\)-variation does not control area.
  The repeated shrinking circle demonstrates the analytic anomaly but is not
  Jordan. The positive-area Osgood construction now supplies a genuinely
  embedded approximation anomaly, but only for a supplied sequence: it does
  not show failure of Asano--Ike's existential condition.
- The finite-\(p\) theorem is likely a short, nearly formal synthesis rather
  than deep novelty.  Targeted search found no explicit statement, but that
  does not establish priority. The independent audit recommends “apparently
  unstated consequence,” not “new rough-integration theorem.”
