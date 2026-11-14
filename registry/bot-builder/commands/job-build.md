---
name: job-build
description: Implement bot engine, FSM transitions, messenger adapters and self-contained simulated test harness.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `fsm.md`, `messenger.md`, `infrastructure.md`
and `quality.md` (plus `payments.md` when payments apply), plus
`docs/projects/ID/living/architecture.md`, `flow.md`, `integrations.md`,
`test-scenarios.md` and `docs/projects/ID/versions/VERSION/checklist.md` and
`handoff.md`. Preserve earlier outputs and authorization.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with no unsubmitted
question round pending. Implement inside `projects/ID/`:
1. **Core Bot Engine (`projects/ID/app/`):**
   - Implement models and migrations on the planned database route (VPS PostgreSQL over
     native OpenSSH tunnel with isolated test data, local Docker PostgreSQL on
     macOS/Linux, or the explicitly selected Windows-no-server SQLite fallback in
     `projects/ID/data/`). If a live VPS tunnel is temporarily unreachable, preserve
     completed code and mark live DB verification pending rather than claiming it passed.
   - Implement the deterministic FSM dispatcher from `flow.md`, selected messenger
     adapters from `integrations.md`, and payment/receipt modules **only if payments are
     in scope**.
   - Read secret tokens only from gitignored `docs/projects/ID/secrets/credentials.md`
     and sync `projects/ID/.env` internally without printing secrets or referring the
     participant to non-`.md` files.
2. **Self-Contained Simulated Harness (`projects/ID/tests/`):**
   - Build a local in-memory messenger harness inside `projects/ID/tests/` that injects
     normalized `Event` fixtures (commands, text, callbacks, media, duplicates, stale
     tokens and mid-dialog restarts) into the dispatcher against isolated test data and
     asserts outgoing replies plus database state without external repos or network calls.
3. **Verification Summary:**
   - Run the automated test suite to green and record what passed and what live checks
     remain pending in a `.md` report under `docs/projects/ID/versions/VERSION/`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-test` or the pending `.md` file).
