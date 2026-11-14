---
name: job-plan
description: Author technical architecture, database route, build checklist and handoff on the strongest reasoning model.
---

# /job-plan

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `infrastructure.md` and `quality.md`, plus
`docs/projects/ID/living/prd.md`, `data-model.md`, `ux.md`, `design-system.md`,
`external-services.md`, `test-scenarios.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `prd.md`, `data-model.md`, `ux.md`, `design-system.md`, `test-scenarios.md` and
the accepted prototype baseline recorded in `docs/projects/ID/living/status.md` are
all in place with no unsubmitted
question round pending. Execute this planning step on the **strongest available reasoning
model**, producing three Markdown deliverables inside `docs/`:
1. **`docs/projects/ID/living/architecture.md`:**
   - *Database & Persistence Route:* Follow `infrastructure.md` and `server.md`: use
     PostgreSQL (and Redis where needed) on the participant's VPS via Docker Compose with
     native OpenSSH forwarding and isolated test/production data (or local Docker
     PostgreSQL on macOS/Linux when server setup was deferred). **Only if the participant
     brought no server (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`projects/ID/data/`) as an explicit last-resort local fallback via `NN-questions.md`,
     recording that PostgreSQL migration and live DB verification remain pending before
     any server deployment.
   - *Backend API & Seam Mapping:* Map every function in `projects/ID/frontend/src/api/`
     to endpoints in `projects/ID/backend/` returning identical response shapes, with
     server-side authorization and idempotency checks.
   - *Styling & Assets:* Confirm locally bundled Tailwind and local fonts under
     `projects/ID/frontend/` with zero runtime CDN dependency.
   - *External Adapters & Secret Boundaries:* Define `projects/ID/backend/app/services/`
     modules, timeouts and fallbacks from `external-services.md`. List non-secret
     variable names here and store actual secret values only in gitignored
     `docs/projects/ID/secrets/credentials.md` (assistant-synced to `projects/ID/backend/.env`,
     with placeholder-only `.env.example` in code—never referring the participant to
     non-`.md` files).
   - *Port & Volume Allocations:* Record distinct Project ports and Compose/volume names.
2. **`docs/projects/ID/versions/VERSION/checklist.md`:** Ordered implementation and test
   items covering every scenario and edge case in `test-scenarios.md`.
3. **`docs/projects/ID/versions/VERSION/handoff.md`:** Self-contained build contract
   confirming `projects/ID/frontend/` keeps its approved layout while replacing the mock
   API seam.

Resolve any non-obvious architectural choices via
`docs/projects/ID/versions/VERSION/NN-questions.md`; once submitted, hand off to `/job-build`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-build` or the pending `.md` file).
