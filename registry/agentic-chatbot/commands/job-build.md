---
name: job-build
description: Implement agent harness, reference monitor, owned services and self-contained security gate tests.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `authority.md`, `budgets.md`, `services.md`,
`infrastructure.md` and `quality.md`, plus `docs/projects/ID/living/architecture.md`,
`capabilities.md`, `privacy.md`, `docs/projects/ID/living/prompts/` and
`docs/projects/ID/versions/VERSION/checklist.md` and `handoff.md`. Preserve earlier
outputs and authorization.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with no unsubmitted
question round pending. Implement inside `projects/ID/`:
1. **Harness, Monitor & Services (`projects/ID/app/`, `projects/ID/services/`):**
   - Implement models and migrations on the planned database route (VPS PostgreSQL over
     native OpenSSH tunnel with isolated test data, local Docker on macOS/Linux, or the
     explicitly selected Windows-no-server SQLite fallback in `projects/ID/data/`). Mark
     live VPS DB verification pending if the tunnel is unreachable rather than faking a pass.
   - Implement the reference monitor enforcing the exact owner-selected `execution_mode`
     + `confirmation_policy` pairs from `capabilities.md`: `read + none`,
     `direct + none`, `direct + soft` and `confirm + hard` (never inventing a mixed
     `soft_confirm` execution mode or overriding owner-chosen `direct` policies with a
     global hard rule).
   - Implement the `[h_*]` handle vault, redacted audit logging, atomic budget accounting,
     deterministic outage fallback, and owned services/bridges loading prompts from
     `docs/projects/ID/living/prompts/` (or synced into `projects/ID/app/prompts/`).
2. **Self-Contained Automated Gate Tests (`projects/ID/tests/`):**
   - Write in-process scripted model-turn tests verifying: `confirm + hard` proposals
     cannot execute without a valid one-use approval bound to `caller + action + args_hash`
     (even if the model passes `confirmed=true`); owner-selected `direct + none` and
     `direct + soft` actions follow their chosen policy without silent global conversion;
     wrong-caller/expired `[h_*]` handles fail; durable audit logs contain zero raw
     secrets/PII; and concurrent runs respect atomic token/spend caps.
3. **Verification Summary:**
   - Run the local test suite to green and summarize results in a `.md` report under
     `docs/projects/ID/versions/VERSION/`, then route to `/job-wire`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-wire` or the pending `.md` file).
