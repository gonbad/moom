# Bot runtime, PostgreSQL policy and webhook cutover

Read `docs/kandoo/living/server.md`, `docs/kandoo/living/profile.md` and
`docs/constitution/03-infrastructure-and-secrets.md`. Allocate distinct bot identity,
Compose project name, PostgreSQL/Redis volumes, public webhook path and loopback ports
in `docs/kandoo/living/server.md` without disturbing existing bots or sites.

## Coherent database and transport route

1. **With a configured VPS (standard path):** Run PostgreSQL (and Redis when needed) on
   the VPS via Docker Compose with persistent volumes and isolated test/production data.
   Laptop processes connect over native OpenSSH local forwarding (`-L`), and local
   webhook testing uses a loopback reverse tunnel behind the shared HTTPS proxy:
   ```sh
   ssh -N -o ExitOnForwardFailure=yes -R 127.0.0.1:28080:127.0.0.1:8080 project-vps
   ```
2. **Deferred server on macOS or Linux:** Use local Docker PostgreSQL if available, and
   long-polling on platforms that support it while marking VPS webhook/DB verification
   pending.
3. **Last resort—no server AND Windows (`job-plan` only):** Only when `server.md` is
   `none`/deferred **and** the participant is on Windows, `/job-plan` may offer
   project-scoped SQLite under `projects/ID/data/` as an explicit last-resort local
   fallback, recording that PostgreSQL migration and live VPS verification remain
   pending; never deploy SQLite as a VPS production substitute.

Choose real ports from the shared ledger. Route public webhooks to loopback listeners
with secret-token header verification, body limits and durable deduplication. Polling is
an option only on selected platforms whose official API supports it. Store bot tokens
and merchant keys only in gitignored `docs/projects/ID/secrets/credentials.md` (synced
by the assistant into `projects/ID/.env`, never printed in chat or logs).

At production cutover, drain/stop the local consumer, start the VPS service, switch
webhook route or polling ownership, verify `getWebhookInfo` (or platform equivalent),
and test one inbound message, callback, reply and restart midway through a dialog. If
network, messenger API or SSH access is blocked, preserve local harness verification and
mark live transport checks pending rather than complete.
