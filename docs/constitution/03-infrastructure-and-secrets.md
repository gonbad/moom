# Shared infrastructure and secrets

The assistant runs technical commands on the participant's actual OS. Detect Git,
native OpenSSH and task-specific tools before use; do not assume Bash on Windows.
Use native tools and shell quoting, installing dependencies only as actually needed.
Python, WSL, Docker Desktop and a local database are not universal prerequisites.
Use repository-local Git identity; never change the participant's global identity.

A participant-owned remote is strongly recommended, including without a server. It
can be a fork, another hosted repository or an owned SSH bare repository. Inspect a
clone before changing it; for a ZIP, initialize local Git and identity when available.
Verify ownership and authenticated read/write backup when connected. Never push to the
template upstream, force-push, replace unrelated history or put credentials in URLs.
Read access alone does not prove backup works. Offline or local-only work may proceed
with local commits and remote backup pending. If identity/Git is unavailable or the user
insists on skipping any setup step, record the skipped check and its concrete consequence,
then continue with the work. Never turn a deferred check into a success claim or a
bootstrap deadlock. Preserve existing commits; revisit pending setup when relevant.

Ask about a server during initial setup. If the answer is no, record `none` for server,
DNS, TLS and proxy and continue. Never require a server purchase for local-only work.
When a later Project needs one, use `kandoo-server`. With a server, perform this same
sequence during initial setup and on infrastructure changes:

1. Collect host, actual public IPv4, SSH user/port and initial access method. Have the
   participant record credentials only in gitignored `docs/kandoo/secrets/credentials.md`,
   never in a question file, logs or chat. Verify the
   host fingerprint through trusted provider information; do not disable host checking.
   Prove login, provision a dedicated local SSH key if needed, install only its public
   key, and test unattended login with that identity before retiring initial access.
   Preserve existing authorized keys and access. Retain that key for future operations.
2. Inventory services, firewalls and occupied ports before changing anything. Record
   shared server facts and a port/deployment ledger in `docs/kandoo/living/server.md`.
   Every Project uses distinct deployment IDs, ports and persistent volumes. Project
   docs describe its allocations and only explicit overrides of the shared server.
3. Ask whether the person has a domain. With one, verify the intended A record points
   to the actual IPv4; fix DNS through scoped Cloudflare access or provide exact manual
   type/name/value instructions. Check conflicting AAAA records and propagation.
   Without one, choose a unique `<label>.<server-ip>.nip.io` hostname and verify its
   public resolution; free DNS does not guarantee that certificate issuance succeeds.
4. Obtain publicly trusted TLS using Caddy or a suitable existing server. Preserve
   other sites, allocate required HTTP/HTTPS ports, persist certificate storage and
   verify hostname/chain, HTTP redirect and renewal configuration. Serve a harmless
   readiness response until a Project supplies an application route. Do not replace
   an existing product just to test TLS. Verify from the participant's network too.
   Record the actual URL and test evidence; DNS alone is not HTTPS readiness.
5. Configure an authenticated **HTTP forward proxy** on the server (for example Squid)
   for package and API access as needed from the participant's network. This is
   separate from the HTTPS reverse proxy. Create unique random credentials, protect
   the password file, require authentication before any allow rule and deny anonymous
   access; bound allowed destination ports and deny internal/metadata destinations.
   Prefer binding to loopback and carrying it over native SSH local forwarding so
   proxy credentials are not exposed on a public unencrypted connection. Record the
   local endpoint/tunnel identity, remote listener and credentials in ignored secrets.
   Prove authenticated HTTP and HTTPS CONNECT downloads, anonymous/wrong-password
   denial and service restart. Apply proxy configuration per command/process rather
   than silently changing global networking; redact environment values in evidence.

If a purchased domain, DNS provider or certificate authority cannot be reached, record
the exact pending work, keep unrelated tasks moving and never label a failed check
verified. Do not substitute a self-signed certificate for a public one. Review current
official DNS, TLS and proxy documentation before implementation; do not promise that
a proxy changes provider eligibility or account access.

The same deferral rule applies to server, proxy, DNS and TLS setup: honor an explicit
skip and continue independent local work. Defer only an operation that actually needs
the missing capability; do not claim a public deployment without its real evidence.

Secret files, keys, tokens, account sessions and password-bearing URLs are ignored at
every level using `**/secrets/`, `*.local.md`, `.env*` and key patterns. Apply owner-only
permissions or equivalent Windows ACLs. Participant-entered or participant-read secrets
live in gitignored Markdown files inside `docs/`: `docs/kandoo/secrets/credentials.md`
for shared infrastructure and `docs/projects/ID/secrets/credentials.md` for Project
tokens, test identities and admin access notes (never unscoped `docs/secrets/`). The
assistant generates runtime `.env` or key files inside `projects/ID/` as needed without
referring the participant to non-`.md` files or paths outside `docs/`, and never prints
secret values in chat, question files or logs. Living docs contain non-secret variable
names and safe references to those ignored `docs/.../secrets/credentials.md` files,
never their values. Verify `git check-ignore` and the staged diff before any backup or
export. Protect private keys outside public source; never copy local state into reusable
procedures or feedback.

Shared helpers/configuration may be generated in root `kandoo/` only when needed.
Project deployments and runtime configuration remain under `projects/ID/`. Use the same
DB schema, handlers and contracts in development/production, with runtime-appropriate
addresses. Software Jobs default to PostgreSQL/Redis on the participant's VPS using
Compose (or local Docker on macOS/Linux when server setup is deferred), native SSH
forwarding for local development and reverse SSH for webhooks when supported. Never
offer SQLite on a production server or when PostgreSQL is available; **only when the
participant brought no server (`none`/deferred) AND is on Windows** may `job-plan`
offer project-scoped SQLite (`projects/ID/data/`) as an explicit last-resort local
fallback, recording that PostgreSQL migration and live DB verification remain pending
before any server deployment. When an external dependency fails (design chat, package
download, SSH tunnel, model provider or messenger), preserve local work, state the local
fallback and mark blocked external evidence honestly. Test with isolated synthetic data,
preserve volumes, and document backup/restore. Reuse credentials on resume; changing an
environment file alone does not rotate an existing DB role. Never overwrite another deployment.

For Persian/RTL outputs, set language/direction deliberately, isolate code, paths and
identifiers as LTR, preserve text shaping, and verify desktop/mobile behavior. Keep
conversation and document language choices distinct.
