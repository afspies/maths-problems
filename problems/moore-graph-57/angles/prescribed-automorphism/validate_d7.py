"""End-to-end validation of the prescribed-automorphism pipeline at d=7:
prescribe a fixed-point-free order-5 automorphism of a putative Moore graph
of degree 7 (n=50, 10 orbits of 5); search orbit matrices; lift via SAT;
verify the result is a genuine Moore graph (necessarily Hoffman-Singleton).
"""

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "harness"))
from verify import verify_moore, spectral_sanity  # noqa: E402
from orbit_matrix import search_orbit_matrices, lift_orbit_matrix  # noqa: E402


def main():
    d, p, f = 7, 5, 0
    t0 = time.time()
    mats = search_orbit_matrices(d, p, f, max_solutions=200)
    t1 = time.time()
    print(f"orbit matrices found (cap 200): {len(mats)} in {t1 - t0:.1f}s")
    if not mats:
        print("NO orbit matrices — pipeline broken (HoS has such a symmetry)")
        return 1

    lifted_any = False
    for k, C in enumerate(mats):
        t0 = time.time()
        graphs = lift_orbit_matrix(C, d, p, f, max_models=1)
        dt = time.time() - t0
        if graphs:
            print(f"orbit matrix #{k}: LIFTED in {dt:.1f}s")
            A = graphs[0]
            verify_moore(A, d)
            spectral_sanity(A, d)
            lifted_any = True
            break
        else:
            print(f"orbit matrix #{k}: no lift ({dt:.1f}s)")
    if not lifted_any:
        print("NO orbit matrix lifted — pipeline broken")
        return 1
    print("PIPELINE VALIDATED at d=7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
