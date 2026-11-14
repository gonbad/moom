---
name: job-deploy
description: Deliver locally or deploy the accepted agent daemon, services, HTTPS route and budget caps to the VPS.
---

# /job-deploy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `budgets.md`, `infrastructure.md` and
`quality.md`, plus `docs/projects/ID/living/architecture.md`, `status.md` and submitted
rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Explicit owner acceptance is recorded in `docs/projects/ID/versions/VERSION/` from
`/job-test`. If local-only delivery was selected or `docs/kandoo/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local summary in
`docs/projects/ID/versions/VERSION/deploy-notes.md` and `living/status.md`, and never
claim live VPS deployment.

For authorized VPS deployment:
1. **Isolated Services & PostgreSQL Provisioning:**
   - Deploy `projects/ID/` under a Project-isolated server directory (such as `/opt/ID/`)
     with distinct Compose/systemd units, scoped service users, ports and **PostgreSQL /
     Redis** persistent volumes recorded in `docs/kandoo/living/server.md` (never
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
     `docs/projects/ID/secrets/credentials.md` safely.

Record a non-colliding project-qualified Git tag `project/ID/release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/projects/ID/versions/VERSION/deploy-notes.md`. Apply the file-review/certainty
protocol on `.md` files inside `docs/`, assess the four domains, update Project and
shared `status.md`, and finish with the current Job's full ordered steps localized plus one exact
final action.
