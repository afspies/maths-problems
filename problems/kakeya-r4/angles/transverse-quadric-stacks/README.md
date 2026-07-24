# Transverse stacks of ruled quadrics

## Status

The harmonic transverse-grain union lemma is proved in
`../../results/transverse-quadric-stack-union.md`. It gives an exponent-level
full dense-shading union estimate, and hence full Minkowski dimension, for an
explicit infinite one-parameter family of ruled
quadratic obstructions satisfying explicit sweep and transversality
hypotheses. The fixed all-scale covering theorem in
`../../results/fixed-stack-hausdorff.md` upgrades the same continuum stack to
Hausdorff dimension four. Neither theorem extracts such a stack from an
arbitrary Kakeya family.

## Idea

A single ruled quadric grain can contain a two-parameter family of line
segments and have delta-neighborhood volume comparable to `delta`. A stack of
`M≈delta^-1` grains therefore has total grain mass of order one.

Uniform pairwise transversality is too strong: adjacent members of a smooth
one-parameter stack naturally meet at angle only `1/M≈delta`. But if the
angle between grains `i,j` is bounded below by `|i-j|/M`, coarea gives

`|N_delta(X_i) intersect N_delta(X_j)|
  ≲ delta² M/|i-j|`.

The sum over index separations is harmonic. A second-moment estimate loses
only `H_M≈log M`, hence only `delta^(-o(1))`.

## Relation to the two primary bridges

This is a Bridge B result: it is an actual semialgebraic union lemma, not a
carrier-extraction theorem. It also informs Bridge A: persistent ruled models
need not become 2-plany if the carriers themselves drift transversely across
scale or position; their drift can instead force volume through overlap
summability.

## Missing bridge

To affect general Kakeya, one must prove that a ruled degree-two branch can be
organized into stacks with:

- a two-parameter line sweep with bounded multiplicity;
- an ordered carrier parameter with angle separation `|i-j|/M`;
- retained shaded mass balanced across `M≈delta^-1` carriers; and
- direction parameters jointly covering a three-dimensional direction set.

The present theorem assumes these outputs and proves the union estimate. It
does not infer them from small union volume or from Proposition 3.12.

For Hausdorff dimension the carriers must additionally sample one fixed line
family across all cover scales, or satisfy the equivalent incidence-Carleson
condition in `fixed-stack-hausdorff.md`. Unrelated good discretizations at
each scale are insufficient.
