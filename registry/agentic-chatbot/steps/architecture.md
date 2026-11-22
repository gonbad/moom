---
name: architecture
description: Author agent harness architecture, reference monitor, database route and build checklist on the strongest reasoning model.
---

# /architecture

Read the project constitution and current status. Use the following references from `docs/references/`: `services.md`, `workflow.md`, `budgets.md`, `payments.md`, `authority.md`, `messenger.md`, `infrastructure.md`, `quality.md`.

Resolve infrastructure at this stage according to the workflow server mode. For dedicated hosting use /server, or record an explicit local deferral. Read the local server record and preserve settled choices.

Gate: `prd.md`, `tools.md`, `sops.md`, `data-model.md`, `privacy.md`, `capabilities.md`,
`edge-cases.md` and `docs/living/prompts/` exist with a closed review. Execute on the **strongest available reasoning model**, writing three
Markdown deliverables inside `docs/`:
1. **`docs/living/architecture.md`:**
   - *Harness & Reference Monitor (`./app/`):* Intercepts every model tool call,
     enforces the exact two-column policies in `capabilities.md` (`read + none`,
     `direct + none`, `direct + soft`, `confirm + hard`), validates schemas and checks
     atomic token/cost budgets before dispatch.
   - *Handle Vault & Redacted Auditing:* Caller-scoped `[h_*]` vault, sink resolution
     rules and redacted audit metadata schema matching `privacy.md`.
   - *Owned Services & Contracts:* `./services/` and
     `./contracts/<service>/openapi.yaml`. For an adopted bridge, carry forward
     the reviewed source/revision and provenance from `tools.md`; plan its isolated
     deployment beside the agent, credentials, session storage, ports and required
     restart/event/authorization checks. Use scoped calls, never a sibling checkout,
     the author's accounts or an assumed public gateway.
   - *Database & Persistence Route:* Follow `infrastructure.md` and the selected Project server record: use
     PostgreSQL and Redis on the participant's VPS via Docker Compose with native OpenSSH
     forwarding and isolated test/production data (or local Docker on macOS/Linux when
     server setup was deferred). **Only if the Project explicitly selected no server
     (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`./data/`) as an explicit last-resort local fallback via `NN-questions.md`,
     recording that PostgreSQL migration and live VPS verification remain pending before
     any server deployment.
   - *Allocations & Secret Keys:* Distinct Project ports/volumes and non-secret variable
     names mapped from gitignored `docs/secrets/credentials.md`
     (assistant-synced to `./.env` with placeholder-only `.env.example` in
     code—never referring the participant to non-`.md` files).
2. **`docs/versions/VERSION/checklist.md`:** Ordered implementation and
   security/gate test items.
3. **`docs/versions/VERSION/handoff.md`:** Self-contained build contract for
   `./`.

Resolve non-obvious architectural choices via
`docs/versions/VERSION/NN-questions.md`; once review closes, hand off to `/build`.
