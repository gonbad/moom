---
name: architecture
description: Author agent harness architecture, reference monitor, database route and build checklist on the strongest reasoning model.
---

# /architecture

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `authority.md`, `budgets.md`, `services.md`,
`infrastructure.md` and `quality.md` (plus `messenger.md` and `payments.md` when in
scope), plus all specs in `docs/projects/ID/living/` (including `docs/projects/ID/living/prompts/`) and
submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and
authorization.

Before choosing infrastructure, resolve `docs/projects/ID/living/server.md` using
the installed infrastructure reference and the Constitution. This stage owns the
initial server question: offer identified existing-server reuse, a new Project-owned server,
or local deferral. Preserve previous selections and ask only for missing facts. Do
not treat unselected as no server or create credentials before a target is chosen.

Gate: `prd.md`, `tools.md`, `sops.md`, `data-model.md`, `privacy.md`, `capabilities.md`,
`edge-cases.md` and `docs/projects/ID/living/prompts/` exist with a closed review. Execute on the **strongest available reasoning model**, writing three
Markdown deliverables inside `docs/`:
1. **`docs/projects/ID/living/architecture.md`:**
   - *Harness & Reference Monitor (`projects/ID/app/`):* Intercepts every model tool call,
     enforces the exact two-column policies in `capabilities.md` (`read + none`,
     `direct + none`, `direct + soft`, `confirm + hard`), validates schemas and checks
     atomic token/cost budgets before dispatch.
   - *Handle Vault & Redacted Auditing:* Caller-scoped `[h_*]` vault, sink resolution
     rules and redacted audit metadata schema matching `privacy.md`.
   - *Owned Services & Contracts:* `projects/ID/services/` and
     `projects/ID/contracts/<service>/openapi.yaml`. For an adopted bridge, carry forward
     the reviewed source/revision and provenance from `tools.md`; plan its isolated
     deployment beside the agent, credentials, session storage, ports and required
     restart/event/authorization checks. Use scoped calls, never a sibling checkout,
     the author's accounts or an assumed public gateway.
   - *Database & Persistence Route:* Follow `infrastructure.md` and the selected Project server record: use
     PostgreSQL and Redis on the participant's VPS via Docker Compose with native OpenSSH
     forwarding and isolated test/production data (or local Docker on macOS/Linux when
     server setup was deferred). **Only if the Project explicitly selected no server
     (`none`/deferred) AND is on Windows**, offer project-scoped SQLite
     (`projects/ID/data/`) as an explicit last-resort local fallback via `NN-questions.md`,
     recording that PostgreSQL migration and live VPS verification remain pending before
     any server deployment.
   - *Allocations & Secret Keys:* Distinct Project ports/volumes and non-secret variable
     names mapped from gitignored `docs/projects/ID/secrets/credentials.md`
     (assistant-synced to `projects/ID/.env` with placeholder-only `.env.example` in
     code—never referring the participant to non-`.md` files).
2. **`docs/projects/ID/versions/VERSION/checklist.md`:** Ordered implementation and
   security/gate test items.
3. **`docs/projects/ID/versions/VERSION/handoff.md`:** Self-contained build contract for
   `projects/ID/`.

Resolve non-obvious architectural choices via
`docs/projects/ID/versions/VERSION/NN-questions.md`; once review closes, hand off to `/build`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/build` or the pending `.md` file).
