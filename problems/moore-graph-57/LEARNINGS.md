# Learnings — missing Moore graph (degree 57)

Distilled, high-level. Chronological detail lives in JOURNAL.md.

## What the problem actually looks like now (post-literature, 2026-07)

1. **The 2026 state is materially different from the folklore state.**
   Ishida (arXiv:2606.29183, June 2026, preprint): no involutions ⟹ |Aut|
   odd ⟹ only 24 odd orders ≤ 375 remain. Exact displacement counts for
   orders 7/11/13/19. Order 13 acts fixed-point-freely; order 19 fixes
   exactly one vertex. Any session that starts from "|Aut| ≤ 375 and much
   is known about primes" without these is working with a stale map.
2. **Nobody has ever published an exhaustive prescribed-automorphism
   search** — the Russian school + Mačaj–Širáň constrain via character/
   orbit-matrix arguments but never enumerate. This is the gap our
   infrastructure targets. The nearest published computational work
   (Smith–Montemanni 2023/24/26) attacks unstructured optimization and the
   cyclic-matchings ansatz (now analytically excluded by them).
3. **Plain SDP cannot exclude**: the standard spectral LMIs admit an
   explicit fractional solution (root/blocks weights 1, cross-blocks 1/56;
   spectrum 57¹ 7⁵⁷ (−8)⁵⁷ 0³¹³⁵). Only integrality/rank-augmented or
   high-level moment relaxations could bite. Don't burn time on vanilla
   SDP relaxations.

## Headline result of session 1 (2026-07-22)

**Perfectness obstruction (new lemma, angles/derangement-56/NOTES.md):**
a Moore graph of degree k with all inter-block matchings from a group H of
order k−1 > 2 forces H perfect; no order-56 group is perfect (Burnside),
so the entire group-of-derangements route to the degree-57 graph is dead —
subsuming Smith–Montemanni 2026 (cyclic case) and closing their open
non-cyclic case. Proof verified line-by-line by the session driver;
numerics triple-redundant (two codex implementations + a from-scratch
session enumerator with exactly matching counts: 1680 = 14·120 for Z₆,
1200 = 10·120 for S₃, all failing girth constraints); extra predictions
(q=4: Z₄, Z₂² infeasible; q=2: Z₂ feasible → Petersen) all confirmed.
Fresh-context codex referee verdict: see JOURNAL end. Next step: 1-2 page
self-contained writeup; check against the actual S–M PDF before claiming
"closes their open problem" in public.

## What worked

- **Verifier-first discipline**: exact verifier (integer identity + modular
  rank spectral check) validated on C₅/Petersen/HoS with mutation tests in
  <1h of session time. CAUTION (referee finding): "float64 BLAS is exact
  for 0/1 matrices" is NOT portable — Strassen-style dgemm subtracts
  blocks, voiding the bounded-intermediate argument. Certificates use pure
  int64 matmul (minutes, fine); float64 is only OK for candidate
  *selection* where downstream checks are exact.
- **The equivariant-decomposition SAT encoding scales in *structure***: the
  same (d, p) encoder rediscovers Petersen (d=3,p=3) instantly and HoS
  (d=7,p=7) in 37 CEGAR iterations / 0.1s. Pipeline validation on known
  Moore graphs catches encoding bugs cheaply before the d=57 run.
- **Semiregular quotient reformulation**: any semiregular |G| = m gives a
  b×b quotient C with C² + C − 56I = mJ (b = 3250/m). Intersecting M–Š's
  odd-order list with divisors of 3250: semiregular orders are exactly
  {1, 5, 13, 25, 125}. m=125 (b=26) is a genuinely small finite question
  nobody seems to have posed at this granularity.
- **PSD entry caps from the projection structure** (C_ii ≤ r + (d−r)/b,
  C_ij ≤ r + 2(d−r)/b) — free, rigorous, and cut the d=7 node counts ~12×.
- **Parallel delegation**: literature agent + codex adversarial consult ran
  while the verifier was built; both returned load-bearing content.

## What did NOT work (and why)

- **CEGAR-only girth enforcement at d=57 does not converge.** Models
  consistently show ~40–90k triangle violations and ~1M 4-cycle pair
  violations; adding 30k–115k cuts/iteration does not trend violations
  down (solver relocates them). Pattern space is ~10⁸⁺ per constraint
  class. CEGAR was fine at d=7 (≈25 violations/model). Lesson: lazy
  constraints work when the violation count is within a few orders of
  magnitude of the cut budget; here eager structure (orbit matrices,
  algebraic ansatz, stronger propagation) must come first.
- **Naive DFS on the m=125 quotient (b=26)**: 2·10⁹ nodes without finding a
  solution or exhausting. Weak propagation + weak symmetry breaking. CP-SAT
  is the right tool for small-b quadratic integer feasibility (d=7 cases:
  instant). Verdict pending.
- **Trusting "easy kill" arguments without checking against M–Š's list**:
  codex's claimed order-57 exclusion has a hole (assumed Fix(g¹⁹) ≡ 1 mod
  19, but g can act with 3-orbits on a fixed Petersen). M–Š kept 57 in
  their list — that's the ground truth check. ALWAYS test claimed
  exclusions against the surviving-order list.

## Traps for the next session

- **Cluster jobs: pod rescheduling resets the solver, not the Job
  deadline.** CP-SAT cannot checkpoint; a rescheduled pod restarts its
  solve from zero while `activeDeadlineSeconds` keeps counting. With only
  30 min slack over the solver budget, 5/7 pods died verdict-less. Next
  time: deadline ≥ 2× solver budget (or none + a cron reaper), and tee
  progress lines to durable storage so partial evidence survives pod GC.

- **a₁ values for order 19 are Ishida-pinned (preprint)**: M–Š (peer-
  reviewed) allow a₁(x) ∈ {57, 342}. Our C₁₉ run constrains a₁ = 57. For
  an unconditional order-19 claim, also run the a₁ = 342 variant (trace
  bound 18 instead of 3), or condition explicitly on Ishida.
- **CP-SAT INFEASIBLE verdicts are solver-verified, not proof-carrying.**
  Before citing any as a lemma: replicate with an independent method
  (finish the DFS, or a second solver, or an analytic argument).
- **MDPI blocks scraping** — Smith–Montemanni 2026 content is double-
  sourced but not directly fetched; fine for steering, re-verify before
  quoting specifics in anything public.
- **Codex wrapper agents can hang after their job finishes.** The
  derangement job completed at 11:59 but its wrapper never notified (found
  ~5h later). If a codex agent is silent long past its expected runtime,
  check `~/.claude/plugins/data/codex-inline/state/<session>/jobs/*.json`
  for status and read the `.log` tail directly.

## Session 2 (2026-07-22, cont.) — what changed

- **Writeup DONE and doubly reviewed**: angles/derangement-56/writeup/
  perfectness.tex (5pp, compiles). Codex xhigh review found 3 repairable
  blocking issues — the big one: the theorem AS PRINTED must carry the
  h_ji = h_ij^{-1} and |J| = |H| hypotheses (proof uses them; without
  them there is a Z₃ counterexample to the literal statement). All fixed
  same session. Lesson: when extracting a theorem from a constraint
  system, the implicit symmetry conventions of the system must be
  restated as explicit hypotheses.
- **Novelty verdict: appears NEW** (fresh web sweep; S–M has ZERO citing
  papers; closest art = Hall–Paige 1955 necessity lemma — single-product
  obstruction; our variation-over-punctures upgrade to H=[H,H] is
  nowhere). S–M PDF directly read this time (mdpi-res.com attachment URL
  bypasses the MDPI block).
- **TRAP FIXED — S–M Props 1–2 shorthand**: they act on the 56-symbol
  label set (Prop 1 = Wielandt divisor lemma; Prop 2 = outgoing-Φ
  distinctness), NOT on the 3192 non-neighbours. Session-1 shorthand was
  wrong; writeup bridge is now the correct statement. Also: the
  group-free permutation system is Faber–Keegan's (arXiv:2210.09577),
  not S–M's — credit accordingly.
- **C₇ encoder BUILT + validated** (codex, 5/5 tests; my line-by-line
  soundness pass OK): angles/c7-sat/. 2.14M vars / 4.84M clauses; first
  CEGAR iteration tri≈81k quad≈122k violations — same non-convergence
  signature as C₁₉. Do NOT burn budget on long CEGAR runs; eager
  orbit-matrix structure first.
- **m=125 cluster run harvested (2026-07-23)**: a=19 and a=21 UNKNOWN at
  a full 12h × 4 workers each (logs in results/m125-quotient/). Five
  indices (a ∈ {11,13,15,17,23}) LOST: pods rescheduled ~1h44m in, then
  killed by a too-tight Job deadline (see trap below). Cleanup done.
  b=26 has now resisted ~30h total CP-SAT + 2e9-node DFS with zero
  signal either way.
- **All-involutions case banked**: angles/derangement-56/INVOLUTIONS.md
  (parity gives no cheap kill at 56 — FPF involutions there are EVEN;
  first step is extracting the structure of HoS's 21 matchings from S–M
  Fig. 5).

## Session 3 (2026-07-23) — what changed

- **TWO NEW VERIFIED LEMMAS (character machinery, m=125):**
  (1) abelian order-125 lifts force **a = 21 exactly** (mod-3 Fourier
  congruence f(g) ≡ 1 ⟹ tr C ≥ 124 ⟹ a ≥ 18, ∩ mod-4 filter);
  (2) nonabelian order-125 lifts force a ∈ {13,17,21}. NET: bare-C
  UNSAT at a ∈ {13,17,21} kills ALL order-125 semiregular actions;
  a=21 alone kills all abelian ones. The old "a ∈ {13,17} first" plan
  is obsolete — a=21 is the prime target now. All in character_notes.md
  + four verify_*.py scripts (each re-derived from scratch, exact).
- **Abelian a=21 diagonal data is multiplier-orbit rigid**: aggregate
  patterns count 46,376 (Z₅³ = 4-point PG(2,5) multisets) / 126
  (Z₂₅×Z₅) / 1 (Z₁₂₅ — uniquely forced). No analytic kill; Z₁₂₅ is the
  most-constrained lift-level search target if one is ever built.
- **SAT+DRAT pipeline validated** (angles/semiregular-quotient/sat/):
  8.3M-clause fixed-a instances, cube split a=21→8 / a=17→78 / a=13→488,
  d=7 gates + proof-checking gate all green. a=23 laptop probe: 8/8
  cubes TIMEOUT at 120s both variants — no cheap kills at d=57.
- **a=21 cluster campaign prepared but NOT launched** (Alex deferred):
  launch kit in gitignored infra-local/ of the main checkout.

### New traps found this session

- **sympy.simplify false-negatives on cyclotomics**: exp-form ζ₅ matrix
  identities that are exactly zero do NOT simplify to zero; verify over
  Z[ζ] with integer coefficient vectors mod Φ₅ instead (see
  verify_mod3_lemma.py). Never let a FAIL from simplify() kill a true
  identity — and never let simplify() "OK" certify one.
- **Codex sandbox has no network**: git clone/pip inside codex jobs
  fails (workspace-write sandbox, no toggle exposed). Pre-stage sources
  or let the orchestrator shell fetch/build (drat-trim was built
  session-side). pytest is also absent in the venv — unittest works.
- **Crashed-wrapper diagnosis**: an empty codex-inline jobs/ dir means
  the CLI never launched (re-dispatch); a populated jobs/*.json with a
  silent wrapper means check the .log directly (LEARNINGS trap variant).
- **Consult-prompt arithmetic must be re-derived, not trusted**: this
  session's consults caught two real errors in MY framings (offdiag cap
  8→10, mod-25 projector split false) and I caught two in THEIRS (rank
  cap off-by-one, 3120 vs 120 noncentral elements). The
  derive-independently-both-ways loop is earning its cost.

## Next-session priority queue (in order)

1. **Launch the a=21 cube campaign** (kit: infra-local/README.md;
   decide MOD5 variant — recommendation: --mod5, or both side by side,
   16 cores 12h still frugal). Harvest ≈ next day. If any cube UNSAT:
   drat-trim verdict is on the PVC; replicate independently (CP-SAT
   fixed-a=21 already has a 12h UNKNOWN — a second solver or longer
   run) before citing. If all 8 UNSAT+verified: ALL abelian order-125
   semiregular actions are excluded — a citable result (results/ +
   writeup section).
2. a=17 (78 cubes) and a=13 (488 cubes) campaigns complete the
   order-125 kill (nonabelian). Budget ~1 core-day per 8 cubes at 12h;
   prioritize by cube count ascending.
3. Writeup endgame for the perfectness theorem: Alex's human pass, then
   venue/arXiv/release.py. The a=21/{13,17,21} lemmas may warrant a
   short second note once the computational side lands.
4. All-involutions case per INVOLUTIONS.md (start: S–M Fig. 5).
5. C₁₃ fixed-point-free (250 orbits) / C₇ only with eager structure.
6. Any full-scale UNSAT: DRAT/LRAT certificate before claiming, always.

## Infrastructure note (from Alex, 2026-07-22)

Long CPU-bound solver jobs should go to the team CPU cluster (see
AGENTS.local.md and the private infra notes), not the laptop — this
session shared 15 cores
with a sibling Conway-99 session at load average ~54. Constraint: use team
resources sparingly (small CPU requests, single pod, clean up after).
Laptop stays fine for smoke tests and short validations.
