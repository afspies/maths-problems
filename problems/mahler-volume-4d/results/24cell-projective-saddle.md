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

## Certified 24-cell critical point

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

The certificate does not assert that the exact critical root is
pair-terminal. Pair-terminality holds at rational points arbitrarily close to
the root, but openness alone cannot transfer it to the root.
