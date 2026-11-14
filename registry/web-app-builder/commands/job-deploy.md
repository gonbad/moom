---
name: job-deploy
description: Deliver locally or deploy the accepted application to the production VPS with PostgreSQL, Caddy and HTTPS.
---

# /job-deploy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `infrastructure.md` and `quality.md`, plus
`docs/projects/ID/living/architecture.md`, `status.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Explicit owner acceptance is recorded in `docs/projects/ID/versions/VERSION/` from
`/job-test`. If local-only delivery was chosen or `docs/kandoo/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local run/snapshot
summary in `docs/projects/ID/versions/VERSION/deploy-notes.md` and `living/status.md`,
and never claim a live production or live PostgreSQL verification.

For authorized VPS deployment:
1. **Isolated Service & PostgreSQL Provisioning:**
   - Deploy under a Project-isolated server directory (such as `/opt/ID/`) with unique
     Compose project/ports/volumes recorded in `docs/kandoo/living/server.md`, preserving
     all other Projects and sites.
   - Run production migrations against **PostgreSQL** on a persistent volume (never
     substituting SQLite on the VPS; if local development used the Windows-no-server
     SQLite fallback, verify schema/migrations against PostgreSQL with isolated test data
     first). Deploy the backend API and locally compiled static frontend bundle.
2. **Reverse Proxy & Public HTTPS:**
   - Route the Project's verified domain or `<label>.<server-ip>.nip.io` hostname in
     Caddy with publicly trusted TLS and auto-renewal.
3. **Live Smoke Test & Safe Credential Handoff:**
   - Verify HTTPS reachability, health checks, one primary smoke flow, and PostgreSQL
     state persistence across `docker compose restart`. If SSH, DNS or TLS fails, preserve
     existing services and record deployment as blocked rather than complete.
   - Report the live `https://` URL and a safe pointer to gitignored
     `docs/projects/ID/secrets/credentials.md` for administrative access—**never print
     passwords, tokens or secret values in chat, logs or `deploy-notes.md`**.

Record a non-colliding project-qualified Git tag `project/ID/release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/projects/ID/versions/VERSION/deploy-notes.md`. Apply the file-review/certainty
protocol on `.md` files inside `docs/`, assess the four domains, update Project and
shared `status.md`, and finish with the current Job's full ordered steps localized plus one exact
final action (reading `deploy-notes.md` in `docs/` or opening the verified URL).
