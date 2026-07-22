#!/usr/bin/env python3
"""Regenerate the root README.md status board from problems/*/STATUS.toml.

Usage: python3 tools/board.py [--check]
  --check   exit 1 if README.md is out of date instead of rewriting it.

README.md is fully generated — never hand-edit it. Sessions update their own
problem's STATUS.toml and rerun this script; concurrent sessions therefore
never edit the same source file.
"""
import argparse
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_ORDER = [
    "solved", "partial-results", "active", "scaffolded",
    "proposed", "excluded", "retired",
]
BADGES = {
    "proposed": "⬜ proposed",
    "scaffolded": "🧩 scaffolded",
    "active": "🔵 active",
    "partial-results": "🟡 partial results",
    "solved": "🟢 solved",
    "excluded": "🟢 excluded (nonexistence)",
    "retired": "⚫ retired",
}

HEADER = """\
# maths-problems

Agent-driven attacks on long-open mathematics problems whose interesting
direction has a **finite explicit certificate with a cheap exact verifier** —
the regime highlighted by the July 2026 Fable-assisted counterexample to the
Jacobian conjecture. Conventions for working sessions live in
[AGENTS.md](AGENTS.md); each problem folder under [problems/](problems/) is
self-contained (statement, verifier, journal, results, writeup).

**This file is generated from `problems/*/STATUS.toml` by `tools/board.py` —
do not edit by hand.**

## Tracked problems

| Problem | Status | Question | Best result so far | DOI |
|---|---|---|---|---|
"""

FOOTER = """
## Adding a problem

```
python3 tools/new_problem.py <slug> --title "Problem name"
```

Then fill in `PROBLEM.md` (statement, certificate + verifier spec, known
structure, attack-angle menu), set `STATUS.toml` to `proposed`, and rerun
`python3 tools/board.py`.
"""


def load_statuses():
    rows = []
    for status_file in sorted(ROOT.glob("problems/*/STATUS.toml")):
        with open(status_file, "rb") as fh:
            data = tomllib.load(fh)
        data.setdefault("slug", status_file.parent.name)
        rows.append(data)
    return rows


def render(rows):
    def sort_key(r):
        status = r.get("status", "proposed")
        rank = STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)
        return (rank, r["slug"])

    lines = [HEADER]
    for r in sorted(rows, key=sort_key):
        slug = r["slug"]
        title = r.get("title", slug)
        badge = BADGES.get(r.get("status", "proposed"), r.get("status", "?"))
        question = r.get("question", "").replace("|", "\\|")
        best = r.get("best_result", "") or "—"
        doi = r.get("doi", "")
        doi_cell = f"[{doi}](https://doi.org/{doi})" if doi else "—"
        lines.append(
            f"| [{title}](problems/{slug}/PROBLEM.md) | {badge} | {question} "
            f"| {best.replace('|', chr(92) + '|')} | {doi_cell} |\n"
        )
    lines.append(FOOTER)
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    content = render(load_statuses())
    readme = ROOT / "README.md"
    if args.check:
        if not readme.exists() or readme.read_text() != content:
            print("README.md is out of date — run: python3 tools/board.py")
            sys.exit(1)
        print("README.md is up to date.")
        return
    readme.write_text(content)
    print(f"Wrote {readme} ({len(load_statuses())} problems).")


if __name__ == "__main__":
    main()
