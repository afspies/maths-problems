# Learnings — Square Peg conjecture

## What the next session should do first

- Obtain human/expert priority and soundness feedback on the short synthesis,
  especially from the authors of Asano--Ike and Boedihardjo--Geng.
- Turn the Dini sewing paragraph into a formally cited lemma if preparing a
  paper, then attack embedded approximation of a prescribed geometric
  \(2\)-rough lift.

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
  Jordan, so it is not a counterexample to the embedded criterion.
- The finite-\(p\) theorem is likely a short, nearly formal synthesis rather
  than deep novelty.  Targeted search found no explicit statement, but that
  does not establish priority.
