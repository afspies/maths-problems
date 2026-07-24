# Handoff prompt — Square Peg conjecture

You are continuing a proof-first attack on the Square Peg conjecture in
`problems/square-peg/`.

Read, in order:

1. `/AGENTS.md` and `AGENTS.local.md` if present.
2. `PROBLEM.md`.
3. `LEARNINGS.md`.
4. `angles/p-variation/README.md`.
5. `angles/critical-p2/README.md`.
6. the latest `JOURNAL.md` section.

The finite-\(p<2\) proof has now received an independent primary-source audit
and been packaged as `writeup/p-variation-note.md`. The audit verdict is
MERGE; the safe priority description is “an apparently unstated immediate
corollary/synthesis of Asano--Ike and Boedihardjo--Geng.”

The \(p=2\) session proved a sharp embedded anomaly. For every positive-area
Jordan trace, inner and outer conformal level curves converge with the same
boundary parameter, but their limiting Liouville periods differ by exactly
the trace area. A scale-controlled positive-area \(1/2\)-Hölder
Hilbert--Osgood Jordan curve places this phenomenon inside finite
\(2\)-variation. GPT-5.6 Sol at xhigh returned MERGE after auditing the
recursive embedding and Hölder proof.

This does **not** show that the Osgood curve fails Asano--Ike's existential
criterion. The actual frontier has narrowed to:

> For a zero-area finite-\(2\)-variation Jordan trace, when are the local
> Liouville primitives uniquely determined and realizable by parameter-aligned
> embedded smooth approximations?

Start from Antonelli--Young, arXiv:2605.15987, which gives beta-number
criteria for signed area of \(1/2\)-Hölder curves. Seek either:

- a beta-number or tubular condition implying uniform local primitives for
  the embedded Boedihardjo--Geng polygons;
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
