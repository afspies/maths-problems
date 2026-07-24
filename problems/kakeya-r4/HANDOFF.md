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
- The exact harness is built and currently has 44 passing tests. Run it before
  changing any exponent claim.
- Treat `13/4` as the sticky benchmark and the corrected Katz–Zahl `>3.059`
  number as the general Hausdorff benchmark. Do not relabel the `3.0543`
  maximal estimate as Hausdorff.
- Treat the polynomial Wolff/QW2 axiom as known for direction-separated
  tubes (Katz--Rogers), not as a conjectural input. The live Bridge B problem
  is multi-grain organization.
- Primary task: prove a shaded extraction dichotomy **for every measurable
  cover group**. Retain `delta^o(1)` of its incidence mass in one of only
  `delta^-o(1)` fixed continuum carrier charts. Whole-union extraction at
  unrelated scales proves at most Minkowski information.
- Any carrier output must cross the ordinary `Mdelta` overlap baseline by
  assigned overlap `lambda>>delta`, excess `q-Mdelta`, or a geometric
  exclusion of transverse slab-grid crossings.
- Do not seek subpolynomial ancestry through a full recursive tree:
  `results/one-shot-cover-partition.md` gives an exact hyperplane-bisection
  countermodel with `K≈r^-1`. Instead use one cover-adapted partition of
  degree `n^(1/4)`. Under bounded proposed `s`-cost its quantitatively
  transverse wall mass is summably negligible. The remaining cellular and
  tangent/singular high-degree wall branches are open.
- Use `results/distributed-quadratic-catalog.md` to turn diffuse catalog
  capture into an explicit polynomial, overlap level, and balanced subfamily.
  Use `results/transverse-quadric-stack-union.md` for the transverse branch.
  Do not silently assume either output.
- The fixed continuum harmonic-stack theorem now gives Hausdorff dimension
  four for a structured infinite ruled-quadric subclass. Its smooth explicit
  pencil actually has positive measure locally by a rank-four inverse
  function theorem, so use the abstract covering theorem for rougher fixed
  stacks rather than selling that pencil as a delicate example.
- `results/fixed-stack-hausdorff.md` gives the exact master criterion:
  cover-group retention `b(r)=r^o(1)` yields the needed scale-sensitive
  incidence inequality. It does not supply extraction.
- `results/carrier-extraction-accounting.md` proves that small union alone
  extracts only high multiplicity, gives the hyperplane-grid no-go model,
  and turns an already-extracted small carrier union into low-Jacobian
  energy.
- `results/degenerate-quadric-classification.md` handles nonlinear rank at
  most two and central rank three by 2-planiness, separates hyperplanes and
  conical spines, and isolates indefinite rank-three parabolics. Its exact
  pencil pays a real `rho` loss in the transverse branch.
- `results/rank-two-separated-parabolic-stacks.md` gives a squared-log union
  and fixed-family Hausdorff theorem when
  `sigma_2(A_s-A_t)≳|s-t|`. It also proves exact common-square rigidity for a
  complete clique of rank-one-dangerous differences.
- `results/rotating-rank-one-endpoint.md` proves that affine projective
  rotation is no longer an inner union obstruction. For
  `A_s=A_0+integral_0^s(p+tq)(p+tq)^Tdt`, the full collar multiplicity obeys
  an endpoint `L^(3/2)` logarithmic bound, yielding cubic SSI and Hausdorff
  dimension four for every fixed stack with uniform sweep/collar geometry.
- The live parabolic obstruction is now extraction of a bounded-complexity
  coefficient path, dense approximate rank-one graphs, common-square
  pencils, and projective rotations with higher-order stationary points.
- Lusin selection can make discarded cover incidence a summable additive
  error, but supplies no SSI chart, quantitative modulus, or subpolynomial
  chart count.
- Keep Bridge A separate. Before revisiting it, define a common two-scale
  refinement and a bounded-entropy model selector. Proposition 3.12 alone
  supplies neither. Any proposed gain must be relative to the full
  Theorem 5.4 right-hand side and satisfy `0<c<1/12`.
- Submit any theorem-shaped output to GPT-5.6 Sol xhigh, explicitly asking it
  to audit circularity, model entropy, scale loss, strict hypotheses, and
  Hausdorff-versus-Minkowski consequences.
- The second-session gate remains GO on Bridge B. No new general or sticky
  dimension bound was proved. The fifth session closes the affine-rotating
  rank-one inner estimate and disproves the proposed full-tree ancestry
  route. Do not claim that the remaining high-degree wall
  organization/cellular induction theorem is known.
