# Two-variable Jacobian conjecture

## Statement
If F = (f, g): C² → C² is a polynomial map with det J(F) a nonzero constant, is F
injective (equivalently, a polynomial automorphism)?

## Status / context
The July 2026 Alpöge–Fable counterexample lives in C³ (degree 7, Jacobian determinant
≡ -2, three points mapping to one). The plane case is untouched by it and many experts
suspect n=2 may genuinely be true — the two-variable case has much more structure
(Abhyankar–Moh, Newton polygon constraints, known degree bounds: any planar
counterexample must have max(deg f, deg g) > 100 by prior computational work, with
gcd(deg f, deg g) constraints from Moh/Heitmann).

## Two viable directions
1. **Search for a planar counterexample** in the structured families the C³ example
   suggests — start by obtaining/reconstructing the actual C³ counterexample and
   studying its shape (is it a twisted variant of a known near-miss family? does it
   restrict/project to anything planar?).
2. **Structural obstruction**: explain *why* dimension 3 admits degree-7 examples while
   dimension 2 resists — e.g. via the Newton-polygon edge calculus, or by showing the
   C³ example's mechanism intrinsically needs a third variable. A clean lemma here is a
   real deliverable even without settling n=2.

## Verifier
- det J(F) constant: exact symbolic computation (sympy/Sage).
- Non-injectivity certificate: distinct points p ≠ q with F(p) = F(q), verified in
  exact arithmetic (algebraic numbers via resultants / Gröbner, not floats).
- Injectivity of candidates on the other side has no cheap certificate — that's the
  hard direction; don't claim it.

## First steps
- Find and record the exact polynomials of the C³ counterexample (search announcement/
  preprint; store in `c3-counterexample/` with a verification script).
- Re-verify it independently: constant Jacobian + the three-preimage collision.
- Build the planar search harness with Newton-polygon and degree-pair pruning baked in.
