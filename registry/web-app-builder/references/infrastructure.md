# Product runtime, PostgreSQL and native SSH

Inherit shared SSH/DNS/TLS/proxy facts from `docs/kandoo/living/server.md`; request only
Project overrides. Inventory ports before allocation. Record a unique Compose project,
DB/cache volumes, loopback ports, service user and public route in the shared ledger.
Keep PostgreSQL/Redis on the VPS using Compose. Laptop development uses native OpenSSH,
including Windows OpenSSH; Docker Desktop, WSL and SQLite are not prerequisites.

Illustrative forwarding, with actual aliases/ports selected from the ledger:

```sh
ssh -N -o ExitOnForwardFailure=yes -L 15432:127.0.0.1:25432 project-vps
```

A laptop process uses its forwarded localhost address; a VPS host process uses the
published loopback port; a container uses the Compose service DNS name. Keep schemas,
migrations and handlers the same. Restrict DB/cache listeners and reuse credentials
on resume; editing an env file does not rotate an existing PostgreSQL role.

Example backend separation is `app/main.py` (startup/router registration),
`app/routers/` (HTTP schemas/auth), `app/services/` (business transactions),
`app/db/` (sessions/models), and `migrations/`. FastAPI `APIRouter` and dependency
injection can express this seam; adapt to the chosen stack. Keep resource ownership
checks in the mutation, not only the UI. See
[FastAPI larger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

Build production frontend assets locally, configure deep-link fallback, and route API
requests deliberately. Prove DB auth from the actual runtime and stop if a tunnel
fails. Run migrations/backups against isolated test data first; test restore, restart
and rollback without deleting volumes. Use the existing scoped proxy for blocked
package downloads and verify public HTTPS from the participant's network.
