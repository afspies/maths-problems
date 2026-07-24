# An explicit nonrectifiable, non-locally-monotone family

Fix \(d\in(1,2)\) and an angle \(\delta\in(0,2\pi)\).  For
\(\theta\in[1,\infty)\), set
\[
 \gamma_0(\theta)=\theta^{-1/d}e^{i\theta},\qquad
 \gamma_1(\theta)=e^{i\delta}\gamma_0(\theta).
\]
Traverse \(\gamma_0\) from the origin out to \(e^{i}\), join \(e^i\) to
\(e^{i(1+\delta)}\) along the circular arc
\[
                 \{e^{i(1+s)}:0\le s\le\delta\},
\]
and traverse \(\gamma_1\) back to the origin.  Call the resulting closed curve
\(C_{d,\delta}\).

## Embedding

Each spiral has strictly monotone radius.  Two points on one spiral with the
same radius have the same \(\theta\), hence are equal.  Points on the two
spirals with the same radius differ by the fixed angle \(\delta\), so the
spirals are disjoint away from the common limiting point \(0\).  The joining
unit-circle arc meets them only at its endpoints.  Parametrize either tail by
\(\theta=1/t\) and set its value at \(t=0\) to \(0\); this explicitly
compactifies the two infinite tails.  The resulting map is continuous and
injective on the parameter circle: \(C_{d,\delta}\) is Jordan.

## Infinite length

On the \(n\)-th full turn,
\[
 |\gamma_0'(\theta)|
 =\sqrt{\theta^{-2/d}+d^{-2}\theta^{-2/d-2}}
 \ge \theta^{-1/d}.
\]
The total length dominates a constant multiple of
\(\sum_n n^{-1/d}\), which diverges because \(d>1\).  Both spiral arms, and
hence the Jordan curve, are nonrectifiable.

## Finite \(p\)-variation for every \(p>d\)

Break a spiral into full-turn blocks
\(I_n=[2\pi n,2\pi(n+1)]\).  Its length \(L_n\) on \(I_n\) is
\(O(n^{-1/d})\).  Given an arbitrary partition, separate its increments into
those contained in one block and those crossing at least one block boundary.
Within \(I_n\), the sum of \(p\)-th powers is at most
\(L_n^p=O(n^{-p/d})\).  Assign a crossing increment to its starting block.
These starting blocks are distinct, and monotonicity of the radii bounds the
increment by \(O(n^{-1/d})\).  Thus
\[
 \sum |\Delta\gamma_0|^p
 \le C_p\sum_{n\ge1}n^{-p/d}<\infty
\]
when \(p>d\).  The finite joining arc does not affect finiteness.  Since
\(d<2\), choose any \(p\in(d,2)\); the finite-\(p\)-variation theorem applies.

## Not locally monotone

At the origin, the projection of either spiral onto any unit vector of angle
\(\phi\) is
\[
       \theta^{-1/d}\cos(\theta-\phi).
\]
It changes sign infinitely often on every tail, so it is not strictly
monotone on any one-sided neighborhood of the origin: a strictly monotone
function tending to \(0\) at an endpoint must have one fixed sign sufficiently
near that endpoint.  Hence the closed curve is not locally monotone in
Stromquist's sense.

## Peg consequence

This family is neither rectifiable nor locally monotone, so it is not covered
by the two named corollaries in Asano--Ike.  By the finite-\(p\)-variation
bridge, every \(C_{d,\delta}\) inscribes a \(\theta\)-rectangle for every
\(\theta\in(0,\pi)\), including a square.
