# Learnings — Four-dimensional Kakeya conjecture

Distilled, high-signal only. What didn't work and *why*; what surprised us;
which angles look dead vs promising; what the next session should do first.
Keep this short enough to read in two minutes — the journal holds the detail.

## What the next session should do first

- Start Bridge B with a theorem whose output is an explicit normalized
  quadratic polynomial `P`, overlap level `lambda`, and balanced subfamily.
  Prove a carrier-extraction statement for one stable subclass (for example,
  families already partitioned into boundedly many transverse quadric
  patches), or construct an exact countermodel to QW2. Charge every
  refinement/model-selection loss before claiming a power gain.

## Dead ends (and why)

- Reapplying the one-scale trilinear estimate: all normalized factors are
  already order one; no fixed negative power appears.
- Inferring grains from Proposition 3.12: it supplies balance at one selected
  scale, not stability, algebraic structure, or a common two-scale
  refinement.
- Literal convex-to-semialgebraic word replacement: greedy factoring is
  formal, but the needed inner/outer union theorem and rescaling closure are
  absent.
- “Ruled implies plany”: false even locally on the exact split quadric.

## Surprises / structure discovered

- The published 13/4 bookkeeping has a multiplicity-sign typo, two reversed
  scale comparisons, and two minor admissibility gaps; all are repairable
  without changing the exponent.
- The raw full quadric line net is not the Convex-Wolff counterexample; it
  must be thinned, then copied.
- The degree-two QW2 test detects the thinned copy by exactly a
  `delta^(-1/2)` factor, but detection alone gives no union theorem.
- Any Bridge A gain must satisfy `c<1/12`, quantify the trilinear threshold
  `theta≈rho²`, bound model entropy, and preserve mass on a common
  two-scale refinement.
