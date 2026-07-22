# Zariski cancellation problem, characteristic zero

## Statement
If A is an affine C-algebra with A[t] ≅ C[x₁,…,xₙ,t], must A ≅ C[x₁,…,xₙ]?
True for n ≤ 2 (Fujita, Miyanishi–Sugie for n=2). Open for n ≥ 3 in char 0.

## Status / context
Neena Gupta (2014) settled it negatively in positive characteristic for n ≥ 3, using
Asanuma's threefolds x^m y = F(x, z, t) — explicit affine rings where cancellation
fails, detected by Makar-Limanov / Derksen invariants and exponential-map techniques.
The char-0, n=3 case is open and has exactly the "explicit polynomial algebra, exact
verification" flavor. Related target with the same flavor: tame vs wild automorphisms
of C[x₁,…,xₙ] for n ≥ 4 (Nagata's wildness in n=3 is Shestakov–Umirbaev; n ≥ 4 open).

## Certificate + verifier
A counterexample is a pair of explicit finitely presented C-algebras with:
1. An explicit isomorphism A[t] ≅ C[x,y,z,t] — verifiable by exhibiting mutually
   inverse maps and checking composites are identity (Gröbner bases, exact).
2. A proof A ≇ C[x,y,z] — the hard part; the standard tool is computing the
   Makar-Limanov invariant ML(A) (intersection of kernels of all locally nilpotent
   derivations) or Derksen invariant and showing it differs from the polynomial
   ring's. LND kernels of specific candidates are computable per-degree; full ML
   computation needs a structural argument, as in Gupta's proof.

## First steps
1. Reproduce Gupta's char-p counterexample end-to-end in Sage/Macaulay2 (isomorphism
   check + the invariant computation) — this builds the entire toolchain.
2. Understand precisely where char p enters (Frobenius in the exponential-map
   argument) and search for char-0 substitutes on Asanuma-like families
   x^m y = F(x, z, t).
3. Deliverable even without a solve: an effective LND/ML computation harness for
   threefolds of this shape, plus a map of which deformation directions die in char 0.
