---
name: deploy
description: Deliver locally or deploy the accepted bot daemon and HTTPS webhook to the production VPS.
---

# /deploy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `messenger.md`, `infrastructure.md`, `quality.md`.

Read the local server record and infrastructure reference. Verify the chosen target, inspect actual services and reserve unique resources during this workflow. Preserve other deployments and existing authorization.

Gate: Explicit owner acceptance is recorded in `docs/versions/VERSION/` from
`/test`. If local-only delivery was selected or `docs/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local summary in
`docs/versions/VERSION/deploy-notes.md` and `docs/living/status.md`, and never
claim live VPS deployment.

For authorized VPS deployment:
1. **Isolated Service & PostgreSQL Provisioning:**
   - Deploy `./` under a Project-isolated server directory (such as `/opt/<project-slug>/`)
     with unique Compose/systemd service names, ports and **PostgreSQL** persistent
     volumes recorded in `docs/living/server.md` (never substituting SQLite on the
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
     `docs/secrets/credentials.md` safely.

Record a non-colliding project-qualified Git tag `release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/versions/VERSION/deploy-notes.md`.
