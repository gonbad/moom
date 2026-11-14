---
name: job-deploy
description: Deliver locally or deploy the accepted bot daemon and HTTPS webhook to the production VPS.
---

# /job-deploy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `messenger.md`, `infrastructure.md` and
`quality.md`, plus `docs/projects/ID/living/architecture.md`, `status.md` and submitted
rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Explicit owner acceptance is recorded in `docs/projects/ID/versions/VERSION/` from
`/job-test`. If local-only delivery was selected or `docs/kandoo/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local summary in
`docs/projects/ID/versions/VERSION/deploy-notes.md` and `living/status.md`, and never
claim live VPS deployment.

For authorized VPS deployment:
1. **Isolated Service & PostgreSQL Provisioning:**
   - Deploy `projects/ID/` under a Project-isolated server directory (such as `/opt/ID/`)
     with unique Compose/systemd service names, ports and **PostgreSQL** persistent
     volumes recorded in `docs/kandoo/living/server.md` (never substituting SQLite on the
     VPS). Drain/stop any local consumer before cutover so only one consumer is active.
2. **Webhook or Managed Poller Cutover:**
   - For webhooks: route the Project's verified HTTPS path in Caddy to the loopback
     listener, configure the secret webhook header via the platform client (without
     exposing tokens in URLs or shell logs), and verify webhook status.
   - For supported polling: configure supervised restart with bounded backoff.
3. **Live Smoke Test & Safe Handoff:**
   - Verify `/start`, one primary journey and state persistence across service restart.
     If SSH or platform reachability fails, preserve existing services and record
     deployment as blocked rather than complete. Never print tokens or secret values in
     chat, logs or `deploy-notes.md`—reference gitignored
     `docs/projects/ID/secrets/credentials.md` safely.

Record a non-colliding project-qualified Git tag `project/ID/release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/projects/ID/versions/VERSION/deploy-notes.md`. Apply the file-review/certainty
protocol on `.md` files inside `docs/`, assess the four domains, update Project and
shared `status.md`, and finish with the current Job's full ordered steps localized plus one exact
final action.
