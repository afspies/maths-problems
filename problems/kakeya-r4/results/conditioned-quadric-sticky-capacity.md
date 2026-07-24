# Conditioned quadrics cannot carry low-entropy sticky mass

## Incidence lemma

Let `0<h<1`, `h≤lambda≤1`, and let `T` be a family of unit `h`-tubes in
`R4` with at most `h^-epsilon` tubes in each `h`-angular direction cap.
Let

`P(x)=x^T A x+ell(x)+c`

have bounded normalized coefficients, with `A` indefinite and
quantitatively invertible. Put

`S=N_(C h)(Z(P)) intersect B(0,2)`.

Then

`#{T in T: |T intersect S|≥lambda|T|}
 ≤ C h^-epsilon min(h^-3,h^-2 lambda^-2)`.                      (1)

For exact tube axes contained in any nonconstant degree-at-most-two
hypersurface, no conditioning or `lambda` loss is needed:

`#T≤C h^(-2-epsilon)`.                                          (2)

## Proof

Fubini across a tube in the left side of (1) selects a line parallel to its
axis that spends a `t`-set of length at least `c lambda` inside `S`. Along
that line, `P` is a quadratic polynomial whose leading coefficient is
`v^T A v`, where `v` is the tube direction. Degree-two Remez gives

`|v^T A v|≤C h lambda^-2`.

Quantitative invertibility makes the null cone a uniformly regular
two-dimensional surface in `S3`. Its
`C h lambda^-2` neighborhood contains at most

`C min(h^-3,h^-2 lambda^-2)`

many `h`-caps. Multiplying by the assumed `h^-epsilon` tubes per cap proves
(1).

If a complete line lies in `Z(P)`, every coefficient of the restriction of
`P` to that line vanishes. Its direction therefore lies in `q_2(v)=0`, or,
if the quadratic homogeneous part vanishes identically, in `ell(v)=0`.
The zero directions of a nonzero homogeneous polynomial of degree at most
two occupy `O(h^-2)` angular caps on `S3`. This proves (2).

## Sticky mass/entropy corollary

Suppose an `epsilon`-extremal family at scale `h` has total shading mass at
least `h^epsilon`. A catalog of `M` conditioned quadrics can carry, at
overlap level `lambda`, at most the tube mass

`C M h^(-epsilon) min(1,h lambda^-2)`.

Hence the carried fraction `f` of the original shading mass obeys

`f≤C M h^(-2epsilon) min(1,h lambda^-2)`.                        (3)

In the nontrivial regime `lambda≥h^(1/2)`, this becomes

`f≤C M h^(1-2epsilon) lambda^-2`.                               (3a)

Write

`h=delta^a`, `f≥delta^tau`, `M≤delta^-zeta`,
`lambda≥delta^ell`.

Assume `ell≤a/2`, equivalently `lambda≥h^(1/2)`. Persistence of such a
carrier conclusion requires the exact exponent inequality

`tau+zeta+2 ell ≥ a(1-2 epsilon)`.                              (4)

In particular, the preferred inverse output

`f≥delta^tau`, `M≤delta^-tau`

with full containment (`ell=0`) is impossible whenever

`2 tau<a(1-2 epsilon)`.                                         (5)

## Consequence for Bridge A

This does not prove inverse trilinear structure. It proves that the earlier
low-entropy formulation was too optimistic even before attempting
two-scale rigidity. At a fixed intermediate scale, a sticky family cannot
put the proposed mass on the proposed number of well-conditioned quadratic
carriers unless it spends the scale loss in (4).

A viable inverse theorem must therefore do at least one of the following:

- output about `h^-1` carrier entropy;
- allow a much smaller captured mass;
- use ill-conditioned/degenerate quadrics as a separate model class;
- exploit repeated directions beyond the sticky cap bound; or
- output a different kind of ruled carrier.

The harmonic transverse-stack theorem treats the first alternative:
roughly `h^-1` coherently ordered carriers can still force an exponent-level
full union through summable overlaps.
