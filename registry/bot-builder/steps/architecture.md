---
name: architecture
description: Author bot engine architecture, database route, build checklist and handoff on the strongest reasoning model.
---

# /architecture

Read the project constitution and current status. Use the following references from `docs/references/`: `fsm.md`, `workflow.md`, `payments.md`, `messenger.md`, `infrastructure.md`, `quality.md`.

Resolve infrastructure at this stage according to the workflow server mode. For dedicated hosting use /server, or record an explicit local deferral. Read the local server record and preserve settled choices.

Gate: `prd.md`, `flow.md`, `data-model.md`, `integrations.md`, `edge-cases.md` and
`test-scenarios.md` exist with a closed review. Execute this
planning step on the **strongest available reasoning model**, writing three Markdown
deliverables inside `docs/`:
1. **`docs/living/architecture.md`:**
   - *Engine & Outbox:* Normalized `Event` dispatcher, transactional FSM state locks,
     deduplication and durable outbound delivery under `./app/`.
   - *Messenger & Conditional Payment Adapters:* Platform boundaries from
     `integrations.md` (marking payment modules `not applicable` when outside scope).
   - *Database & Persistence Route:* Follow `infrastructure.md` and the selected Project server record: use
     PostgreSQL (and Redis when needed) on the participant's VPS via Docker Compose with
     native OpenSSH forwarding and isolated test/production data (or local Docker
     PostgreSQL on macOS/Linux when server setup was deferred). **Only if the Project explicitly
     selected no server (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`./data/`) as an explicit last-resort local fallback via `NN-questions.md`,
     recording that PostgreSQL migration and live VPS verification remain pending before
     any server deployment.
   - *Transport & Allocations:* Webhook reverse-tunnel/Caddy path or supported poller,
     unique Project ports/volumes, and non-secret variable names mapped from gitignored
     `docs/secrets/credentials.md` (assistant-synced to `./.env`
     with placeholder-only `.env.example` in code—never referring the participant to
     non-`.md` files).
2. **`docs/versions/VERSION/checklist.md`:** Ordered implementation and
   harness test items covering every scenario in `test-scenarios.md`.
3. **`docs/versions/VERSION/handoff.md`:** Self-contained build guide for
   `./`.

Resolve non-obvious architectural choices via
`docs/versions/VERSION/NN-questions.md`; once review closes, hand off to `/build`.
