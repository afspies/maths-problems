# Casas–Alvero conjecture

## Statement
If a degree-d monic polynomial f ∈ C[x] shares a root with each of its derivatives
f′, f″, …, f^(d-1) (a possibly different root for each), then f = (x - a)^d.

## Status / context
Known true when d = p^k or 2p^k (p prime) via reduction mod p (Graf von Bothmer–
Labs–Schicho–van de Woestijne) and for small d by direct computation. First open
degrees historically: d = 12 was open for a while, current frontier is around
d = 20, 24, 28, … (composite degrees not of the form p^k or 2p^k — e.g. 12 was
settled computationally; **re-check current status per degree first** and record it).
The conjecture is per-degree a purely algebraic finite question — exactly the
Jacobian counterexample's cousin: explicit object, exact verification.

## Certificate + verifier
- **Counterexample**: a degree-d polynomial f (coefficients as exact algebraic
  numbers) that is not a perfect power, plus for each i a common root of f and f^(i).
  Verify with exact gcd computations: gcd(f, f^(i)) ≠ 1 for all i, and f ≠ (x-a)^d.
- **Per-degree proof**: the condition "gcd(f, f^(i)) ≠ 1 ∀i" is Res(f, f^(i)) = 0 ∀i —
  a polynomial system in the coefficients. Casas–Alvero at degree d ⟺ this variety
  is just the (x-a)^d locus. Decidable per degree by Gröbner bases / elimination —
  in practice the computation explodes; the game is finding normalizations,
  weightings, and symmetry reductions that tame it (this is how d=12 fell).

## Approach notes
- Normalize: monic, f(0)=0 root arrangement, scaling action on coefficients — the
  resultant system is weighted-homogeneous; work in the weighted projective quotient.
- Model-guided value: propose good elimination orders, intermediate ideals,
  specializations mod p (a char-p counterexample for p ∤ stuff lifts obstructions),
  and detect structure in the per-degree ideals across d.
- Deliverables: harness (resultant system builder + Gröbner pipeline in
  Sage/Macaulay2/msolve), reproduction of a settled degree (d=12), then attack the
  smallest genuinely open degree.

## First steps
1. Literature check: exact current per-degree status (which d are open as of 2026).
2. Build + validate the pipeline on d = 5..8 (fast), then reproduce d = 12.
3. Smallest open d: try msolve/FGb-scale Gröbner with the symmetry reductions.
