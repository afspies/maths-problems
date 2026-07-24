# Exact dependency ledger for the 13/4 sticky bound

Primary source: Rai Choudhuri, arXiv:2410.23579v1 and the published version,
Rev. Mat. Iberoam. 42 (2026), 1227–1256.

## Output convention

For shaded delta-tubes in R⁴, a bound `|U| ≥ delta^(alpha+o(1))` corresponds
to dimension at least `4-alpha`. Thus:

- trilinear `alpha = 3/4` ↔ dimension `13/4`;
- plany `alpha = 2/3` ↔ dimension `10/3`;
- an exhaustive dichotomy has global exponent `max(3/4,2/3)=3/4`.

The harness verifies these identities exactly.

## Discretization and extremality

1. Definition 3.1 defines `M(s,t,delta)`, `N(s,t)`, and `sigma_n`.
2. Proposition 3.2 imports from Wang–Zahl:
   `dim_H K ≥ n-sigma_n` for a sticky Kakeya set.
3. An eta-extremal collection has:
   - essentially distinct delta-tubes;
   - at most `delta^(-eta)` essentially parallel rho-tubes at every scale;
   - total shading mass at least `delta^eta`;
   - union volume at most `delta^(sigma_n-eta)`.
4. Equations (3.5)–(3.8) give, up to eta losses:
   `#T ≈ delta^(1-n)`, density near one, union volume
   `delta^(sigma_n)`, and multiplicity `delta^(-sigma_n)`.
5. The displayed lower bound for average multiplicity in the published
   text has a sign typo: mass at least `delta^eta` divided by volume at most
   `delta^(sigma_n-eta)` gives
   `mu_Y ≳ delta^(-sigma_n+2 eta)`, not
   `delta^(sigma_n+2 eta)`. Subsequent uses have the required negative sign.
6. Proposition 3.12 is the balanced multiscale input. At every admissible
   intermediate scale rho it gives, after refinement:
   - one coarse rho-tube per fine tube;
   - an extremal coarse family;
   - an extremal rescaled fine family inside each coarse tube;
   - coarse and fine multiplicity upper bounds;
   - constant fine multiplicity;
   - constant fine mass per coarse tube/coarse cube incidence.

The last item is what makes canonical refinements preserve a controlled mass
fraction. It is balance, not an algebraic grain theorem. Moreover, it is
applied at one selected scale in each induction step; it does not provide a
single refinement on which conclusions at two separated scales coexist.

## Trilinear/plany dichotomy

Proposition 4.1 says that a multiset of directions is either:

- quantitatively trilinear, with a constant fraction of triples satisfying
  `|u1 wedge u2 wedge u3| ≳ rho²`; or
- a constant fraction lies within angle `O(rho)` of a 2-plane.

Lemma 4.3 applies this cube by cube to an extremal sticky family.

- Branch (a): a refinement is trilinear at threshold `theta ≍ rho²`.
- Branch (b): after a
  `delta^(23 eta + 2 epsilon³)` refinement, Proposition 3.12 upgrades weak
  pointwise rho-planiness of delta-tubes to actual planiness of the coarse
  rho-tube family, retaining balanced coarse/fine multiplicities.

## Trilinear branch and its slack

Theorem 5.4 (Guth–Zahl, in the Katz–Zahl form) is

`|U| ≥ c_e delta^e s^(9/4) lambda^(13/4) delta^(3/4)
        theta (delta³ #T)^(1/4).`

Lemma 4.3 supplies `s ≍ 1` and `theta ≍ rho²`. Extremality supplies
`lambda ≥ delta^(4 eta)` and `#T ≥ delta^(-3+eta)`.
In Section 6 this yields

`|U| ≥ delta_tilde^(3/4)
        delta_tilde^(epsilon_1 + 13 eta + eta/4) rho²`.

The proof spends two factors `delta^(1/N)` on the auxiliary losses and
`rho²=delta^(2/N)`, reaching the inductive allowance `delta^(4/N)`.

Near equality in this branch therefore requires, at the exponent level:

- the trilinear fraction `s` is only constant, not improving with scale;
- shading density and normalized tube count are extremal up to `delta^o(1)`;
- the wedge threshold is only the dichotomy scale `rho²`;
- the Guth–Zahl trilinear estimate itself is near sharp.

These numerical requirements do **not** imply a grain, ruled variety, or
projection structure. Such a conclusion is precisely the missing inverse
theorem.

## Weakly plany branch and its slack

Theorem 5.5 gives the plany exponent `2/3`. The coarse planebrush bound and
the fine inductive hypothesis combine in equation (6.10). For a general
target volume exponent `alpha`, the scale gain has leading factor

`rho^(-alpha+2/3)`.

At `alpha=3/4` this is `rho^(-1/12)`. All refinement, two-ends,
robust-transversality, and epsilon losses must be smaller than this fixed
gap. Hence the plany branch has genuine exponent room up to any
`alpha > 2/3`; it is not the `13/4` bottleneck.

Near equality requires the planebrush estimate, the coarse multiplicity
upper bound, the fine inductive volume bound, and the multiplicity product
to be simultaneously tight, while using almost all of the `1/12` gap to pay
parameter losses.

There are two additional admissibility details:

- for `rho=delta^(1/N)` and
  `delta_tilde=delta^((j+1)/N)`, the asserted inclusion
  `rho in [delta_tilde^(1-eta_j),delta_tilde^eta_j]` requires
  `eta_j≤1/(j+1)`; it follows after adding `eta_0≤1/N` to the initial
  hierarchy;
- Theorem 5.5 assumes strict `0<epsilon_2<epsilon_1<1`, so the printed
  substitution `epsilon_1=1` is formally inadmissible. If `sigma_4=0` the
  desired dimension is already four. Otherwise the known `sigma_4<1`
  permits a fixed `a` with `sigma_4<a<1`; a `(1,C)` two-ends estimate implies
  the weaker `(a,C)` estimate, and the resulting fixed change in the
  `C^(-1/a)` loss is absorbed by shrinking the eta hierarchy.

## Published parameter-bookkeeping defect and repair

Section 6 chooses `N` minimally with `4/N < epsilon_0`. The exact consequence
is

`epsilon_0/(4+epsilon_0) ≤ 1/N < epsilon_0/4`,

not `epsilon_0 < 2/N` (the latter sentence appears in arXiv v1 and was
removed from the journal version).

Two displayed journal-version comparisons still use the wrong side:

1. `epsilon_1 < epsilon_0/4` does not imply `epsilon_1 ≤ 1/N`, needed in
   the trilinear budget.
2. When the rho exponent in (6.10) is negative, replacing `1/N` by
   `epsilon_0/4` reverses the displayed lower-bound comparison.

This is a constants defect, not evidence against the theorem. For
`0<epsilon_0<1`, minimality gives `1/N > epsilon_0/5`. Choosing
`epsilon_1 < epsilon_0/5`, substituting the lower bound
`1/N ≥ epsilon_0/5` with the correct sign, and shrinking `epsilon_2, eta_0`
retains a strictly negative bracket exponent. Add `eta_0≤1/N` and use the
strict planebrush substitution described above. The harness gives exact
rational witnesses for these checks and for one repaired regime.

## Equality information actually available

The current argument provides scalar near-equality constraints only. It has
no stability statement for Theorem 5.4, no classification of near-extremal
direction triples, and no cross-scale coherence of a putative algebraic
model. Therefore an “inverse trilinear theorem” cannot be cited from this
paper; it must be proved as new input.
