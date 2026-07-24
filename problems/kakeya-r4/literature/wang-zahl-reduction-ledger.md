# R³ full-to-sticky reduction and its R⁴ failure points

Primary sources: Wang–Zahl, arXiv:2502.17655; Guth,
arXiv:2508.05475; Zahl, arXiv:2512.09397.

## R³ logical skeleton

1. For a finite family of convex sets `W` and a convex test set `K`, define

   `Delta(W,K)=sum_{W subset K}|W|/|K|`

   and `Delta_max(W)=sup_K Delta(W,K)`.

2. The R³ union theorem says that essentially distinct
   `delta×delta×1` tubes with `Delta_max≲delta^(-o(1))` and dense shadings
   have union comparable, up to subpolynomial losses, to total tube mass.
   Direction-separated tubes satisfy the convex nonconcentration hypothesis,
   so this implies the set-dimension Kakeya theorem.

3. Uniformize the tube family at a finite geometric list of scales. A family
   is sticky when every coarse rho-tube contains, up to subpolynomial losses,
   `(rho/delta)²` fine tubes.

4. Express small union volume as large average multiplicity. Introduce:

   - `K_KT(beta)`: Katz–Tao/convex-nonconcentrated families have
     multiplicity at most `#T^beta`;
   - `K_F(beta)`: convex-Frostman families have the corresponding
     scale-normalized multiplicity bound.

5. Greedy maximal-density factoring decomposes a large subfamily into pieces
   inside near-maximizing convex sets `W`. The pieces are Frostman in `W`;
   the collection of factors is Katz–Tao. This converts a multiplicity
   problem into an inner problem and an outer problem.

6. Rectangularize convex factors in R³ as planks. Slab `L²` incidence bounds,
   affine rescaling of planks to tubes, and product bounds for multiplicity
   let the induction pass between Katz–Tao and Frostman regimes.

7. A stopping-time decomposition follows intermediate scales:

   - if all relevant scales are near-Frostman, a large sticky subfamily is
     located and the R³ sticky theorem gives an essentially sharp union;
   - if some scale is quantitatively nonsticky, maximal factoring produces
     either an eccentric plank (giving a power gain) or a small factor
     (allowing induction/rescaling).

8. The two bootstraps are:

   `K_KT(beta) => K_F(beta)`,

   and

   `K_KT(beta) + K_F(beta) => K_KT(beta-nu(beta))`.

   Starting from the trivial `beta=1` and iterating gives every `beta>0`,
   hence the R³ union theorem and full Hausdorff/Minkowski dimension three.

## What fails in R⁴

### Failure 1: the direct union theorem is false

Guth explicitly names the split quadric

`x1²+x2²-x3²-x4²=1`

as a low-degree ruled obstruction. Zahl's survey gives the sharpened
Convex-Wolff model: the raw three-parameter line family on the quadric must
first be thinned, then many translated/rotated copies are combined. The
result still obeys the R⁴ convex nonconcentration axiom but has union volume
far below total tube mass. Therefore convex tests do not detect all relevant
R⁴ concentration.

### Failure 2: factor geometry is no longer plank geometry

The abstract greedy factoring lemma works for any chosen class of measurable
sets. But the subsequent R³ geometry uses much more than the greedy lemma:
convex factors are approximated by rectangular planks, have controlled
sections, and behave well under affine normalization. A curved ruled
3-fold has tangent directions varying with position and may support many
lines; it cannot be replaced by one plank without losing a power.

### Failure 3: the inner/outer multiplicity theorem is missing

Even if factors are chosen from bounded-complexity semialgebraic grains, no
analogue is known of the slab/plank incidence package that bounds both the
family inside a grain and the family of grains. “Use semialgebraic sets in
the greedy lemma” therefore does not prove a union theorem.

### Failure 4: full sticky input is unavailable in R⁴

The R³ bootstrap terminates at a full-dimensional sticky theorem. In R⁴ the
verified sticky input is only `13/4`. Even a perfect semialgebraic
factorization would not by itself close the full conjecture.

### Failure 5: class closure and entropy

A workable grain class must remain bounded-complexity after affine
rescaling, thickening, intersection, and pigeonholing. It also needs a
finite-resolution parameter net with only subpolynomial selection loss.
Degree alone does not supply these quantitative properties.

## Consequence for bridge B

The weakest credible first target is not “the greedy lemma for
semialgebraic sets” (already formal). It is a degree-2 inner/outer
multiplicity or union estimate that:

- detects the thinned/copied split-quadric construction;
- is stable under the affine rescalings used by the bootstrap;
- gives a power saving unless the factors carry coherent ruling data;
- passes that ruling data to a lower-complexity or sticky subproblem.

No such estimate is proved in the audited sources.
