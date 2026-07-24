# Dual isotropic and covariance route

Let

\[
A=\operatorname{cov}(K),\qquad
B=\operatorname{cov}(K^\circ),\qquad
L_K^{8}=\frac{\det A}{|K|^2}
\]

in dimension four. At a local Mahler minimizer, projective second variation
gives

\[
B\succeq\frac1{36}A^{-1}.
\]

Taking determinants yields the exact reduction

\[
\mathcal P(K)
\ge\frac1{6^4(L_KL_{K^\circ})^4}.
\]

Thus it would suffice to prove, only for bi-centered pair-terminal minimizer
candidates,

\[
\boxed{L_KL_{K^\circ}\le L_{\Delta_4}^2.}
\]

This paired inequality is weaker than the strong isotropic-constant
conjecture applied separately to \(K\) and \(K^\circ\), but it remains
unknown in dimension four [klartag-2018; kipp-2026-decomposability].

## Alternative trace target

A stronger but sometimes cheaper separator would be

\[
\operatorname{tr}(AB)\le\frac19.
\]

The covariance PSD condition supplies the reverse inequality at a local
minimum. Equality would force \(B=A^{-1}/36\); one could then try to use third
and fourth projective variations to obtain homogeneous-cone rigidity.

This trace ceiling is false without additional structure.
Balacheff--Solanes--Tzanev construct bi-centered projectively critical
pentagons above the dimension-two simplex/ball trace. Covariance equality
also holds for ellipsoids and more general homogeneous-cone sections, so it
does not characterize simplices.

## Stop/go tests

1. Certify terminality and the trace at the exact Paffenholz bi-centering
   root. A terminal example with trace above \(1/9\) kills the trace route.
2. Search structured pair-terminal realization charts for
   \(L_KL_{K^\circ}>L_{\Delta_4}^2\). One certified example kills the paired
   isotropic route.
3. If both inequalities survive, derive their first variations using the
   paired incidence-stress coordinates rather than trying to prove the full
   strong slicing conjecture.
