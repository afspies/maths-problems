# Exact check of the Section 6 parameter choices

## Verdict

The published 13/4 proof has one obvious multiplicity-sign typo and a
repairable induction-constants defect. Two displayed Section 6 comparisons
do not follow from the stated choices. This result
does not challenge the geometric inputs or the claimed exponent: tightening
the auxiliary constants repairs the comparisons.

## Reproduction

From `problems/kakeya-r4/harness/` run:

```bash
python3 -m unittest -v test_induction_parameters.py
```

All quantities are `fractions.Fraction`.

## Counterexample to the stated implication

Earlier, the published text prints the average-multiplicity lower bound as
`mu_Y ≳ delta^(sigma_n+2 eta)`. The defining quotient gives
`delta^eta/delta^(sigma_n-eta)=delta^(-sigma_n+2 eta)`.
Later uses require the negative sign, so this is a typographical error.

The paper takes `N` minimal with `4/N<epsilon_0`. With
`epsilon_0=1/10`, exact arithmetic gives `N=41`. Hence

`2/N=2/41<1/10=epsilon_0`.

The arXiv v1 sentence claiming the opposite is false. The journal version
removes that sentence, but retains uses of `epsilon_0/4` as though it were a
safe lower bound for `1/N`.

For example,

`epsilon_1=249/10000 < epsilon_0/4=1/40`

but

`epsilon_1 > 1/N=1/41`.

Thus the trilinear display cannot assign `delta^epsilon_1` a lower bound
`delta^(1/N)` under only the printed hypothesis.

In the plany display, the leading rho exponent is negative. Since
`1/N<epsilon_0/4`, replacing `1/N` by `epsilon_0/4` reverses the printed
lower-bound direction.

## Repair

Minimality gives exactly

`epsilon_0/(4+epsilon_0) ≤ 1/N < epsilon_0/4`.

For `0<epsilon_0<1`, use the convenient lower bound
`epsilon_0/5<1/N`. Choose `epsilon_1<epsilon_0/5`; keep `eta_0`
small enough that `14 eta_0≤1/N`; and in the plany bracket use
`1/N≥epsilon_0/5` with the correct sign. Further shrinking
`epsilon_2,eta_0` leaves the bracket exponent strictly negative.

The test suite includes one complete rational witness to the repaired
trilinear and plany budgets.

Two small admissibility repairs are also required. The chosen intermediate
scale lies in Lemma 4.3's interval only when `eta_j≤1/(j+1)`; imposing
`eta_0≤1/N` suffices for every step. Theorem 5.5 requires
`0<epsilon_2<epsilon_1<1`, so its printed use with `epsilon_1=1` is outside
the stated hypotheses. If `sigma_4=0` the dimension conclusion is already
full; otherwise choose a fixed `a` with `sigma_4<a<1` and weaken the
available `(1,C)` two-ends condition to `(a,C)`.

## Scope

This checks the displayed exponent arithmetic and the two elementary
admissibility conditions only. The harness contains one exact repaired
parameter witness, not a formalization of the imported multiscale,
trilinear, or planebrush theorems.
