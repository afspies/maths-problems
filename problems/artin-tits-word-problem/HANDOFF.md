# Handoff prompt — Word problem for the minimal unknown Artin-Tits group

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: decidability of the word problem for the Artin–Tits group
G = ⟨a,b,c,d | ad=da, xyx=yxy for the other five pairs⟩ — Gowers's Polymath
proposal (2026-03-20), the simplest Artin–Tits group with unknown status.

Work in problems/artin-tits-word-problem/ of the maths-problems repo. Read:
1. /AGENTS.md (repo root) + AGENTS.local.md if present.
2. problems/artin-tits-word-problem/PROBLEM.md — statement, Polymath thread
   state, the decidable-class analysis (VERIFY it), tiered attack menu.
3. LEARNINGS.md → do what "next session should do first" says; JOURNAL.md for
   detail.

## Operating mode: orchestrator (token-frugal Fable) — same as rota-basis

You (Fable) are research director: delegate literature digestion, coding,
experiments, theory drafts, and reviews to GPT-5.6 Sol subagents via the
codex agent (--model gpt-5.6-sol explicit; --effort high mechanical / xhigh
for theory, proofs, reviews — use liberally, in parallel, one lane per
theory angle). Maintain workbench/TASKS.md + briefs/<id>.md + out/<id>.md;
every subagent brief lists dependency out/ files to read and requires full
workings written to its out/ file. Your tokens: direction, QC, novel angles,
synthesis. JOURNAL/LEARNINGS/HANDOFF/STATUS stay yours, kept short.

## Community norms (Polymath!)

Results are shaped for Gowers's blog thread first (the repo owner posts
them), DOI second. Full credit to Gowers, Schaumann, Riley, and the thread.
Check the thread for updates at session start — it is live and others are
working on it.

Current priorities (update each session):
- Tier 0: exact move engine + independent A₂ from Gowers's written spec;
  exhaustive verdict on Schaumann's word bbdCbbcDBBdCBBcD + family; A₂ vs it.
- Tier 1: adjudicate arXiv:2305.11622; verified decidable-class map.
- Tier 2 (the campaign): Garside-theoretic innovation — relative/interval
  Garside via enlargement (McCammond–Sulway analogue), amalgam-of-decidable-
  parabolics gluing, computable filling-length bound, bounded-detour
  rewriting completeness.
