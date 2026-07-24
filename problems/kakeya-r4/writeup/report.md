# Four-dimensional Kakeya: sticky grains campaign

**Status:** partial-results, no new dimension bound · **Date:** 24 July 2026

## Abstract

The current general Hausdorff benchmark in R⁴ is the corrected Katz–Zahl
bound above 3.059; the current Kakeya maximal benchmark is the distinct
3.0543 result of Borges et al.; and the current sticky Hausdorff benchmark is
13/4. We reconstructed the 13/4 induction, found a repairable constants defect
and a multiplicity-sign typo in the published bookkeeping, and verified a
corrected rational parameter regime. We also built an exact split-quadric
stress test: a ruled quadratic 3-fold can be pointwise trilinear, so a
two-scale rigidity lemma cannot equate ruledness with 2-planiness. No strict
sticky exponent gain, new full-dimensional subclass, inverse theorem, or
semialgebraic union theorem is claimed.

## Result

### Verified bookkeeping result

If `N` is minimal with `4/N<epsilon_0`, then

`epsilon_0/(4+epsilon_0) ≤ 1/N < epsilon_0/4`.

The published Section 6 comparisons use `epsilon_0/4` on the wrong side. For
`epsilon_0=1/10`, the exact counterexample is `N=41`. Replacing the unsafe
choice by `epsilon_1<epsilon_0/5`, using `1/N>epsilon_0/5`, and shrinking the
remaining losses repairs the closing exponent. The earlier printed
multiplicity exponent must also be `-sigma_n+2 eta`, not
`sigma_n+2 eta`.

The scale interval additionally needs `eta_0≤1/N`. The printed use of the
planebrush theorem at a two-ends exponent equal to one is outside its strict
hypotheses; weaken it to any fixed `a` with `sigma_4<a<1`. These are
elementary admissibility repairs, not new geometric input.

### Verified geometric stress test

Under

`M(x)=[[x1+x3,x2+x4],[x4-x2,x1-x3]]`,

the quadric `x1²+x2²-x3²-x4²=1` is `SL_2(R)`. Rank-one nilpotents give an
infinite rational family of lines. The harness verifies three concurrent
rational lines with normalized squared wedge `1/50`. Thus a ruled quadratic
carrier need not be 2-plany even locally.

The exact Convex-Wolff countermodel is the thinned-and-copied quadric family
from Zahl's survey, not the raw full line net. A degree-2 polynomial Wolff
test detects each thinned copy by a factor `delta^(-1/2)`.

### Conditional exponent bridge

If a new multiscale trilinear theorem gave
`|U|≥delta^(3/4-c+o(1))` uniformly for some `0<c<1/12`, the weakly plany
recurrence retains gain `rho^(-(1/12-c))`. The existing induction would then
give `dim_H K≥13/4+c`. The new trilinear theorem is not proved. The xhigh
soundness review also rejected combining two separate Proposition 3.12
refinements without proving that their balanced mass survives on a common
refinement, and rejected ignoring polynomial model-selection losses. The
session therefore ends STOP/PIVOT.

## Verification

From `problems/kakeya-r4/harness/`:

```bash
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

The first command prints the exact global exponent `3/4`, dimension `13/4`,
and bottleneck `trilinear`. The test suite checks the branch ledger, the
published parameter counterexample and repair, and exact rational incidence
models. Runtime is below one second on a laptop.

## Method

We audited primary sources through 24 July 2026, reconstructed Rai
Choudhuri's Definitions 3.1–3.11, Proposition 3.12, Lemma 4.3, Theorems
5.4–5.5, and the Section 6 induction, then independently reviewed both bridge
formulations with GPT-5.6 Sol at xhigh effort. The campaign used only local
exact rational tests and primary-source text; there was no numerical tube
search and no substantial compute.

## What we tried that didn't work

- Reapplying the one-scale Guth–Zahl estimate cannot yield a fixed gain:
  every normalized factor in its right-hand side is at most order one.
- Proposition 3.12 balances mass and multiplicity but gives no cross-scale
  stability or bounded-entropy algebraic model.
- Replacing “convex” by “semialgebraic” in the abstract greedy factoring
  lemma is formal and insufficient; the missing input is an inner/outer
  incidence or carrier-extraction theorem.
- A ruled carrier cannot simply be declared 2-plany: the exact quadric model
  has trilinear concurrent directions.

## Relation to prior work

Rai Choudhuri proves the sticky 13/4 bound by combining Guth–Zahl's
trilinear estimate with Katz–Zahl's 10/3 planebrush estimate and Wang–Zahl
multiscale structure. Wang–Zahl's R³ full-to-sticky reduction relies on
three-dimensional convex factor geometry and a full R³ sticky endpoint.
Guth and Zahl identify ruled low-degree hypersurfaces as the obstruction to a
literal R⁴ convex-union theorem. Full citations are in
`../literature/refs.bib`.

## Cite as

See `CITATION.cff` in this folder. No DOI is assigned because no conjecture
milestone is being released.
