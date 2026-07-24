# Certified projective saddle in the Paffenholz 24-cell family

## Necessary conditions

Put a local Mahler minimizer \(K\) in Santaló position. For

\[
T_t(x)=\frac{x}{1+t\,u\cdot x},
\qquad T_t(K)^\circ=K^\circ+t u,
\]

the Jacobian identity gives

\[
\left.\frac{d}{dt}\right|_{0}|T_t(K)|
=-(d+1)|K|\,u\cdot c(K).
\]

Since the origin-polar product is an upper bound for the Santaló volume
product and is exact at \(t=0\), local minimality forces

\[
c(K)=c(K^\circ)=0.
\]

At such a projectively critical body, the Balacheff--Solanes--Tzanev/Klartag
second variation says that a local minimizer in dimension four must satisfy

\[
\operatorname{cov}(K^\circ)
\succeq \frac1{36}\operatorname{cov}(K)^{-1}.
\]

## Certified connected pair-terminal critical point

For the rational Paffenholz realization with
\(a=(1/5,2/5,3/5,4/5)\), translate by \(z\), then apply the unique projective
normalization which centers the polar. The exact centroid equations have a
unique zero in the box of radius \(10^{-10}\) centered at

```text
(0.065348617243,
 0.127816191744,
 0.153467113574,
 0.022269205148).
```

The existence and uniqueness proof is a Krawczyk inclusion carried out with
outward-rounded dyadic rational intervals. On the entire certified box,

\[
e_1^\mathsf T\left(
\operatorname{cov}(K^\circ)-\frac1{36}\operatorname{cov}(K)^{-1}
\right)e_1
<
-0.0075809.
\]

Hence the exact bi-centered representative is a projective saddle, not a
local Mahler minimizer.

The same box now certifies much more. For a projective image with vertex
denominators \(d_v\), affine circuit coefficients transform by

\[
\lambda_v=d_v\mu_v.
\]

Thus every fixed-active-facet circuit matrix changes only by an invertible
diagonal column scaling and keeps its rank. Terminality can fail along the
projective family only if a new set of four facet normals becomes dependent.

Indeed, let \(W_t\) be the normals waived by a direction at the target
parameter. They span rank at most three. If no four normals independent at
the reference point become dependent, \(W_t\) also has reference rank at
most three. Its reference normal-flat closure \(\overline W_0\) contains
\(W_t\). Reference terminality says the circuit rows outside
\(\overline W_0\) already have rank \(f_0-5\); those facets remain active at
the target, and projective column scaling preserves that rank. The five
global affine speeds give the reverse rank bound, so the target is terminal.
Old dependencies may disappear harmlessly, since that only waives fewer
facets and adds equations.

At the rational center of the Krawczyk box, exact normal-flat enumeration
and transported small-denominator circuit ranks give

```text
primal normal flats     1941
polar normal flats      1911
all speed dimensions       5
```

Across the full interval box, exact-center nonzero four-normal determinants
remain separated from zero:

```text
                         nonzero   zero   unresolved
primal normals             10498    128       0
polar normals              10488    138       0
```

Both kinds of projective denominator are strictly positive. Hence no new
four-normal dependency appears, and the one-sided terminality transport
lemma proves every projective pair in the box is pair-terminal.

Minimal facet-circuit supports are projectively preserved. Exact enumeration
at the rational reference realization gives 120 primal circuits of sizes
four and five and 72 polar circuits of size four; both support graphs are
connected. Therefore the unique Krawczyk root is an exact
**bi-centered, connected, pair-terminal non-simplex**.

Finally, interval moments certify

\[
0.0999343391445795
<
\operatorname{tr}\bigl(
\operatorname{cov}K\operatorname{cov}K^\circ
\bigr)
<
0.0999343606091986
<
\frac19.
\]

This is the first fully certified connected pair-terminal test object for
the terminal trace-gap conjecture.

Reproduce with:

```text
PYTHONPATH=problems/mahler-volume-4d/harness \
python3 -B problems/mahler-volume-4d/harness/bicenter_certificate.py
```

The program uses exact rational interval endpoints. Dyadic outward rounding
after each operation controls denominator growth without weakening rigor.

## Open-family consequence

The Krawczyk certificate also proves the centroid Jacobian nonsingular, and
the negative covariance inequality is strict. The implicit-function theorem
and continuity therefore give an open neighborhood in the four-parameter
Paffenholz realization family whose nearby bi-centered critical branch
consists entirely of projective saddles. This is an infinite non-pyramidal
family excluded from local minimality.

The interval normal-determinant certificate now proves pair-terminality and
circuit connectivity at the exact critical root itself; no limiting
argument is used.
