# Inherit shared infrastructure

Read `docs/kandoo/living/server.md` and the infrastructure/secrets Constitution before
connecting. Inherit its verified SSH identity, server, domain or `nip.io` hostname, TLS
and authenticated HTTP forward proxy; do not gather them anew for each Project.
A missing needed server routes to `kandoo-server`; local-only tasks remain valid.
Record only Project allocations and explicit overrides in Project infrastructure docs.

Inventory services and allocate a unique deployment ID, host loopback ports and volumes
in the shared ledger. Never assume 5432, 6379 or 8000 is free or reuse another Project's
Compose identity. Generate actual Project Compose/configuration when needed. Keep
PostgreSQL/Redis on the participant's VPS and use native OpenSSH local forwarding from
Windows/macOS/Linux; Docker Desktop and WSL are not prerequisites. Preserve volumes,
reuse secrets on resume and test backup/restore. Use isolated test DBs for destructive
checks. No replacement of PostgreSQL with SQLite to conceal connectivity failures.

For application containers, DB/cache hosts are service names inside the Compose network;
laptop processes use allocated forwarded localhost ports; VPS host processes use VPS
loopback ports. Keep schema, migrations, dispatch and API contracts identical while
using runtime-appropriate addresses. Prove authenticated DB access from the actual
runtime. Keep long-running tunnels alive and detect forwarding failure.

For local webhooks use a loopback reverse SSH forwarding endpoint behind the shared
public HTTPS route. Polling is an alternative only if the current platform supports
it. Use one normalized dispatcher, deduplicate updates, and prove a single active
consumer. During production cutover drain local delivery, switch the route to the
production runtime and verify a live round trip and restart. Preserve unrelated sites.

Use the shared forward proxy per process for package/API access when necessary, via
its protected credentials and tunnel; never print credential-bearing environment
variables. Check current official service documentation instead of guessing API behavior.
Project code stays in `projects/ID/`; genuinely shared helpers may be generated in
root `kandoo/`. There are no executable starter assets to copy.
