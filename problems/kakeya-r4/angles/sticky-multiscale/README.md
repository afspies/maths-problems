# Sticky multiscale trilinear attack

## Status

Active formulation; no exponent improvement proved.

## Exact bridge implication

Let `c` satisfy `0<c<1/12`. Suppose the trilinear alternative in the
balanced eta-extremal induction can be strengthened uniformly, relative to
the complete right-hand side of Theorem 5.4 (including
`theta≈rho²`), to

`|U(T,Y)| ≥ delta^(3/4-c+o(1))`.

Then the Section 6 induction can target
`alpha=3/4-c`. The weakly plany recurrence has leading gain

`rho^(-alpha+2/3) = rho^(-(1/12-c))`,

which remains a negative power and absorbs sufficiently small refinement and
epsilon losses. Consequently `sigma_4 ≤ 3/4-c` and Proposition 3.2 gives

`dim_H K ≥ 13/4+c`.

This is the exact reason a fixed trilinear gain, rather than a qualitative
grain picture, is needed.

## Preferred theorem pair

### Inverse trilinear lemma (target)

In the normalized eta-extremal, Proposition 3.12-balanced setting, if a
quantitatively trilinear family fails to gain a fixed `delta^(-kappa)` over
the full Theorem 5.4 union bound, then at a scale `delta^a`, with
`a in [a_0,1-a_0]` for fixed `a_0>0`, at least `delta^tau` of the shaded
incidence mass (for a prescribed loss `tau<kappa`) is controlled by the
delta-neighborhood of one of at most `delta^(-tau)` bounded-degree ruled
semialgebraic 3-fold models, with ruling data coherent across coarse tubes.

### Two-scale ruled rigidity (target)

Such a ruled model cannot persist through two quantitatively separated
balanced sticky scales unless:

1. a refinement enters the 2-plany branch, where the `2/3` volume exponent is
   available; or
2. the union already gains a fixed negative power of delta.

This remains a schematic target: “controlled” and “coherent” still need
incidence-level definitions, and the displayed `tau` losses must be propagated
through a common refinement. In particular, the model 3-fold may depend on
the coarse tube but must have bounded parameter entropy if a global exponent
gain is to survive pigeonholing.

## First serious attempt and obstruction

The Guth–Zahl estimate contains only the scalar factors

`s^(9/4) lambda^(13/4) theta (delta³ #T)^(1/4)`.

All are at most order one in the normalized regime. Reapplying this
one-scale estimate cannot manufacture `delta^(-kappa)`. Proposition 3.12
balances multiplicity and mass across scales, but gives no relation between
the near-equality sets for the trilinear estimate at two scales.

The exact missing step is therefore a *stability/inverse theorem for the
trilinear estimate*, with a model whose parameter entropy is small enough
that selecting one model costs only `delta^o(1)`. Without that entropy
bound, “some grain at each scale” loses a fixed power and the claimed gain
is circular. Proposition 3.12 itself only supplies a refinement at the one
scale selected in an induction step; applying it twice does not automatically
put both balanced structures on a common positive-mass refinement.

## Stress test

The split quadric

`x1²+x2²-x3²-x4²=1`

is ruled and can be pointwise trilinear: the exact harness constructs three
rational concurrent lines on it whose direction rank is three. Thus the
second lemma cannot assert “ruled implies plany”. It must use two separated
balanced scales and coherent ruling data.

## GO/STOP test

GO only after either:

- an inverse theorem with a quantified bounded-entropy ruled model and at
  least one degree-2 model class excluded at two scales; or
- a direct fixed `kappa>0` for a stable, independently defined infinite
  subclass.

At present neither has been proved.

## Independent soundness verdict

The GPT-5.6 Sol xhigh review found no derivation of either target from the
audited inputs. It specifically rejected (i) treating the scalar near-equality
conditions as an inverse theorem, (ii) assuming two independently chosen
balanced refinements coexist, and (iii) allowing a polynomial-size model
pigeonhole loss without subtracting it from `kappa`. This angle is therefore
STOP/PIVOT, not a claimed structural theorem.
