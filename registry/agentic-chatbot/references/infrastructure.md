# Runtime identities, PostgreSQL policy and service deployment

Read `docs/constitution/03-infrastructure-and-secrets.md`, the profile, and
`docs/projects/ID/living/server.md`. `/architecture` owns initial intake: offer an
identified existing server, a new Project-specific server or local deferral. Reuse a
saved explicit choice. Resolve shared facts/credentials from `docs/kandoo/living/server.md`
only when the Project selected that target. New Project-server facts and credentials
stay in its own `living/server.md` and ignored `secrets/credentials.md` inside `docs/`.
For an explicitly selected prior Project target, follow the Constitution's reuse
procedure: link its owning facts/secret reference and update only its allocation ledger.
Record unique deployment identity, Compose name, ports, volumes, service user and
public routes in the selected target's ledger and Project architecture. Never replace
the shared target or another Project's access while configuring this one.

## Coherent database route

1. **With a configured VPS (standard path):** Run PostgreSQL and Redis on the VPS via
   Docker Compose with persistent volumes and isolated test/production data; laptop
   development uses native OpenSSH local forwarding (`-L`) and optional loopback reverse
   forwarding (`-R`) behind Caddy for webhooks.
2. **Deferred server on macOS or Linux:** Run isolated PostgreSQL/Redis locally via
   Docker when available, or mark live VPS persistence checks pending until configured
   via `/preferences`.
3. **Last resort—no server AND Windows (`architecture` only):** Only when the Project server selection is
   `none`/deferred **and** the participant is on Windows, `/architecture` may offer
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
