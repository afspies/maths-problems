# Incidence and affine-dependence bounds

**Status:** promising; exact necessary inequalities proved, not a full
classification.

For a realized 4-polytope \(P\), let \(V=f_0(P)\), \(F=f_3(P)\), and
\(I=f_{03}(P)\). For each facet \(G\), write \(m_G\) for its number of
vertices. Let \(E_G\) be the \(m_G\times5\) matrix with rows \((1,x_v)\).
Because \(G\) is three-dimensional, \(\operatorname{rank}E_G=4\).

The intrinsic, incidence-indexed description of the speed space is
\[
 A_\theta(P)=\left\{\alpha\in\mathbb R^V:
 \lambda^\mathsf T\alpha|_G=0
 \text{ for every }G\not\parallel\theta
 \text{ and }\lambda\in\ker E_G^\mathsf T\right\}.
\]
Equivalently it is the kernel of the direct sum of restriction maps to
\(\mathbb R^{m_G}/\operatorname{im}E_G\). This makes the distinction precise:
incidence gives the block support, while the affine matroid of the realization
gives the coefficients.

Choose \(\theta\) parallel to a facet \(G_0\) having
\(\Delta=\max_G m_G\) vertices. Rank subadditivity gives
\[
\dim A_\theta(P)
\ge V-\sum_{G\not\parallel\theta}(m_G-4)
\ge V-I+4F+\Delta-4.
\]
If \(P\) is terminal, \(\dim A_\theta(P)=5\), hence
\[
\Delta\le I-V-4F+9. \tag{1}
\]
Applying the same argument to a terminal combinatorial dual gives, with
\(\delta\) the maximum number of facets at a vertex,
\[
\delta\le I-F-4V+9. \tag{2}
\]
Since \(\Delta,\delta\ge4\), every pair-terminal 4-polytope satisfies the
campaign-derived necessary inequality
\[
2f_{03}\ge5(f_0+f_3)-10. \tag{3}
\]

The relevant four-dimensional flag/Dehn--Sommerville calculation is
\[
f_{03}-f_{02}+2f_2=2f_3,\qquad
f_{03}=f_{02}-2f_1+2f_0. \tag{4}
\]
Indeed, sum Euler's relation over all 3-facets. Each 2-face lies in two
facets, every 2-face is a polygon, and the link of an edge is a polygon, so
\(f_{23}=2f_2\) and \(f_{13}=f_{12}=f_{02}\). The second identity follows
from \(f_0-f_1+f_2-f_3=0\).

## Infinite subclasses

If \(P\) is simplicial, every facet has exactly four vertices and imposes no
admissibility equation. Thus \(A_\theta(P)=\mathbb R^{f_0}\) for every
direction. Terminality forces \(f_0=5\), so \(P\) is a 4-simplex.

If \(P\) is simple and both \(P\) and a combinatorial dual are terminal, the
dual is simplicial and the same argument forces both to be simplices. Hence a
non-simplex Mahler minimizer can be neither simple nor simplicial.

The 4-cube is a useful warning: the exact harness gives speed dimension five
in a generic direction but a larger space in facet-parallel directions.
Generic-direction rigidity is therefore much weaker than terminality.
