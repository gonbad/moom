# Runtime identities, PostgreSQL policy and service deployment

Read `docs/kandoo/living/server.md`, `docs/kandoo/living/profile.md` and
`docs/constitution/03-infrastructure-and-secrets.md`. Allocate Project-specific ports,
Compose project name, PostgreSQL/Redis volumes and service users in
`docs/kandoo/living/server.md` without disturbing existing Projects.

## Coherent database route

1. **With a configured VPS (standard path):** Run PostgreSQL and Redis on the VPS via
   Docker Compose with persistent volumes and isolated test/production data; laptop
   development uses native OpenSSH local forwarding (`-L`) and optional loopback reverse
   forwarding (`-R`) behind Caddy for webhooks.
2. **Deferred server on macOS or Linux:** Run isolated PostgreSQL/Redis locally via
   Docker when available, or mark live VPS persistence checks pending until configured
   via `/kandoo-server`.
3. **Last resort—no server AND Windows (`job-plan` only):** Only when `server.md` is
   `none`/deferred **and** the participant is on Windows, `/job-plan` may offer
   project-scoped SQLite under `projects/ID/data/` as an explicit last-resort local
   fallback, recording that PostgreSQL migration and live VPS verification remain
   pending; never substitute SQLite on a production VPS.

Deploy the agent worker, owned backends and optional bridges with separate scoped
credentials; the inference worker never receives coding-host or SSH deployment keys.
Read Project secrets from gitignored `docs/projects/ID/secrets/credentials.md` (synced
by the assistant to `projects/ID/.env`, never printed in chat or telemetry). Apply the
configured forward proxy per service when external model or messenger endpoints require
it; if an upstream provider or tunnel is unreachable, preserve local harness verification
and mark live checks blocked/pending honestly.

Before production cutover, back up domain and agent state, drain local consumers, test
migrations, service restart, restored quota/cooldown/pending-proposal state and
rollback, and confirm retries/fallbacks cannot bypass `confirm + hard` gates or repeat
mutations.
