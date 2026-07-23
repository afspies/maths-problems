# Design: C₇-equivariant SAT for the a₀ = 2 case (not yet implemented)

Target: order-7 automorphism g with Fix(g) = K₁,₁ = a fixed edge {r₁, r₂}
(the a₀ = 2 row of Ishida Thm 1.2 / Kováčiková; a₁ = 7·2 + 35 = 49).
Other a₀ ∈ {9,16,23,30,37} have larger fixed stars — separate encodings.

## Orbit structure (root the tree at r₁)

- r₁, r₂ fixed, adjacent. λ=0 ⟹ no common neighbours — consistent.
- Neighbours of r₁: r₂ (fixed) + 56 vertices in 8 free 7-cycles u[c][t],
  c ∈ [8], t ∈ Z₇.
- Blocks (size 56 each):
  - B_R = N(r₂)∖{r₁}: g-invariant AS A SET, internal free action —
    label its leaves (τ, α), τ ∈ Z₇, α ∈ [8], g: τ ↦ τ+1.
  - B[c][t] = N(u[c][t])∖{r₁}: permuted in 8 cycles of 7; equivariant
    labels (c, t, a), a ∈ [56].
- Count: 2 + 56 + 56 + 56·56 = 3250 ✓; g free outside {r₁, r₂} (a₀=2 ✓).

## Variables (all 56×56 permutation matrices)

1. Same-cycle: P[c][q], c ∈ [8], q ∈ {1,2,3} — 24 matrices.
2. Cross-cycle: Q[c][c'][q], c<c', q ∈ Z₇ — 28·7 = 196 matrices.
3. B_R-to-cycle: R[c], c ∈ [8] — the matching (τ,α) ↔ (c,t,a) depends
   only on δ = τ − t; variable x_c[(α,δ), a]; the constraint "each leaf of
   B_R has exactly one neighbour in each B[c][t], and vice versa" is
   EXACTLY the permutation-matrix condition on the 56×56 matrix indexed by
   rows (α,δ) and columns a. — 8 matrices.
Total 228 orbit matrices, 228·56² ≈ 715k primary vars (C₁₉ had 84).

## Constraints

- Permutation rows/cols on all 228 matrices.
- Trace: a₁(g^q) = 49 ⟹ Σ_{c∈[8]} tr P[c][q] = 7 for q ∈ {1,2,3}.
  (Only same-cycle diagonal fixed points contribute; B_R is independent;
  u-cycles contribute nothing — neighbours of r₁ are pairwise
  non-adjacent.)
- Girth via CEGAR as in C₁₉ (violations again leaf-only — but re-prove the
  leaf-only lemma for this shape: now "leaves" = B_R ∪ blocks; edges
  between B_R and blocks exist, B_R internal edges do not).
- Gauge normalization: relabel each u-cycle's leaves (8 × S₅₆) and B_R's
  α-labels... safe minimum: set Q[0][c'][0] = id for c' = 1..7 (uses up 7
  of the 8 cycle relabelings, relative to cycle 0). B_R's labeling
  freedom: S₈ on α × (offset choice) — normalize R[0] to a canonical
  form (e.g. R[0] = id under a chosen (α,δ)→a bijection).

## Validation problem

No small Moore graph has an order-p automorphism with fixed K₁,₁ (Petersen
order-3 fixes one vertex; HoS order-7 fixes one vertex). So validate by:
(a) encode↔decode consistency tests (as angles/c19-sat/test_encoding.py);
(b) drop the trace constraint and run d=7-style sanity on a FAKE small
    parameter set? — no honest analogue; rely on (a) + code review.

## Expected scale

715k vars, ~5M clauses base. CEGAR violation counts will be worse than
C₁₉ (466 leaf-block orbits vs 168). Same convergence concern applies —
consider orbit-matrix-level preprocessing before investing.
