# Product runtime, PostgreSQL policy and native SSH forwarding

Read `docs/kandoo/living/server.md`, `docs/kandoo/living/profile.md` and
`docs/constitution/03-infrastructure-and-secrets.md`. Request only Project-specific
overrides. Inventory ports before allocation, and record a unique Compose project name,
PostgreSQL/Redis volumes, loopback ports, service user and public route in
`docs/kandoo/living/server.md` and `docs/projects/ID/living/architecture.md`.

## Coherent database route

1. **With a configured VPS (standard path):** Run PostgreSQL (and Redis when needed) on
   the VPS via Docker Compose with persistent volumes and separate test/production
   databases. Laptop development connects over native OpenSSH local forwarding
   (including native Windows OpenSSH—no Docker Desktop or WSL required):
   ```sh
   ssh -N -o ExitOnForwardFailure=yes -L 15432:127.0.0.1:25432 project-vps
   ```
2. **Deferred server on macOS or Linux:** Run isolated PostgreSQL locally via Docker if
   available, or continue specifications/prototype work while marking live DB checks
   pending until a server is configured via `/kandoo-server`.
3. **Last resort—no server AND Windows (`job-plan` only):** Only when `server.md` is
   `none`/deferred **and** the participant is on Windows, `/job-plan` may offer
   project-scoped SQLite under `projects/ID/data/` as an explicit last-resort local
   fallback so local full-stack exercises can proceed. Record that PostgreSQL migration
   and live VPS database verification remain pending; never deploy SQLite as a VPS
   production substitute.

A laptop process uses its forwarded localhost port, a VPS host process uses the
published loopback port, and a container uses its Compose service DNS name while keeping
ORM models, migrations and API contracts identical. Reuse DB credentials on resume from
gitignored `docs/projects/ID/secrets/credentials.md` (synced by the assistant into
`projects/ID/backend/.env`); editing an environment file alone does not rotate an
existing PostgreSQL role.

Example backend layout under `projects/ID/backend/`: `app/main.py` (startup/routers),
`app/routers/` (HTTP schemas/auth), `app/services/` (business transactions and external
adapters), `app/db/` (sessions/models), and `migrations/`. Enforce resource ownership
inside backend mutations, not only in the UI. See
[FastAPI larger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

Build production frontend assets locally under `projects/ID/frontend/`, configure SPA
deep-link fallback, and route API requests deliberately. When SSH tunnels or package
registries fail, apply the configured forward proxy or local fallback and mark blocked
live checks honestly without claiming verified connectivity.
