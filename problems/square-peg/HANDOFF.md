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
8. `angles/unrestricted-zero-trace/README.md`.
9. `results/null-spiral-no-primitive.md`.
10. `literature/UNRESTRICTED_AUDIT.md`.
11. the latest `JOURNAL.md` section.

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

The unrestricted session then proved that the approximation bridge itself is
not universal.  Asano--Ike Remark 5.5 already handles positive-measure
traces, so only null traces remain.  Nevertheless the interleaved spirals
\[
a(\theta)=\theta^{-1/2},\qquad
b(\theta)=\frac{a(\theta)+a(\theta+2\pi)}2
\]
close to a planar-null Jordan curve with finite enclosed area but
logarithmically divergent action along one smooth arm.

A local action-rigidity lemma shows that uniform convergence of
parameter-aligned \(C^1\) Jordan curves and their primitives forces the
limiting primitive to equal the classical integral on every regular smooth
subarc.  The logarithmic divergence therefore excludes **every** possible
Asano--Ike Theorem 1.1 approximation sequence for this curve.  GPT-5.6 Sol at
xhigh independently returned MERGE.  The example has infinite
\(2\)-variation, so the finite-\(2\) frontier remains separately open.

The actual unrestricted frontier is now exactly Asano--Ike Remark 4.2:

> For a null Jordan trace and \(\theta=\pi/2\), prove the diagonal
> \(\mu hom\)-cohomology vanishing at the critical value without constructing
> a single-valued continuous primitive.

Do not retry two audited false shortcuts.  Conservative \(C^0\) smoothing
does not control action potentials: shrinking high-turn radial twists have
order-one action.  Greene--Lobb square-angle duality swaps spectral degrees
\(1\) and \(2\), while the triangle inequality applies only to degree \(2\);
it does not pin either action at half the enclosed area.

Do not run numerical square searches. The rational harness is conjecture
hygiene only. Consult GPT-5.6 Sol at xhigh for any proposed microlocal
vanishing theorem. Preserve both claim boundaries: the general Square Peg
conjecture remains open, and failure of the primitive criterion does not
refute the weaker diagonal-cohomology criterion.
