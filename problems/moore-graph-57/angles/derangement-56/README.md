# Angle: order-56 group-of-derangements ansatz

**Idea.** Root the Moore graph at a vertex; the 56×56 block structure makes
every inter-block edge set a perfect matching. Assume all matchings come
from the right-regular representation of a group H of order 56 (gain graph
over H on K₅₇) and search/obstruct the gain assignments — the setting of
Smith–Montemanni (Axioms 2026), who excluded cyclic H and left the other
12 groups open.

**Status: RESOLVED (2026-07-22) — the strongest result of the campaign.**

**Verdict.** Theorem (new): any H with |H| = k−1 > 2 supporting such a
gain assignment must be perfect (H = [H,H]). Burnside ⟹ every order-56
group is solvable ⟹ none is perfect ⟹ the entire ansatz dies at degree 57,
closing S–M's open case. Proof: `NOTES.md` (discovery form) and
`../../writeup/perfectness.tex` (refereed writeup). Exhaustive k=7 / k=3
corroboration: `RESULTS.md`, `runs/`, triple-redundant code
(`search.py`, `test_search.py`, `independent_check.py`).

**Open continuation.** The all-involutions subcase (how Hoffman–Singleton
itself is assembled — matchings that do NOT form a group): banked framing
and first steps in `INVOLUTIONS.md`.
