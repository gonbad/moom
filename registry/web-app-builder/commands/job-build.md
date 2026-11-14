---
name: job-build
description: Implement backend services, migrations, API endpoints and wire the approved frontend seam.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `infrastructure.md` and `quality.md`, plus
`docs/projects/ID/living/architecture.md`, `external-services.md`, `test-scenarios.md`
and `docs/projects/ID/versions/VERSION/checklist.md` and `handoff.md`. Preserve earlier
outputs and authorization.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with no unsubmitted
question round pending. Implement inside `projects/ID/`:
1. **Backend & Database (`projects/ID/backend/`):**
   - Implement models, migrations, transactional ownership checks and API routes matching
     `architecture.md`.
   - Connect to the planned database route (VPS PostgreSQL over verified native OpenSSH
     tunnel with isolated test data, local Docker PostgreSQL on macOS/Linux, or the
     explicitly selected Windows-no-server SQLite fallback in `projects/ID/data/`). If a
     live VPS tunnel or external API is temporarily unreachable, preserve completed code,
     run local fallback adapters and mark live database/service verification pending rather
     than claiming it passed.
   - Read secret values from gitignored `docs/projects/ID/secrets/credentials.md` and sync
     runtime `projects/ID/backend/.env` internally; never print secrets in chat or ask the
     participant to edit `.env` or code files.
2. **Frontend Wiring (`projects/ID/frontend/`):**
   - Preserve the approved screens and Tailwind classes unchanged; replace mock generators
     inside `projects/ID/frontend/src/api/` with real HTTP calls.
   - Verify production frontend compilation with zero external CDN dependencies.
3. **Automated Tests & Local Stack:**
   - Write and run self-contained backend/contract/migration tests under
     `projects/ID/backend/tests/` covering scenarios, authorization denials, idempotency
     and upstream failures.
   - Start the full-stack application on its allocated local port (`http://127.0.0.1:APP_PORT`),
     walk the primary flows, and record build/test evidence in a `.md` summary under
     `docs/projects/ID/versions/VERSION/`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-test` or the pending `.md` file).
