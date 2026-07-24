# A critical \(1/2\)-Hölder bridge

**Status:** proof complete modulo Antonelli--Young Theorem 1.2,
Boedihardjo--Geng Theorem 2.2, and Asano--Ike Theorem 1.1 with Remark 5.6.

This note isolates a class at the critical quadratic-variation threshold.  It
is strictly beyond the finite-\(p\)-variation theorem for \(p<2\): the explicit
family in `../../results/critical-spiral-comb.md` has infinite
\(p\)-variation for every \(p<2\).

## The dyadic quadratic-diameter condition

Let \(c:[0,1]\to\mathbb R^2\).  For \(i\geq0\) and
\(0\leq j<2^i\), put
\[
\delta_{i,j}(c)=\operatorname {diam}\left\{
c(j2^{-i}),\
c((2j+1)2^{-i-1}),\
c((j+1)2^{-i})
\right\}
\]
and
\[
                    \sigma(c)=
\sum_{i=0}^{\infty}\sum_{j=0}^{2^i-1}\delta_{i,j}(c)^2.       \tag{1}
\]

## Theorem

Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization which, after cutting
the parameter circle at one point, is \(1/2\)-Hölder and satisfies
\(\sigma(c)<\infty\).  Then \(c\) satisfies the embedded-approximation and
primitive-convergence hypotheses of Asano--Ike Theorem 1.1.  Consequently
the image of \(c\) inscribes a \(\theta\)-rectangle for every
\(\theta\in(0,\pi)\), including a nondegenerate square.
Moreover, \(\mathcal H^2(c(S^1))=0\).

The condition is parametrization-dependent.  No claim is made that every
finite-\(2\)-variation Jordan curve admits such a parametrization.

## Proof

Write \(c=(x,y)\), orient \(\mathbb R^2\) in the standard way, and use the
antisymmetric area primitive
\[
 {\cal A}_P(c;t)=\frac12\sum_{k}
 \det(c(t_k),c(t_{k+1}))                              \tag{2}
\]
for a partition \(P=\{0=t_0<\cdots<t_m=t\}\) of \([0,t]\).

### 1. Antonelli--Young gives more than a convergent dyadic sequence

Antonelli--Young Theorem 1.2 does not merely say that the dyadic polygon
areas converge.  Under the \(1/2\)-Hölder and (1) hypotheses, it proves that
there is a number \({\cal A}(c)\) such that
\[
 {\cal A}_P(c;1)\longrightarrow{\cal A}(c)
       \quad\text{as }\operatorname {mesh}P\longrightarrow0             \tag{3}
\]
over **all** partitions of \([0,1]\).

We need a local primitive, uniformly in its upper endpoint.  This follows
formally, but importantly, from the all-partition quantifier in (3).

**Uniform-prefix lemma.**  If (3) holds for a continuous path \(c\), then
there is a continuous function \({\cal A}_c:[0,1]\to\mathbb R\), with
\({\cal A}_c(0)=0\), such that
\[
 \sup_{0\leq t\leq1}
 \left|{\cal A}_{P_t}(c;t)-{\cal A}_c(t)\right|\longrightarrow0          \tag{4}
\]
whenever, for every \(t\), \(P_t\) is a partition of \([0,t]\) whose mesh
is bounded by a common number tending to zero.

**Proof.**  Use the Cauchy form of (3).  Given \(\varepsilon>0\), choose
\(\eta>0\) so that the area sums of any two partitions of \([0,1]\) of
mesh less than \(\eta\) differ by less than \(\varepsilon\).  Fix
\(t\in[0,1]\), and let \(P,Q\) be two partitions of \([0,t]\) of mesh less
than \(\eta\).  Extend both by the same partition \(R\) of \([t,1]\), also
of mesh less than \(\eta\).  Additivity of (2) gives
\[
 {\cal A}_{P\cup R}(c;1)-{\cal A}_{Q\cup R}(c;1)
       ={\cal A}_{P}(c;t)-{\cal A}_{Q}(c;t).            \tag{5}
\]
The right side therefore has absolute value less than \(\varepsilon\),
uniformly in \(t\).  The resulting uniform Cauchy net defines
\({\cal A}_c(t)\) and proves (4).

To prove continuity without assuming any critical area estimate on a short
subinterval, fix partitions \(Q_n\) of \([0,1]\) with mesh tending to zero
and define
\[
 H_n(t)={\cal A}_{(Q_n\cap[0,t])\cup\{t\}}(c;t).
\]
Each \(H_n\) is continuous: between consecutive vertices of \(Q_n\), only
the final determinant varies, and the two formulas agree when \(t\) crosses
a vertex.  The uniform Cauchy estimate just proved shows that \(H_n\)
converges uniformly to \({\cal A}_c\).  Hence \({\cal A}_c\) is continuous.
\(\square\)

This step is the bridge from Antonelli--Young's total signed area to the
local primitive required by Asano--Ike.

### 2. The approximating polygons are embedded

By Boedihardjo--Geng Theorem 2.2, choose partitions \(P_n\) of the original
parameter interval, with mesh tending to zero, whose affine interpolants
\(a_n=c^{P_n}\) are Jordan polygons.  These are not arbitrary secant
polygons: their theorem is what guarantees embeddedness while retaining the
original parameter times.  Uniform continuity of \(c\) gives
\(a_n\to c\) uniformly.

Let
\[
 G_n(t)=\frac12\int_0^t(x_{a_n}\,dy_{a_n}-y_{a_n}\,dx_{a_n}).            \tag{6}
\]
At a partition vertex, (6) is exactly the sum (2), so the uniform-prefix
lemma gives uniform convergence at all vertices of \(P_n\).  Between two
consecutive vertices \(u<v\),
\[
 |G_n(t)-G_n(u)|
 \leq \|a_n\|_\infty\operatorname {diam}c([u,v]),
       \qquad u\leq t\leq v,
\]
because \(a_n([u,v])\) is the chord from \(c(u)\) to \(c(v)\).
The right side tends to zero uniformly by uniform continuity of \(c\), and
\({\cal A}_c\) is uniformly continuous.  Therefore
\[
                         \|G_n-{\cal A}_c\|_\infty\longrightarrow0.       \tag{7}
\]

### 3. Relative corner rounding preserves the primitives

Apply the relative corner-rounding lemma proved in
`../p-variation/README.md`.  It gives a regular \(C^1\) Jordan embedding
\(b_n:S^1\to\mathbb R^2\), on the same parameter circle, arbitrarily close
to \(a_n\) in both the uniform and \(1\)-variation norms.  For the fixed
finite polygon \(a_n\), choose the rounding so small that
\[
\begin{split}
 &\|b_n-a_n\|_\infty<1/n,\\
 &\|b_n-a_n\|_\infty\operatorname {Var}(a_n)
  +\bigl(\|a_n\|_\infty+1\bigr)
     \operatorname {Var}(b_n-a_n)<1/n.                \tag{8}
\end{split}
\]
This diagonal choice is available even though
\(\operatorname {Var}(a_n)\) need not be uniformly bounded.

For either Liouville form, integration by parts and the elementary
Riemann--Stieltjes estimate for bounded-variation paths give
\[
\sup_t\left|
\frac12\int_0^t(x_{b_n}\,dy_{b_n}-y_{b_n}\,dx_{b_n})
-
\frac12\int_0^t(x_{a_n}\,dy_{a_n}-y_{a_n}\,dx_{a_n})
\right|<C/n.                                           \tag{9}
\]
For example, each difference is split into an integrand difference against
one polygonal coordinate and a bounded coordinate against
\(d(b_n-a_n)\); (8) bounds all four terms.  Thus the antisymmetric
primitives of \(b_n\) converge uniformly to \({\cal A}_c\).

Asano--Ike use a primitive of \(\lambda=y\,dx\).  The identity
\[
 y\,dx=\frac12\,d(xy)-\frac12(x\,dy-y\,dx)             \tag{10}
\]
shows that (7)--(9), together with \(b_n\to c\) uniformly, give uniform
convergence of the required Liouville primitives on \([0,1]\).  Normalize
them to vanish at \(0\).  Periodicity then gives
\[
 F_n(t+k)=F_n(t)+kF_n(1),
\]
so convergence on one period, including the period itself, implies local
uniform convergence on the universal cover \(\mathbb R\).

Antonelli--Young also prove under (1) that
\(\mathcal H^2(c(S^1))=0\).  Asano--Ike Remark 5.6 permits regular \(C^1\),
rather than \(C^\infty\), Jordan approximants.  The \(b_n\) therefore meet
their hypotheses, and Theorem 1.1 supplies every prescribed rectangle.
\(\square\)

## Claim boundary

Antonelli--Young prove the signed-area criterion; Boedihardjo--Geng prove
the embedded polygonal interpolation; Asano--Ike prove the rectangular-peg
implication.  The content here is the uniform-prefix observation, the
embedded diagonal rounding, and the synthesis of those three results.
It should be described as an apparently unstated critical corollary, not as
a new theory of critical integration.
