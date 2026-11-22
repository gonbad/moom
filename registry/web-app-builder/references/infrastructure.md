# Product runtime, PostgreSQL policy and native SSH forwarding

Follow the workflow server mode and local server instructions. Read project-owned `docs/living/server.md` and its protected access file only when the stage needs access. Inspect the actual target before allocating resources. Preserve other deployments.

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
   pending until a server is configured at its declared infrastructure stage.
3. **Last resort—no server AND Windows (`architecture` only):** Only when the Project server selection is
   `none`/deferred **and** the participant is on Windows, `/architecture` may offer
   project-scoped SQLite under `./data/` as an explicit last-resort local
   fallback so local full-stack exercises can proceed. Record that PostgreSQL migration
   and live VPS database verification remain pending; never deploy SQLite as a VPS
   production substitute.

A laptop process uses its forwarded localhost port, a VPS host process uses the
published loopback port, and a container uses its Compose service DNS name while keeping
ORM models, migrations and API contracts identical. Reuse DB credentials on resume from
gitignored `docs/secrets/credentials.md` (synced by the assistant into
`./backend/.env`); editing an environment file alone does not rotate an
existing PostgreSQL role.

Example backend layout under `./backend/`: `app/main.py` (startup/routers),
`app/routers/` (HTTP schemas/auth), `app/services/` (business transactions and external
adapters), `app/db/` (sessions/models), and `migrations/`. Enforce resource ownership
inside backend mutations, not only in the UI. See
[FastAPI larger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

Build production frontend assets locally under `./frontend/`, configure SPA
deep-link fallback, and route API requests deliberately. When SSH tunnels or package
registries fail, apply the configured forward proxy or local fallback and mark blocked
live checks honestly without claiming verified connectivity.
