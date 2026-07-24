# Priority audit: finite-\(p\)-variation rectangular pegs

**Audit date:** 2026-07-24  
**Claim audited:** if a Jordan parametrization
\(c:S^1\to\mathbb R^2\) has finite \(p\)-variation for some \(p<2\), then
it satisfies Asano--Ike's primitive-approximation criterion and hence
inscribes every prescribed rectangle.

## Verdict

**No explicit prior statement was found.  The result should nevertheless be
presented as an unstated, nearly immediate corollary/synthesis of
Asano--Ike and Boedihardjo--Geng, not as a new rough-integration theorem.**

The division of credit is unusually clean:

- Asano--Ike [AI] prove that their parametrized smooth-approximation and
  Liouville-primitive convergence condition implies every prescribed
  rectangular peg.
- Boedihardjo--Geng [BG] already prove the two hard approximation facts for a
  finite-\(p\)-variation Jordan path: embedded polygonal interpolation and
  convergence of those interpolants in every \(q\)-variation topology with
  \(q>p\).  Their paper also states the Young estimate needed to pass the
  Liouville primitives to the limit, and uses the same ingredients to prove
  Green's theorem.
- What remains is to put the two papers together and, if one applies
  Asano--Ike Theorem 1.1 literally, round the finitely many polygonal corners
  without losing embeddedness, the original parameter, or variation control.
  Alternatively, Asano--Ike's closure observation in Section 5 can be applied
  to the rectifiable Jordan polygons, making even this rounding step
  unnecessary once the identification of their primitives is written down.

Thus the *peg consequence* appears not to have been written before, and it
does add a geometrically strict nonrectifiable class.  But the analytic
mechanism is already present in [BG], while the peg implication is exactly
[AI].  In priority language this is strongest as a useful new observation,
not as a new theory or a technically independent theorem.

This audit cannot prove priority against unpublished manuscripts,
unindexed notes, talks, or private correspondence.  The negative conclusion
below means only that no statement was located in the searched primary
literature and citation trail through 2026-07-24.

## Why the implication is so close to being explicit

Fix \(p<q<2\).  Boedihardjo--Geng provide Jordan polygonal interpolants
\(a_n=c^{P_n}\) with mesh tending to zero and
\[
             \|a_n-c\|_{q\text{-var}}\longrightarrow 0.
\]
For \(a_n=(x_n,y_n)\), \(c=(x,y)\), the standard Young--Loeve estimate gives,
uniformly in the upper integration endpoint,
\[
\int y_n\,dx_n\longrightarrow\int y\,dx.
\]
The period integrals converge as well, so normalization at one basepoint
upgrades uniform convergence on a period to locally uniform convergence of
the quasiperiodic primitives on \(\mathbb R\).  These are the hypotheses in
Asano--Ike Theorem 1.1.

None of those analytic assertions is new:

- Young [Young] is the original integration result.
- [BG, Theorem 2.2] supplies the embedded, parameter-respecting polygonal
  interpolants.
- [BG, Lemma 3.1 and Theorem 3.1] supply variation convergence and the
  quantitative continuity of the indefinite Young integral.
- [BG, Theorem 3.2] already applies that package to the area form on a
  finite-\(p\)-variation Jordan curve.

The repository proof is still worth spelling out because two details are
easy to suppress incorrectly: unparametrized Hausdorff approximation does
not meet [AI], and arbitrary convolution does not preserve a Jordan
embedding.  Those are proof-hygiene contributions, not evidence of broad
conceptual priority.

## Peg-problem literature checked

### Asano--Ike and its 2026 citation trail

The official arXiv record for [AI] has v3 submitted 2026-01-05.  The paper
states the primitive criterion and names two consequences: every rectifiable
Jordan curve and every locally monotone Jordan curve inscribes every
prescribed rectangle.  Searches of the full text found no occurrence of
“\(p\)-variation”, “Young”, “Hölder”, or “Boedihardjo”.  Consequently the
finite-\(p\)-variation corollary is not explicit there.

The two relevant later 2026 preprints found in the citation trail were also
checked:

- Greene--Lobb [GL-positive] prove that an arbitrary Jordan curve inscribes a
  positive-measure set of rectangle angles.  They cite [AI] for the
  rectifiable prescribed-rectangle theorem.  Their result does not guarantee
  any fixed angle, so it neither yields the square nor the audited theorem.
- Barber [Barber] cites [AI] as covering rectifiable and locally monotone
  curves and develops spectral invariants for isosceles trapezoids.  It does
  not state a finite-variation or Young-integral rectangle result.

This citation-trail evidence is useful but not decisive: neither paper was
trying to enumerate every immediate regularity corollary of [AI].

### Other regularity results

- Greene--Lobb's smooth theorem [GL-smooth] and Gao's generic multiplicity
  theorem [Gao] concern smooth Jordan curves.
- Greene--Lobb's Jordan Floer paper [GL-floer] gives an interval of rectangle
  angles for rectifiable curves, with an area/diameter condition for the
  square.  It does not cover the full finite-\(p\)-variation class.
- Greene--Lobb's graph theorem [GL-graphs] gives every rectangle for the
  union-of-two-graphs class at Lipschitz constant at most \(1\), and a square
  under a larger Lipschitz bound.  These graph curves are rectifiable.
- Tao [Tao] proves a square for a union of two graphs with Lipschitz constant
  strictly below \(1\); this is a graph-specific bounded-variation argument,
  not a finite-\(p\)-variation or every-rectangle theorem.
- Chambers [Chambers] proves a square for curves quantitatively close to a
  \(C^2\) curve.  This can overlap nonrectifiable finite-\(p\)-variation
  examples but neither contains that class nor gives every prescribed
  rectangle.
- Stromquist [Stromquist] proves the square for locally monotone curves;
  [AI] upgrades this to every rectangle.
- Matschke's survey [Matschke] predates both [AI] and the recent Floer
  results.  It contains no finite-\(p\)-variation peg theorem.

Accordingly, no earlier peg theorem found in this audit subsumes the audited
claim.  The overlap with [AI]'s named corollaries is substantial but not
total: \(p=1\) is precisely the rectifiable case, while finite
\(p\)-variation for \(1<p<2\) includes infinite-length curves that need not
be locally monotone.  The double-spiral family proved in
`../results/spiral-family.md` is an explicit strict witness.

There is also no accidental inclusion in [AI]'s positive-area-boundary
discussion: a finite-\(p\)-variation path with \(p<2\) has image of Hausdorff
dimension at most \(p<2\), hence planar measure zero.

## Young, rough-path, and Jordan-approximation literature checked

The most relevant primary source is [BG], not a general rough-path textbook.
Its abstract already advertises generalized Green's theorem and uniqueness
of signature for planar Jordan curves of finite \(p\)-variation,
\(1\leq p<2\).  Its proof contains exactly the embedded-interpolation and
Young-continuity package needed here.  This makes a claim that the present
work introduces a new approximation-stable area theory untenable.

Yam's thesis [Yam] had earlier proved rough Green-type results for boundaries
of certain Hölder domains.  [BG] explicitly describes its own theorem as a
partial generalization of that work.  Neither source connects the rough area
primitive to an inscription theorem.

Searches were also made for combinations of:

- “square peg”, “rectangular peg”, and “inscribed rectangle” with
  “finite \(p\)-variation”, “bounded variation”, “Young integral”,
  “rough path”, “Hölder Jordan curve”, and “fractal Jordan curve”;
- the identifiers/title of [AI] with “\(p\)-variation”, “Young”, and
  “Boedihardjo--Geng”;
- post-[AI] arXiv papers citing or discussing its prescribed-rectangle
  theorem.

The searches returned [AI], [BG], the known smooth/rectifiable/graph results,
and unrelated uses of variation, but no explicit version of the audited
corollary.

## Classification of the claim

### Explicit prior theorem

**Not found.**  No checked source states that all finite-\(p\)-variation
Jordan curves with \(p<2\) inscribe every prescribed rectangle, or explicitly
asserts that this class satisfies [AI]'s primitive criterion.

### Immediate but unstated corollary

**Yes, with high confidence.**  To an expert simultaneously familiar with
[AI] and [BG], the proof is short:

1. choose \(p<q<2\);
2. use [BG] for parameter-aligned Jordan polygons converging in
   \(q\)-variation;
3. use Young continuity for the normalized Liouville primitives; and
4. invoke [AI].

The only implementation choice is whether to use [AI]'s Section 5 closure
observation on the rectifiable polygons or to round their corners and apply
Theorem 1.1 directly.

### Genuinely new synthesis

**Yes in the limited sense of connecting two previously separate papers.**
The synthesis exposes a natural regularity threshold, covers strict
nonrectifiable examples, and points toward the \(p=2\) area-lift obstruction.
What is *not* supported is a claim of a new Young estimate, a new Jordan
approximation theorem, or new sheaf/Floer machinery.

## Recommended public priority claim

Use:

> We record an apparently unstated consequence of Asano--Ike's
> approximation criterion and Boedihardjo--Geng's embedded polygonal
> approximation theorem: every Jordan curve admitting a finite
> \(p\)-variation parametrization for some \(p<2\) inscribes every prescribed
> rectangle.  The proof is a short Young-integration argument.  We do not
> know whether this consequence has previously been observed.

For an abstract, “We observe” or “We deduce” is preferable to “We prove a new
theorem”.  It is fair to emphasize the strict consequence:

> This includes infinite-length Jordan curves outside the rectifiable and
> locally monotone classes named in Asano--Ike.

Do **not** use “first”, “new rough-path method”, “new area theory”, or “largest
known class” without confirmation from the authors and a broader
bibliographic review by a domain expert.

## Draft author inquiry

Subject: finite-\(p\)-variation corollary of the rectangular-peg criterion

> Dear Professors Asano, Ike, Boedihardjo, and Geng,
>
> We noticed that Asano--Ike Theorem 1.1 appears to combine with the embedded
> polygonal approximation and \(q\)-variation convergence in
> Boedihardjo--Geng to give the following short corollary: every Jordan
> parametrization of finite \(p\)-variation, \(p<2\), satisfies the
> primitive-convergence criterion and therefore inscribes every prescribed
> rectangle.  Young continuity gives locally uniform convergence of the
> normalized Liouville primitives; one can either round the Jordan polygons
> with variation-small corner modifications or use the Section 5 closure
> observation.
>
> We have not found this consequence stated in the literature and intend to
> describe it explicitly as an observation/corollary of your results.  Are
> you aware of an earlier source, or of any issue with this deduction or
> attribution?
>
> Best wishes,

