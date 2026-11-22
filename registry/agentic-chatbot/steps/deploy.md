---
name: deploy
description: Deliver locally or deploy the accepted agent daemon, services, HTTPS route and budget caps to the VPS.
---

# /deploy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `budgets.md`, `infrastructure.md`, `quality.md`.

Read the local server record and infrastructure reference. Verify the chosen target, inspect actual services and reserve unique resources during this workflow. Preserve other deployments and existing authorization.

Gate: Explicit owner acceptance is recorded in `docs/versions/VERSION/` from
`/test`. If local-only delivery was selected or `docs/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local summary in
`docs/versions/VERSION/deploy-notes.md` and `docs/living/status.md`, and never
claim live VPS deployment.

For authorized VPS deployment:
1. **Isolated Services & PostgreSQL Provisioning:**
   - Deploy `./` under a Project-isolated server directory (such as `/opt/<project-slug>/`)
     with distinct Compose/systemd units, scoped service users, ports and **PostgreSQL /
     Redis** persistent volumes recorded in `docs/living/server.md` (never
     substituting SQLite on the VPS, and never giving the runtime agent coding/SSH keys).
     Drain local consumers before cutover.
2. **Transport & HTTPS Cutover:**
   - Configure Caddy HTTPS routing or supervised polling/scheduler execution as selected,
     verifying health checks without exposing secret URLs.
3. **Budget & Restart Verification:**
   - Verify atomic token/spend caps, redacted audit logging, one bounded live smoke turn,
     and state/quota/pending-proposal persistence across service restart. If SSH,
     provider or platform reachability fails, preserve existing services and record
     deployment as blocked rather than complete. Never print API keys, tokens or
     passwords in chat, logs or `deploy-notes.md`—reference gitignored
     `docs/secrets/credentials.md` safely.

Record a non-colliding project-qualified Git tag `release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/versions/VERSION/deploy-notes.md`.
