# Angle: C₇-equivariant SAT (order-7 automorphism, fixed edge, a₀=2)

**Idea.** Generalize the C₁₉ encoder to the mixed fixed/free structure of
an order-7 automorphism with two fixed adjacent vertices (a₀ = 2, the
minimal Ishida/Kováčiková displacement case): 228 permutation matrices
(24 same-cycle P, 196 cross-cycle Q, 8 B_R-to-block R), 715,008 primary
variables, orbit-level CEGAR cuts (one clause blocks the whole
7-translate orbit). Full derivation: `DESIGN.md`.

**Status: encoder BUILT and validated (2026-07-22), long runs
deliberately NOT launched.** 5/5 encoding tests pass
(`test_encoding.py`); a line-by-line soundness review of the transpose
conventions, decode consistency, orbit-cut argument, and normalization
freedoms was done by a second model pass. Smoke probe: 2.14M vars /
4.84M clauses built in 3s; first CEGAR iteration shows ~81k triangle +
~122k quad violations — the same non-convergence signature as C₁₉.

**Verdict.** Infrastructure banked; blocked on the same prerequisite as
C₁₉ (eager structural reduction before CEGAR). Trace constraints are
conditional on the a₁ = 7a₀+35 preprint displacement counts — restate
before citing anything unconditional.
