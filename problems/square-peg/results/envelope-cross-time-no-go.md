# Cross-time avoidance does not control square-envelope winding

## Purpose

The square-envelope area identity would prove Square Peg if Hugelmeyer's
envelope had one-sided outer and inner winding.  This note shows that neither
the regular-level construction nor its full cross-time relation avoidance
implies such a sign condition.

## The deleted-product level set allows arbitrary winding

Write the deleted-product cylinder as
\[
 C=S^1\times(0,1),\qquad
 (x,\delta)\longleftrightarrow(x,x+\delta).
\]
For an integer \(N\geq1\), define
\[
 r_N(x,\delta)=\exp(2\pi i(x-N\delta)).
\]
It has degree one on the cylinder core, \(1\) is a regular value, and
\[
 r_N^{-1}(1)
 =\{(N\delta,(N+1)\delta):0<\delta<1\}
\]
where the first two coordinates are read modulo \(1\). It is one proper
embedded component joining the two cylinder ends. Its two
coordinate strands wind \(N\) and \(N+1\) times.  Replacing \(N\delta\) by
\(1/\delta\) gives a proper regular component with infinite winding and no
endpoint limit as \(\delta\to0\).

Thus degree one and proper embeddedness of the ordered-pair path do not
bound either coordinate strand.  Any stronger conclusion must use geometry
specific to Hugelmeyer's test map.

## A square-coupled separated countermodel

Put
\[
 L=\log2,\qquad \kappa=\pi/L,\qquad \varepsilon=1/20,
\]
and
\[
 z(t)=\exp\!\left(-t+i\varepsilon\sin(\kappa t)\right),
 \qquad t\geq0.
\]
Consider the moving square in envelope order (its perimeter order is
\(a,b,d,c\)):
\[
 (a,b,c,d)
 =\bigl(z,\,2z,\,(1+i)z,\,(2+i)z\bigr).                 \tag{1}
\]
This is a smooth injective proper path in the punctured square-configuration
space and its side length tends to zero.

It satisfies the full outer--inner cross-time avoidance.  An equality
\[
 O\,z(s)=I\,z(t),\qquad
 O\in\{1,2\},\quad I\in\{1+i,2+i\},
\]
would imply, modulo \(2\pi\),
\[
 \arg(I/O)
 =\varepsilon(\sin\kappa s-\sin\kappa t).
\]
The right side lies in \([-0.1,0.1]\), while the left side is either
\(\arctan(1/2)\) or \(\pi/4\), both greater than \(0.4\).  Hence no such
collision occurs.

The separation can be realized by a single Jordan domain.  Let
\[
 \Omega=\operatorname{conv}
 \{0,10e^{i/5},10e^{6i/5}\}.
\]
The arguments of \(a,b\) lie in \([-0.05,0.05]\), outside the angular
sector of \(\Omega\), while those of \(c,d\) lie strictly between \(0.2\)
and \(1.2\).  Their radii are small enough that \(c,d\in\Omega\).
Thus (1) is a genuine exterior/interior separated shrinking half-envelope.

## Alternating winding lenses

At the exact times \(nL\),
\[
 a(nL)=b((n+1)L)=2^{-n}.
\]
The \(a\)-arc on \([nL,(n+1)L]\) and the \(b\)-arc on
\([(n+1)L,(n+2)L]\) are polar graphs symmetric across the positive real
axis.  They form a simple lens in the annulus
\[
 2^{-(n+1)}\leq |z|\leq2^{-n}.
\]
The sign of the angular oscillation reverses at every half-period, so the
lens has index \(+1\) for even \(n\) and \(-1\) for odd \(n\).
Different lenses lie in disjoint annuli. For any internal lens whose annulus
misses the two end connectors, closing a synchronized finite ribbon gives
winding exactly \((-1)^n\) on that lens.

Consequently a smooth, finite-length, square-coupled, separated path with
full cross-time avoidance can have infinitely many negative winding
regions.

## Relation to Hugelmeyer's theorem

Hugelmeyer's regular-value component supplies a proper embedded path of
ordered pairs, a fixed test-map cone, outer/inner separation, and a total
outer winding.  Cross-time avoidance says that an outer vertex at one time
does not equal an inner vertex at another; once exterior/interior separation
is known, this adds no further geometric restriction.

Moreover, the relation-avoiding origin path used later in the paper obtains
a common endpoint limit from the finite-singularity hypothesis.  That step
is unavailable for an arbitrary Jordan curve.  Even granting the endpoint
limit does not repair the winding problem, as (1) shows.

## Verdict

The implication
\[
\text{proper deleted-product path + cross-time avoidance}
\Longrightarrow
\text{one-sided square-envelope winding}
\]
is false.  The square-envelope area route now requires a genuinely global
theorem coupling Hugelmeyer's total winding-one condition at both ends to
the entire small-scale tail.  No local relation-avoidance or regular-level
argument can provide it.
