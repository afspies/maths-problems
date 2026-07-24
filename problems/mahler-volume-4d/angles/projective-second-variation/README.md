# Projective second variation

## Idea

Replace the false terminal-pair classification bridge by the full stack of
necessary variational conditions. A local minimizer, in Santaló position,
must be:

1. pair-terminal for all admissible shadow flows;
2. bi-centered, \(c(K)=c(K^\circ)=0\); and
3. positive semidefinite for projective second variations:
   \[
   \operatorname{cov}(K^\circ)\succeq
   (d+2)^{-2}\operatorname{cov}(K)^{-1}.
   \]

The last condition is due to Klartag and has an elementary projective-Hessian
derivation in Balacheff--Solanes--Tzanev.

## Status

**Promising filter, not a completed global bridge.**

The exact interval harness certifies a unique bi-centered representative in
a nonregular Paffenholz 24-cell projective chart and proves that its
covariance Hessian has a negative \(e_1\)-direction. By nonsingularity and
strictness, this excludes an open four-parameter branch of non-pyramidal
24-cell critical bodies from local minimality. Interval normal determinants
also prove the exact representative is connected and pair-terminal; it is
therefore a fully certified object satisfying the first two filters and
failing the third.

## Next proof target

The arbitrary realization-space second variation is now the exact
stress-corrected KKT form in `../realization-stress/README.md`. The next
target is a volume-specific sign theorem for its Schur complement on the
q-regular stress cone. For a pair-terminal non-simplex, combine:

- the facet-coplanarity tangent equations;
- exact first and second moment formulas from a fixed triangulation; and
- dual incidence constraints

to seek a dimension-count theorem producing a negative Hessian direction.
The first test case is the full-rank 24-cell realization space, which has
genuine nonprojective degrees of freedom [rastanawi-sinn-ziegler-2020].

Stop if this becomes face-lattice enumeration. The intended output is a
coordinate-free tangent-space lemma applying to an infinite realization
class.
