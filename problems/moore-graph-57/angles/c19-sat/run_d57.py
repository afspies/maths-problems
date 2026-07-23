"""The real search: d=57, p=19, s=3 — one fixed vertex, a1(g^q) = 57
(Ishida arXiv:2606.29183 Thm 1.2).  Resumable via cuts file."""

import sys
import time
from pathlib import Path

import numpy as np

from equivariant_sat import EquivariantMooreSAT


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 7200
    here = Path(__file__).resolve().parent
    cut_file = str(here / "d57_cuts.txt")
    t0 = time.time()
    print("building encoding...", flush=True)
    enc = EquivariantMooreSAT(57, 19, a1_per_power=57)
    print(f"built: {enc.pool.top:,} vars, {enc.n_clauses:,} clauses, "
          f"{time.time()-t0:.1f}s", flush=True)
    status, result = enc.run(time_budget=budget, cut_file=cut_file,
                             log=lambda m: print(m, flush=True))
    print(f"RESULT: {status}", flush=True)
    if status == 'SAT':
        out = here.parents[1] / "certificates" / "moore57_c19.npy"
        np.save(out, result)
        print(f"saved certificate to {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
