# Rectangular pegs from Young-regular Jordan curves

**Status:** partial result; the unrestricted Square Peg conjecture remains
open.

## Abstract

We combine Asano--Ike's 2026 smooth-approximation criterion with
Boedihardjo--Geng's parameter-respecting Jordan polygon interpolation and
Young integration.  Every Jordan parametrization of finite \(p\)-variation
for some \(p<2\) satisfies the criterion and hence inscribes every prescribed
rectangle.  The same proof works at the critical scale under the coordinate
Dini condition
\[
\int_0^1\omega_x(r)\omega_y(r)r^{-2}\,dr<\infty.
\]
At the exact \(1/2\)-Hölder threshold, Antonelli--Young's finite dyadic
quadratic-diameter sum also suffices.  An explicit critical spiral comb
satisfies this condition while having infinite \(p\)-variation for every
\(p<2\).
An explicit double-spiral family is nonrectifiable and not locally monotone,
yet has finite \(p\)-variation for some \(p<2\).  Thus the result gives
rectangular pegs for a class not contained in the two named Asano--Ike
corollaries. At the critical exponent we construct a positive-area,
\(1/2\)-Hölder Jordan curve whose inner and outer smooth embedded
approximations have incompatible Liouville-period limits. Thus finite
\(2\)-variation plus parameter-aligned embedded \(C^0\) approximation does
not force primitive convergence. More sharply, an explicit planar-null
double spiral admits no parameter-aligned \(C^1\) Jordan approximation with
convergent Liouville primitives. Thus the Asano--Ike primitive criterion
cannot cover all Jordan curves.  Its conformal exhaustion realizes a fixed
action spike on intervals of exponentially small harmonic measure and
vanishing critical trace capacity.  At the microlocal level this becomes an
infinitely winding eye of vanishing phase width.  The universal conjecture
remains open.

## Main result

**Theorem.** Let \(c:S^1\to\mathbb R^2\) be a Jordan parametrization.  If
\(c\) has finite \(p\)-variation for some \(1\le p<2\), then \(c(S^1)\)
inscribes a \(\theta\)-rectangle for every \(\theta\in(0,\pi)\).

**Critical extension.** The same conclusion holds if the periodic coordinate
moduli satisfy
\[
\int_0^1\frac{\omega_x(r)\omega_y(r)}{r^2}\,dr<\infty.
\]

**Critical quadratic-diameter extension.** The same conclusion holds if
\(c\) is \(1/2\)-Hölder and
\[
\sigma(c)=\sum_{i\geq0}\sum_{j<2^i}
\operatorname {diam}\{c(j2^{-i}),c((2j+1)2^{-i-1}),
c((j+1)2^{-i})\}^2<\infty.
\]

The complete argument, including the fixed-parameter embedded \(C^1\) rounding
lemma and explicit Young--Loeve estimate, is in
`../angles/p-variation/README.md`.  The Dini refinement and \(p=2\) boundary
are in `../angles/critical-p2/README.md`; the quadratic-diameter proof is in
`../angles/critical-p2/antonelli-young-bridge.md`.

## Proof architecture

Choose \(p<q<2\).  Boedihardjo--Geng construct partitions of mesh tending to
zero whose affine interpolants are still Jordan; their separate variation
lemma gives convergence to \(c\) in \(q\)-variation.  Each finite Jordan
polygon can be rounded inside pairwise disjoint vertex disks so that the
result is a regular \(C^1\) Jordan embedding on the same parameter circle and
the \(1\)-variation of the change is arbitrarily small. Thus the approximants
also converge in \(q\)-variation. Asano--Ike Remark 5.6 explicitly permits
these \(C^1\) approximants.

Writing \(c=(x,y)\), normalize the primitives by
\[
F_n(t)=\int_0^t y_n\,dx_n,\qquad F_n(0)=0.
\]
Young's estimate for \(q<2\) makes \(F_n\) converge uniformly on one period.
The period increments converge as well, so the primitives converge locally
uniformly on the universal cover \(\mathbb R\).  These are exactly
Asano--Ike's hypotheses.  No mollified curve is silently assumed to remain
embedded.

For the Dini extension, dyadic refinement errors are summable with tail
bounded by
\[
C\int_0^\delta\omega_x(r)\omega_y(r)r^{-2}\,dr.
\]
This supplies primitive convergence directly; the same embedded polygons and
corner rounding then apply.

For the exact critical extension, Antonelli--Young prove convergence of
polygonal signed areas over all fine partitions under \(\sigma(c)<\infty\).
That all-partitions quantifier upgrades total area to a uniform local
primitive: extend any two fine partitions of \([0,t]\) by the same fine
partition of \([t,1]\), and the common tail cancels. Boedihardjo--Geng then
supplies embedded Jordan polygons among the controlled partitions; diagonal
\(C^1\) rounding preserves their primitives.

## Strict witness beyond rectifiability and local monotonicity

For \(1<d<2\), take two disjoint rotated spirals
\[
\gamma_0(\theta)=\theta^{-1/d}e^{i\theta},\qquad
\gamma_1(\theta)=e^{i\delta}\gamma_0(\theta),
\quad \theta\ge1,
\]
and join their radius-one endpoints by a circular arc.  Strictly monotone
radius proves embeddedness.  Its length dominates
\(\sum n^{-1/d}=\infty\), while its \(p\)-variation is finite for every
\(p>d\).  Every linear projection oscillates infinitely often at the common
origin, so the curve is not locally monotone.  Details are in
`../results/spiral-family.md`.

The sharper critical witness replaces disjoint tiny axis diameters by
many-turn simple annular detours. At scale \(n\), take
\[
a_n=2^{-n-20},\qquad
N_n=\left\lceil4^n/n^2\right\rceil,\qquad
w_n=N_na_n^2.
\]
The supports have summable lengths \(w_n\asymp n^{-2}\), and constant-speed
traversal gives a uniform \(1/2\)-Hölder bound. A supported-bump estimate
gives
\[
\sigma(f_n)\lesssim w_n+a_n^2\log(e/a_n^2),
\]
so \(\sigma(c)<\infty\). But \(\sum_nN_na_n^p=\infty\) for every \(p<2\).
Disjoint detour disks prove embeddedness, and the full turns accumulating at
the basepoint defeat every linear projection. Details are in
`../results/critical-spiral-comb.md`.

## Verification

The exact rational harness is deliberately limited to finite conjecture
hygiene:

```text
python3 -m unittest discover -s problems/square-peg/harness -p 'test_*.py' -v
```

Five tests verify rational polygonal simplicity, reject crossings and
degeneracies, check the shoelace/Liouville sign, prove exact primitive
invariance under rational subdivision, and verify/reject candidate inscribed
squares.  These tests do not certify the universal theorem, whose proof is
analytic.

## Critical obstruction

The obstruction persists with every approximant embedded. For any Jordan
trace \(C=\partial\Omega\), inner conformal level curves converge with
parameter to \(C\) and have Liouville periods tending to \(-|\Omega|\).
Outer conformal level curves also converge with parameter to \(C\), but their
periods tend to
\[
                         -|\overline\Omega|
                         =-|\Omega|-|C|.
\]
If \(|C|>0\), interleaving the two smooth Jordan sequences destroys primitive
convergence.

A scale-controlled Hilbert--Osgood construction gives a positive-area
\(1/2\)-Hölder Jordan curve. Since
\[
 |c(t)-c(s)|\le H|t-s|^{1/2}
 \quad\Longrightarrow\quad
 \sup_P\sum_{[u,v]\in P}|c(v)-c(u)|^2\le H^2,
\]
this is a finite-\(2\)-variation counterexample to **automatic primitive
stability for a supplied embedded approximation sequence**. It does not show
that the curve fails Asano--Ike's existential criterion, and it is not a
counterexample to the Square Peg conjecture.

For zero-area Jordan traces, winding-number stability forces the total
periods of all uniformly convergent oriented Jordan approximants to converge.
The Antonelli--Young theorem now also controls the full local primitive when
the curve is \(1/2\)-Hölder and \(\sigma(c)<\infty\). The remaining frontier
is uniqueness or realizability of the local area lift outside this
quadratic-diameter class.

## Unrestricted zero-trace obstruction

Asano--Ike Remark 5.5 already supplies every prescribed rectangle when the
Jordan trace has positive planar measure. Hence the unrestricted problem
reduces to null traces. Null trace stabilizes total enclosed areas and permits
an area-preserving Hamiltonian filling, but it does not force a continuous
boundary action lift.

Let
\[
a(\theta)=\theta^{-1/2},\qquad
b(\theta)=\frac{a(\theta)+a(\theta+2\pi)}2.
\]
Follow \(a(\theta)e^{i\theta}\) inward to the origin, follow
\(b(\theta)e^{i\theta}\) outward, and close across the outer radial gap.
The inequalities
\[
a(\theta)>b(\theta)>a(\theta+2\pi)
\]
prove that the curve is Jordan. Its trace is a countable union of rectifiable
arcs and therefore has planar measure zero. Its enclosed area is finite
because
\[
a(\theta)^2-b(\theta)^2=O(\theta^{-2}).
\]
However, for \(\alpha=(x\,dy-y\,dx)/2\),
\[
\int_{\theta_0}^{\Theta}\alpha
=\frac12\int_{\theta_0}^{\Theta}\frac{d\theta}{\theta}
=\frac12\log(\Theta/\theta_0).
\]

A local action-rigidity lemma makes this divergence unavoidable. If
parameter-aligned \(C^1\) Jordan curves and their normalized primitives both
converge uniformly, then on every regular smooth subarc of the limit the
limiting primitive equals the classical line integral. The proof extracts a
proper crosscut in a shrinking tubular rectangle and applies Green's theorem;
uniform primitive convergence removes its moving-endpoint errors. Applied to
the inward spiral, it would force a continuous function at the origin
parameter to diverge.

Therefore this null Jordan curve satisfies no Asano--Ike Theorem 1.1
approximation. Explicit nested finite-spiral truncations have convergent
periods but local primitives diverging like \(-\tfrac12\log N\), even after
smooth embedded corner rounding.

This is not a counterexample to Square Peg. It shows that a universal proof
must instead establish Asano--Ike Remark 4.2's weaker diagonal
\(\mu hom\)-cohomology vanishing, or use a different no-shrinkout mechanism.
The square symmetry \(R_{\pi/2}^2=R_\pi\) does not settle it formally:
Greene--Lobb duality swaps the two spectral degrees rather than identifying
their actions.

## Universal conformal \(L^2\) compactness

There is nevertheless a canonical weak area lift for every Jordan domain.
Let \(f(z)=\sum a_nz^n:\mathbb D\to\Omega\) be conformal and
\(c_r(t)=f(re^{it})\).  If \(P_r\) is the mean-zero periodic part of the
\(\alpha=(x\,dy-y\,dx)/2\) primitive, then for \(k>0\)
\[
\widehat P_r(k)=\frac{C_{r,k}}{4i}+\frac{D_{r,k}}{2ik},
\]
\[
C_{r,k}=\sum_{m\ge0}\bar a_ma_{m+k}r^{2m+k},\qquad
D_{r,k}=\sum_{m\ge0}m\bar a_ma_{m+k}r^{2m+k}.
\]
Carathéodory gives \(C_r\to C\) in \(\ell^2\), while the conformal area
formula gives
\[
\sum_{m\ge1}m|a_m|^2=|\Omega|/\pi,\qquad
|D_{r,k}|\le|\Omega|/\pi.
\]
Dominated convergence and Parseval therefore give
\[
P_r\longrightarrow P\quad\text{strongly in }L^2(S^1).
\]
The exact identity \(y\,dx=\tfrac12d(xy)-\alpha\) gives the same result in
the Asano--Ike convention.

This has a sharp dichotomy.  If the lifted primitives are asymptotically
equicontinuous, the convergence is uniform and Asano--Ike gives every
prescribed rectangle.  Otherwise an order-one action concentrates on arcs
whose parameter length and image diameter tend to zero.  Closing by a chord
and applying the area--winding formula forces
\[
\|\operatorname{Wind}\|_\infty\gtrsim\rho^{-2}.
\]
Thus every unresolved conformal case has unbounded winding concentration at
a prime end.

The null double spiral realizes this branch sharply.  In logarithmic
coordinates its tail is a strip of width
\[
h(v)=\frac{\pi}{2v}-\frac{5\pi^2}{8v^2}+O(v^{-3}).
\]
Between heights \(V\) and \(cV\), its longitudinal modulus and reciprocal
condenser capacity are
\[
M(V,cV)=\frac{(c^2-1)V^2}{\pi}+O(V),\qquad
\operatorname {Cap}(V,cV)\asymp V^{-2}.
\]
Taking \(c=e^{2\varepsilon}\), the inward boundary action is exactly
\(\varepsilon\), while area and conformal energy are \(O(V^{-1})\) and the
harmonic measure of the tail is \(\exp(-\Theta(V^2))\).  In harmonic
parameter the divergent primitive grows only like
\(\frac14\log\log(1/|s-s_0|)\).  Hence \(L^p\), \(W^{1,2}\), harmonic
measure, and critical trace capacity cannot remove the exceptional action.

## Persistent diagonal locality

Individual shrinking-square actions cannot be controlled.  Four disjoint
fixed-vertex Hamiltonian twists preserve an exact shrinking square and
converge uniformly, together with their inverses, to the identity.  Their
action potentials change the square action by an arbitrary four-point
second difference.  A two-fjord model gives the same conclusion directly:
the sum of the two projected capping windings can carry order-one signed
area on support of vanishing planar area.

Accordingly, the exact missing theorem is bar-level:
\[
R\Gamma\!\left(\rho^{-1}\Delta_0;
\mu hom(F_0,T_aQF_0)|_{\rho^{-1}\Delta_0}\right)=0
\quad(a\notin\pi\mathbb Z),
\]
where
\[
Q=(\phi\times\phi)^{-1}R_{\pi/2}(\phi\times\phi)
\]
and \(L_0\cap Q(L_0)=\Delta_0\).  At approximation level, arbitrary
interior-action generators collapsing to the diagonal must pair into
persistence bars whose lengths vanish and leave no exact-action endpoint
microstalk.  No audited source supplies this \(C^0\) clean-intersection
theorem, and small interleaving distance alone does not imply it because
\(\mu hom\) does not commute with metric limits.

For every finite smooth truncation of the null spiral, the clean diagonal
complex is \(H^*(S^1;\mathbb F_2)\) entirely at action \(0\pmod\pi\).
Nevertheless, in the limit its diagonal phase is
\[
t_{AA}(\theta)=s^2\left(
\log\frac{\theta}{\theta_0}
-\frac{\sin2\theta}{2\theta}\right)+t_0\pmod\pi ,
\]
so the reduced microsupport contains the full action circle over the
collapsed prime end.  The two sheets form a vanishing-width eye with gap
\[
\delta(\theta)=\frac{\pi}{2\theta}+O(\theta^{-2}).
\]
The original collapsed-point eye model was incorrect.  The actual
restriction retains the full action circle.  After fixing one punctured
side-boundary convention, the \(!\)-versus-\(*\) cone is locally constant
along that circle, has \(\tau_t=0\), and vanishes in the Tamarkin quotient.
The deep eye itself is arbitrarily torsion.

The remaining calculation is instead the Milnor boundary term of the
metric-completion telescope.  This distinction matters: the constructible
objects
\[
 V_\varepsilon
 =V_{\rm std}\oplus\mathbb k_{[a_0,a_0+\varepsilon)}
\]
converge to \(V_{\rm std}\) while retaining a non-zero microstalk at the
fixed endpoint \(a_0\).  An action skyscraper has zero one-sided
interleaving distance from zero but non-zero global cohomology.  Therefore
an arbitrarily small Hofer cut-off of the diagonal germ does not prove
Asano--Ike Remark 4.2.

Matschke's obstruction gives a complementary exact degeneration statement:
a square-free Jordan curve has a special trapezoid at every parameter
scale.  These trapezoids have only normal, crossed, pair-coalescent, genuine
trapezoid, and equilateral collision screens, but ordinary
Fulton--MacPherson topology excludes none without tangent data.
More strongly, over every compact positive scale interval the exact
trapezoid locus contains a fixed-type connected continuum spanning the two
endpoint scales.  Local prime-end topology still excludes no screen; any
remaining configuration-space obstruction must be global along that
continuum.

Hugelmeyer's square envelope supplies a second global formulation.  If
\(a,b\) are its outer paths, \(v=b-a\), and
\(c=a+Jv,d=b+Jv\) are the inner paths, direct Young calculus gives
\[
 \mathcal A(\Gamma_{\rm in})-\mathcal A(\Gamma_{\rm out})
 =\frac{|v(s)|^2-|v(t)|^2}{2}.                            \tag{*}
\]
Thus a compactified finite-\(p<2\) envelope with simple nested ribbons is
impossible: the endpoint gaps vanish, so the two ribbon areas are equal,
while strict containment makes them unequal.  The calculation is exact for
synchronized polygons as well.

This remains conditional.  Hugelmeyer's definition gives outer winding one,
not simple ribbons or the stronger bounds
\(n_{\rm out}\geq\mathbf1_\Omega\) and
\(0\leq n_{\rm in}\leq\mathbf1_\Omega\) with strict area deficit; the paths
also need not have a joint geometric rough lift.  Signed areas can cancel
through repeated positive and negative winding.  Matschke's connected
carrier need not even contain a spanning path.

## Relation to prior work and novelty boundary

Asano--Ike already cover every rectifiable and every locally monotone Jordan
curve; this report does not rediscover those results.  Boedihardjo--Geng
already prove the hard embedded polygonal approximation and finite-\(p\)
Green theorem. Antonelli--Young already prove the critical signed-area
criterion. The contribution here is the synthesis of these inputs with
Asano--Ike's sheaf criterion, the uniform-prefix observation, and explicit
strict witnesses. Independent source-by-source searches found no explicit
prior peg theorem in either the finite-\(p<2\) or critical
quadratic-diameter terms, but both should be described as apparently
unstated corollaries/syntheses. Expert confirmation should precede a formal
priority claim.

## Cite as

See `CITATION.cff`.  No DOI has been minted.
