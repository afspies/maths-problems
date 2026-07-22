# Slice-ribbon and exotic S⁴ candidates

## Statement
Slice-ribbon conjecture (Fox, 1962): is every smoothly slice knot ribbon?
Adjacent and entangled: the smooth 4-dimensional Poincaré conjecture (SPC4) —
do exotic smooth structures on S⁴ exist? Standing candidate objects link the
two: Gompf–Scharlemann–Thompson (GST) family knots, Cappell–Shaneson spheres,
and Gluck twists on knotted 2-spheres.

## Why this fits us
The working unit is finite and checkable: **pick a specific candidate, compute
a specific invariant**. Piccirillo's Conway-knot theorem (2020) is the template
— one well-chosen knot trace, one Rasmussen-s computation, a decades-old
question dead. A single success in either direction here is a major theorem:
- A slice knot certified non-ribbon ⇒ slice-ribbon is false.
- A GST-type knot certified non-slice would kill the associated standardness
  route toward exotic S⁴ candidates; certified slice keeps it alive — map the
  exact logical state per candidate before computing anything.

## Certificates + verifiers (direction-dependent — be precise in every claim)
- **Sliceness (positive)**: an explicit slice disk / band-move movie / ribbon
  presentation — verifiable by Kirby-calculus bookkeeping (SnapPy, KLO, or
  band-word verification). A ribbon presentation certifies ribbonness too.
- **Non-sliceness**: a nonvanishing obstruction — Rasmussen s, Heegaard-Floer
  τ/ε/Υ, involutive correction terms, twisted Alexander / Casson–Gordon,
  metabelian ρ-invariants. Each is a finite computation with published
  software (knotjob, khoca, kht++, snappy, hf-hat family) — reproducible;
  record software versions and inputs with every claim.
- **Non-ribbonness of a slice knot** (the conjecture-killing direction): no
  general computable obstruction exists — current levers are fibered-knot
  criteria, representation-counting obstructions on branched double covers,
  and exhaustive ribbon-move search failures (evidence, NOT proof). Be
  scrupulously honest about which lever proves what; any claimed new
  obstruction gets adversarial review (Codex xhigh) before use.
- **Exotic S⁴ side**: standardization of a candidate (via Kirby moves) is
  fully rigorous; *distinguishing* would need invariants beyond current
  technology — flag ideas for expert review before investing compute.

## First steps
1. Literature map with citations: status of each GST knot (slice? open?),
   Cappell–Shaneson standardizations (Akbulut, Gompf), Gluck-twist results,
   and an obstruction-toolkit matrix: invariant × software × feasible knot
   size (crossing number limits per tool).
2. Build the harness: one interface wrapping the invariant calculators with
   reproducible outputs; validate on knots with known answers (Conway knot
   and its Piccirillo companion; standard slice and ribbon examples).
3. Assemble the candidate ledger: slice-suspect and ribbon-suspect knots from
   the literature + GST members, prioritized by smallness and obstruction
   coverage gaps. Run full obstruction batteries; every completed battery is
   a citable data point in results/ regardless of outcome.

## Angle-of-attack menu
- Per-candidate obstruction batteries (bread and butter).
- Trace/satellite tricks à la Piccirillo: find sibling knots sharing a trace
  where an invariant computes on one sibling and transfers to the other.
- Representation-counting ribbon obstructions on double branched covers
  (finite-group representation counts are exact and automatable).
- Automated ribbon-move / band-presentation search to certify ribbonness of
  suspects — killing candidates cleanly is progress too.
