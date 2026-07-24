# Audit of the 24-cell realization-space input

Primary source: Rastanawi--Sinn--Ziegler, *On the Dimensions of the
Realization Spaces of Polytopes*, arXiv:2007.00645v4 / Mathematika 67 (2021)
[rastanawi-sinn-ziegler-2020].

## Claims used

- The paired vertex--facet incidence model has 192 variables and 144
  bilinear equations for the 24-cell.
- The regular realization has Jacobian rank 140.
- Nonregular members of Paffenholz's four-parameter family have rank at most
  142. This family is only a four-dimensional subset of projective
  realization space; it is not a complete parametrization.
- Proposition 5.8(3) gives eight signed one-parameter centrally symmetric
  families. Their Jacobian has full row rank 144 for \(0<x<1\).
- Consequently an open subset of paired realization space is a smooth
  48-dimensional manifold.

## Independent checks

The displayed signed coordinates were transcribed from the primary PDF, not
from secondary prose. `harness/polytope.py::full_rank_24_cell` reconstructs
them exactly.
At \(x=1/2\), for every sign triple, the rational harness independently
finds:

```text
vertices 24
facets 24
incidences 144
paired-tangent-dimension 48
```

The harness does not use the paper's Sage computation for this point.
The theorem that the symbolic rank stays 144 for the entire open interval is
cited to Proposition 5.8(3).

The new Mahler calculations are independent of the source. Direct
pyramid/cap decompositions and exact moments yield the closed volume and
covariance formulas recorded in
`../results/full-rank-24cell-exclusion.md`.

## Boundaries of the citation

The source does not classify the full 24-cell realization space. It proves
dimension bounds and exhibits smooth and singular loci. No campaign claim
therefore treats either Paffenholz's four parameters or the eight signed
curves as exhaustive.
