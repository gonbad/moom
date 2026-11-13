# Bot runtime and webhook cutover

Reuse the shared SSH identity, server/DNS/TLS and authenticated forward proxy from
`docs/kandoo/living/server.md`. Allocate distinct bot identity, Compose project,
PostgreSQL/Redis volumes, public webhook path and loopback ports. Preserve other bots
and sites. Run services on the VPS; laptop processes use native SSH forwarding rather
than requiring Docker Desktop/WSL or substituting SQLite.

Example topology: platform HTTPS → reverse proxy → loopback webhook listener →
normalized dispatcher → business service/PostgreSQL → durable outbound sender.
For local development put the local listener behind a loopback reverse tunnel:

```sh
ssh -N -o ExitOnForwardFailure=yes -R 127.0.0.1:28080:127.0.0.1:8080 project-vps
```

Choose real ports from the ledger. Route the public webhook to that loopback listener
without exposing an unauthenticated tunnel endpoint directly. Keep inbound authentication,
body limits and durable acknowledgment at the transport boundary. Polling is an option
only on a selected platform that supports it; verify its actual API.

At deployment drain/stop the local consumer, start the production runtime, switch the
webhook route or polling ownership, inspect provider status and prove one inbound
message/callback/reply. Test restart while a dialog is in progress, outbox recovery,
DB backup/restore and rollback to the previous app revision. Containers use service DNS,
host processes loopback ports and laptops forwarded ports. Reuse secrets safely and
record pending live checks honestly if the user defers infrastructure.
