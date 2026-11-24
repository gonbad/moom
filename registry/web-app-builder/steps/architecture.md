---
name: architecture
description: Author technical architecture, database route, build checklist and handoff on the strongest reasoning model.
---

# /architecture

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `infrastructure.md`, `quality.md`.

Resolve infrastructure at this stage according to the workflow server mode. For dedicated hosting use /server, or record an explicit local deferral. Read the local server record and preserve settled choices.

Gate: `prd.md`, `data-model.md`, `ux.md`, `design-system.md`, `test-scenarios.md` and
the accepted prototype baseline recorded in `docs/living/status.md` are
all in place with a closed review. Execute this planning step on the **strongest available reasoning
model**, producing three Markdown deliverables inside `docs/`:
1. **`docs/living/architecture.md`:**
   - *Database & Persistence Route:* Follow `infrastructure.md` and the selected Project server record: use
     PostgreSQL (and Redis where needed) on the participant's VPS via Docker Compose with
     native OpenSSH forwarding and isolated test/production data (or local Docker
     PostgreSQL on macOS/Linux when server setup was deferred). **Only if the Project explicitly
     selected no server (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`./data/`) as an explicit last-resort local fallback via `NN-analysis-architecture.md`,
     recording that PostgreSQL migration and live DB verification remain pending before
     any server deployment.
   - *Backend API & Seam Mapping:* Map every function in `./frontend/src/api/`
     to endpoints in `./backend/` returning identical response shapes, with
     server-side authorization and idempotency checks.
   - *Styling & Assets:* Confirm locally bundled Tailwind and local fonts under
     `./frontend/` with zero runtime CDN dependency.
   - *External Adapters & Secret Boundaries:* Define `./backend/app/services/`
     modules, timeouts and fallbacks from `external-services.md`. List non-secret
     variable names here and store actual secret values only in gitignored
     `docs/secrets/credentials.md` (assistant-synced to `./backend/.env`,
     with placeholder-only `.env.example` in code—never referring the participant to
     non-`.md` files).
   - *Port & Volume Allocations:* Record distinct Project ports and Compose/volume names.
2. **`docs/versions/VERSION/checklist.md`:** Ordered implementation and test
   items covering every scenario and edge case in `test-scenarios.md`.
3. **`docs/versions/VERSION/handoff.md`:** Self-contained build contract
   confirming `./frontend/` keeps its approved layout while replacing the mock
   API seam.

Resolve any non-obvious architectural choices via
`docs/versions/VERSION/NN-analysis-architecture.md`; once review closes, hand off to `/build`.
