"""Validate the equivariant SAT machinery on the known Moore graphs:
  - d=3, p=3 (Petersen, order-3 automorphism fixing one vertex, a1=0)
  - d=7, p=7 (Hoffman-Singleton, order-7 automorphism fixing one vertex)
Both must come out SAT and pass the exact verifier.
"""

import sys
import time

from equivariant_sat import EquivariantMooreSAT


def run(d, p, a1, budget):
    t0 = time.time()
    enc = EquivariantMooreSAT(d, p, a1_per_power=a1)
    status, A = enc.run(time_budget=budget,
                        log=lambda m: print(f"  {m}", flush=True))
    print(f"d={d} p={p} a1={a1}: {status} in {time.time()-t0:.1f}s", flush=True)
    return status


def main():
    ok = True
    ok &= run(3, 3, 0, 60) == 'SAT'
    ok &= run(7, 7, None, 600) == 'SAT'
    print("VALIDATION " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
