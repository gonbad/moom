---
name: test
description: Conduct adversarial boundary probes, live dialogue verification and owner acceptance rounds.
---

# /test

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `budgets.md`, `authority.md`, `quality.md`.

Gate: `/wire` report is recorded (keeping any deferred live dependencies explicit).
Keep structural tests, live model dialogues and human owner acceptance separate:
1. **Adversarial & Policy Probes:**
   - Exercise direct and indirect prompt injection (via tool outputs), stale-history
     replay, ambiguous refusals on `direct + soft` actions, unapproved execution attempts
     on `confirm + hard` actions (confirming non-bypassability), verification that
     owner-selected `direct + none` / `direct + soft` actions follow their chosen policy,
     audit-log redaction checks and budget-cap exhaustion.
   - Record redacted findings in
     `docs/versions/VERSION/adversarial-report.md`—never logging secrets or
     real PII.
2. **Owner Acceptance Rounds:**
   - Prepare synthetic test callers and isolated test credentials referenced safely via
     gitignored `docs/secrets/credentials.md`.
   - Write a pre-filled `.md` observation sheet
     `docs/versions/VERSION/NN-test-round.md` so the owner can test primary
     workflows, confirmation policies, refusals and fallback behavior, recording feedback
     in Obsidian.
3. **Refinement:**
   - Repair prompt specs in `docs/living/prompts/` or harness code in
     `./`, rerun regression/gate suites and repeat affected live probes until
     the owner records explicit acceptance in `docs/`.
