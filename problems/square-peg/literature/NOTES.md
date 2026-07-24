# Literature audit through 2026-07-24

## Status boundary

The unrestricted Square Peg conjecture remains open: a general Jordan curve is
not yet known to inscribe a nondegenerate square.  The regularity boundary
changed materially after the older surveys:

- Greene--Lobb prove the prescribed-rectangle theorem for smooth curves and
  develop Jordan Floer homology and action spectral invariants.  Their
  shrink-out paper gives only an interval of aspect angles for a rectifiable
  curve, with the square following under an area/diameter inequality
  [GL-floer].
- Their graph paper, now published online in 2026, proves a square for a union
  of two graphs of Lipschitz constant below \(1+\sqrt2\), and every rectangle
  at Lipschitz constant at most \(1\) [GL-graphs].
- Asano--Ike v3 remove the area/diameter condition: every rectifiable Jordan
  curve and every locally monotone Jordan curve inscribes every prescribed
  rectangle [AI].  Rectifiable curves therefore are **not open territory**.

The official arXiv record labels Asano--Ike v3 as submitted 2026-01-05 and the
downloadable v3 PDF is headed 2026-01-06.  A secondary experimental HTML
rendering retrieved during this audit displayed 2026-03-22, matching the date
reported in the campaign prompt, but that date is not on the official v3
record.  The mathematical audit below uses the downloadable v3 PDF.

## Asano--Ike Theorem 1.1, with quantifiers

Identify \(\mathbb R^2\) with \(T^*\mathbb R\), and let \(\lambda\) be the
Liouville form (the paper uses \(\lambda=\xi\,dx\); reversing the contact sign
only reverses all primitives).  Let
\(e:\mathbb R\to\mathbb R/2\pi\mathbb Z\simeq S^1\) be the quotient.

For a *parametrized* Jordan curve \(c:S^1\to\mathbb R^2\), Theorem 1.1 assumes
there are smooth Jordan embeddings \(c_n:S^1\to\mathbb R^2\) such that:

1. \(c_n\to c\) uniformly as maps on this same parameter circle; and
2. after choosing primitives
   \(df_n=(c_n\circ e)^*\lambda\), the functions \(f_n:\mathbb R\to\mathbb R\)
   converge locally uniformly to a continuous \(f\).

The additive constants are not specified in the theorem.  Equivalently one may
normalize all \(f_n(0)=0\).  Since the pullbacks are \(2\pi\)-periodic,
\[
 f_n(t+2\pi)=f_n(t)+\int_0^{2\pi}(c_n\circ e)^*\lambda.
\]
Thus uniform convergence on one period plus convergence of the period
integrals is exactly local-uniform convergence on \(\mathbb R\).  The
parametrizations are not disposable: unparametrized Hausdorff convergence is
not the stated hypothesis.  Remark 5.6 allows \(C^1\), rather than smooth,
Jordan approximants.

No area-\(\pi\) normalization appears in the statement.  In the proof the
limit curve is first scaled to enclose area \(\pi\); the approximants are then
scaled by factors tending to \(1\).  The limiting primitive forces the conic
microsupport of the limiting sheaf quantization to have no nonintegral
\(\pi\)-translate self-intersections.  Theorem 4.1 converts that disjointness
into a non-diagonal intersection with the rotated torus, hence a
\(\theta\)-rectangle.  The ingredients actually used after Theorem 1.1 are:

- completeness and microsupport semicontinuity for the Tamarkin interleaving
  metric;
- a compactly supported area-preserving/Hamiltonian homeomorphism taking the
  standard circle to the measure-zero Jordan curve;
- the critical value \(a(\theta,C)\in(0,\pi)\) in the persistence object; and
- the fact that diagonal intersections can occur only at action shifts in
  \(\pi\mathbb Z\).

For positive-area Jordan images the paper gives a separate density argument.

### Where rectifiability enters

Proposition 5.8 (Corollary 5.9 in v3) takes a Riemann map
\(\varphi:\mathbb D\to D\), extends it to the closed disk by Carathéodory, and
uses the inner level curves
\(c_n=\varphi|_{\partial\mathbb D_{1-1/n}}\).  They are smooth Jordan curves.
Riesz--Privalov supplies convergence of their lengths to the boundary length;
the rectifiable Green-theorem lemmas then give convergence of the primitives.
Rectifiability enters at precisely this length/Green-theorem step, not in the
sheaf criterion itself.

## Greene--Lobb shrink-out and its relation to Asano--Ike

For a smooth/analytic curve \(\gamma\),
\[
 L_0=\gamma\times\gamma,\qquad L_1=R_\theta(L_0)\subset\mathbb C^2.
\]
Off the clean diagonal \(\Delta(\gamma)\), intersections correspond to
nondegenerate \(\theta\)-rectangles.  Greene--Lobb build a two-dimensional
Jordan Floer homology using strips that avoid the diagonal divisor.  The
top-class spectral invariant \(\ell(\gamma,\theta)\) is an action value,
monotone in \(\theta\), tends from \(0\) to the enclosed area as
\(\theta:0\to\pi\), and has derivative bounded above by
\(\operatorname{Rad}(\gamma)^2\).  The resulting action window selects
rectangles whose action cannot shrink to zero.  For rectifiable limits, a
uniform length bound converts this action lower bound into geometric
nondegeneracy.

The sheaf proof retains the same Lagrangian rotation and action filtration, but
packages them as \(F_C\), \(R_\theta F_C\), and a persistence object in the
Tamarkin category.  Primitive convergence rules out unwanted action
translations on the diagonal; a critical value strictly between \(0\) and
\(\pi\) must therefore be realized off the diagonal.  For the present bridge,
the Floer construction need not be reproved: after verifying the hypotheses of
Asano--Ike Theorem 1.1, their sheaf-theoretic implication can be cited.

## Rough/Young approximation already in the literature

Boedihardjo--Geng prove two facts that are decisive here [BG]:

1. every parametrized Jordan curve admits arbitrarily fine polygonal
   interpolants that are themselves Jordan; prescribed parameter times may be
   included; and
2. if the original path has finite \(p\)-variation, its polygonal
   interpolants converge to it in \(q\)-variation for every \(q>p\).

They use these facts to prove Green's theorem for finite-\(p\)-variation Jordan
curves when \(p<2\).  This is much stronger than merely knowing that some
unparametrized polygon lies nearby, and it is exactly what prevents the
embedded-approximation step below from being a hidden assumption.

Targeted searches for combinations of “2412.21057”, “finite p-variation”,
“Young integral”, “rough path”, and “rectangular/square peg” found no paper
through 2026-07-24 stating the corollary proved in the accompanying
`angles/p-variation/README.md`.  This is a novelty check, not a proof of
priority: the result is a short synthesis of published theorems and may be
regarded by experts as an immediate corollary once pointed out.

## July 2026 addendum

### Greene--Lobb, arXiv:2604.17116

Greene--Lobb prove that every Jordan curve inscribes rectangles for a set of
diagonal angles of measure at least \(A/R^2\), where \(A\) is enclosed area
and \(R\) is half the diameter. This is a major arbitrary-Jordan result but
does not guarantee any prescribed angle, including \(\pi/2\). It therefore
neither subsumes the finite-\(p<2\) prescribed-rectangle consequence nor
solves the Square Peg conjecture.

### Antonelli--Young, arXiv:2605.15987

Antonelli--Young define signed area for critical \(1/2\)-Hölder curves
through polygonal approximations and prove geometric convergence criteria
using beta-number control. Their work confirms that the \(p=2\) area problem
requires geometry beyond a bare Hölder or variation bound. It is the first
published input to test for any positive theorem on the remaining zero-area,
local-primitive frontier.
