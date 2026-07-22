# Rota's basis conjecture

## Statement
(Rota, 1989) Given n bases B₁, …, Bₙ of a rank-n matroid (in particular, an
n-dimensional vector space), can the n² elements always be arranged in an n×n
grid whose i-th row is Bᵢ and whose every column is also a basis? Equivalently:
do n bases always admit n disjoint transversal bases?

## Status / context (as corrected by a Sol xhigh consult, 2026-07-22 — re-verify)
- **Asymptotics essentially done**: Montgomery–Sauermann (2025,
  arXiv:2508.05601) obtain (1−o(1))n disjoint transversal bases for *general*
  matroids, and cover all elements with (1+o(1))n transversal bases; they
  explicitly flag **absorption of the residual defect** as the plausible route
  to the full conjecture. A 2026 paper gives a polynomial-time constructive
  asymptotic version via matroid-intersection coloring.
- **Exact cases**: paving matroids (Geelen–Humphries), strongly base-orderable
  matroids, small n; for even-dimensional vector spaces the Alon–Tarsi
  Latin-square identities apply over suitable fields (odd n is blocked by a
  parity/sign obstruction). Map the exact variant lattice — general matroid vs
  representable vs vector space, characteristic conditions — as a first
  deliverable; claims differ subtly across it.
- The live proof cultures: (1) exchange/cascade packing + absorption;
  (2) matroid intersection / covering / topological methods; (3) Alon–Tarsi
  polynomial identities for representable cases. (Matroid Hodge theory has no
  demonstrated bridge — don't chase it without a concrete idea.)

## Certificate + verifier
- **Per-instance**: given explicit bases, a valid grid is instantly verifiable
  (n rank checks, exact arithmetic / matroid oracle). Non-existence of a grid
  for a specific instance is SAT-decidable with a proof log — so a
  counterexample to RBC (believed unlikely but not excluded for general
  matroids) would be a *finite, DRAT-certifiable object*. Both directions have
  computational footholds.
- **Bridge-lemma work**: candidate absorption lemmas are falsifiable by
  instance search — "every repairable k-defect instance admits a repair
  supported on f(k) rows/columns, independent of n" is testable on adversarial
  instances before anyone tries to prove it.

## The target (per the Sol consult — our adopted plan)
The conjecture has reached "almost all, two complementary senses" status with
an isolated residual defect: exactly the moment a searched absorber/exchange
lemma can matter. Session-one target is NOT a proof attempt; it is **one
falsifiable residual-absorption bridge lemma that the harness has failed to
kill**, backed by exact positive controls and an automated counterexample
search.

## First steps
1. Variant map with citations into literature/ (general vs representable vs
   vector space; even/odd; known-true classes; the Montgomery–Sauermann and
   matroid-intersection-coloring papers read carefully, absorption bottleneck
   extracted precisely).
2. Harness: exact rank oracles (linear over Q/F_p + abstract matroid), grid
   verifier, SAT encoder for grid-completion with proof logging; validate on
   known-true small cases.
3. Adversarial instance library: binary and graphic matroids of rank 5–12,
   maximal near-decompositions; measure minimum repair support for k-defect
   residuals; mine and stress-test candidate f(k)-bounded absorption lemmas —
   minimal counterexamples to a candidate lemma are as valuable as
   confirmations.

## Angle-of-attack menu
- Residual absorption via exchange graphs (primary — see above).
- Matroid-intersection coloring: can the constructive asymptotic pipeline's
  loss be localized?
- Alon–Tarsi: searched algebraic identities for the representable odd case.
- Counterexample hunt on general matroids: adversarial families (spikes,
  free swirls, paving perturbations) through the SAT pipeline.
