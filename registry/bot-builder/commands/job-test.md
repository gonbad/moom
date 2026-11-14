---
name: job-test
description: Conduct live messenger rehearsal with isolated test credentials and owner acceptance rounds.
---

# /job-test

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `messenger.md`, `infrastructure.md` and
`quality.md`, plus `docs/projects/ID/living/test-scenarios.md`, `integrations.md` and
submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and
authorization.

Gate: Automated simulated harness tests in `/job-build` pass. Fixture tests never prove
live messenger connectivity:
1. **Isolated Live Test Connection:**
   - Load isolated test bot credentials from gitignored
     `docs/projects/ID/secrets/credentials.md` (never unscoped `docs/secrets/` and never
     printing token values in chat or logs). Start the bot locally via polling or the
     verified reverse SSH webhook tunnel. If messenger network access or a test token is
     unavailable, apply the configured forward proxy or mark live messenger rehearsal
     blocked/pending without fabricating acceptance.
2. **Owner Rehearsal Rounds:**
   - Share the non-secret test bot handle and prepare a pre-filled `.md` observation
     sheet `docs/projects/ID/versions/VERSION/NN-test-round.md` referencing
     `docs/projects/ID/living/test-scenarios.md` so the owner can test real turns,
     buttons, cancellations, restarts and conditional payment cases, recording results in
     Obsidian.
3. **Defect Resolution:**
   - Fix reported transport, keyboard, RTL formatting or state defects in `projects/ID/`,
     rerun harness regressions and repeat affected live turns until the owner records
     explicit acceptance in `docs/`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist owner
acceptance, evidence and next action in `docs/projects/ID/living/status.md` and mirror
`docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered steps localized
and one exact next action (`/job-deploy` or the `.md` test-round file in `docs/`).
