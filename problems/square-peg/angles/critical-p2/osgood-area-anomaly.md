# A finite-\(2\)-variation embedded area anomaly

**Status:** theorem and construction; pending the independent review recorded in
`JOURNAL.md`.

This note isolates a sharp obstruction at the critical exponent. It does
**not** construct a Jordan curve without a square, nor does it show that an
Osgood curve cannot satisfy Asano--Ike's approximation criterion. It shows
that, even for a finite-\(2\)-variation Jordan parametrization, uniform
parameter-aligned approximation by smooth Jordan curves does not determine
the Liouville primitive.

Throughout, a Jordan curve is positively oriented and
\[
             P(a)=\oint_a y\,dx .
\]
For a smooth positively oriented Jordan curve \(a\), Green's theorem gives
\[
             P(a)=-|\operatorname{int}(a)|.          \tag{1}
\]

## 1. Inner and outer approximations see different boundary area

**Theorem 1 (embedded period anomaly).** Let
\(c:S^1\to\mathbb C\) be a parametrized Jordan curve, let \(C=c(S^1)\),
and let \(\Omega\) be its bounded complementary component. There are two
sequences of regular smooth Jordan embeddings
\[
              c_n^-,c_n^+:S^1\longrightarrow\mathbb C
\]
such that both converge uniformly to \(c\), with the same parameter, and
\[
\begin{aligned}
 \lim_n P(c_n^-)&=-|\Omega|,\\
 \lim_n P(c_n^+)&=-|\overline\Omega|
                 =-|\Omega|-|C|.                    \tag{2}
\end{aligned}
\]
Consequently, when \(|C|>0\), the interleaved sequence
\[
              c_1^-,c_1^+,c_2^-,c_2^+,\ldots        \tag{3}
\]
is a uniformly convergent sequence of regular smooth Jordan embeddings
whose normalized Liouville primitives cannot converge locally uniformly.

**Proof.** Let \(\phi:\mathbb D\to\Omega\) be a Riemann map.
Carathéodory's theorem extends it to a homeomorphism
\(\overline{\mathbb D}\to\overline\Omega\). Its boundary map and \(c\)
have the same cyclic order, so there is an orientation-preserving circle
homeomorphism \(h\) such that
\[
                    c(t)=\phi(h(t)),\qquad t\in S^1. \tag{4}
\]
Choose orientation-preserving smooth circle diffeomorphisms \(h_n\to h\)
uniformly and radii \(r_n\uparrow1\), and put
\[
                    c_n^-(t)=\phi(r_nh_n(t)).        \tag{5}
\]
Here a point of \(S^1\) is regarded as a unit complex number. Since
\(\phi\) is analytic with nonzero derivative in \(\mathbb D\), each
\(c_n^-\) is a regular smooth embedding. Uniform continuity of the
Carathéodory extension gives \(c_n^-\to c\) uniformly. Its bounded
component is exactly \(\phi(r_n\mathbb D)\). These domains increase to
\(\Omega\), so continuity of Lebesgue measure from below and (1) give
\[
             P(c_n^-)=-|\phi(r_n\mathbb D)|
                     \longrightarrow-|\Omega|.      \tag{6}
\]

For the other side, let
\[
 \psi:\{z:|z|>1\}\cup\{\infty\}
       \longrightarrow(\mathbb C\setminus\overline\Omega)\cup\{\infty\}
\]
be the exterior Riemann map. It too has a Carathéodory boundary
homeomorphism. Thus, after choosing the compatible orientation, there is
an orientation-preserving circle homeomorphism \(k\) with
\[
                       c(t)=\psi(k(t)).              \tag{7}
\]
Choose smooth orientation-preserving diffeomorphisms \(k_n\to k\) and
\(R_n\downarrow1\), and set
\[
                       c_n^+(t)=\psi(R_nk_n(t)).      \tag{8}
\]
Again these are regular smooth embeddings and converge uniformly, with
parameter, to \(c\).

Let \(B_R\) be the bounded region cut off by
\(\psi(RS^1)\). As \(R\downarrow1\), the unbounded domains
\(\psi(\{|z|>R\})\) increase to
\(\mathbb C\setminus\overline\Omega\); equivalently, the closures of the
bounded regions \(B_R\) decrease to \(\overline\Omega\). Taking one fixed
\(R_0>1\), all later \(B_R\) lie in the finite-measure set \(B_{R_0}\).
Continuity of measure from above therefore gives
\[
             |B_{R_n}|\longrightarrow|\overline\Omega|
                       =|\Omega|+|C|.                \tag{9}
\]
Equation (1) proves the second limit in (2).

Normalize each primitive to be zero at \(t=0\). Its increment over one
period is \(P(c_n^\pm)\). If \(|C|>0\), (2) says that the periods of the
interleaved sequence have two distinct limits. Uniform convergence of the
primitives even on one parameter period is therefore impossible. \(\square\)

The theorem is deliberately about a supplied approximation sequence.
Asano--Ike require the **existence** of one sequence with convergent
primitives. Thus (3) refutes the implication
\[
 \text{``uniform embedded smooth approximation''}
 \Longrightarrow
 \text{``primitive convergence for that approximation''},              \tag{10}
\]
but does not refute their criterion for the limiting curve.

## 2. A critical Osgood curve

For completeness, the anomaly can be placed exactly at finite
\(2\)-variation rather than merely on an unspecified positive-area Jordan
curve. Positive-area injective curves go back to Osgood; Nasso--Volčič give
a modern account of homogeneous area-filling arcs. The scale-controlled
Hilbert routing below records the extra endpoint \(1/2\)-Hölder estimate
needed here rather than inferring it from positive area alone.

**Lemma 2 (Hilbert--Osgood arc).** There is an injective
\(1/2\)-Hölder map \(g:[0,1]\to[0,1]^2\) whose image has positive planar
Lebesgue measure.

**Construction and proof.** Fix
\(\varepsilon_n=2^{-n-4}\) and define
\[
       \ell_0=1,\qquad
       \ell_n={1-\varepsilon_n\over2}\ell_{n-1}.       \tag{11}
\]
Inside each level-\((n-1)\) square of side \(\ell_{n-1}\), put four
level-\(n\) squares of side \(\ell_n\), one in each corner. Write
\(\mathcal Q_n\) for the resulting \(4^n\) squares and
\[
       K=\bigcap_{n\ge0}\bigcup_{Q\in\mathcal Q_n}Q.  \tag{12}
\]
The squares at a fixed level have disjoint interiors and
\[
 |K|=\lim_n4^n\ell_n^2
     =\prod_{n=1}^{\infty}(1-\varepsilon_n)^2>0.      \tag{13}
\]

We now give the routing invariant explicitly. An oriented square is a square
with two designated **adjacent corner gates**, called entry and exit. In the
model square take entry at the southwest corner and exit at the southeast
corner. Order its children
\[
        Q_{\rm SW},Q_{\rm NW},Q_{\rm NE},Q_{\rm SE}. \tag{14}
\]
Give them, respectively, the following ordered adjacent gate pairs:
\[
\begin{array}{c|c}
Q_{\rm SW}&({\rm SW},{\rm NW})\\
Q_{\rm NW}&({\rm SW},{\rm SE})\\
Q_{\rm NE}&({\rm SW},{\rm SE})\\
Q_{\rm SE}&({\rm NE},{\rm SE}).
\end{array}                                           \tag{15}
\]
Join the exit of each child to the entry of the next by the straight segment
between the two facing corners. The three segments lie, respectively, in
the left, top-middle, and right parts of the gap between the children. For
any other oriented square, rotate or reflect this model so that its
designated gates match the model gates.

Induction on the word length gives the following precise invariant:

1. the route in \(Q_w\) starts and ends at its designated boundary-corner
   gates and visits its four child routes in the order (14);
2. each level-\(n\) connector is an open straight segment of length
   \(\varepsilon_n\ell_{n-1}\), apart from its two endpoints;
3. a connector in \(Q_w\) is contained in
   \(Q_w\setminus\bigcup_jQ_{wj}\), so it is disjoint from every descendant
   connector except at the prescribed gate shared with its adjacent child;
4. connectors in incomparable parent squares are disjoint because those
   parent squares are disjoint; and
5. every gate is a persistent corner: repeatedly choosing the corner child
   at that gate gives nested squares whose intersection is the gate itself.

Items 1--5 hold at the root by (14)--(15). Replacing every child by a rotated
or reflected copy preserves its two boundary gates and keeps all descendants
inside that child. The three new straight connectors lie in the parent gap
and have only their endpoints in the children. This proves the induction.

Let \(G\) be \(K\) together with all these connectors. Distinct points of
\(K\) have different corner codes and are separated at their first differing
child. Connector interiors lie outside \(K\), are mutually disjoint by the
invariant, and meet \(K\) only at persistent gate endpoints. The ordering
(14) therefore gives \(G\) exactly the order of an interval, with root
endpoints at the southwest and southeast corners.

It remains to record the critical parametrization rather than appeal to the
picture. Assign the interval for a level-\(n\) square length
\(\ell_n^2\). In a parent interval of length \(\ell_{n-1}^2\), the four
child intervals use total length
\[
             4\ell_n^2=(1-\varepsilon_n)^2
                         \ell_{n-1}^2.               \tag{16}
\]
Split the remaining length equally among the three intervening connector
intervals, and parametrize each straight connector at constant speed.
Nested square intervals define their image by the unique point in the
corresponding nested squares. The routing invariant makes the resulting map
\(g:[0,1]\to G\) injective: distinct infinite codes separate in disjoint
child squares, connector interiors are mutually disjoint and avoid \(K\),
and shared gate endpoints correspond to a single shared parameter endpoint.

There is a universal \(H\) such that
\[
                       |g(t)-g(s)|\le H|t-s|^{1/2}.  \tag{17}
\]
Here is the complete scale estimate. A square interval \(I_w\) has
\[
        \operatorname {diam}g(I)\le\sqrt2\,\ell_n
             =\sqrt2\,|I|^{1/2}.                    \tag{18}
\]
A level-\(n\) connector interval has length
\[
 \tau_n={1-(1-\varepsilon_n)^2\over3}\ell_{n-1}^2
       ={2\varepsilon_n-\varepsilon_n^2\over3}
          \ell_{n-1}^2,                             \tag{19}
\]
whereas its image is a straight segment of length
\(\varepsilon_n\ell_{n-1}\). Since
\(\varepsilon_n<1/2\),
\[
 {\varepsilon_n\ell_{n-1}\over\sqrt{\tau_n}}
 \le \sqrt{3\varepsilon_n}<\sqrt3.                  \tag{20}
\]

We also need a one-sided estimate at a gate. Let \(u\) be either endpoint of
a square interval \(I_w\), and let \(t\in I_w\). Put \(d=|t-u|>0\), and
choose a descendant level \(m>|w|\) such that
\[
                         \ell_m^2\le d\le\ell_{m-1}^2.
\]
The persistent corner-child interval of level \(m-1\) is the interval of
length \(\ell_{m-1}^2\) immediately adjacent to \(u\). Hence it contains
\(t\), and both images lie in its level-\((m-1)\) square. Since
\[
        {\ell_{m-1}\over\ell_m}
          ={2\over1-\varepsilon_m}<3,                \tag{21}
\]
the preceding inclusions give
\[
               |g(t)-g(u)|\le3\sqrt2\,|t-u|^{1/2}.  \tag{22}
\]

For arbitrary \(s<t\), take the least square interval whose recursive
decomposition places \(s,t\) in different pieces. If a complete child
interval lies between their pieces, then
\[
 |t-s|\ge\ell_n^2,\qquad
 |g(t)-g(s)|\le\sqrt2\,\ell_{n-1}
              <3\sqrt2\,|t-s|^{1/2}.                \tag{23}
\]
Otherwise the pieces are a child and an adjacent connector, or two
consecutive children with their connector between. Split at the one or two
connector gates. Equations (20) and (22), followed by
\[
 \sqrt a+\sqrt b\le\sqrt{2(a+b)},\qquad
 \sqrt a+\sqrt b+\sqrt c\le\sqrt{3(a+b+c)},          \tag{24}
\]
give (17), for example with \(H=9\). If both points lie in one connector,
(20) applies directly; if they lie in one child, descend to its
decomposition. Letting nested square diameters tend to zero covers
infinite-code points. Thus \(g\) is continuous. Since it is an injection
from a compact interval into the plane, it is a homeomorphism onto \(G\).
Together with (13), the lemma follows. \(\square\)

The two endpoints of \(G\) are the southwest and southeast root corners.
Join them by a finite polygonal arc in the open lower half-plane, meeting
the square only at those endpoints. Parametrize \(G\) on one semicircle and
the closing arc Lipschitzly on the other. Each piece is \(1/2\)-Hölder after
this fixed affine rescaling. For points on different pieces, split the
shorter parameter-circle arc at its splice point and use the two-term
inequality in (24). If that shorter arc contains both splice points, it has
a fixed positive length and the estimate follows from the bounded diameter
of the whole curve. Thus one obtains a \(1/2\)-Hölder Jordan parametrization
\[
                         c:S^1\to\mathbb C            \tag{25}
\]
whose trace contains \(K\), and hence has positive area.

**Lemma 3 (critical variation).** Every \(H\)-\(1/2\)-Hölder path has
finite \(2\)-variation, with
\[
                         \|c\|_{2\text{-var}}^2\le H^2. \tag{26}
\]

**Proof.** For every partition \(0=t_0<\cdots<t_m=1\),
\[
 \sum_i|c(t_{i+1})-c(t_i)|^2
 \le H^2\sum_i(t_{i+1}-t_i)=H^2. \quad\square        \tag{27}
\]

Combining Theorem 1 with Lemmas 2--3 gives the promised sharp example.

**Corollary 4 (finite-\(2\)-variation anomaly).** There is a
finite-\(2\)-variation Jordan parametrization \(c\) and an interleaved
sequence of parameter-aligned regular smooth Jordan embeddings converging
uniformly to \(c\) whose normalized Liouville primitives do not converge.
All approximants are embedded; the failure is exactly the positive area of
the limiting trace.

## 3. The complementary zero-area fact

Positive boundary area is not an artifact of the proof at the level of the
period.

**Proposition 5 (period stability for null traces).** Suppose
\(|C|=0\) and \(c_n\to c\) uniformly, where all maps are positively
oriented Jordan embeddings. Then
\[
             |\operatorname{int}(c_n)|
                 \longrightarrow|\Omega|,            \tag{28}
\]
so the full Liouville periods converge.

**Proof.** If \(z\notin C\), then for all sufficiently large \(n\) the
straight-line homotopy between \(c_n\) and \(c\) avoids \(z\). Their winding
numbers about \(z\) are therefore equal. Hence, for every \(\delta>0\) and
all sufficiently large \(n\),
\[
 \operatorname{int}(c_n)\triangle\Omega
       \subset\{z:\operatorname{dist}(z,C)<\delta\}.  \tag{29}
\]
The measures of these neighborhoods decrease to \(|C|=0\). Equation (28)
follows. \(\square\)

This proposition controls only the increment over a full period. Local
primitive convergence along subarcs can still require a second-level area
lift. The remaining \(p=2\) problem is therefore:

> For zero-area finite-\(2\)-variation Jordan traces, what geometric
> condition prevents local area anomalies and makes the embedded lift
> unique?

The Dini--Young condition in `README.md` is one sufficient answer. Corollary
4 shows why finite \(2\)-variation plus uniform embedded approximation, by
itself, is not.
