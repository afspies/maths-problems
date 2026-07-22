# Conventions for problem-attack sessions

This repo hosts parallel, agent-driven attacks on long-open mathematics problems
whose interesting direction has a **finite explicit certificate with a cheap exact
verifier** — the regime highlighted by the July 2026 Fable-assisted counterexample
to the Jacobian conjecture. Many sessions work here concurrently; these conventions
exist so their work composes.

If a gitignored `AGENTS.local.md` exists in the repo root, read and follow it too
(it holds machine/infra-specific conventions that don't belong in a public repo).

## Layout

```
README.md            auto-generated status board — NEVER hand-edit; run tools/board.py
AGENTS.md            this file
CITATION.cff         repo-level citation metadata
tools/               board.py · new_problem.py · release.py
_template/           canonical problem skeleton (instantiate via tools/new_problem.py)
problems/<slug>/     one folder per tracked problem (structure below)
```

Per problem:

```
PROBLEM.md      statement, certificate + verifier spec, known structure, attack menu
STATUS.toml     machine-readable status — the ONLY input to the README board
JOURNAL.md      append-only chronological log, one dated section per session
LEARNINGS.md    distilled: what failed and WHY, surprises, what to do first next time
HANDOFF.md      the prompt for the NEXT session on this problem — keep it current
harness/        verifier + shared code; the verifier is always built and tested first
angles/<name>/  one subfolder per attack angle, each with its own README.md
literature/     notes + refs.bib — every status claim about prior work needs a citation
certificates/   verified positive objects: object + verify script + expected output
results/        citable negative results (exhaustions/exclusions) + repro metadata
writeup/        report.md + CITATION.cff; becomes the DOI-bearing artifact on release
```

## Session lifecycle

1. **Branch**: `problem/<slug>/<YYYY-MM-DD>-<topic>`. Never work directly on main.
2. **Scope**: touch only `problems/<your-slug>/` — plus the generated `README.md`
   via `tools/board.py`. Never edit another problem's folder or shared tooling
   without a very good reason stated in your journal.
3. **Verify before search**: the first artifact on any problem is a working
   verifier in `harness/`, validated on a known object. No exceptions.
4. **Merge**: when done, update `STATUS.toml`, run `python3 tools/board.py`,
   rebase on latest main, and merge your branch to main yourself. Conflicts
   should be near-impossible if you stayed in scope; if you hit one in
   `README.md`, regenerate it rather than resolving by hand.

## Working style

- **Second opinions**: consult GPT-5.6 Sol at xhigh effort (via the codex agent;
  pass `--model gpt-5.6-sol --effort xhigh` explicitly) at major decision points —
  attack-angle selection, encoding design, soundness of any exclusion argument,
  stuck states. Treat it as an independent adversarial reviewer and record its
  verdicts in the journal.
- **Be exploratory**: deliberately rotate across branches of mathematics and
  attack styles (algebraic, spectral/SDP, SAT/constraint, probabilistic,
  geometric). Don't tunnel on the first encoding that runs. Each angle gets its
  own `angles/<name>/` with a README stating the idea, status, and verdict.
- **Exact arithmetic only** in anything verification-adjacent: integers,
  rationals, symbolic algebraic numbers. Floats may steer heuristics, never
  certify claims.
- **Negative results are first-class**: an exhausted subspace ("no solution with
  symmetry X in family Y") goes in `results/` with exact search-space definition,
  tooling, and seeds so it is reproducible and citable.
- **Honesty**: these are famous open problems. Claim existence only with an
  object passing the checked-in verifier; claim exclusions only with a complete,
  reproducible case analysis (prefer proof-logging solvers, e.g. SAT + DRAT).

## Logging (mandatory before ending any session)

- Append a dated section to `JOURNAL.md`: what was tried, exact commands and
  encodings, outcomes, wall-clock/compute spent.
- Update `LEARNINGS.md`: the distilled deltas only — what didn't work and *why*,
  what surprised you, what the next session should do first.
- Refresh `HANDOFF.md` so the next session's prompt encodes those learnings.
- Update `STATUS.toml` (status, `best_result`, append to `sessions`), run
  `python3 tools/board.py`, commit, merge.

## Publishing and citation

- **Substantive results** (new certificate, new exclusion, completed milestone
  writeup): publish the HTML report to `tmp.afspies.com/<slug>/` via the
  `afspies-publish` skill before ending the session.
- **DOIs are per problem subfolder**: `python3 tools/release.py <slug> --version vN`
  bundles `writeup/` + `certificates/` + `PROBLEM.md` and creates/updates a Zenodo
  deposition for that problem (versioned DOI; needs `ZENODO_TOKEN`). The DOI is
  written back into `STATUS.toml` and `writeup/CITATION.cff`. Only release when a
  result is verified and written up.
