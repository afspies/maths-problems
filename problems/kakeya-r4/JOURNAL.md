# Journal — Four-dimensional Kakeya conjecture

Append-only. One dated section per session: what was tried (exact commands,
encodings, parameters), outcomes, compute spent and where it ran. Newest at the
bottom. Do not rewrite history — corrections get their own dated entry.

## 2026-07-24 — scaffolded

Problem folder created from template. No work yet.

## 2026-07-24 — sticky grains proof-first audit

### Scope and exact harness

Worked on branch `problem/kakeya-r4/2026-07-24-sticky-grains`, only in this
problem folder plus the generated repository board. The verifier was built
before the proof campaign. It uses `fractions.Fraction` throughout and covers:

- the exact `3/4` versus `2/3` branch aggregation and dimension conversion;
- the extremal multiplicity sign;
- the Section 6 scale-count, trilinear, plany, scale-interval, and strict
  planebrush-parameter checks;
- exact rational plany, trilinear, and ruled-quadric incidence models.

Commands:

```bash
python3 tools/new_problem.py kakeya-r4 --title "Four-dimensional Kakeya conjecture"
cd problems/kakeya-r4/harness
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

The ledger printed global exponent `3/4`, dimension `13/4`, bottleneck
`trilinear`. All 15 tests passed in 0.001 seconds.

### Literature audit

Primary-source audit through 24 July 2026 found:

- general R⁴ Hausdorff lower bound
  `3+(sqrt(17665)-97)/600>3.059` from corrected Katz–Zahl;
- separate maximal-function record
  `(159+sqrt(145))/56≈3.0543` from arXiv:2511.22824, whose final remark says
  it does not improve the Hausdorff record;
- sticky R⁴ Hausdorff bound `13/4`, with no later improvement found;
- full R³ sticky and general results, plus restricted and finite-field
  results kept in separate categories.

The 2511.22824 graininess/multiplicity discussion supplies balanced
bookkeeping and a suggested improvement, not an R⁴ inverse theorem.

### Independent 13/4 reconstruction

Reconstructed Definitions 3.1–3.11, Proposition 3.12, the trilinear/plany
dichotomy, Theorems 5.4–5.5, and the Section 6 induction. The global
bottleneck is exactly the trilinear `3/4` branch; the plany `2/3` branch has
an exponent gap `1/12`.

The source ledger records four repairable bookkeeping/admissibility issues:

1. the average-multiplicity display needs `-sigma_n+2 eta`, not
   `sigma_n+2 eta`;
2. minimal `N` with `4/N<epsilon_0` gives
   `epsilon_0/(4+epsilon_0)≤1/N<epsilon_0/4`, invalidating two printed
   comparisons;
3. the intermediate-scale interval needs `eta_0≤1/N`;
4. the strict planebrush hypothesis is repaired by replacing the printed
   exponent `1` with fixed `a` satisfying `sigma_4<a<1`.

The first two change no geometry; the last two are elementary admissibility
repairs. The harness certifies a rational repaired exponent regime but does
not formalize the imported geometric theorems.

### Bridge A: sticky multiscale

Wrote the exact conditional implication: a uniform trilinear gain
`delta^(-c)`, with `0<c<1/12`, relative to the full Theorem 5.4 right-hand
side would leave plany gain `rho^(-(1/12-c))` and imply
`dim_H≥13/4+c`.

The preferred inverse-trilinear/two-scale-ruled-rigidity pair was
pressure-tested. Proposition 3.12 balances one selected scale but provides
neither near-equality stability, bounded model entropy, nor a common
positive-mass refinement at two scales. A polynomial model-selection loss
must be explicitly subtracted from any proposed `c`. No inverse theorem or
fixed gain was proved.

### Bridge B: semialgebraic reduction

Reconstructed the Wang–Zahl R³ convex factoring skeleton and marked five R⁴
failure points. Built the split quadric exactly via its `SL_2` model. Three
rational concurrent lines have normalized squared wedge `1/50`, so ruledness
does not imply 2-planiness.

The raw line net fails Convex Wolff in a tangent prism. The actual
countermodel is the thinned net followed by `delta^(-1/2)` moved copies. A
degree-two polynomial-Wolff test was defined and detects every thinned copy
by `delta^(-1/2)`. This is an exact obstruction/detection lemma, not a union
or carrier-extraction theorem.

### Adversarial reviews and verdict

At attack selection and again after theorem formulation, independent
GPT-5.6 Sol agents were run with model `gpt-5.6-sol` and effort `xhigh`.
The reviews checked hypotheses, exponent signs, epsilon losses,
Hausdorff/Minkowski implications, circularity, and cross-scale loss.

Verdict: prefer Bridge B's degree-two carrier-extraction target for a future
campaign, but **STOP/PIVOT now**. None of the two-session GO conditions was
met. In particular, the exact quadric stress test and repaired ledger must
not be described as a new dimension bound, inverse theorem, or
semialgebraic union theorem.

No numerical tube search or substantial compute was used. Work ran in the
local Codex repository worktree; source extraction and all exact tests took
negligible laptop-scale compute. No private infrastructure details are
recorded.
