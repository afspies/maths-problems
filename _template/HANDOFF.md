# Handoff prompt — {{TITLE}}

Keep this current: every session updates it before finishing, so the next
session's chip/prompt encodes the latest LEARNINGS. This file IS the prompt —
paste it (or point a session at it) to continue work on this problem.

---

You are working on: {{TITLE}} — {{QUESTION}}

Work in problems/{{SLUG}}/ of the maths-problems repo. Read, in order:
1. /AGENTS.md (repo root) — session conventions: branch `problem/{{SLUG}}/<date>-<topic>`,
   stay in your subfolder, exact-arithmetic verification, Codex second opinions
   (GPT-5.6 Sol, xhigh), JOURNAL/LEARNINGS/STATUS updates, board regeneration,
   publishing and DOI rules. If AGENTS.local.md exists, follow it too.
2. problems/{{SLUG}}/PROBLEM.md — statement, certificate/verifier spec, known
   structure, attack-angle menu.
3. problems/{{SLUG}}/LEARNINGS.md — do what "next session should do first" says.
4. problems/{{SLUG}}/JOURNAL.md — recent sessions' detail, if needed.

Current priorities (update each session):
- Build/validate the verifier on a known object; then first angle from PROBLEM.md.
