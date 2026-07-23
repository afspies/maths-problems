# Angle: prescribed-automorphism orbit matrices (shared machinery)

**Idea.** The published literature (Russian school, Mačaj–Širáň)
constrains automorphisms via character/orbit-matrix arguments but nobody
has ever published an exhaustive search under ANY prescribed
automorphism — the structural gap this campaign's SAT/CP infrastructure
targets. This folder holds the shared orbit-matrix machinery
(`orbit_matrix.py`) and its d=7 validation (`validate_d7.py`).

**Status: supporting machinery, validated at d=7.** Consumers:
`../c19-sat/`, `../c7-sat/`, and the planned C₁₃ fixed-point-free
formulation (250×250 orbit-matrix level — LEARNINGS queue item 4).

**Verdict.** No standalone claims; see the consuming angles.
