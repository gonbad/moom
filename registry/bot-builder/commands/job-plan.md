---
name: job-plan
description: Author bot engine architecture, database route, build checklist and handoff on the strongest reasoning model.
---

# /job-plan

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `fsm.md`, `messenger.md`, `infrastructure.md`
and `quality.md` (plus `payments.md` when payments are in scope), alongside
`docs/projects/ID/living/prd.md`, `flow.md`, `data-model.md`, `integrations.md`,
`edge-cases.md`, `test-scenarios.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `prd.md`, `flow.md`, `data-model.md`, `integrations.md`, `edge-cases.md` and
`test-scenarios.md` exist with no unsubmitted question round pending. Execute this
planning step on the **strongest available reasoning model**, writing three Markdown
deliverables inside `docs/`:
1. **`docs/projects/ID/living/architecture.md`:**
   - *Engine & Outbox:* Normalized `Event` dispatcher, transactional FSM state locks,
     deduplication and durable outbound delivery under `projects/ID/app/`.
   - *Messenger & Conditional Payment Adapters:* Platform boundaries from
     `integrations.md` (marking payment modules `not applicable` when outside scope).
   - *Database & Persistence Route:* Follow `infrastructure.md` and `server.md`: use
     PostgreSQL (and Redis when needed) on the participant's VPS via Docker Compose with
     native OpenSSH forwarding and isolated test/production data (or local Docker
     PostgreSQL on macOS/Linux when server setup was deferred). **Only if the participant
     brought no server (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`projects/ID/data/`) as an explicit last-resort local fallback via `NN-questions.md`,
     recording that PostgreSQL migration and live VPS verification remain pending before
     any server deployment.
   - *Transport & Allocations:* Webhook reverse-tunnel/Caddy path or supported poller,
     unique Project ports/volumes, and non-secret variable names mapped from gitignored
     `docs/projects/ID/secrets/credentials.md` (assistant-synced to `projects/ID/.env`
     with placeholder-only `.env.example` in code—never referring the participant to
     non-`.md` files).
2. **`docs/projects/ID/versions/VERSION/checklist.md`:** Ordered implementation and
   harness test items covering every scenario in `test-scenarios.md`.
3. **`docs/projects/ID/versions/VERSION/handoff.md`:** Self-contained build guide for
   `projects/ID/`.

Resolve non-obvious architectural choices via
`docs/projects/ID/versions/VERSION/NN-questions.md`; once submitted, hand off to `/job-build`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-build` or the pending `.md` file).
