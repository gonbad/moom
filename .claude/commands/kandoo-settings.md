---
name: kandoo-settings
description: Change shared languages, workspace preferences, Git backup or server settings while preserving Project progress.
---

# /kandoo-settings

Read `AGENTS.md`, all of `docs/constitution/`, profile, shared status/server and current
Job. Use workspace-root paths. If initial setup is incomplete, continue its saved
question/check through the retained `/moom-start` entry point; never reset answers or
repeat finalization. In a configured Kandoo, handle the requested settings change
independently of the active Project. Save its selection, version, progress and next
action before starting, and preserve them throughout.

## Resolve the requested change

Read the current values and the person's request. Apply an explicit change directly
within existing authorization; do not ask the person to repeat it in an answer file.
For an ambiguous request, clarify its scope in chat. Put unresolved non-obvious choices
in the next numbered review under the shared open `docs/kandoo/versions/VERSION/`;
if that version is closed, open a new shared version without changing Project versions.
Use the usual file submission/certainty rules for that review. Record completed changes
and evidence without inventing a second approval step for routine settings.

| Setting | Action and affected checks |
| --- | --- |
| Conversation language | Update the profile and use it immediately in chat/progress; do not change document language implicitly. |
| Document language | Apply to new and actively maintained docs; preserve submitted historical records and keep command/path identifiers intact. |
| Workspace display name | Update shared display references; do not infer a folder, remote or public URL rename. |
| Git identity or authentication | Inspect effective identity and working access; change only requested/missing local values, never global settings; reuse valid keys/credentials. |
| Git remote | Inspect all fetch/push destinations, ownership and nonempty history; preserve branches, avoid force-push, verify authorized backup/ref and update the profile. |
| Server, DNS, HTTPS or proxy | Follow the affected infrastructure procedure below and retain unrelated services/allocations. |

Detect the current host from the session; it is not a setting that locks the workspace
to a tool. All supported command copies remain installed. A language/name change must
not trigger network/server checks. Route method evolution to `/kandoo-iterate`, a concrete
defect to `/kandoo-issue`, and publication removal through the maintenance guide.

## Infrastructure, only when affected

Read the existing port/deployment ledger and ignored secret references. Ask only for
missing or changed facts. `none` remains a valid choice for local-only work; do not
remove a live server or its data just because a new Project has no hosting need.
For initial infrastructure, perform the complete sequence in
`docs/constitution/03-infrastructure-and-secrets.md`. For a later change, reuse verified
facts and execute only the affected checks; do not replace keys, reprovision a proxy
or move unrelated services for a domain-only request. The full checklist is:
verify SSH/fingerprint, provision/reuse the dedicated key, inventory services, ask
about a domain, verify/correct its IPv4 DNS or choose a free `nip.io` hostname,
obtain publicly trusted TLS and verify renewal, and provision/reuse the authenticated
HTTP forward proxy with protected ignored credentials and native SSH forwarding.
Check authenticated HTTP/HTTPS downloads, anonymous denial and service restart.

Create/preserve the ignored credentials scaffold before asking the person to fill it,
following the infrastructure constitution. A missing or empty local file in a configured
workspace means missing local access, not removal of an existing server. Keep confirmed
choices and delegated recommendations distinct. Do not invent access or verification
evidence. Pending provider/account/DNS work remains explicitly pending.

Record shared non-secret facts and port allocations in `docs/kandoo/living/server.md`;
participant-entered or participant-read credentials stay in gitignored
`docs/kandoo/secrets/credentials.md`, never in chat, question files or non-`.md` files
referred to the participant. Generate root `kandoo/` code/configuration only if useful
for shared repeatable operations. Assess effects on the Job, shared docs/code, active
Project and inert feedback. Individual Projects inherit the shared server and record
only their own allocations or explicit overrides.

When replacing a live server, preserve old services/data and verify backups, migration,
routes and rollback before any authorized cutover. Do not redeploy existing Projects
just to finish this command.

For an added domain, record the publication origin and all supported aliases in the
shared publication/server docs. Verify DNS, the actual public reverse-proxy route,
certificate hostname coverage/renewal and HTTPS pages/assets for every supported name.
A DNS record alone is not completion. Preserve old routes unless removal was requested;
adding an alias does not imply redirecting it. Inspect the actual TLS termination layer
before editing an internal application server. The next Project inherits these facts.

## Save and resume

Record changed values in the shared profile/server/publication docs as applicable,
with the owning shared version's non-secret decision and verification record. Keep
credentials in ignored Markdown and report pending checks honestly. Assess effects on
the Job, shared docs/code, active Project and inert feedback; a settings change does
not reinstall the template, regenerate the Job or rebuild existing outputs.

Restore the saved Project next action after completed settings work; if an unresolved
settings review/access action remains, identify it alongside the unchanged Project
progress. End with the localized progress block and one concrete next action.
