# Bounded gaps between primes: below 246

## Statement
Unconditionally, liminf (p_{n+1} − p_n) ≤ 246 (Polymath8b, 2014, building on
Zhang and Maynard–Tao). The frontier: lower 246. Under Elliott–Halberstam-type
hypotheses the bound drops to 12 (EH) / 6 (generalized EH); the parity barrier
blocks 2 by these methods. **This is not a certificate problem — the deliverable
is a smaller proven constant, or a sharp map of why 246 is a wall.**

## Where the number comes from (the attack surface)
The Maynard–Tao sieve reduces the bound to two separable subproblems:
1. **A variational problem**: M_k = sup over admissible weight functions F on
   (a domain containing) the simplex R_k of a ratio of quadratic forms
   I(F), J(F). If M_k > 4, infinitely many admissible k-tuples contain ≥ 2
   primes. Polymath8b got M_k > 4 at k = 50 using an ε-enlarged simplex domain
   and high-dimensional polynomial ansätze — a *numerical optimization with a
   rigorous certification step* (exact rational/interval arithmetic on the
   final quadratic forms).
2. **Narrowest admissible k-tuple**: diameter H(50) = 246 — a finite
   combinatorial optimization, believed optimal for k = 50.

So improvements must come from: (a) certifying M_k > 4 for some k < 50
(known upper bounds on M_k over the *standard* simplex forbid this — map
precisely what is proven for enlarged domains vs merely unexplored);
(b) further domain enlargements / asymmetric weights / degrees of freedom the
2014 optimization did not exploit; (c) partial distribution-level inputs
(Zhang-type equidistribution beyond θ = 1/2, Polymath8a machinery) re-optimized
jointly with (a); (d) verifying H(k) values for any newly viable k.

## "Verifier" for this problem
- Variational claims: the optimizing F is a polynomial with rational
  coefficients; I(F), J(F) are exact rational integrals — the claim M_k > 4 is
  certified by exact arithmetic on one candidate. Ship every claimed bound with
  such a certificate (this IS certificate-shaped at the leaf level).
- Admissible-tuple claims: explicit tuple + residue-class check (exact), and
  exhaustive lower-bound searches logged reproducibly.
- Any claimed prime-gap bound must trace the full pipeline: which theorem
  consumes M_k > 4, with citations.

## First steps
1. Literature sweep: post-2014 improvements or barriers (any movement on 246,
   on M_k bounds for enlarged domains, on equidistribution inputs). Record in
   literature/ with citations.
2. Reproduce the Polymath8b optimization for k = 50 end-to-end with a modern
   stack (their code and ansätze are public); certify M_50 > 4 in exact
   arithmetic ourselves.
3. Re-attack the variational problem with modern tooling: larger/smarter
   ansatz spaces (neural or spectral parametrizations are fine for *search*,
   certification stays exact), asymmetric domains, joint optimization with
   distribution inputs. Map the provable barriers as a first-class deliverable
   (the honest outcome may be "246 is optimal within this framework, here is
   the sharp reason").

## Angle-of-attack menu
- Modern large-scale optimization over enlarged-simplex domains + exact
  certification (SOS/rational rounding).
- Upper-bound theory for M_k on enlarged domains (close the gap from above —
  a proof that the framework caps at 246 is publishable).
- Equidistribution: any usable strengthening of Zhang/Polymath8a exponents,
  re-run the joint optimization.
- H(k) combinatorics for nearby k (admissible-tuple searches, known-optimal
  tables).
