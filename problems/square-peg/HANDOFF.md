# Handoff prompt — Square Peg conjecture

You are continuing a proof-first attack on the Square Peg conjecture in
`problems/square-peg/`.

Read, in order:

1. `/AGENTS.md` and `AGENTS.local.md` if present.
2. `PROBLEM.md`.
3. `LEARNINGS.md`.
4. `literature/TAO56_CLAIM_AUDIT.md`.
5. `angles/tao-conormal-bridge/README.md`.
6. `angles/gks-positive-telescope/README.md`.
7. `angles/envelope-global-linking/README.md`.
8. `angles/global-collision-charge/README.md`.
9. `angles/conormal-tail-splicing/README.md`.
10. `angles/p-variation/README.md`.
11. `angles/critical-p2/README.md`.
12. `angles/critical-p2/antonelli-young-bridge.md`.
13. `results/critical-spiral-comb.md`.
14. `angles/unrestricted-zero-trace/README.md`.
15. `results/null-spiral-no-primitive.md`.
16. `literature/UNRESTRICTED_AUDIT.md`.
17. `angles/conformal-l2/README.md`.
18. `angles/configuration-degeneration/README.md`.
19. `results/shrinking-square-action-injection.md`.
20. `angles/diagonal-microlocal/README.md`.
21. `results/null-spiral-conformal-concentration.md`.
22. `results/null-spiral-microlocal-eye.md`.
23. `angles/local-floer-engulfing/README.md`.
24. `results/envelope-cross-time-no-go.md`.
25. `angles/wild-configuration-degree/README.md`.
26. the latest `JOURNAL.md` section.

The newest wide-net session audited a July 2026 unrefereed proof of Tao's
four-curve alternating-area Conjecture 5.6. The public manuscript is false as
written because it defines
\(\mathcal A=-\int y\,dx\) but uses the opposite sign in the Liouville
normalization. Replacing the definition by Tao's
\(\mathcal A=+\int y\,dx\) repairs every downstream sign. The
square--conormal shear, exact essential-circle lemma, product cutoff,
conormal PSS theorem, and embedded polygonal limit then passed two
independent audits, including GPT-5.6 Sol at xhigh. Treat this only as an
apparently sound repaired argument, not as established literature.

The corrected result is a forcing module, not an unrestricted proof. Four
horizontal essential circles at heights
\((0,s,3s,2s)\) have zero alternating action and a clean circle of exact
joint squares. After exactness normalization this is precisely the zero
conormal over an affine diagonal, and its two Morse generators exhaust
\(H_*(S^1)\). As \(s\to0\) both generators totally collide; as
\(s\to\infty\) they escape physically while normalized action stays zero.
Thus rank two, absolute action, finite covers, balanced four-copy
perturbations, and naive detour essentialization do not select a planar
square. The surviving conormal target is a relative class outside a fixed
diagonal neighborhood, or a theorem making all artificial/mixed
intersections acyclic or pro-zero in a fixed spectral window.

The hoped-for generic GKS repair is also dead. The smooth exact-graph
telescope in `angles/gks-positive-telescope/README.md` uses invertible
compactly supported GKS stages, summable Hamiltonian amplitudes, and
canonical positive epigraph maps, yet has zero finite microlocal restrictions
and a rank-one restriction in the homotopy colimit. Only a theorem special
to the conjugated quarter-rotation and its four-sheet cap maps remains
plausible.

Two global topological refinements were computed exactly. Hugelmeyer's total
outer winding is the two-ended order defect \(n_- - n_+=1\); disjoint proper
cylinder arcs can realize it, so an end-order rigidity theorem in the full
admissible-square space is still missing. The resolved total-collision
boundary carries an integer, but the nonorientable cyclic configuration
quotient sees only its reduction modulo two. An explicit determinant
\(-8\) motif realizes one boundary unit, so ordinary integral, mod-four,
prime-end-location, and unfiltered-persistence repairs fail.

One sharply conditional conormal route survives. Select four retained
compact arcs \(\alpha_i\subset C\) with empty common intersection, splice
each to an essential cylinder circle, balance action only in artificial
chambers, and make the product transverse. The retained pieces must lie in a
lifted disk whose horizontal plus vertical diameter is smaller than the
cylinder period; this prevents a retained cylinder square from wrapping.
If exactly one ordered square uses any artificial piece, rank \(HF=2\)
forces a second all-retained square; the empty common intersection prevents
its limit from collapsing.
The two-zero graph construction in
`angles/conormal-tail-splicing/README.md` gives exactly two transverse
artificial generators and, after a generic offset choice, opens four splice
windows around one while keeping the other. The missing odd artificial
splice lemma must exclude every
connector, tail, and correction-ear square for all fifteen nonempty
artificial-incidence patterns. This is a finite interval-congruence target,
but it is unproved and must not be replaced by genericity.

The finite-\(p<2\) proof has now received an independent primary-source audit
and been packaged as `writeup/p-variation-note.md`. The audit verdict is
MERGE; the safe priority description is “an apparently unstated immediate
corollary/synthesis of Asano--Ike and Boedihardjo--Geng.”

The first \(p=2\) session proved a sharp embedded anomaly. For every positive-area
Jordan trace, inner and outer conformal level curves converge with the same
boundary parameter, but their limiting Liouville periods differ by exactly
the trace area. A scale-controlled positive-area \(1/2\)-Hölder
Hilbert--Osgood Jordan curve places this phenomenon inside finite
\(2\)-variation. GPT-5.6 Sol at xhigh returned MERGE after auditing the
recursive embedding and Hölder proof.

The next session proved a genuinely critical positive class:

> Every \(1/2\)-Hölder Jordan parametrization with finite
> Antonelli--Young dyadic quadratic-diameter sum satisfies Asano--Ike and
> therefore inscribes every prescribed rectangle.

The key observation is that Antonelli--Young define signed area by convergence
over all fine partitions. Two prefix partitions can be extended by the same
tail, which cancels and yields uniform convergence of the entire local
primitive. Boedihardjo--Geng supplies embedded polygons and a diagonal
\(C^1\) rounding preserves their primitives.

The strict spiral-comb witness uses
\(a_n=2^{-n-20}\), \(N_n\asymp4^n/n^2\), and
\(w_n=N_na_n^2\). It is Jordan, \(1/2\)-Hölder, and has
\(\sigma(c)<\infty\), but has infinite \(p\)-variation for every \(p<2\),
infinite length, and is not locally monotone. GPT-5.6 Sol at xhigh returned
MERGE after three local proof repairs.

The unrestricted session then proved that the approximation bridge itself is
not universal.  Asano--Ike Remark 5.5 already handles positive-measure
traces, so only null traces remain.  Nevertheless the interleaved spirals
\[
a(\theta)=\theta^{-1/2},\qquad
b(\theta)=\frac{a(\theta)+a(\theta+2\pi)}2
\]
close to a planar-null Jordan curve with finite enclosed area but
logarithmically divergent action along one smooth arm.

A local action-rigidity lemma shows that uniform convergence of
parameter-aligned \(C^1\) Jordan curves and their primitives forces the
limiting primitive to equal the classical integral on every regular smooth
subarc.  The logarithmic divergence therefore excludes **every** possible
Asano--Ike Theorem 1.1 approximation sequence for this curve.  GPT-5.6 Sol at
xhigh independently returned MERGE.  The example has infinite
\(2\)-variation, so the finite-\(2\) frontier remains separately open.

The actual unrestricted frontier is now exactly Asano--Ike Remark 4.2:

> For a null Jordan trace and \(\theta=\pi/2\), prove the diagonal
> \(\mu hom\)-cohomology vanishing at the critical value without constructing
> a single-valued continuous primitive.

The latest session proves a universal compactness theorem one topology below
that target.  For the analytic levels of the Riemann map of any bounded
Jordan domain, the mean-centered Liouville primitives converge strongly in
\(L^2(S^1)\).  Either this upgrades to uniform convergence, so Asano--Ike
applies, or order-one action concentrates at one prime end with winding
multiplicity \(\gtrsim\rho^{-2}\).

The concentration branch is genuinely realized by the null double spiral.
In logarithmic coordinates, cells between \(V\) and \(cV\) have fixed action,
area \(O(V^{-1})\), critical trace capacity \(O(V^{-2})\), and harmonic
measure \(\exp(-\Theta(V^2))\).  This rules out any repair based only on
conformal energy, \(L^p\) integrability, harmonic measure, or capacity.

The chord-level version of the remaining problem is false.  Fixed-vertex
Hamiltonian twists in four shrinking disks preserve an exact shrinking
square but change its action by an arbitrary four-point second difference.
Equivalently, two disjoint spiral fjords make the sum of the projected
capping windings carry order-one area on vanishing support.  Do not try to
bound individual collapsing actions or force square-symmetric cancellation.

The exact theorem to attack is **persistent diagonal locality**:
\[
R\Gamma\!\left(\rho^{-1}\Delta_0;
\mu hom(F_0,T_aQF_0)|_{\rho^{-1}\Delta_0}\right)=0
\quad(a\notin\pi\mathbb Z),
\]
where \(Q=(\phi\times\phi)^{-1}R_{\pi/2}(\phi\times\phi)\), assuming
\((C_0\times C_0)\cap Q(C_0\times C_0)=\Delta_0\).  At approximation level
this must pair arbitrary interior-action collapsing generators into
persistence bars whose lengths vanish **and** exclude their exact-action
endpoint microstalks.  The latter is strictly stronger than interleaving
convergence.

The null spiral now supplies the exact local model.  Every finite smooth
truncation has diagonal cohomology only at \(0\pmod\pi\), but the limit's
common phase winds through the entire action circle while its two sheets
have separation \(\pi/(2\theta)+O(\theta^{-2})\).  The decisive question is
the Milnor boundary term of the metric-completion telescope.  The earlier
collapsed-point toy was false: the actual space retains the action circle,
the \(!\)-versus-\(*\) cone has \(\tau_t=0\), and a common boundary stalk
does not create a translated morphism.  Every deep eye tail is arbitrarily
torsion, but a cap/continuation telescope could still leave a zero-lifetime
exact-action class.

An attractive cut-off attack is also fully audited and false as stated.
The conjugated Hamiltonian vanishes on the diagonal and can be cut off to
arbitrarily small Hofer norm without changing its shrinking germ.  However
\(\mathbb k_{[a,a+\varepsilon)}\to0\) while retaining a fixed endpoint
microstalk, and an action skyscraper has zero one-sided interleaving distance
but non-zero cohomology.  The missing theorem is no-ephemeral rigidity for
restricted diagonal \(\mu hom\), equivalently a pro-zero statement for the
derived cross-stage tower.  See `results/metric-germ-cutoff-no-go.md`.

Matschke supplies a second exact input: a square-free Jordan curve has a
special trapezoid at every parameter scale.  More strongly, one fixed-type
connected continuum spans every compact positive scale interval.  The
collision screens are classified in
`angles/configuration-degeneration/README.md`; all can occur locally at one
prime end, so any useful obstruction must be global along the continuum.

There is a new exact global invariant.  For a moving square with outer
vertices \(a,b\) and inner vertices \(a+J(b-a),b+J(b-a)\), the two closed
ribbon areas differ only by half the endpoint side-length squares.  A
compactified square envelope with simple nested ribbons is therefore
impossible.  Hugelmeyer supplies neither simple ribbons nor one-sided
winding bounds \(n_{\rm out}\geq1_\Omega\),
\(0\leq n_{\rm in}\leq1_\Omega\) with strict area deficit, and Matschke's
continuum need not contain a spanning path.
`angles/configuration-degeneration/square-envelope-area.md` gives the
identity and the exact missing topological lemma.

Do not retry two audited false shortcuts.  Conservative \(C^0\) smoothing
does not control action potentials: shrinking high-turn radial twists have
order-one action.  Greene--Lobb square-angle duality swaps spectral degrees
\(1\) and \(2\), while the triangle inequality applies only to degree \(2\);
it does not pin either action at half the enclosed area.  Arbitrarily small
Hofer cut-offs do not control endpoint microstalks.

Do not run numerical square searches. The rational harness is conjecture
hygiene only. Consult GPT-5.6 Sol at xhigh for any proposed microlocal
vanishing theorem. Preserve both claim boundaries: the general Square Peg
conjecture remains open, and failure of the primitive criterion does not
refute the weaker diagonal-cohomology criterion.

The newest session closes three additional formal shortcuts.

First, Oh's engulfable \(C^0\)-localization identifies the relevant
cotangent local/global complexes and fundamental-class invariant under a full
engulfable homotopy. It does not identify Asano--Ike's twisted
\(v\)-complex or compare the original rotation with the cutoff. Their
critical \(v\) microlocalizes to \(v\otimes1+1\otimes v\), which restricts
to zero on the clean diagonal over \(\mathbb F_2\). A formal two-parameter
\(\mathbb k[v]/(v^2)\)-module germ shows that zero endpoint \(v\)-action,
nonzero angle-continuation of \(wv\), and \(A\leftrightarrow\pi-A\) duality
are compatible; it is not a realization of the full \(R_\pi\) barcode or
GKS geometry.

Second, even fixing a bounded finite-stalk constructible first input does not
make microlocal Hom commute with the exact completeness telescope:
\[
F=\mathbb k_{(0,1)},\qquad G_n=\mathbb k_{(1/n,1)},\qquad
\operatorname{hocolim}G_n=F.
\]
Every finite restriction over \(T^*_0\mathbb R\) is zero, while
\(\mu hom(F,F)\) has a rank-one negative-conormal microstalk. The failure
already appears in the internal-Hom germ, and microlocal specialization also
contains an open-embedding \(Rj_*\). The next sheaf attack must find a
property special to completed GKS continuation maps which excludes this
translated-left-front model.

Third, Hugelmeyer's cross-time avoidance does not control winding. The
exact square path in `results/envelope-cross-time-no-go.md` is smooth,
strictly exterior/interior separated, and relation avoiding, but has
alternating signed lenses. Any envelope proof must use a genuinely global
two-ended consequence of total outer winding one.

Finally, local configuration degree can really escape. The note
`angles/wild-configuration-degree/README.md` constructs a regular square
zero with determinant \(-2\) which collapses into a locally square-free
\(1/4\)-Lipschitz Jordan germ while retaining an exact square screen and
fixed prime-end side. Exact square zeros escape only through the unique
cyclic orbit of total-collision vertices, and that orbit can absorb odd
local degree. A viable degree proof needs a nonlocal boundary correction.
