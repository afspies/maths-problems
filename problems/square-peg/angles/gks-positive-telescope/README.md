# GKS-positive telescopes and the exact no-ephemeral gap

## Verdict

**KILL positivity alone; HOLD the unrestricted theorem.**

The strongest natural statement based only on GKS origin, invertibility,
summable Hofer/interleaving size, and positive translated continuation maps
is false.  There is a smooth exact-graph counterexample in which

- the fixed first object is simple along a smooth compact exact
  Lagrangian;
- every stage is its image under an invertible, compactly supported GKS
  kernel;
- the Hamiltonian amplitudes are summable;
- after the tail translations used in the Asano--Ike completeness proof,
  the transition maps are the canonical positive epigraph maps; and
- every finite microlocal restriction over a fixed compact locus is zero,
  while the homotopy-colimit restriction is non-zero.

Thus merely excluding the translated open fronts
\(\mathbb k_{(1/n,1)}\) does not produce a no-ephemeral theorem.
Any theorem capable of proving Asano--Ike Remark 4.2 must use structure
special to the **conjugated relative rotation** (and not merely to GKS
kernels), or prove a uniform non-characteristic estimate which the null
spiral presently fails.

## 1. The attractive theorem, stated strongly

Let \(M\) be compact, let \(F\) be a simple sheaf quantization of a smooth
compact exact Lagrangian \(L\subset T^*M\), and let \(Z\subset L\) be
compact.  Consider a summable sequence of compactly supported Hamiltonian
diffeomorphisms \(\psi_n\) and put
\[
 G_n=K_{\psi_n}F.
\]
After the tail action translations in the completeness construction,
suppose the comparison maps
\[
 u_n:\widetilde G_n\longrightarrow\widetilde G_{n+1}       \tag{1}
\]
are the standard positive GKS continuation maps.  The tempting
GKS-positive no-ephemeral theorem is
\[
 \left.
 \mu hom(F,\widetilde G_n)\right|_{\rho^{-1}Z}\simeq0
 \quad\hbox{for all }n
 \quad\Longrightarrow\quad
 \left.
 \mu hom\!\left(F,\operatorname {hocolim}_n\widetilde G_n\right)
 \right|_{\rho^{-1}Z}\simeq0.                             \tag{2}
\]
One can also ask only for the vanishing of derived global sections over
\(\rho^{-1}Z\).  The counterexample below violates both versions.

This formulation already excludes the earlier translated-left-front
example as stated: all fronts below are smooth graphs, every object is a
simple exact-Lagrangian quantization, and every deformation is realized by
an invertible compactly supported GKS kernel.  Nevertheless (2) fails.

## 2. Smooth positive-GKS counterexample

### 2.1 A summable family of exact graphs

Work in a coordinate chart about \(x=0\) in \(S^1_x\).  Choose
\[
 g\in C^\infty_c((-2,2)),\qquad
 g\geq0,\qquad g'(0)=1,
\]
for example a positive bump times \(e^x\), rescaled by a constant.  Set
\[
 \varepsilon_n=2^{-n},\qquad
 f_n(x)=\varepsilon_n g(x/\varepsilon_n).                 \tag{3}
\]
Then
\[
 \|f_n\|_\infty=O(\varepsilon_n),\qquad
 f_n'(0)=1,\qquad
 f_n\longrightarrow0\quad\hbox{uniformly}.                \tag{4}
\]
Let
\[
 a_n=\|f_{n+1}-f_n\|_\infty,\qquad
 b_n=\sum_{j\geq n}a_j.
\]
The series is finite and \(b_n\to0\).  Define
\[
 \widetilde f_n=f_n-b_n .
\]
Since \(a_n\geq f_n-f_{n+1}\) pointwise,
\[
 \widetilde f_{n+1}-\widetilde f_n
 =f_{n+1}-f_n+a_n\geq0,                                  \tag{5}
\]
and \(\widetilde f_n\uparrow0\) pointwise and uniformly.

On \(S^1_x\times\mathbb R_t\), put
\[
 E(f)=\mathbb k_{\{t\geq f(x)\}},\qquad F=E(0).            \tag{6}
\]
The inclusions of the decreasing epigraphs in (5) give the canonical
restriction morphisms
\[
 E(\widetilde f_n)\longrightarrow E(\widetilde f_{n+1}).
                                                                    \tag{7}
\]
Filtered colimits of sheaves of vector spaces are exact and are computed
stalkwise.  Hence
\[
 \operatorname {hocolim}_n E(\widetilde f_n)
 \simeq E(0)=F.                                           \tag{8}
\]
Indeed, a point with \(t<0\) eventually leaves the epigraphs, while a point
with \(t\geq0\) remains in all of them.  Equations (5)--(8) are exactly the
tail-translation construction: the untranslated objects are
\(E(f_n)\), and \(E(\widetilde f_n)=T_{-b_n}E(f_n)\), in the convention
\(T_cE(f)=E(f+c)\).

The difference in (5) is non-negative.  Thus (7) is a positive contact/GKS
continuation map.  Its constant term \(a_n\) is precisely the forward
Tamarkin translation inserted by the interleaving; the underlying
symplectic map depends only on \(d(f_{n+1}-f_n)\).

### 2.2 Compact Hamiltonian realization

The positive-GKS claim is not merely terminology.  Choose
\(\chi\in C^\infty_c(T^*S^1)\) with \(\chi=1\) on
\[
 |p|\leq 1+\sup |g'|.
\]
The compactly supported Hamiltonian
\[
 H_n(x,p)=f_n(x)\chi(p)\geq0                              \tag{9}
\]
has Hofer amplitude \(O(\varepsilon_n)\).  On the zero-section its flow
stays in the region where \(\chi=1\) and sends
\[
 (x,0)\longmapsto(x,-df_n(x))
\]
with the sign convention
\(\iota_{X_H}d(p\,dx)=-dH\).  The GKS transform of \(E(0)\) is therefore
microlocally \(E(f_n)\); the cutoff does not alter this germ.  In
particular, every \(E(f_n)\) in the construction is obtained from the
fixed simple object \(F\) by an invertible compactly supported GKS kernel,
and
\[
 \sum_n\|H_n\|_{\rm osc}<\infty.                          \tag{10}
\]
If a compact positive-dimensional test locus is desired, take the external
product with the zero-section quantization on a second circle \(S^1_y\).
All statements then hold over
\[
 Z=\{(x,p_x)=(0,0)\}\times 0_{S^1_y}\simeq S^1.           \tag{11}
\]

### 2.3 Exact microlocal failure

The positive reduced microsupport of \(E(f)\) along its front is the exact
graph
\[
 \rho\bigl(SS(E(f))\cap\{\tau>0\}\bigr)
 =\{(x,p=-f'(x))\}.                                      \tag{12}
\]
At \(x=0\), (4) gives \(p=-1\) at every finite stage, whereas the
microsupport of \(F\) is the zero-section.  Consequently
\[
 \left.\mu hom(F,E(\widetilde f_n))\right|_{\rho^{-1}Z}
 \simeq0
 \qquad\text{for every }n.                               \tag{13}
\]
The action translation by \(-b_n\) does not change the reduced covector.
But (8) and simplicity of \(F\) give
\[
 \left.
 \mu hom\!\left(F,\operatorname {hocolim}_n
 E(\widetilde f_n)\right)\right|_{\rho^{-1}Z}
 \simeq
 \left.\mu hom(F,F)\right|_{\rho^{-1}Z}
 \simeq\mathbb k_Z                                      \tag{14}
\]
up to the universal grading convention.  In the external-product version,
\[
 R\Gamma(\rho^{-1}Z;\mathbb k_Z)
 \simeq R\Gamma(S^1;\mathbb k)\neq0.                     \tag{15}
\]

This proves the failure of (2) with smooth exact fronts and genuine
positive GKS continuation maps.  The geometric reason is visible in (3):
although the covector at \(x=0\) stays separated from zero, the spatial
support of \(df_n\) shrinks to \(x=0\).  No fixed conic neighborhood of
\((0,0)\) is disjoint from all the graph fronts.  Positivity orders the
maps; it does not make microlocal specialization cocontinuous.

The construction is local in the action line.  Replacing the epigraph
outside a fixed action chart by a half-open object with a distant right
cutoff puts the same left-front calculation inside
\(\mathbb R_t/\pi\mathbb Z\); the cutoff front is outside the tested chart
and does not change (12)--(15).  Thus no global periodization of an
epigraph is being assumed.

## 3. What remains plausible

The counterexample leaves one genuinely square-specific theorem:

> **Conjugated-rotation no-ephemeral theorem (open).**  Let
> \(L=C_0\times C_0\), let
> \(Q_n=\Phi_n^{-1}R_{\pi/2}\Phi_n\) converge through the Asano--Ike
> completed GKS construction to
> \(Q=\Phi^{-1}R_{\pi/2}\Phi\), and suppose
> \(L\cap Q(L)=\Delta_0\).  For every
> \(a\notin\pi\mathbb Z\), the cross-stage diagonal tower for
> \[
> R\Gamma\!\left(\rho^{-1}\Delta_0;
> \mu hom(F_0,T_aQ_nF_0)|_{\rho^{-1}\Delta_0}\right)
> \]
> is pro-zero and has zero Milnor boundary term.

This statement excludes the graph example because it uses all of the
conjugated-rotation structure: a common fixed diagonal, zero finite-stage
diagonal action, \(Q_n^2=R_\pi\), and the twisted torus quantization.  It is
also essentially the missing theorem, not a consequence of positivity.
The formal \(v\)-module model in
`../local-floer-engulfing/README.md` already shows that the square symmetry
and the known \(v\)-relations, without a geometric computation of the
telescope maps, do not prove it.

A standard sufficient replacement is a **uniform conic gap**: one fixed
conic neighborhood of the forbidden diagonal-action locus misses every
finite-stage microsupport and every transition-cone microsupport.  Then the
microsupport limsup estimate gives the required vanishing.  This is
proof-grade but does not advance Square Peg: it is precisely the uniform
separation lost at a wild prime end and is stronger than the hypothesis
available for the null spiral.

## 4. Normalized null-spiral truncations

### 4.1 Quantities which are determined

Let \(\Theta_N=\theta_0+2\pi N\), let \(A=|\Omega|\), and let
\[
 D_N=\frac12\int_{\Theta_N}^{\infty}(a^2-b^2)\,d\theta
 =\frac{\pi}{2\Theta_N}+O(\Theta_N^{-2})                  \tag{16}
\]
be the omitted tail area.  The truncation has area \(A-D_N\), so its
area-\(\pi\) normalization is
\[
 s_N^2=\frac{\pi}{A-D_N}
 =s^2\left(1+\frac{D_N}{A}+O(D_N^2)\right),
 \qquad s^2=\frac{\pi}{A}.                               \tag{17}
\]
At the inner cap, with the outer endpoint used as the primitive basepoint,
the common \(AA\)-sheet phase is
\[
 c_N=s_N^2\log\frac{\Theta_N}{\theta_0}+t_{0,N}
 \pmod\pi,                                                \tag{18}
\]
because \(\sin(2\Theta_N)=0\).  The total eye width is
\[
 w_N=s_N^2\left(\frac{\pi}{\Theta_N}
 +O(\Theta_N^{-2})\right).                               \tag{19}
\]
For consecutive one-turn truncations,
\[
 c_{N+1}-c_N-(t_{0,N+1}-t_{0,N})
 =\frac{2\pi s^2}{\Theta_N}
 +O\!\left(\frac{\log\Theta_N}{\Theta_N^2}\right)
 =2w_N+o(w_N).                                           \tag{20}
\]
Thus neither full action support nor the shrinking width determines a
persistent endpoint: the cap phase moves on the same scale as the eye
itself.

In spatial radius \(r_N\asymp s\Theta_N^{-1/2}\), (19) says
\[
 w_N\asymp r_N^2.                                        \tag{21}
\]
Since the common helical phase satisfies
\[
 t(r)=-2s^2\log r+O(1),
\]
the positive conormal to its front has
\[
 \frac{\tau_t}{|\nu_r|}
 \asymp\frac{r}{2s^2}\longrightarrow0.                   \tag{22}
\]
The null spiral therefore has strict stagewise positive \(t\)-direction
but no **uniform positive angle** away from \(\tau_t=0\).  Any theorem
whose checkable hypothesis is a uniform inequality
\(\tau_t\geq\kappa|\nu_r|\), \(\kappa>0\), excludes both the smooth graph
counterexample and the null spiral.

### 4.2 The continuation maps are not fixed by completeness

There is no canonical ``normalized null-spiral truncation telescope'' whose
endpoint scalar can be read from (16)--(22).

Asano--Ike's completeness theorem
(arXiv:2201.02598v4, Theorem 4.3 and Corollary 4.5) starts with **chosen**
\(a_n\)-isomorphisms.  It forms
\[
 G_n=T_{-a_{\geq n}}F_n,\qquad
 F_\infty\simeq\operatorname {hocolim}_nG_n,              \tag{23}
\]
where the maps \(G_n\to G_{n+1}\) are built from those choices.
The theorem bounds the cones by torsion; it does not specify their endpoint
microstalk maps.

For Jordan curves, Asano--Ike Proposition 5.1 proves that the normalized
quantizations are Cauchy **after translating them in the action
direction**.  Its proof compares curves through auxiliary annuli and a
Hamiltonian-distance estimate.  It does not select a direct Hamiltonian
isotopy \(C_N\to C_{N+1}\), a preferred action translation \(t_{0,N}\), or
a preferred GKS continuation morphism.  The time-one GKS object is
canonical, but the comparison morphism used in (23) is additional data.

This matters here.  Equation (20) changes when \(t_{0,N}\) changes, while
the forbidden diagonal cohomology is invariant under translating the whole
quantization.  Moreover, the two area-normalized truncation domains both
have area \(\pi\).  In any non-trivial boundary isotopy between them the
outward normal velocity must change sign, since
\[
 \frac{d}{ds}\operatorname {Area}(D_s)
 =\int_{\partial D_s}V_n\,d\ell=0.                        \tag{24}
\]
Thus the simplest nested-domain positive continuation does not exist.

After restriction to a rank-one simple summand of a shrinking eye, the
minimal unresolved coefficient is the map on its cap endpoint microstalk:
\[
\mathbb k\xrightarrow{\ 0\ \text{or}\ 1\ }\mathbb k .
                                                                  \tag{25}
\]
Identity maps can leave a skyscraper/Milnor class, as the exact graph
telescope proves; zero maps kill it.  Neither the GKS completeness theorem,
the Hofer estimate, (16)--(22), nor stagewise positivity computes (25).
One must choose an explicit conservative isotopy between successive
normalized spiral truncations and calculate its microlocal continuation
map, together with the four-sheet differential and any resulting matrix of
such coefficients.  Calling those maps ``positive'' does not determine
them because the necessary tail translation is part of the choice.

## 5. Consequence for the campaign

The next sheaf attack should not seek a generic GKS no-ephemeral theorem.
The smooth graph telescope refutes it at essentially the maximum plausible
level of generality.  There are only two honest ways forward:

1. prove the conjugated-rotation theorem using a new relation among the
   four sheets and the common clean diagonal which forces the scalar in
   (25) to be zero; or
2. construct an explicit normalized null-spiral comparison isotopy and
   calculate (25).  A non-zero scalar would be a sharp no-go for this proof
   route, while a zero scalar would be the first genuine evidence for
   persistent diagonal locality.

At present the adversarial verdict on unrestricted Square Peg remains
**HOLD**.  The new rigorous result is the **KILL** verdict for GKS
positivity, invertibility, and summable translated continuation as
sufficient no-ephemeral hypotheses.
