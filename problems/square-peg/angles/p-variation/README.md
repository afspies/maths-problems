# Finite \(p\)-variation bridge

**Status:** proof complete modulo the cited Asano--Ike v3 theorem (including
its Remark 5.6, which allows \(C^1\) approximants) and the published
Boedihardjo--Geng interpolation theorem.

## Theorem

Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization of finite
\(p\)-variation for some \(1\le p<2\).  Then \(c\) satisfies the approximation
and primitive-convergence hypotheses of Asano--Ike Theorem 1.1.  Consequently,
for every \(\theta\in(0,\pi)\), the image of \(c\) inscribes a
\(\theta\)-rectangle; in particular it inscribes a nondegenerate square.

This is a theorem about a parametrization, but finite \(p\)-variation is
invariant under orientation-preserving reparametrization, so the resulting
curve class is geometric.

## Proof

Write \(T=2\pi\) and regard \(c\) as a \(T\)-periodic map on \(\mathbb R\).
Fix
\[
             p<q<2. \tag{1}
\]
If \(p=1\), either invoke Asano--Ike's rectifiable corollary directly or first
choose \(1<p_0<q\); finite \(1\)-variation implies finite
\(p_0\)-variation, and the argument below applies with \(p_0\).

### 1. Embedded polygonal interpolation

For each \(n\), apply Boedihardjo--Geng Theorem 2.2 to obtain a partition
\(P_n\) of \([0,T]\), of mesh at most \(1/n\), whose affine interpolant
\(a_n=c^{P_n}\) is a Jordan polygon with the same parametrization times.
Their Lemma 3.1 gives
\[
       \|a_n-c\|_{q\text{-var};[0,T]}\longrightarrow0. \tag{2}
\]
In particular \(a_n\to c\) uniformly, and
\(\sup_n\|a_n\|_{q\text{-var}}<\infty\).

This is the point at which an arbitrary polygonal or mollified approximation
would be insufficient: Theorem 2.2 proves that these particular interpolants
remain embedded.

### 2. \(C^1\)-smooth the polygon without losing embeddedness

We use the following elementary lemma.

**Corner-rounding lemma.**  If \(a:S^1\to\mathbb R^2\) is a finite Jordan
polygon and \(\varepsilon>0\), there is a regular \(C^1\) Jordan embedding
\(b:S^1\to\mathbb R^2\), on the same parameter circle, such that
\[
 \|b-a\|_\infty<\varepsilon,\qquad
 \|b-a\|_{1\text{-var}}<\varepsilon.                 \tag{3}
\]

**Proof.**  Retain every breakpoint of the affine parametrization, including
the cyclic seam \(0=T\).  Choose pairwise disjoint vertex disks \(D_j\), each
meeting the polygon only in terminal subsegments of its two incident edges.
Shrink the disks until the sum of the lengths
\(\ell_j=\operatorname{len}(a(I_j))\) of those broken subarcs is as small as
desired, where \(I_j\) is the original preimage interval.

At a noncollinear vertex, replace \(a|_{I_j}\) by the standard tangential
fillet in the empty local sector between its incident subsegments.  Parametrize
the fillet regularly on the *same* interval \(I_j\), with its endpoint
velocities equal to the two constant velocities of \(a\).  (An
orientation-preserving \(C^1\) change of speed on the fillet supplies any
prescribed positive endpoint speeds.)  The replacement is a regular \(C^1\)
arc and agrees with \(a\), including its first derivative, at the endpoints of
\(I_j\).  Its length is at most \(K_j\ell_j\), where \(K_j<\infty\) depends
only on that fixed vertex angle.

If the incident directions are positively collinear, retain the same straight
image and replace its piecewise-constant positive speed on \(I_j\) by a
positive \(C^1\) speed with the same endpoint speeds and the same integral.
Negative-collinear incident directions would locally retrace a segment and
are impossible for a Jordan polygon.  These replacements are confined to
the pairwise disjoint disks, meet the unchanged polygon only at their
endpoints, and are simple within each disk, so the resulting map remains an
embedding.

With \(K=\max_j K_j\) (and \(K=1\) for a collinear replacement),
\[
 \operatorname{Var}(b-a;I_j)
 \le\operatorname{len}(b|_{I_j})+\operatorname{len}(a|_{I_j})
 \le (K+1)\ell_j.                                      \tag{4}
\]
Choose the disks so that
\(\sum_j\ell_j<\varepsilon/(K+1)\) and
\(\max_j\operatorname{diam}D_j<\varepsilon\).  This gives (3).  The resulting
map is a regular \(C^1\) Jordan embedding on the original parameter circle.
\(\square\)

Asano--Ike Remark 5.6 explicitly weakens “smooth” in Theorem 1.1 to \(C^1\),
so this relative \(C^1\) rounding is sufficient; no unproved
\(C^\infty\)-smoothing step is being used.

Apply the lemma to \(a_n\), choosing the error so small that
\[
 \|b_n-a_n\|_\infty+
 \|b_n-a_n\|_{1\text{-var}}<1/n.                     \tag{5}
\]
Since \(q\)-variation is bounded by \(1\)-variation,
(2)--(5) imply
\[
       \|b_n-c\|_{q\text{-var};[0,T]}\to0.            \tag{6}
\]
Thus the \(b_n\) are the required \(C^1\) *Jordan* approximants and converge
uniformly with the correct parametrization.

### 3. Stability of the Liouville primitives

Use coordinates \(c=(x,y)\) and the convention \(\lambda=y\,dx\).  Normalize
\[
 F_n(t)=\int_0^t y_n\,dx_n,\qquad
 F(t)=\int_0^t y\,dx,                                \tag{7}
\]
where the integrals are Young integrals.  They exist because \(q<2\).

For paths \(u=(u^1,u^2)\), \(v=(v^1,v^2)\) of finite \(q\)-variation, Young's
inequality with \(C_q=2\zeta(2/q)\) gives, uniformly in \(t\in[0,T]\),
\[
\begin{aligned}
\left|\int_0^t u^2\,du^1-\int_0^t v^2\,dv^1\right|
&\le |u^2(0)-v^2(0)|\,\|u^1\|_{q\text{-var}}\\
&\quad + C_q\|u^2-v^2\|_{q\text{-var}}
                  \|u^1\|_{q\text{-var}}\\
&\quad + |v^2(0)|\,\|u^1-v^1\|_{q\text{-var}}\\
&\quad + C_q\|v^2\|_{q\text{-var}}
                  \|u^1-v^1\|_{q\text{-var}}.        \tag{8}
\end{aligned}
\]
Indeed, subtract the integrals as
\[
 \int(u^2-v^2)\,du^1+\int v^2\,d(u^1-v^1)
\]
and apply Young's estimate to each term, retaining the two basepoint
increments.  Equation (6), boundedness of the \(q\)-variation norms, and
uniform convergence make the right side of (8) tend to zero for
\(u=b_n,v=c\).  Hence
\[
                  \|F_n-F\|_{\infty;[0,T]}\to0.      \tag{9}
\]

The pullback one-forms are periodic and
\[
 F_n(t+kT)=F_n(t)+kF_n(T).
\]
Equation (9), including at \(T\), therefore implies \(F_n\to F\) uniformly on
every compact subset of \(\mathbb R\).  These are exactly the two hypotheses
of Asano--Ike Theorem 1.1, which supplies every prescribed rectangle.
\(\square\)

## Normalization and invariance checks

- A different additive normalization of the primitives is harmless provided
  the constants converge.  Setting \(F_n(0)=0\) is canonical.
- Translating the curve in the fibre coordinate adds a constant multiple of
  \(x(t)-x(0)\) to the primitive, which also converges under (6).
- Reversing orientation changes the period/action sign but not the existence
  of rectangles; the approximants above preserve the chosen orientation.
- The proof does not assume that a convolution of \(c\) is embedded.
- Boedihardjo--Geng's Green theorem also identifies \(F(T)\), up to the chosen
  Liouville sign, with the enclosed area.  This is consistent with the
  area-\(\pi\) scaling inside Asano--Ike's proof, but is not an extra
  hypothesis here.

## Novelty boundary

The analytic and topological approximation ingredients are published
theorems.  The new content is their combination with the 2026 Asano--Ike
criterion.  It should be advertised as a concise corollary/synthesis, not as a
new rough-integration theory.
