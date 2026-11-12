# Infrastructure, credentials and development parity

Use for each software Project's infra/deploy steps. The assistant performs setup and
keeps long-running tunnels under its process/session management. The person only
handles purchases, login/OS consent that cannot be automated, and product decisions.

## Early server access and ownership

During start, collect missing SERVER_HOST (IP or hostname), SSH_USER, SSH_KEY_PATH,
and the verified server IPv4 address separately from the product idea. Prefer an
unattended key after an initial password login; preserve the same identity in all SSH
and copy commands. Verify the host fingerprint and prove access with that identity.
Detect native OpenSSH on Windows instead of assuming it is installed; provision it
or surface the necessary OS consent. WSL and Docker Desktop are optional. The job
works with native Python/Node on Windows and Docker Compose on the Ubuntu VPS.

Choose a server-wide unique DEPLOYMENT_ID once (workspace plus Project, with a short
random suffix if needed). Record it and reserved ports in LIVING/infrastructure.md;
resume that same deployment, rather than creating a new stack on each run. Inspect
existing server services and port ownership before allocation. Reserve independent
PG_PORT, REDIS_PORT, APP_PORT and, for webhooks, WEBHOOK_REVERSE_PORT. Record separate
LOCAL_PG_PORT, LOCAL_REDIS_PORT and LOCAL_HTTP_PORT on the laptop. Candidate defaults
5432/6379/8000 are usable only if free. A second Project must receive distinct ports,
Compose project identity and volumes. Never stop or replace another Project's stack.

## Compose and secrets

Copy the supplied compose.yaml to DEPLOY and to `/opt/DEPLOYMENT_ID/deploy/` on the
VPS. Install Docker Engine and Compose on the VPS when needed. Generate a high-entropy
DB_PASSWORD before provisioning; a URL-safe hexadecimal secret avoids DSN escaping
ambiguity. Persist it with DB_NAME, DB_USER, the deployment identity and allocated
ports in `DEPLOY/.env.infra`, ignored by Git; transfer this explicitly to the matching
VPS deployment directory. Use owner-only permissions (or equivalent Windows ACLs).
Generate credentials only for a new deployment; reuse the retained values on resume.
Changing an environment file does not rotate an existing PostgreSQL role password;
perform deliberate rotations through the database and update all clients together.
Use a separate, ignored `.env.app` for application/provider tokens. No real secret
belongs in living documents, review packets, logs, prompts or the reusable Job.

The assistant executes argv appropriate to its host shell, for example on the VPS:

```sh
docker compose --project-name DEPLOYMENT_ID --env-file .env.infra -f compose.yaml config --quiet
docker compose --project-name DEPLOYMENT_ID --env-file .env.infra -f compose.yaml up -d --wait
```

Replace the example identifier with the retained value. Supply all required variables
explicitly; empty credentials and missing allocations fail interpolation. Rendered
configuration includes secrets, so do not paste full config into chat. Prove authenticated
PostgreSQL access and a Redis PING. Volumes are project-scoped and retained across
updates; never use `down -v` during deployment. Record backup/restore and migration
procedures before the first production release.

## One native SSH session for local development

The assistant constructs and runs a single SSH argv with the actual values:

```text
ssh -i KEY_PATH -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -N -L LOCAL_PG_PORT:127.0.0.1:PG_PORT -L LOCAL_REDIS_PORT:127.0.0.1:REDIS_PORT USER@HOST
```

For webhook jobs append `-R 127.0.0.1:WEBHOOK_REVERSE_PORT:127.0.0.1:LOCAL_HTTP_PORT`
before USER@HOST. Use an argument list or host-appropriate quoting; Bash `${...}`
examples are not CMD or PowerShell environment syntax. The same OpenSSH flags work
on all three operating systems. Keep the process alive, detect failed forwarding,
and check the actual database/cache/webhook route before claiming connectivity.

The laptop's ignored application environment points to
`postgresql://USER:PASSWORD@127.0.0.1:LOCAL_PG_PORT/DB_NAME` and
`redis://127.0.0.1:LOCAL_REDIS_PORT/0`. Server host processes use the allocated VPS
ports instead. Keep schema, migrations, dispatch logic and API contracts the same;
network addresses differ by runtime. Do not replace PostgreSQL with SQLite. Use a
separate test database/schema on the same server for destructive automated tests;
production data is not a test fixture.

## Application runtime on the VPS

For the default container branch, put the application Dockerfile in DEPLOY with its
build context SOURCE. Write its actual start command and dependencies for this
Project. Merge compose.app.yaml with compose.yaml under the same project identity;
service DNS `postgres:5432` and `redis:6379` works inside that network. The container
listens on 0.0.0.0:8000 and publishes only to the allocated host loopback APP_PORT.
Do not pass laptop/host localhost URLs into this container. Use authenticated queries
from the running application container to prove DB/cache connectivity.

For a host systemd/venv branch, use 127.0.0.1:PG_PORT and 127.0.0.1:REDIS_PORT with
the same database schema. Verify startup/restart under the actual service identity.
Choose either branch explicitly in infrastructure.md; never infer connectivity from a
container simply being running. Other server arrangements are allowed if these
boundaries and checks still hold.

## Domains, HTTPS and webhook handoff

Web apps use the participant's domain. Resolve SERVER_HOST to the actual IPv4 before
creating an A record. Cloudflare is optional and limited to DNS record provisioning;
otherwise provide the exact name/type/IP for manual DNS entry. Verify public DNS,
including conflicting AAAA records. Cloudflare Tunnel is not part of this workflow.
Bots can use a project-unique `<deployment>.<server-ip>.nip.io` hostname. Confirm its
resolution instead of assuming reachability. Open required HTTP/HTTPS firewall ports.

Use a host Caddy service (or a configured Nginx/Certbot equivalent) to terminate TLS
and proxy to the loopback APP_PORT. Add this site's configuration without overwriting
existing sites. Obtain a publicly trusted certificate, verify hostname and chain, and
verify certificate renewal/persistent certificate storage. Test HTTP redirect, public
HTTPS frontend/API or webhook, and service restart. DNS alone does not complete deploy.
See [Caddy HTTPS](https://caddyserver.com/docs/quick-starts/https) and
[Compose networking](https://docs.docker.com/compose/how-tos/networking/).

For local webhook work, proxy the same public HTTPS route to WEBHOOK_REVERSE_PORT;
the reverse tunnel reaches the laptop's handler. Use an unguessable platform-specific
webhook path and the provider's authenticated webhook mechanism where supported;
redact tokens from HTTP logs. The chosen platform's current authentication/registration
contract must be verified. During production handoff, stop local consumption, drain
updates, repoint that proxy to APP_PORT, and verify deduplication on the unchanged
handler and public URL. Keep unrelated sites running. If reverse forwarding is
unavailable, use the same normalized dispatcher with polling on both environments
where the platform supports it; unregister webhook delivery and prove there is only
one consumer. Never invent polling support for a platform that does not provide it.
