# Handoff prompt — Four-dimensional Kakeya conjecture

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: Four-dimensional Kakeya conjecture — Must every Kakeya set in R^4 have Hausdorff and Minkowski dimension 4?

Work in problems/kakeya-r4/ of the maths-problems repo. Read, in order:
1. /AGENTS.md (repo root) — session conventions: branch `problem/kakeya-r4/<date>-<topic>`,
   stay in your subfolder, exact-arithmetic verification, Codex second opinions
   (GPT-5.6 Sol, xhigh), JOURNAL/LEARNINGS/STATUS updates, board regeneration,
   publishing and DOI rules. If AGENTS.local.md exists, follow it too.
2. problems/kakeya-r4/PROBLEM.md — statement, certificate/verifier spec, known
   structure, attack-angle menu.
3. problems/kakeya-r4/LEARNINGS.md — do what "next session should do first" says.
4. problems/kakeya-r4/JOURNAL.md — recent sessions' detail, if needed.

Current priorities (update each session):
- The exact harness is built and currently has 27 passing tests. Run it before
  changing any exponent claim.
- Treat `13/4` as the sticky benchmark and the corrected Katz–Zahl `>3.059`
  number as the general Hausdorff benchmark. Do not relabel the `3.0543`
  maximal estimate as Hausdorff.
- Treat the polynomial Wolff/QW2 axiom as known for direction-separated
  tubes (Katz--Rogers), not as a conjectural input. The live Bridge B problem
  is multi-grain organization.
- Primary task: prove an extraction dichotomy from small union and graininess.
  Its outputs should be one of: a distributed catalog with explicit `q`; an
  ordered family of about `delta^-1` harmonically transverse ruled patches;
  or a classified degenerate/ill-conditioned quadratic branch.
- Use `results/distributed-quadratic-catalog.md` to turn diffuse catalog
  capture into an explicit polynomial, overlap level, and balanced subfamily.
  Use `results/transverse-quadric-stack-union.md` for the transverse branch.
  Do not silently assume either output.
- The harmonic stack theorem is approved and gives full Minkowski dimension
  for a structured infinite ruled-quadric subclass. It does not give
  Hausdorff dimension. A weighted covering upgrade is a separate target.
- Keep Bridge A separate. Before revisiting it, define a common two-scale
  refinement and a bounded-entropy model selector. Proposition 3.12 alone
  supplies neither. Any proposed gain must be relative to the full
  Theorem 5.4 right-hand side and satisfy `0<c<1/12`.
- Submit any theorem-shaped output to GPT-5.6 Sol xhigh, explicitly asking it
  to audit circularity, model entropy, scale loss, strict hypotheses, and
  Hausdorff-versus-Minkowski consequences.
- The second-session gate is GO on Bridge B. No new general or sticky
  dimension bound was proved, but there is now a genuine semialgebraic union
  theorem for an explicit infinite family of ruled obstructions.
