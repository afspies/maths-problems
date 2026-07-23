# Journal — missing Moore graph (degree 57)

Chronological log of what was tried, exact commands, and outcomes.

## 2026-07-22

### Session setup
- Worktree branch `alex/musing-elion-d3e5cb`; project lives in
  `maths-problems/moore-graph-57/` with structure: `harness/` (shared code),
  `angles/<name>/` (one per attack angle), `literature/`, `certificates/`.
- Python venv `.venv` with numpy/sympy/python-sat/networkx; system kissat +
  cadical available.
- Launched two background agents: (1) literature mapper (automorphism
  exclusions, substructure results, prior computational searches);
  (2) Codex GPT-5.6-Sol xhigh adversarial consult on attack-angle priority.

### Milestone: verifier validated end-to-end (goal 1) ✅
- `harness/verify.py` — `verify_moore(A, d)`: 0/1 symmetric, zero diagonal,
  row sums d, A²+A−(d−1)I=J, all exact. Matmul via float64 BLAS — exact
  because all intermediates are integers ≤ 3250 < 2^53 (justified in code).
- `spectral_sanity(A, d)`: exact rank of A−rI, A−sI mod p=10⁹+7 pins the
  multiplicities (rank_p ≤ rank_Q + eigenspace dimension count argument in
  docstring). Handles irrational d=2 case via sqrt mod p (p≡3 mod 4, disc QR).
- `harness/hoffman_singleton.py` — C₅, Petersen, Hoffman–Singleton (Robertson
  pentagon/pentagram construction). All three PASS both checks.
- `harness/test_verifier.py` — mutation tests: edge removal, degree-preserving
  2-switch, asymmetry, loops, wrong size, random 7-regular graph — all
  correctly REJECTED. Timing: full verify at n=3250 ≈ 0.3 s.
- Command: `.venv/bin/python harness/hoffman_singleton.py && .venv/bin/python harness/test_verifier.py`

### Literature map complete (goal 2) ✅
- Background agent produced `literature/exclusion-map.md` (fully cited).
  Key updates over PROBLEM.md's summary:
  - **Ishida 2026 (arXiv:2606.29183, VERIFIED on arXiv): no involutions;
    |Aut| is ODD.** Only 24 odd orders ≤ 375 remain (Mačaj–Širáň list).
  - Exact displacement counts (order 7: a₀∈{2,…,37}, a₁=7a₀+35; order 11:
    a₀=5; order 13: a₀=0 — semiregular!; order 19: a₀=1, a₁=57).
  - No published exhaustive search under ANY prescribed automorphism —
    genuine gap our infra targets.
  - Smith–Montemanni 2026 (Axioms 15(5):332, DOI resolves): all-matchings-
    cyclic excluded; the 12 non-cyclic order-56 derangement groups OPEN.
  - Makhnev's 2020 nonexistence claim REBUTTED (Faber–Keegan 2210.09577);
    problem is open.
- Codex (GPT-5.6 Sol, xhigh) adversarial consult recorded. Ranking:
  (1) C₁₉-equivariant SAT (1 fixed vertex, 84 permutation orbits);
  (2) non-cyclic order-56 derangement-group gain-graph search;
  (3) C₇ with a₀=2. Rejected: plain SDP (provably feasible — explicit
  fractional point), 3–4-block local gluing (too loose), order-2 (Ishida),
  order-57 (dies on character integrality via 3∤ trace argument).
  Missing angle flagged: modular rep theory at p ∈ {3,5}.

### Angle: semiregular quotient scan (new observation)
- For ANY group G acting semiregularly with |G| = m: quotient C is b×b
  symmetric (b = 3250/m), row sums 57, **C² + C − 56I = m·J**; C[i][i] even
  when m odd. Nonexistence of C ⟹ exclusion of all semiregular order-m
  actions. Combined with M–Š odd list ∩ divisors of 3250:
  **semiregular orders are exactly {1, 5, 13, 25, 125}** — m=125 (b=26) is
  the top case. `angles/semiregular-quotient/quotient_scan.py` (DFS with
  sum/sumsq/Cauchy–Schwarz pruning + diagonal symmetry breaking).
  d=7 self-tests: m=25,10,5 all FEASIBLE fast (HoS sanity ✓).
  d=57 m=125 scan RUNNING (bg).

### Angle: C₁₉-equivariant CEGAR SAT (Codex's #1) — built + validated ✅
- `angles/c19-sat/equivariant_sat.py`: general (d,p) encoder, permutation-
  matrix vars per block-pair orbit (84 orbits × 56² = 263k vars for d=57),
  a₁ trace constraints (Σ_c tr P[c][q] = 3), gauge normalization
  Q[0][c'][0] = id, lazy girth clauses (CEGAR; each added clause is a girth-5
  consequence ⟹ UNSAT would be a valid conditional nonexistence proof).
- Validation: d=3,p=3,a₁=0 → Petersen (instant); d=7,p=7 → HoS in 37
  iterations (0.1s). Both pass exact verifier. `angles/c19-sat/validate.py`.
- d=57 run launched (2h budget, cuts persisted to d57_cuts.txt, resumable).

### Delegated: order-56 derangement gain-graph search → Codex agent (bg)
- Full spec incl. derivation, symmetry breaking soundness requirements,
  smoke tests (k=3/H=Z₂ must find Petersen; k=7/H=Z₆ must be INFEASIBLE
  by S–M counting; k=7/H=S₃ informative either way), analytic-first
  attempt to generalize S–M's counting to abelian groups.

### Codex order-57 claim — HOLE FOUND (do not cite)
Codex asserted order-57 automorphisms are "already dead": g⁵⁷=1 ⟹ g³ has
order 19 ⟹ fixes unique v ⟹ g fixes v; then claimed |Fix(g¹⁹)| ≡ 1 mod 19.
That last step is wrong: g acts on Fix(g¹⁹) with orbit sizes 1, 3, 19, 57;
if Fix(g¹⁹) ≅ Petersen (10 = 1 + 3·3 vertices), g can act on it with order
3 (Aut(Petersen) = S₅ has order-3 elements). No contradiction. Consistent
with M–Š keeping 57 in their allowed list. Lesson: verify every "easy
kill" claim against the M–Š list before using it.

### Semiregular m=125: DFS inconclusive → CP-SAT pivot
- DFS burned 2·10⁹ nodes (~35 min) without finding a solution or exhausting:
  UNKNOWN. (Contrast d=7 analogues: feasible within hundreds of nodes —
  weak-propagation DFS is the wrong tool at b=26.)
- Built `angles/semiregular-quotient/cp_quotient.py` (OR-Tools CP-SAT,
  same math, same sound symmetry breaking + PSD caps; d=7 self-tests
  instant). d=57 m=125 launched (3h limit, 8 workers). NOTE: a CP-SAT
  INFEASIBLE is solver-verified only (no exportable proof) — would need
  independent replication (e.g. the DFS run to completion, or a second
  solver) before citing as a theorem.

### C₁₉ CEGAR — quantitative negative signal
First 17 iterations: violations per model hold at ~40–80k triangles and
~1M 4-cycle pairs, NOT decreasing; solver pushes violations around rather
than converging. Restarted with all-triangles + 100k-quad cuts per
iteration (cuts persist in d57_cuts.txt and reload across restarts).
Realistic assessment: plain CEGAR won't converge at this scale; the run is
kept as accumulating infrastructure + lottery ticket.

### Codex referee report on session math (GPT-5.6 Sol xhigh) — verdicts
- A (quotient equation): CORRECT (clean proof via orbit-incidence matrix R,
  AR = RC, R^T R = mI).
- B (semiregular orders {1,5,13,25,125}): CORRECT-WITH-CAVEAT — my
  factorization typo 3250 = 2·5⁴·13 → actually 2·5³·13 (set unaffected;
  FIXED in literature/exclusion-map.md). Also: phrase as "candidate
  orders" (existence not asserted), conditional on Ishida for evenness.
- C (PSD caps 8/10): CORRECT; proof gap (needed C_ii ≥ 0 ⟹ E_ii ≤
  (r+a)/(r−s), not E_ii ≤ 1) — docstring FIXED.
- D (canonicalization): CORRECT. Found cp_quotient.py missed C[0,2]≤C[0,1]
  (weaker breaking only, no soundness issue) — FIXED for future runs; the
  in-flight m=125 run uses the weaker version (still sound).
- E (character/Galois, a ∈ {13,17,21} for abelian lifts): CORRECT,
  including the J-transform and multiplicity bookkeeping. Rank prime must
  avoid {2,3,5,13} — noted in character_notes.md.
- F (leaf-only violations; girth-5+regular ⟹ srg): CORRECT.
- G (float64 BLAS exactness): WRONG as a portable claim — Strassen-style
  dgemm does subtractions that void the bounded-intermediate argument.
  FIXED: verify.py now uses pure int64 matmul (~3 min at n=3250 under
  load); CEGAR keeps the float fast path for candidate SELECTION only
  (cuts are built from exact integer adjacency; unsoundness impossible,
  comment added).
- Upgrade path for citable claims (recorded): CP-SAT infeasibility needs
  independent replication; CEGAR-UNSAT needs frozen CNF + cut manifest +
  DRAT/LRAT with an external checker; unconditional order-19 exclusion
  needs the a₁=342 branch too.

### C₁₉ CEGAR final result: TIMEOUT (negative data, quantified)
3h budget exhausted: 229 iterations, 20.5M clauses (18.7M persisted cuts in
angles/c19-sat/d57_cuts.txt), violations FLAT from start to finish
(~55–90k triangle pairs, ~0.9–1.3M 4-cycle pairs per model; no downward
trend whatsoever). Command: `.venv/bin/python angles/c19-sat/run_d57.py
10800`. Conclusion: pure lazy-girth CEGAR on the 84-orbit permutation
encoding does not converge at d=57 — eager structural reduction
(orbit-matrix level, algebraic ansatz, or per-block-triple eager encoding
of a SUBSET of triangle constraints) is required first. Cuts file kept for
possible reuse but reload cost (~19M clauses) likely exceeds value.

### CP-SAT m=125 verdict: UNKNOWN at 3h — question confirmed hard
`cp_quotient.py 57 125 10800` (8 workers, shared machine): status UNKNOWN,
466,612 conflicts, 1,667,484 branches, 34.6M LP iterations. Neither a
quotient matrix nor an infeasibility proof. Combined with the DFS run
(2·10⁹ nodes, no solution), the b=26 quadratic system resists laptop-scale
attack from both directions. Signal: solutions, if any, are rare — d=7
analogues (b=2,5,10) were instant. Next: re-run on the team CPU cluster (frugal usage) with a longer
budget; ALSO worth trying the fixed-a decomposition (add the constraint
tr C = 15a − 143 for each a ∈ {11,...,23} separately — seven smaller
problems, each more constrained; the abelian-lift filter needs only
a ∈ {13,17,21}).

### Fixed-a probe (a=11): also UNKNOWN at 1h
`cp_quotient.py 57 125 3600 11`: UNKNOWN; ~33M conflicts on the strongest
subsolver. Fixed-trace decomposition does NOT qualitatively ease the b=26
system on laptop budgets. Cluster plan: long budgets (12h+), 7 parallel
fixed-a jobs (a ∈ {11,...,23} odd) + possibly a pure-SAT bit-blasted
encoding with DRAT output as the replication path.

### ⭐ Derangement-56 angle RESOLVED: perfectness obstruction (new lemma)
The codex implementation agent (job completed 11:59; its wrapper hung and
never notified — found via the codex job state file) returned far more
than the requested search: a clean analytic theorem, written up in
angles/derangement-56/NOTES.md.

**Theorem.** If a Moore graph of degree k admits the group-of-derangements
ansatz (all inter-block matchings from the right-regular representation of
a group H, |H| = k−1) and |H| > 2, then H is perfect (H = [H,H]).
Proof sketch: for gain vertices a,b with t = h_ab, the lists x_i = h_ai,
y_i = h_ib, z_i = x_i·y_i are each permutations of H∖{e,t} (via V/T/Q);
abelianizing, S_t = S_t² ⟹ S_t = e ⟹ all nonidentity elements share one
abelianized image ⟹ H perfect or |H| ≤ 2.

**Corollary.** No group of order 56 is perfect (Burnside p^a q^b ⟹
solvable), so NO group of derangements yields the degree-57 Moore graph —
closing the non-cyclic case that Smith–Montemanni (Axioms 2026) left open,
and subsuming their cyclic theorem.

**Verification performed (session driver):**
1. Line-by-line proof check — the nonabelian step x_i y_i y_j⁻¹ x_j⁻¹ =
   z_i z_j⁻¹ is exact (no hidden commutativity); counting q−2 = |H∖{e,t}|
   checks; endgame (kernel trivial ⟹ |H| ≤ 2) checks.
2. Triple-redundant numerics at k=7: codex production DFS (UNSAT),
   codex independent enumerator (14/10 V-complete leaves, 0 valid),
   MY from-scratch full-space brute force (angles/derangement-56/
   independent_check.py): infeasible, leaf counts 1680 = 14·120 and
   1200 = 10·120 — exact match with first-row-fixed counts × 5!.
3. Positive control k=3/H=Z₂: feasible, Petersen verified (both codex and
   my checker).
4. Extra prediction tests: q=4 (H = Z₂×Z₂ and Z₄) both infeasible by brute
   force, as the theorem demands.
5. Fresh-context codex referee launched on the theorem (pending).

**Caveat for any writeup:** "closes S–M's open case" presumes their exact
framing (their PDF was never directly fetched — MDPI blocks scraping; the
order-56-exactly lemma is theirs, used as stated by two independent
research passes). The theorem itself is self-contained and independent of
their paper.

### Fresh-context codex referee verdict on the perfectness theorem
(Originally committed to the worktree-root JOURNAL.md by mistake; moved
here 2026-07-22 session 2.)
All eight attack points addressed: PASS on the y-list inverse-set step,
the nonabelian 4-cycle orientation, all counts, the endgame (incl. V₄
loophole check — referee brute-forced V₄ and Z₃ itself: 6 resp. 2
V-complete assignments, 0 valid, theorem-consistent), the |H|>2 boundary
(Petersen recovered at q=2), necessity+sufficiency of (V,T,Q), and the
Burnside chain. PARTIAL on point 8: the theorem is consistent with and
subsumes Smith–Montemanni (their cyclic contradiction 27 mod 56 drops out
as the t=1 special case), and the referee DIRECTLY INSPECTED their PDF
(iris.unimore.it) confirming the noncyclic case was open — but a journal
writeup must add the explicit bridge (S–M Props 1–2: semiregular ⟹
|G| = 56 ⟹ regular ⟹ right-regular after relabeling).
**Overall: theorem correct; corollary correct; sharper dichotomy proved
(solution ⟹ H perfect or |H| ≤ 2).** Referee's writeup checklist (9
items: explicit index sets, the two adversarial algebra steps written out,
formal V/T/Q lemma, normalization calculation h_ij = g_1i g_ij g_1j^{-1},
the S–M bridge, narrow phrasing — "excludes the group-of-derangements
case", formal Burnside citation, computation-as-corroboration wording,
priority/novelty search) recorded for the writeup session.

### Session 1 wrap
Goals: (1) verifier ✓ validated + mutation-tested + referee-hardened;
(2) literature map ✓ with 2026 state (Ishida, S–M) and verification notes;
(3) multiple angles ✓ — C₁₉ SAT (built, validated, quantified negative),
semiregular quotients (new reduction, m=125 confirmed hard, character
machinery ready), derangement-56 (RESOLVED: perfectness obstruction, new
lemma, doubly refereed), SDP (rejected on principled grounds — explicit
feasible point). All work committed on alex/musing-elion-d3e5cb.

## 2026-07-22 — session 2

### m=125 fixed-a decomposition moved to the k8s cluster
- Verified a-window independently: tr C = 15a − 143 ≥ 0 ⟹ a ≥ 10; C_ii
  even ⟹ trace even ⟹ a odd; diag_cap = 8 ⟹ trace ≤ 208 ⟹ a ≤ 23.
  Odd a ∈ {11,…,23}: the 7 jobs exhaust m=125.
- `cp_quotient.py` gained a workers CLI arg (argv[5]).
- Launched indexed cluster Job `alex-moore125-fixed-a` (7 pods x 4 CPU/4Gi,
  python:3.12-slim + pip ortools, tl=43200s, workers=4; job manifest kept
  in private infra notes, not in this repo). All 7 pods admitted and
  solving within ~2 min of apply. Harvest ~2026-07-23 morning; CLEANUP
  MANDATORY (job + configmap).

### Perfectness theorem writeup (checklist items 1–8)
- `angles/derangement-56/writeup/perfectness.tex` (compiles, 5pp):
  explicit index sets I/J, formal Lemma 1 (blocks) + Lemma 2 (gain
  conditions, stated over the ASSEMBLED graph to avoid circularity, both
  directions), normalization calc h_ij = c_i g_ij c_j^{-1} with
  c_j = g_1j, the two adversarial algebra steps written out verbatim
  (inverse-set for the y-list; the no-commutativity 4-cycle identity),
  endgame dichotomy, Burnside citation (Proc LMS 1904), narrow-scope
  phrasing throughout, computation-as-corroboration section separated
  from the proof.

### Novelty/priority search (fresh web agent) — VERDICT: appears NEW
- S–M 2026 PDF directly fetched this time (mdpi-res.com attachment URL
  works). Google Scholar: ZERO citing articles; Semantic Scholar doesn't
  index the DOI; arXiv full-text sweep finds nothing equivalent.
- CORRECTION to session-1 shorthand: S–M Props 1–2 are about the
  56-symbol LABEL SET, not the 3192 non-neighbours. Prop 1 = Wielandt
  (semiregular order divides degree); Prop 2 = outgoing Φ's pairwise
  distinct (4-cycle argument) ⟹ |H| = 56 exactly ⟹ regular. Writeup
  bridge paragraph rewritten accordingly.
- Faber–Keegan (arXiv:2210.09577) own the group-free permutation system
  (their Thm 4 / Cors 5–6 = our V/T/Q before the group specialization);
  intro rewritten to credit them.
- Closest classical art: Hall–Paige 1955 necessity lemma (complete
  mapping ⟹ product of all elements ∈ [G,G]) — same abelianization
  device; our variation-over-t upgrade to H = [H,H] appears nowhere.
  Related-work remark + HP/Dénes–Hermann/FK citations added to writeup.
- S–M's own text predicted a proof would need "larger configuration"
  of the Φ_ij — exactly what (T)+(Q) provide. Their Fig. 5: HoS from
  involutions NOT forming a group (consistency at k=7 noted in writeup).

### Codex xhigh review of the writeup — verdict + fixes applied
Initial verdict FAIL-as-written (all repairable; all core algebra PASSED
adversarial S₃ checks, S–M bridge PASSED, scope hygiene PASSED):
1. BLOCKING: Theorem 3 as printed dropped the h_ji = h_ij^{-1}
   hypothesis its proof uses (codex gave a Z₃ counterexample to the
   literal statement). FIXED: hypothesis (+ |J| = |H|) added to theorem
   and corollary; proof's "|J|=q by (V)" mis-citation removed.
2. BLOCKING: "girth forces matchings to be derangements" parenthetical
   imprecise (normalized M_1j = id is the opposite). FIXED: fixed-point-
   freeness is identification-dependent; stated for non-reference blocks
   in the normalized labelling.
3. BLOCKING: "smallest perfect group is A5" → "smallest NONTRIVIAL".
4. Non-blocking fixes applied: exactly-k²+1 counting + explicit
   girth-exactly-5 argument in Lemma 2's proof; Hall–Paige claim narrowed
   (sufficiency only for solvable; converse = H–P conjecture, later);
   footnote softened (corroboration = small accessible cases); A/I/J
   notation collision removed (Moore identity now M²+M−(k−1)I = 11^T);
   unused \ab macro dropped.
All fixes applied and recompiled same session; ready for a human pass.

### C₇ (a₀=2, fixed-edge) equivariant encoder — BUILT + validated (codex)
angles/c7-sat/: equivariant_sat.py, test_encoding.py (5 tests, all pass:
edge_var round-trip/equivariance, hand-planted decode 57-regular +
g-invariant, trace counting, 715,008 primary vars, mixed B_R/cycle cut
invariance), run_d57.py. Smoke: 2,143,296 vars / 4,838,470 clauses built
in 3s; first CEGAR iteration tri=81,494 quad=122,080 violations,
+148,650 cuts — same non-convergence signature as C₁₉, as DESIGN.md
predicted. Cut persistence + reload verified (c7_cuts.txt).
Codex's flagged risks (recorded): trace constraint conditional on
Ishida/Kováčiková a₁=49; gauge-normalization justification and
single-clause-per-orbit cut soundness deserve independent review before
any UNSAT claim. NOT launching a long run — orbit-matrix-level eager
structure needed first (C₁₉ lesson).

## 2026-07-23

### m=125 cluster harvest: a=19 and a=21 UNKNOWN at 12h; five indices lost
- Job `alex-moore125-fixed-a` finished. Completed indices (full 43,200s
  walltime, 4 workers): **a=19 UNKNOWN** (275.8M conflicts, 375.3M
  branches, det-time 93,475) and **a=21 UNKNOWN** (det-time 94,466).
  Full solver logs: `results/m125-quotient/moore125_a19.log`, `_a21.log`.
- **INCIDENT (verdicts lost):** 5 of 7 pods (a ∈ {11,13,15,17,23}) were
  rescheduled by the cluster ~1h44m into the run (CP-SAT has no
  checkpointing → solves restarted from zero) and were then killed by the
  Job's `activeDeadlineSeconds: 45000` — the deadline had only 30 min of
  slack over the 43,200s solver budget, so restarted pods could never
  finish. Their logs were garbage-collected with the pods. No verdicts
  for those five a values.
- Cleanup done: job + configmap deleted; no solver workloads left.
- Net new knowledge: the b=26 quotient system resists 12h × 4-worker
  CP-SAT at fixed a ∈ {19, 21} (adds to: DFS 2·10⁹ nodes, 3h + 1h laptop
  CP-SAT). a=21 matters — it is in the abelian-lift character filter
  {13,17,21}. Still zero evidence in either direction on feasibility.

### Migration into afspies/maths-problems
- This problem folder moved from the playground worktree (branch
  `alex/musing-elion-d3e5cb`, final commit 8fa70be; backed up to the
  private playground remote as `archive/moore-graph-57-d3e5cb` @ a3508c7
  with the two oversized solver-cut files filtered from history) into
  `afspies/maths-problems` `problems/moore-graph-57/` on branch
  `problem/moore-graph-57/2026-07-23-import`, restructured to repo
  conventions: theorem writeup → `writeup/` (perfectness.tex + report.md),
  citable/negative artifacts → `results/`, per-angle READMEs added,
  private infra details removed per AGENTS.local.md (job manifest stays
  in the playground branch only). Large regenerable artifacts (19M-clause
  `d57_cuts.txt`, `c7_cuts.txt`) were NOT migrated — regenerate via each
  angle's `run_d57.py` if ever needed.

## 2026-07-23 — session 3 (m=125: analytic + proof-carrying SAT)

Branch `problem/moore-graph-57/2026-07-23-m125-analytic-sat` (canonical repo,
worktree). Executing LEARNINGS queue item 1.

### Session-side exact verification (laptop, minutes)
- `angles/semiregular-quotient/verify_mod5_and_filter.py`: independent
  re-derivation of the abelian a-filter {13,17,21} (Galois orbits 4/20/100
  on all three abelian order-125 groups ⟹ a ≡ 1 mod 4) — all checks pass.
  NEW: mod 5 the quotient equation collapses to (C−2I)² ≡ 0 (x²+x−56 ≡
  (x−2)² mod 5), so C ≡ 2I + N, N symmetric nilpotent, N·1 ≡ 0. Mod-25
  "projector split" idea is FALSE (7−17 not a unit mod 25) — caught by the
  codex consult below.

### Codex xhigh consult #1 (attack design; job task-mrxkyl6j-1uh38n)
First dispatch lost to a host restart before the CLI launched (empty jobs
dir — the LEARNINGS wrapper-hang trap has a new variant: check the jobs/
dir to distinguish "never started" from "finished, wrapper hung").
Second dispatch completed. Verdicts: one-hot + totalizer SAT encoding;
existing symmetry breaking sound but incomplete; row-0 pattern DP cube
split (a=21,23 collapse to ~8 cubes); mod-5 structure correct but their
rank cap min(a,25−a) was off by one (corrected: min(26−a, a+1, 12));
offdiag cap is 10 not 8 (my prompt's error, caught against repo files);
and a NEW mod-3 analytic claim: abelian lifts force a = 21.

### Mod-3 lemma VERIFIED (session, from scratch)
`angles/semiregular-quotient/verify_mod3_lemma.py` — 38/38 exact checks:
- Derivation: 125 f(g) = 15a + 65 + 15 T(g) for g ≠ 0 (Fourier inversion
  + per-character trace identities, T(g) ∈ Z by Galois invariance of m₇);
  mod 3 ⟹ f(g) ≡ 1, so f ≥ 1 on 124 elements ⟹ tr C = 15a−143 ≥ 124
  ⟹ a ≥ 18 ⟹ a = 21 after the mod-4 filter.
- Machinery validated end-to-end on a REAL object: HoS with the Robertson
  shift automorphism (order 5, FPF) — b=10 quotient, a=8, all four
  character blocks satisfy (Ĉ−2I)(Ĉ+3I) = 0 exactly over Z[ζ₅]
  (hand-rolled integer cyclotomic arithmetic; sympy.simplify was NOT
  trusted — it false-failed on exp-form zeta), f ≡ 5 matches the identity.
- **LEMMA (new): any abelian order-125 semiregular lift has a = 21.**
  Kills the planned a ∈ {13,17} abelian targets analytically. Banked in
  character_notes.md; commit a06e977.

### In flight (background codex jobs, gpt-5.6-sol xhigh)
- SAT+DRAT encoder build per consult design (angles/semiregular-quotient/
  sat/): one-hot, totalizer, cubes, optional mod-5 clauses, d=7 validation
  gates, drat-trim build. No long runs authorized.
- Analytic follow-up: rigorize nonabelian sketch (central f(g) ≡ 1 mod 3,
  coset counts F(ḡ) ≡ 2 mod 3 ⟹ only a ≥ 13 so far; degree-5 irrep
  constants need exact care) + session's tentative reduction of abelian
  a=21 diagonal data to multiplier-orbit multiplicities (Z₅³: a 4-point
  multiset in PG(2,5); Z₁₂₅: e forced uniquely; Z₂₅×Z₅: six values
  summing to 4) — unverified until that job reports.

### Analytic follow-up consult #2 (job task-mrxmbfks-nld0kj) — results
Session-replicated (both scratch scripts re-run, all checks pass; promoted
to verify_a21_rigidity.py + verify_nonabelian_characters.py):
- **Nonabelian theorem: order-125 nonabelian lifts force a ∈ {13,17,21}.**
  Central g: f(z) = 208 − 3μ ≡ 1 mod 3 (μ = common deg-5 multiplicity,
  61 ≤ μ ≤ 69); noncentral cosets: F(q̄) ≡ 2 mod 3; a ≥ 13; Galois mod-4
  extends (deg-5 irreps form one 4-orbit). My sketch's 3120-noncentral
  count was wrong (120), constants otherwise held (−1040 correct).
- **Abelian a=21 rigidity:** e = (f−1)/3 is multiplier-orbit constant,
  Σe = 16 ⟹ aggregate diagonal patterns: Z₅³ = 4-point multisets in
  PG(2,5) (46,376, all pass), Z₂₅×Z₅ = 126, Z₁₂₅ = UNIQUE (f = 13 on
  the four order-5 elements, f = 1 on the other 120). m₇ ∈ [11,17]
  windows. No analytic kill — verdict (C): needs computational
  completion. Z₁₂₅ is the most-constrained lift target.
- **CAMPAIGN REDUCTION: bare-C UNSAT at a ∈ {13,17,21} kills all
  order-125 semiregular actions; a=21 alone kills all abelian ones.**
  Commit d2ebbea.

### SAT+DRAT encoder (codex job task-mrxm44zx-64xr2y) — BUILT, gates green
angles/semiregular-quotient/sat/ (commit f8152d6): one-hot entries +
deterministic binary product buses (codex rejected the forward-only aux
variant as unsound) + truth-table ripple adders (hand-rolled; pip
install blocked in codex sandbox) + row-0 cube DP (consult's square-sum
formula corrected to 181−h−h²; counts 218/241/169/70/8 nevertheless
reproduced exactly) + optional theorem-backed mod-5 automata clauses.
Sizes: 297,840 vars / 8,294,680 clauses per fixed-a instance (374,085 /
11,617,662 with --mod5). Cubes: a=21 → 8, a=17 → 78, a=13 → 488,
a=23 → 8. Validation: d=7 analogues (m=25,10,5) SAT + exact int64
decode-verified; deliberate UNSAT proof drat-trim VERIFIED; cube-union
soundness confirmed; 5/5 unittest gates pass after session-side
drat-trim build (codex sandbox has NO network — clone done by
orchestrator shell from marijnheule/drat-trim, gcc make clean).

### a=23 laptop probes (local, ~35 min wall total)
run_and_check.py on both a=23 cube dirs (8 cubes each), 120s/cube:
ALL TIMEOUT in both variants (plain and --mod5). No cheap kills at
d=57; no variant discrimination at this budget. Probe outputs preserved
in session task logs; instances regenerable deterministically.

### a=21 cluster campaign: PREPARED, LAUNCH DEFERRED (Alex's call)
Launch kit (job.yaml + runner.sh + instructions) in the gitignored
problems/moore-graph-57/infra-local/ of the MAIN checkout (private infra
per AGENTS.local.md — 8-core single pod, 12h kissat/cube, deadline
90000s > 2× budget, on-pod drat-trim, durable PVC teeing, no proofs on
the shared PVC). Alex asked to stop before launching; next session
launches after the MOD5 variant decision.
