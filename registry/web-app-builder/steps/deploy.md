---
name: deploy
description: Deliver locally or deploy the accepted application to the production VPS with PostgreSQL, Caddy and HTTPS.
---

# /deploy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `infrastructure.md`, `quality.md`.

Read the local server record and infrastructure reference. Verify the chosen target, inspect actual services and reserve unique resources during this workflow. Preserve other deployments and existing authorization.

Gate: Explicit owner acceptance is recorded in `docs/versions/VERSION/` from
`/test`. If local-only delivery was chosen or `docs/living/server.md` is
`none`/deferred, mark VPS deployment skipped, record the verified local run/snapshot
summary in `docs/versions/VERSION/deploy-notes.md` and `docs/living/status.md`,
and never claim a live production or live PostgreSQL verification.

For authorized VPS deployment:
1. **Isolated Service & PostgreSQL Provisioning:**
   - Deploy under a Project-isolated server directory (such as `/opt/<project-slug>/`) with unique
     Compose project/ports/volumes recorded in `docs/living/server.md`, preserving
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
     `docs/secrets/credentials.md` for administrative access—**never print
     passwords, tokens or secret values in chat, logs or `deploy-notes.md`**.

Record a non-colliding project-qualified Git tag `release/VERSION` (or an
immutable local snapshot hash if Git was deferred) and write
`docs/versions/VERSION/deploy-notes.md`.
