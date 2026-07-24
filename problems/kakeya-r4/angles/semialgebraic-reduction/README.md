# Semialgebraic reduction attack

## Status

Candidate parameter defined; the split quadric is exactly detected. No
four-dimensional union theorem is proved.

## Scale-aware nonconcentration parameter

Fix degree/Boolean complexity `D` and a scale `r≥delta`. Let
`G_D(r)` be the class of subsets of `B(0,2)` described by at most `D`
polynomial weak inequalities of degree at most `D`, with every geometrically
thin equality thickened at scale `r`.

For a delta-tube family `T`, define

`Delta_SA,D(T;r) =
 sup_G [ sum_{T subset G} |T| / |G| ]`,

where the supremum is over `G in G_D(r)` with `|G|>0`; containment may be
relaxed to `T subset N_(C delta)(G)` with `C` fixed in advance.

A useful R⁴ replacement for the convex Katz–Tao hypothesis would control
this parameter at every scale and prove a near-disjoint union bound. Merely
running the abstract greedy factoring lemma with this class is valid but
does not supply the needed incidence/union estimate.

## Degree-2 detection lemma

Let

`P(x)=x1²+x2²-x3²-x4²-1`

and work in `B(0,2)`, with tube cores in a fixed smaller interior patch. For
small delta, the grain

`G_delta={x in B(0,2): |P(x)|≤C delta}`

has bounded semialgebraic complexity and volume comparable to `delta`.
Every unit line segment in the chosen interior patch of `P=0`, and hence
every sufficiently thin tube around it,
lies in such a grain after increasing `C` by a fixed amount. Therefore a
family of `N` such tubes satisfies

`Delta_SA,D(T;delta) ≳ N delta²`.

In particular, the three-parameter ruled family with
`N≈delta^(-3)` has semialgebraic density `≳delta^(-1)` and is rejected by a
bounded semialgebraic Katz–Tao axiom. The direction-separated subfamily has
only `N≈delta^(-2)` (null directions form a two-dimensional set) and merely
saturates this density test; the extra parameter is a family of parallel
translates. This explains exactly why the quadric obstructs the
essentially-distinct-tube convex theorem but is not itself a Kakeya
direction set.

The raw net itself fails Convex Wolff in a tangent intermediate prism.
Zahl's exact convex-axiom countermodel randomly thins it to
`delta^(-5/2)` tubes and then takes `delta^(-1/2)` translated/rotated
copies. The combined `delta^-3` family obeys Convex Wolff but has union
volume only about `delta^(1/2)`. A degree-2 semialgebraic test detects every
copy, so it targets precisely the obstruction missed by convex tests.

The volume assertion follows from `|grad P|` being bounded below near
`P=0` and the tubular-neighborhood formula. The radius must exceed one:
`P=0` only touches the unit ball, so `B(0,1)` would be a degenerate
truncation. The rational line
parameterization and on-quadric identities are checked in
`harness/incidence_models.py`.

## Known degree-2 polynomial Wolff control

For every coefficient-normalized degree-at-most-two polynomial `P`, put
`S=N_(C delta)(Z(P))∩B(0,2)`. Require

`#{T: |T∩S|≥lambda |T|}
  ≤ C |S| delta^(-3) lambda^(-4)`

for `delta≤lambda≤1`. On the split quadric, `|S|≈delta`, so this permits
only `O(delta^-2)` tubes and detects each thinned copy
(`delta^(-5/2)` tubes) by a fixed power.

Equivalently, define the certificate-producing ratio

`Delta_2(T)=sup_(P,lambda)
  #{T: |T∩S|≥lambda|T|}
  / (|S| delta^(-3) lambda^(-4))`.

The thinned split-quadric copy has
`Delta_2(T)≳delta^(-1/2)`.

Katz–Rogers, Theorem 1.1 (arXiv:1802.09094), proves this
bounded-complexity semialgebraic inequality for every direction-separated
tube family, with an arbitrary `delta^-epsilon` loss. Zahl's
arXiv:1801.05106 also proves the fixed-hypersurface direction bound
`O(delta^(-2-epsilon))` in R⁴. Therefore QW2 is a known input in the
direction-separated Kakeya setting, not a candidate axiom awaiting proof.
The thinned/copied quadric model evades the theorem because it has repeated
directions.

A noncircular carrier-extraction target for the broader essentially-distinct
setting is: if a Convex-Wolff family fails
the expected union gain, then after a subpolynomial refinement either the
ordinary convex factorization advances the induction or an explicit
quadratic `P`, scale `lambda`, and balanced subfamily violate the displayed
axiom. This extraction statement is conjectural.

## Exact ruled parameterization

Under the linear identification

`M(x)=[[x1+x3,x2+x4],[x4-x2,x1-x3]]`,

we have `det M=P(x)+1`. Thus the quadric is `SL_2(R)`. If
`M_0 in SL_2` and `N=p q^T` with `q^T p=0`, then

`det(M_0(I+tN))=1`

for every real `t`, giving an infinite rational family when the parameters
are rational.

## What remains

Detection is only the first hygiene check. The missing theorem is a
scale-stable union estimate for families with bounded
`Delta_SA,D(T;r)`, plus a factoring argument whose selected grains retain
controlled complexity under affine rescaling and intersection. Those
closure and entropy requirements are where a naive “replace convex by
semialgebraic” slogan can fail.

For direction-separated tubes, the second-session results sharpen this
further: one conditioned quadric carries only
`O(delta^-2 lambda^-2)` directions, so a full Kakeya family needs roughly
`delta^-1` carriers at constant overlap. The harmonic transverse-stack lemma
proves a logarithmic-loss union bound when those carriers can be ordered with
summable pairwise overlaps. Extraction of such an ordering is the remaining
bridge.

The distributed-catalog layer-cake lemma also handles the case where no tube
is assigned to one carrier: average total catalog overlap `q` across `M`
grains forces a single explicit QW2 witness of size

`Delta_2≳N delta²(q/M)^4`

once `q≥2Mdelta`. The fourth power is the exact cost of diffuse membership.
What remains unproved is the implication from small union volume to either
large distributed overlap or a transverse-stack decomposition.
