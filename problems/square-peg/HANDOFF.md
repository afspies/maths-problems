# Handoff prompt — Square Peg conjecture

You are continuing a proof-first attack on the Square Peg conjecture in
`problems/square-peg/`.

Read, in order:

1. `/AGENTS.md` and `AGENTS.local.md` if present.
2. `PROBLEM.md`.
3. `LEARNINGS.md`.
4. `angles/p-variation/README.md`.
5. `angles/critical-p2/README.md`.
6. `angles/critical-p2/antonelli-young-bridge.md`.
7. `results/critical-spiral-comb.md`.
8. the latest `JOURNAL.md` section.

The finite-\(p<2\) proof has now received an independent primary-source audit
and been packaged as `writeup/p-variation-note.md`. The audit verdict is
MERGE; the safe priority description is “an apparently unstated immediate
corollary/synthesis of Asano--Ike and Boedihardjo--Geng.”

The first \(p=2\) session proved a sharp embedded anomaly. For every positive-area
Jordan trace, inner and outer conformal level curves converge with the same
boundary parameter, but their limiting Liouville periods differ by exactly
the trace area. A scale-controlled positive-area \(1/2\)-Hölder
Hilbert--Osgood Jordan curve places this phenomenon inside finite
\(2\)-variation. GPT-5.6 Sol at xhigh returned MERGE after auditing the
recursive embedding and Hölder proof.

The next session proved a genuinely critical positive class:

> Every \(1/2\)-Hölder Jordan parametrization with finite
> Antonelli--Young dyadic quadratic-diameter sum satisfies Asano--Ike and
> therefore inscribes every prescribed rectangle.

The key observation is that Antonelli--Young define signed area by convergence
over all fine partitions. Two prefix partitions can be extended by the same
tail, which cancels and yields uniform convergence of the entire local
primitive. Boedihardjo--Geng supplies embedded polygons and a diagonal
\(C^1\) rounding preserves their primitives.

The strict spiral-comb witness uses
\(a_n=2^{-n-20}\), \(N_n\asymp4^n/n^2\), and
\(w_n=N_na_n^2\). It is Jordan, \(1/2\)-Hölder, and has
\(\sigma(c)<\infty\), but has infinite \(p\)-variation for every \(p<2\),
infinite length, and is not locally monotone. GPT-5.6 Sol at xhigh returned
MERGE after three local proof repairs.

This does **not** cover every finite-\(2\)-variation Jordan curve. The actual
frontier is now:

> Which zero-area finite-\(2\)-variation Jordan curves outside the
> Antonelli--Young \(\sigma\)-class possess a canonical local area lift
> realizable by parameter-aligned embedded smooth approximations?

Seek either:

- a weaker geometric/tubular condition implying uniform local primitives;
- an embedded realization theorem for a prescribed geometric \(2\)-rough
  lift; or
- a zero-area Jordan trace with two embedded approximation sequences having
  the same total-period limit but incompatible local primitive limits.

Do not run numerical square searches. The rational harness is conjecture
hygiene only. Consult GPT-5.6 Sol at xhigh for any proposed \(p=2\) theorem or
counterexample. Preserve both claim boundaries: the general Square Peg
conjecture remains open, and failure of primitive convergence for one
approximation sequence does not refute an existential approximation
criterion.
