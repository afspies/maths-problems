# Learnings — Square Peg conjecture

## What the next session should do first

- Compute the actual GKS continuation maps in the normalized null-spiral
  telescope. Formal fixed-input cocontinuity is false: a translated open
  front creates a new microlocal boundary class in the homotopy colimit.
- Any persistent diagonal-locality theorem must identify a
  **GKS-specific uniform gap or positivity property** which excludes that
  translated-front model. Bounded constructibility, small Hofer norm, square
  duality, and multiplicativity have all been audited.
- On the finite-dimensional side, search for a genuinely global two-ended
  envelope invariant or a nonlocal correction to square degree. Cross-time
  avoidance permits alternating winding, and the unique total-collision
  orbit can absorb odd local degree.

## Results

- Boedihardjo--Geng already solve the topological approximation problem that
  initially looked dangerous: their parameter-respecting polygonal
  interpolants can be chosen Jordan, and a separate lemma gives
  \(q\)-variation convergence for every \(q>p\).
- Fixed-parameter cyclic corner rounding can be made arbitrarily small in
  both uniform and \(1\)-variation norms.  Collinear speed jumps must be
  retained and smoothed; deleting their vertices loses parameter data.
- Young--Loeve stability then gives Asano--Ike primitive convergence for every
  finite-\(p\)-variation Jordan parametrization with \(p<2\).
- A Dini coordinate modulus
  \(\int\omega_x\omega_y/r^2<\infty\) gives a critical-scale extension via a
  quantitative sewing estimate.
- For every positive-area Jordan trace, inner and outer conformal level
  curves converge with the same boundary parameter but their Liouville
  periods differ in the limit by exactly the trace area.
- A four-corner Hilbert--Osgood routing with summable gaps gives a
  positive-area \(1/2\)-Hölder Jordan curve, hence the embedded period anomaly
  occurs within finite \(2\)-variation.
- For a zero-area Jordan trace, winding-number stability forces convergence
  of total enclosed areas under uniform oriented Jordan approximation. This
  does not by itself control local subarc primitives.
- Antonelli--Young's all-partitions signed-area convergence has a hidden
  uniform-local consequence: extend two prefix partitions by the same tail.
  The common tail cancels, giving a Cauchy estimate uniform in the endpoint.
- Therefore every \(1/2\)-Hölder Jordan parametrization with finite dyadic
  quadratic-diameter sum \(\sigma(c)\) satisfies Asano--Ike and gets every
  prescribed rectangle.
- A disjoint many-turn spiral comb can have
  \(\sigma(c)<\infty\) but infinite \(p\)-variation for every \(p<2\):
  choose radius \(a_n=2^{-n-20}\), turn count
  \(N_n\asymp4^n/n^2\), and time \(w_n=N_na_n^2\).
- The two-arm spiral \(r=\theta^{-1/d}\), \(1<d<2\), is Jordan,
  nonrectifiable, finite \(p\)-variation for every \(p>d\), and not locally
  monotone.  It proves the new class is strictly outside Asano--Ike's two
  named corollaries.
- Asano--Ike Remark 5.5 already solves every positive-planar-measure Jordan
  trace by density.  The unrestricted problem therefore reduces to null
  traces.
- A null trace still need not satisfy Asano--Ike Theorem 1.1.  Interleave
  \(a(\theta)=\theta^{-1/2}\) with
  \(b(\theta)=(a(\theta)+a(\theta+2\pi))/2\).  The logarithmically divergent
  arm actions cancel in the full period to an integrable
  \(O(\theta^{-2})\) remainder.
- Local action rigidity: on every regular smooth subarc of the limit, uniform
  convergence of both parametrized Jordan curves and their primitives forces
  the limiting primitive to equal the classical line integral.  The proof
  extracts a proper crosscut in a shrinking tubular rectangle and applies
  Green's theorem; uniform primitive convergence removes the moving-endpoint
  errors.
- Consequently the null double spiral admits no parameter-aligned regular
  \(C^1\) approximants with convergent primitives.  This excludes every
  possible Asano--Ike Theorem 1.1 sequence, not just conformal or polygonal
  approximants.
- For every bounded Jordan domain, the analytic level curves of the Riemann
  map have mean-centered Liouville primitives converging strongly in
  \(L^2\).  The proof is an explicit Fourier decomposition using
  \(\sum n|a_n|^2=|\Omega|/\pi\).
- This gives an exhaustive dichotomy.  Either the primitives are
  asymptotically equicontinuous and hence converge uniformly, giving every
  rectangle, or order-one action concentrates on intervals shrinking to one
  prime end.  In the second branch the winding multiplicity grows at least
  like \(\rho^{-2}\).
- If a Jordan curve has no square, Matschke's obstruction produces an exact
  special trapezoid at every parameter scale.  Direct coordinates classify
  the only possible normal, crossed, pair-coalescent, and equilateral
  collision screens.
- Exact shrinking squares can carry arbitrary prescribed limiting action.
  Four disjoint fixed-vertex Hamiltonian twists change the action by an
  arbitrary four-point second difference while the maps and their inverses
  converge uniformly to the identity.
- The exact unrestricted target is persistent diagonal locality: collapsing
  interior-action generators must pair into bars of vanishing length so that
  derived global diagonal \(\mu hom\) vanishes away from \(\pi\mathbb Z\).
- The conformal concentration branch is nonempty and quantitatively sharp.
  On the null spiral a fixed action survives while harmonic measure is
  \(\exp(-\Theta(V^2))\), area is \(O(V^{-1})\), and critical trace capacity
  is \(O(V^{-2})\).
- Finite null-spiral truncations have clean diagonal cohomology only at
  \(0\pmod\pi\), but the limit has the full projected action circle over the
  collapsed point.  Its sheets form an infinitely winding eye of total width
  \(\pi/\theta+O(\theta^{-2})\).
- Under the no-square hypothesis, Matschke's special-trapezoid locus contains
  a connected fixed-type continuum spanning each compact positive scale
  interval.
- In the action-retaining helical-eye model, the boundary quotient between
  \(!\) and \(*\) is locally constant along the action circle and has
  \(\tau_t=0\).  The two extensions are therefore identical after Tamarkin
  localization.  A narrow eye of width \(w\) is \(w\)-torsion.
- For any moving square with outer paths \(a,b\) and inner paths
  \(a+J(b-a),b+J(b-a)\), the two ribbon areas differ only by half the
  endpoint side-length squares.  A simple compactified square envelope is
  therefore impossible.
- Oh's engulfable localization identifies the cotangent local/global complex
  and fundamental invariant under a full engulfable homotopy, but it does
  not identify Asano--Ike's twisted \(v\)-complex. Asano--Ike's
  distinguished \(v\) microlocalizes to \(v\otimes1+1\otimes v\), which
  restricts to zero on the clean diagonal; it is not Oh's fundamental class.
- Fixed-first-input microlocal Hom fails to preserve the exact translated
  homotopy colimit used by completeness:
  \(F=\mathbb k_{(0,1)}\), \(G_n=\mathbb k_{(1/n,1)}\) have zero finite
  restriction at \(T^*_0\mathbb R\), while
  \(\operatorname{hocolim}G_n=F\) and \(\mu hom(F,F)\) has a rank-one
  boundary microstalk.
- Hugelmeyer's cross-time avoidance admits the exact shrinking square path
  \((z,2z,(1+i)z,(2+i)z)\) with
  \(z=e^{-t+(i/20)\sin(\pi t/\log2)}\). It is strictly separated by a
  Jordan domain but has infinitely many alternating-winding lenses.
- A square-test zero with exact Jacobian determinant \(-2\) can collapse into
  a locally square-free \(1/4\)-Lipschitz Jordan germ. The exact square
  screen and prime-end side persist, so local odd square degree is not
  \(C^0\)-closed.

## Dead ends and cautions

- Do not describe rectifiable curves as open: Asano--Ike v3 prove every
  prescribed rectangle for them.
- Bare mollification is not an embedded approximation argument.
- Uniform convergence plus bounded \(2\)-variation does not control area.
  The repeated shrinking circle demonstrates the analytic anomaly but is not
  Jordan. The positive-area Osgood construction now supplies a genuinely
  embedded approximation anomaly, but only for a supplied sequence: it does
  not show failure of Asano--Ike's existential condition.
- That last limitation does not apply to the new null double spiral: local
  action rigidity proves failure of the existential primitive criterion
  itself.  The curve has infinite \(2\)-variation, so it does not weaken the
  positive finite-\(2\)-variation results.
- Conservative \(C^0\) smoothing controls maps, not action potentials.
  Shrinking high-turn radial twists have vanishing displacement and
  order-one action oscillation.
- Square-angle Floer symmetry does not pin the top action at half the area.
  Duality exchanges degrees \(1\) and \(2\), while the available triangle
  inequality is only for degree \(2\).  The axioms permit the two actions to
  tend to \(0\) and the full enclosed area.
- Strong \(L^2\) convergence does not control normalization at a point and
  does not imply diagonal sheaf-cohomology vanishing.  A point-supported
  action spike disappears in \(L^2\) but can support a skyscraper sheaf.
- Even critical \(H^{1/2}\) trace capacity is too weak: the null spiral puts
  fixed action on intervals whose capacity tends to zero.
- The old collapsed-point helical-eye model was wrong: it discarded the
  action circle, compared different punctured side-boundary conventions,
  and inferred a sheaf morphism from a common stalk.  Do not reuse it.
- Closed microsupport and \(C^0\) barcode convergence still do not identify
  exact-action cohomology.  The correct obstruction is a Milnor/ephemeral
  term in the continuation telescope, not a \(!\)-versus-\(*\) choice.
- Jordan separation and square symmetry do not cancel the two projected
  capping windings.  Two disjoint spiral fjords make their sum have order-one
  integral on support of vanishing area.
- Small local Hamiltonian oscillation gives a small interleaving estimate,
  not equality of microlocal germs or endpoint microstalks.  The interval
  \(\mathbb k_{[a,a+\varepsilon)}\) converges to zero while keeping a
  non-zero microstalk at \(a\); an action skyscraper has zero one-sided
  distance but non-zero global cohomology.
- Matschke's all-scales carrier need not contain a spanning path.  Even a
  path need not have finite variation or simple/one-sided-winding ribbons,
  so the square-envelope area identity is conditional rather than a proof.
- Ordinary Fulton--MacPherson collision screens require tangent data.
  Arbitrary Jordan arcs can have normalized square screens, so the standard
  compactification has no curve-independent nonzero boundary test map.
- The stronger compactification by cyclic gaps, a normalized secant screen,
  and prime-end side also fails locally: the four total-collision vertices
  are one cyclic orbit, and an odd regular square zero can be absorbed there.
- Do not invoke fixed-first-input constructibility to commute \(\mu hom\)
  with the metric-completion telescope. The fixed sheaf is a contravariant
  internal-Hom test object, and microlocal specialization also contains
  \(Rj_*\); both obstruct a generic cocontinuity theorem.
- Do not identify Asano--Ike's \(v\) with the clean diagonal fundamental
  class or use Oh's fundamental-class spectral bound for it.
- Cross-time relation avoidance is already implied by exterior/interior
  separation and does not give a sign for envelope winding.
- The finite-\(p\) theorem is likely a short, nearly formal synthesis rather
  than deep novelty.  Targeted search found no explicit statement, but that
  does not establish priority. The independent audit recommends “apparently
  unstated consequence,” not “new rough-integration theorem.”
- Do not call Antonelli--Young Theorem 1.2 a planar beta-number criterion.
  Its directly usable planar hypothesis is the dyadic diameter-square sum;
  beta numbers occur in the ambient Heisenberg-map/fibre argument.
- Convergence of dyadic polygon areas alone is not enough at \(1/2\)-Hölder
  regularity. The essential Antonelli--Young input is convergence over all
  fine partitions.
