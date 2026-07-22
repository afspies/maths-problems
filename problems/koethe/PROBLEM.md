# Köthe's conjecture

## Statement
(Köthe, 1930) If a ring has a nonzero nil one-sided ideal, does it have a
nonzero nil two-sided ideal? Standard equivalent forms (Krempa and others —
re-verify the exact equivalence chain in the literature pass):
- The sum of two nil left ideals is nil.
- For every nil ring R, the matrix ring M₂(R) is nil.
- For every nil ring R, the polynomial ring R[x] is Jacobson radical.

## Status / context
Open for 95 years; one of the oldest problems in ring theory. Known TRUE for:
PI rings, right noetherian rings (Lanski), algebras over uncountable fields
(Amitsur). The decisive modern development is Smoktunowicz's school of
**explicit graded nil-algebra constructions**: she disproved Amitsur's
adjacent conjecture (a nil ring R over a countable field with R[x] not nil,
2000) by building a graded algebra whose relations are chosen degree-by-degree
via combinatorial counting. That is the template for a Köthe counterexample:
these constructions are *search-shaped* — a space of homogeneous relation
choices with locally checkable conditions — and essentially nobody attacks
them computationally. This is why the problem is on our list.

## Certificate + verifier (subtle — read carefully)
A counterexample is a nil ring R with a non-nilpotent 2×2 matrix over it
(equivalently a non-nil sum of two nil left ideals). Two-layer verification:
- **Finite layer (exact, automatable)**: in a graded algebra presented by
  homogeneous relations, computing whether a given element is nilpotent up to
  degree d, dimensions of graded pieces, and Gröbner–Shirshov normal forms are
  finite exact computations (noncommutative GB: letterplace in Singular, GAP's
  GBNP, Magma). "Matrix m is non-nilpotent up to degree d for all tested d"
  is machine-checkable evidence and a search signal.
- **Infinite layer (needs proof)**: nilness of R itself is an infinite
  condition — a genuine counterexample requires a Smoktunowicz-style
  combinatorial argument (counting/avoidance lemmas guaranteeing every element
  is nilpotent). Any such argument gets adversarial review (Codex xhigh) and
  is the write-up's mathematical core. NEVER claim a counterexample from
  finite evidence alone.
Positive-direction results (Köthe for a new class of rings) are conventional
theorems — same review bar.

## Angle-of-attack menu (be exploratory)
- **Smoktunowicz-template search**: parametrize her graded constructions
  (choices of homogeneous relations over F₂ / countable fields), and search
  the choice space for presentations where a 2×2 matrix resists nilpotency
  degree-by-degree while the counting lemma for nilness of R still closes.
- **Monomial algebras / combinatorics on words**: nilness of monomial algebras
  is governed by combinatorics of forbidden factors (avoidability, growth of
  languages); Köthe-type questions restricted to monomial-like classes may be
  decidable or searchable — map what is known, then search.
- **Golod–Shafarevich counting**: GS algebras are the classical source of
  infinite-dimensional nil algebras; revisit whether GS-style dimension
  counting can be tuned to break M₂-nilness.
- **Positive direction**: push the known-true frontier (e.g. new classes over
  countable fields, graded variants) — partial theorems are publishable and
  sharpen where a counterexample must live.
- **R[x] Jacobson-radical reformulation**: Smoktunowicz's Amitsur
  counterexample lives one equivalence away from Köthe — understand exactly
  why it fails to settle Köthe; the gap is a precise research target.

## First steps
1. Literature map with citations into literature/: the equivalence chain
   (Krempa), known-true classes, Smoktunowicz's constructions (read the actual
   papers, extract the construction as pseudocode), and any post-2020
   movement.
2. Harness: noncommutative Gröbner/normal-form pipeline for graded F₂-algebras
   with per-degree nilpotency testing; validate by reproducing a known
   Smoktunowicz-style object's stated properties in low degree.
3. First search: small relation-choice spaces in the Smoktunowicz template,
   logging per-degree survival of candidate non-nil matrices.
