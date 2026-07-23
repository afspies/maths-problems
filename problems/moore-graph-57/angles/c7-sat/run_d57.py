"""Short or long C7 fixed-edge CEGAR runner for d=57."""

import sys
import time
from pathlib import Path

import numpy as np

from equivariant_sat import EquivariantMooreSAT


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 7200
    here = Path(__file__).resolve().parent
    cut_file = str(here / "c7_cuts.txt")
    t0 = time.time()
    print("building encoding...", flush=True)
    enc = EquivariantMooreSAT()
    print(f"built: {enc.pool.top:,} vars, {enc.n_clauses:,} clauses, "
          f"{time.time()-t0:.1f}s", flush=True)
    status, result = enc.run(time_budget=budget, cut_file=cut_file,
                             log=lambda message: print(message, flush=True))
    print(f"RESULT: {status}", flush=True)
    if status == "SAT":
        out = here / "moore57_c7.npy"
        np.save(out, result)
        print(f"saved certificate to {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
