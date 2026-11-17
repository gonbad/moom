# Shared infrastructure and secrets

The assistant runs technical commands on the participant's actual OS. Detect Git,
native OpenSSH and task-specific tools before use; do not assume Bash on Windows.
Use native tools and shell quoting, installing dependencies only as actually needed.
Python, WSL, Docker Desktop and a local database are not universal prerequisites.
Reuse effective Git identity, including inherited settings; write only necessary
overrides locally. Never change the participant's global identity.

A participant-owned remote is strongly recommended, including without a server. It
normally comes from GitHub **Use this template → Create a new repository**, choosing
public or private visibility, then cloning the participant's HTTPS URL. Existing forks,
other hosted repositories and owned SSH bare repositories are valid too. Inspect a
clone before changing it; for a ZIP, initialize local Git when available. Reuse valid
local/inherited `user.name` and `user.email` without another question. Fill missing
fields from trustworthy supplied or authenticated account facts, respecting email
privacy; ask only for a still-unknown field. Authentication does not itself configure
commit identity. Do not infer an author from the remote owner or template history,
and do not create separate identities for individual Projects.

Public HTTPS cloning does not require repository authentication. Private clones and
pushes require supported authentication: reuse a working credential manager, GitHub
CLI with HTTPS/browser login, or existing SSH access. GitHub account passwords cannot
authenticate Git. Check/install the needed tooling and request only unavoidable account
consent; bare Git does not guarantee browser login. Never embed credentials in clone
URLs, copied commands or prompts. Keep working HTTPS access while optional SSH setup
is pending. For GitHub SSH setup, reuse a suitable key or generate one, provide only its
public key in a Markdown note inside `docs/`, guide account installation and verify
access before changing remotes. Keep GitHub and server keys distinct.

Sources: [GitHub templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template),
[authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github),
[credential managers](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git),
[Git name](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git)
and [commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

Verify ownership and authenticated read/write backup when connected. Never push to the
template upstream, force-push, replace unrelated history or put credentials in URLs.
Read access alone does not prove backup works. Offline or local-only work may proceed
with local commits and remote backup pending. If identity/Git is unavailable or the user
insists on skipping any setup step, record the skipped check and its concrete consequence,
then continue with the work. Never turn a deferred check into a success claim or a
bootstrap deadlock. Preserve existing commits; revisit pending setup when relevant.

## Job-owned infrastructure intake

Universal `/start`, `/job` and `/new-project` do not ask about a server, create a
credentials scaffold or provision infrastructure. Each installed Job declares an
intake stage: software Jobs use `/architecture`, the publication Job uses `/deploy`,
and local content Jobs require none. A presentation asks only if hosting is explicitly
selected at delivery. An explicit `/preferences` request can configure access sooner.
Earlier stages may record supplied constraints without starting a server questionnaire.

At the owned stage, read `docs/projects/ID/living/server.md` and shared
`docs/kandoo/living/server.md`. Resolve the Project's target before choosing a database
route, reading credentials or connecting. Reuse an already explicit selection on resume.
If unselected, offer in the Project's current numbered review (unless already answered):

- **Reuse an existing configured server**, naming its non-secret identity and current
  verified/pending capabilities and owner. Read its existing secret reference only
  after selection; do not ask the participant to copy credentials or silently inherit
  another Project's target.
- **Use a new server for this Project.** Record non-secret facts and its ledger in
  `docs/projects/ID/living/server.md`; use the Project's ignored credentials file.
  Keep shared facts and other Projects unchanged. Promoting a target to shared scope
  requires an explicit scope choice; the first Project is not automatically shared.
- **Continue locally / defer hosting.** Record this Project's `none`/deferred choice
  and pending dependent work, leaving every shared/live target intact. Never require
  a server purchase for independent local work.

For reuse discovery, inspect only non-secret current server records, including a
prior Project's `living/server.md`; do not scan its inputs, historical versions or
credentials. Offer identified existing targets with their owner. After explicit
selection, link to that owner's facts, ledger and existing secret reference instead
of copying secrets. A Project-owned target may be reused by another Project only with
that explicit choice; this does not promote it to shared scope or change its routes.
Each consumer records its own allocations, and the target owner's ledger tracks all
consumers so ports/volumes remain unique. Never mutate an owning Project's other work.

Only offer reuse when a real identified target exists. A review's submitted blank may
delegate local deferral or a recommendation, but cannot authorize remote access or
deployment. `unselected` is not `none`; merely finding an empty credential file is not
an answer. Partial/promised access stays pending. Record target identity, ownership
(`shared` or an identified owning Project), secret-reference path, selected delivery mode and actual
verification evidence. Keep setup permission and live deployment permission distinct.

Create or preserve the correctly scoped ignored Markdown file **only when access is
needed and the person is being asked to supply it**: `docs/kandoo/secrets/credentials.md`
for explicit shared scope, or `docs/projects/ID/secrets/credentials.md` for Project scope.
Verify `git check-ignore` when available (otherwise inspect rules and mark verification
pending), apply owner-only permissions/Windows ACLs, and preserve existing content.
Use empty fields in the document language; never put secrets in chat or question rounds:

```markdown
# Selected server access

Enter access details only for the server selected in the owning living server document.
Missing fields mean access is pending. Ask to defer if local work should continue.

- Host / public IPv4:
- SSH user:
- SSH port:
- Initial access method:
- Initial credential or local key reference:
```

A missing local file on a configured checkout means missing local access, not removal
of the server or permission to overwrite a working credential. `/preferences` uses
this same scoped procedure. No participant secret file ships in the pristine template.

## Server verification and later changes

With an explicitly selected newly supplied server, perform this sequence within
existing authorization. Resolve choices in the owning version's file review; do not
re-ask supplied answers. Perform DNS/TLS when a public route is needed and the forward
proxy when needed for access; record not-needed capabilities honestly. Later settings changes reuse
verified facts and execute only affected checks; a domain-only change does not need
new keys, a new proxy or unrelated Project deployment:

1. Collect host, actual public IPv4, SSH user/port and initial access method. Have the
   participant record credentials only in the already-created, gitignored
   shared or Project `docs/.../secrets/credentials.md` selected above,
   never in a question file, logs or chat. Verify the
   host fingerprint through trusted provider information; do not disable host checking.
   Prove login, provision a dedicated local SSH key if needed, install only its public
   key, and test unattended login with that identity before retiring initial access.
   Preserve existing authorized keys and access. Retain that key for future operations.
2. Inventory services, firewalls and occupied ports before changing anything. Record
   facts and a port/deployment ledger in the selected target's owning living server
   document. Every Project uses distinct deployment IDs, ports and persistent volumes.
   For a reused server, link its identity and record this Project's allocations
   in both its own selection record and the target owner's ledger. For a new
   Project-owned server, retain its full facts locally. Inventory the actual host and active local forwarding
   ports; different aliases for one host do not create separate port namespaces.
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
server access, tokens, test identities and admin access notes (never unscoped `docs/secrets/`). The
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
Project explicitly selected no server (`none`/deferred) AND the participant is on Windows** may `architecture`
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
