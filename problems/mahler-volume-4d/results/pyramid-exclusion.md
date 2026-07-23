# The sharp Mahler inequality for all 4-pyramids

## Result

Every 4-dimensional pyramid \(P\) satisfies
\[
\mathcal P(P)\ge 3125/576,
\]
with equality if and only if \(P\) is a 4-simplex.

The proof uses the exact identity
\[
\mathcal P(\operatorname{pyr}_d K)
=\frac{(d+1)^{d+1}}{d^{d+2}}\mathcal P(K)
\]
and the audited three-dimensional Mahler theorem of Chen--Li--Xi--Xu. The
polar-section derivation, including identification of the pyramid's Santaló
point, is in `angles/pyramids/README.md`.

## Independent terminal-polytope certificate

There is also a separate proof that a pair-terminal 4-pyramid is a simplex.
Its finite certificate has three components:

1. the repaired dimension-four face-lattice persistence argument and the
   minimizer-to-terminal chain in `literature/shadow-flow-audit.md`;
2. the natural speed-space isomorphisms for a pyramid and its 3D base in
   `angles/pyramids/README.md`; and
3. the 3D dual-pair counting lemma from Section 5 of
   Chen--Li--Xi--Xu, whose proof uses only face-lattice duality.

Together they force the base of a pair-terminal 4-pyramid to be a tetrahedron.
This route excludes non-simplex pyramids from any bounded-vertex-class
minimum even without using the direct product factorization.

## Reproduction

The realization-level sanity check uses exact rationals:

```bash
python3 -m unittest discover -s problems/mahler-volume-4d/harness -v
```

The test `test_pyramid_tangent_speed_dimension_matches_base_pattern` checks a
pyramid over the 3-cube. No seeds, floating point arithmetic, or face-lattice
database are used.

## Scope

This proves the full sharp conjectured inequality on an infinite geometric
family. It does not prove the 4D Mahler conjecture for non-pyramidal bodies and
makes no claim that the present flag inequalities classify all non-simple,
non-simplicial terminal 4-polytopes.
