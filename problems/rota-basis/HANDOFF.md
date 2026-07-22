# Handoff prompt — Rota's basis conjecture

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: Rota's basis conjecture — can n bases of a rank-n matroid
always be rearranged into an n×n grid whose rows are the given bases and whose
columns are all bases?

Work in problems/rota-basis/ of the maths-problems repo. Read, in order:
1. /AGENTS.md (repo root) — session conventions; AGENTS.local.md if present.
2. problems/rota-basis/PROBLEM.md — statement, status (with 2025-26
   corrections), certificate/verifier spec, the adopted bridge-lemma plan.
3. problems/rota-basis/LEARNINGS.md — do what "next session should do first" says.
4. problems/rota-basis/JOURNAL.md — recent sessions' detail, if needed.

## Operating mode for THIS problem: orchestrator (token-frugal Fable)

You (Fable) are the research director, not the workhorse. Delegate almost all
concrete work — literature digestion, coding, experiments, proof drafting,
verification — to GPT-5.6 Sol subagents via the codex agent, at `--effort
high` for mechanical work and `--effort xhigh` for mathematical reasoning,
proof review, and stuck states. Use Sol liberally and in parallel; your own
output should be limited to high-level direction, quality control, novel-angle
proposals, and synthesis.

The shared state lives in workbench/ (create it if missing):
- workbench/TASKS.md — the delegation queue: one entry per dispatched task
  (id, brief, status, output file). You maintain this.
- workbench/briefs/<id>.md — the self-contained brief each Sol subagent is
  pointed at (context, exact task, output contract).
- workbench/out/<id>.md — where each subagent is INSTRUCTED (in its brief) to
  write its full workings, intermediate reasoning, and results, so state
  survives across subagent calls and sessions. Subagents should read prior
  out/ files their brief lists as dependencies.

You review out/ files at high level, steer, and dispatch the next round.
JOURNAL/LEARNINGS/HANDOFF/STATUS duties from AGENTS.md remain yours (keep them
short); substantive artifacts (harness code, instance libraries, lemma
write-ups) are produced by the subagents directly in the problem folder.

Current priorities (update each session):
- Variant map (general vs representable vs vector space) → literature/.
- Exact rank-oracle + grid-verifier + proof-logging SAT harness → harness/.
- Adversarial near-decomposition library (binary/graphic, rank 5–12); minimum
  repair-support measurements; first candidate f(k)-bounded absorption lemma
  the harness fails to kill.
