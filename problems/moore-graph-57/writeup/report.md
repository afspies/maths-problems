# The missing Moore graph (degree 57): results

**Status of this write-up:** draft (theorem refereed, awaiting human pass) ·
**Problem:** Does a 57-regular graph on 3250 vertices with girth 5
(srg(3250,57,0,1)) exist?

## Abstract

We prove a new structural obstruction: if a Moore graph of degree k admits
the "group-of-derangements" construction — all inter-block matchings drawn
from the right-regular representation of a group H of order k−1 > 2 — then
H must be a perfect group (H = [H,H]). Since every group of order 56 is
solvable (Burnside p^a q^b) and hence not perfect, **no group of order 56
can build the degree-57 Moore graph this way**. This closes the non-cyclic
case left open by Smith–Montemanni (Axioms 2026) and subsumes their cyclic
theorem. Epistemic status: complete analytic proof (`perfectness.tex`),
verified line-by-line in-session, independently refereed twice by an
adversarial model pass, with exhaustive-computation corroboration in every
accessible small case. A novelty search (2026-07-22) found no prior
statement; closest prior art is the Hall–Paige single-product obstruction.
Not yet human-refereed or published.

## Result

**Theorem.** Let H be a finite group, |H| > 2, J an index set with
|J| = |H|. If gains (h_ij), h_ji = h_ij⁻¹, over H satisfy the derived
constraints (V), (T), (Q) of the rooted Moore-graph block structure, then
H is perfect. **Corollary.** No group of order 56 admits such gains; the
group-of-derangements ansatz cannot produce the degree-57 Moore graph.
Full statement, proof, and the bridge to Smith–Montemanni's framing:
`perfectness.tex`. Discovery-form notes: `../angles/derangement-56/NOTES.md`.

Also in this problem's scope (see `../results/README.md`): exhaustive k=7
exclusions (Z₆, S₃) corroborating the theorem, quantified negative data on
the m=125 semiregular quotient, and the C₁₉ CEGAR non-convergence result.

## Verification

From a clean clone (Python ≥ 3.11):

```bash
cd problems/moore-graph-57
python3 -m venv .venv && .venv/bin/pip install numpy sympy networkx
.venv/bin/python angles/derangement-56/test_search.py      # independent enumerator, k=7 cases
.venv/bin/python angles/derangement-56/independent_check.py # third-path brute force
.venv/bin/python harness/hoffman_singleton.py               # verifier positive controls
.venv/bin/python harness/test_verifier.py                   # verifier mutation tests
```

(re-verified from this location 2026-07-23; all pass)

Expected: Z₆ → 1680 = 14·120 V-complete leaves, 0 valid; S₃ → 1200 =
10·120 leaves, 0 valid; k=3/Z₂ → feasible, rebuilds Petersen, passes the
exact Moore verifier. Minutes on a laptop. The theorem itself needs only
the two-page proof — the computations corroborate, they do not carry it.

## Method

Rooted block decomposition → gain-graph reformulation (constraints V/T/Q,
proved complete and correct) → the new counting step: for each puncture t,
the x-, y-, and z-lists are all permutations of H∖{e,t}, forcing S_t = S_t²
in the abelianization → every nonidentity element shares one abelianized
image → H perfect or |H| ≤ 2. Machine-assisted throughout: two independent
model implementations plus a from-scratch session enumerator with exactly
matching leaf counts; adversarial model referee passes at theorem and
writeup stage (verdicts in `../JOURNAL.md`).

## What we tried that didn't work

See `../LEARNINGS.md`. Highlights: plain SDP relaxations are provably
non-binding (explicit fractional feasible point); lazy-girth CEGAR does not
converge at d=57 on either the C₁₉ or C₇ equivariant encodings (violations
flat at ~10⁵–10⁶ per model); the b=26 quotient system resists ~30h of
CP-SAT and a 2·10⁹-node DFS in both directions.

## Relation to prior work

Smith–Montemanni [smith-montemanni2026] excluded cyclic H = Z₅₆ and left
the remaining 12 order-56 groups open; our theorem removes all of them at
once and explains why their counting worked. The permutation-system
formulation is Faber–Keegan's [faber-keegan2022]. The abelianization
device generalizes the Hall–Paige necessity lemma [hall-paige1955]. The
surviving-order landscape is Mačaj–Širáň [macaj-siran2010] as sharpened by
Ishida's no-involutions preprint [ishida2026]. All keys:
`../literature/refs.bib`.

## Cite as

See CITATION.cff in this folder (DOI is added by tools/release.py on release).
