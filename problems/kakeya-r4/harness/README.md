# Exact exponent and incidence harness

Everything in this directory uses integers or `fractions.Fraction`.

Run the complete exact harness with:

```bash
python3 exponent_ledger.py benchmark_ledger.json
python3 -m unittest -v
```

It verifies the audited branch arithmetic

`trilinear: 3/4 ↔ 13/4`, `weakly plany: 2/3 ↔ 10/3`,

and certifies that the exhaustive-branch bottleneck is the trilinear branch.
`induction_parameters.py` records the exact Section 6 scale recurrence,
the published constants defect, the balanced-scale and strict-planebrush
admissibility conditions, and one repaired rational parameter regime.
This verifies the scalar exponent ledger; it does not formalize the imported
geometric theorems or prove a proposed improvement.

`incidence_models.py` gives three rational stress tests. In particular, it
certifies three concurrent rational lines on

`x1^2 + x2^2 - x3^2 - x4^2 = 1`

whose directions have rank three. Thus “ruled quadric” does not imply
pointwise 2-planiness, even at a single point.

The second-session extensions add:

- an exact two-parameter line sweep of the split quadric;
- a rank-four seed for an explicit transverse pencil of ruled quadrics;
- exact harmonic-number and second-moment union ledgers;
- the quadratic direction-capacity, catalog-evasion, and sticky
  mass/entropy exponent conversions.
- high-multiplicity extraction and assigned-catalog entropy ledgers;
- the inverse low-Jacobian carrier-pair mass bound;
- the fixed-stack Hausdorff cover cost at exact integer codimensions;
- an exact trilinear rank-three parabolic pencil and its normal-wedge
  degeneration identity.
- the rank-two-separated parabolic stack's double-harmonic ledger;
- an exact ruled parabolic coefficient path with full direction and sweep
  determinants;
- the parent-ancestry transverse error `K D delta/alpha`;
- a rotating rank-one tangent whose second coefficient direction appears
  only at cubic order.
- the exact moment-height cubic, its square derivative, and its critical
  cubic gap;
- the cubic-SSI Hausdorff cover-cost ledger at exact integer half-codimension.
- the exact `2^L-1` dyadic parent-wall count and one-shot transverse tail
  threshold `4-s-4epsilon>0`.

The suite currently contains 44 exact tests. The geometric coarea,
Crofton--Bézout, reach, and Remez lemmas are proved in the result notes; the
harness certifies their algebraic models and exponent bookkeeping, not those
continuous theorems themselves.
