# Explicit Dixmier / Poisson counterexamples

## Statement
Dixmier conjecture: every algebra endomorphism of the Weyl algebra
A₁ = C⟨x, y⟩ / (yx - xy - 1) is an automorphism. Equivalently: if P, Q ∈ A₁ satisfy
[P, Q] = 1, does x ↦ P, y ↦ Q generate all of A₁?

Poisson analogue: every Poisson endomorphism of C[x, y] with {x, y} preserved is an
automorphism.

## Status / context
Stable equivalences (Belov-Kanel–Kontsevich; Tsuchimoto) say: Jacobian conjecture in
dim 2n ⇒ Dixmier in n, and Dixmier is stably equivalent to Jacobian. The July 2026
C³ Jacobian counterexample should therefore falsify Dixmier_n for some n via these
reductions — but the reductions are indirect (they route through positive
characteristic / ultraproducts) and do NOT hand you an explicit endomorphism.

**Goal: directly construct an explicit non-surjective endomorphism of a Weyl algebra
Aₙ (ideally A₁, realistically maybe A₃ by pushing the C³ example through the
reduction machinery made effective).**

## Certificate + verifier
- Candidate: pairs (Pᵢ, Qᵢ) of noncommutative polynomials with [Pᵢ, Qⱼ] = δᵢⱼ,
  [Pᵢ, Pⱼ] = [Qᵢ, Qⱼ] = 0 — exact check by normal-ordering in sympy/Sage
  (Weyl algebra normal form is a finite exact computation).
- Non-surjectivity: harder but certifiable — e.g. show x is not in the image up to a
  degree bound using the Bernstein filtration: the image of the degree-≤d part is a
  finite-dimensional linear subspace; exact linear algebra decides membership per d.
  A non-surjectivity *proof* needs the degree-d obstruction to persist (find the
  structural reason, e.g. a filtration/growth invariant the image can't attain).

## First steps
1. Obtain the C³ Jacobian counterexample polynomials; verify them.
2. Work through Tsuchimoto / Belov-Kanel–Kontsevich to see how effective the
   Jacobian→Dixmier direction can be made on a *specific* counterexample (which n,
   what the endomorphism looks like).
3. In parallel, build the A₁ harness: normal-form computation, [P,Q]=1 solver over
   low-degree ansätze, Bernstein-filtration image-membership checker.
