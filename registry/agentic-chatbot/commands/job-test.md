---
name: job-test
description: Conduct adversarial boundary probes, live dialogue verification and owner acceptance rounds.
---

# /job-test

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `authority.md`, `budgets.md` and
`quality.md`, plus `docs/projects/ID/living/capabilities.md`, `privacy.md`,
`edge-cases.md` and `docs/projects/ID/versions/VERSION/wire-report.md`. Preserve earlier
outputs and authorization.

Gate: `/job-wire` report is recorded (keeping any deferred live dependencies explicit).
Keep structural tests, live model dialogues and human owner acceptance separate:
1. **Adversarial & Policy Probes:**
   - Exercise direct and indirect prompt injection (via tool outputs), stale-history
     replay, ambiguous refusals on `direct + soft` actions, unapproved execution attempts
     on `confirm + hard` actions (confirming non-bypassability), verification that
     owner-selected `direct + none` / `direct + soft` actions follow their chosen policy,
     audit-log redaction checks and budget-cap exhaustion.
   - Record redacted findings in
     `docs/projects/ID/versions/VERSION/adversarial-report.md`—never logging secrets or
     real PII.
2. **Owner Acceptance Rounds:**
   - Prepare synthetic test callers and isolated test credentials referenced safely via
     gitignored `docs/projects/ID/secrets/credentials.md`.
   - Write a pre-filled `.md` observation sheet
     `docs/projects/ID/versions/VERSION/NN-test-round.md` so the owner can test primary
     workflows, confirmation policies, refusals and fallback behavior, recording feedback
     in Obsidian.
3. **Refinement:**
   - Repair prompt specs in `docs/projects/ID/living/prompts/` or harness code in
     `projects/ID/`, rerun regression/gate suites and repeat affected live probes until
     the owner records explicit acceptance in `docs/`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist owner
acceptance, evidence and next action in `docs/projects/ID/living/status.md` and mirror
`docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered steps
localized and one exact next action (`/job-deploy` or the `.md` test-round file).
