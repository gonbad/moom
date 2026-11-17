---
name: preferences
description: Change shared languages, workspace preferences, Git backup or server settings while preserving Project progress.
---

# /preferences

Read `AGENTS.md`, all of `docs/constitution/`, profile, shared status/server and current
Job. Use workspace-root paths. If initial setup is incomplete, continue its saved
question/check through the retained `/start` entry point; never reset answers or
repeat finalization. In a configured Kandoo, handle the requested settings change
without resetting the active Project. Resolve infrastructure ownership as shared
or the explicitly selected Project before modifying access or routes. Save the active
selection, version, progress and next action before starting, and preserve them throughout.

## Resolve the requested change

Read the current values and the person's request. Apply an explicit change directly
within existing authorization; do not ask the person to repeat it in an answer file.
For an ambiguous request, clarify its scope in chat. Put unresolved non-obvious choices
in the next numbered review under the owner's open version (`docs/kandoo/versions/VERSION/`
for shared changes or `docs/projects/ID/versions/VERSION/` for Project access);
if that version is closed, open the next version for that owner, preserving its closed
records. A shared change does not open a new Project version; a Project access change
does not open a shared version unless shared infrastructure is also affected.
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
not trigger network/server checks. Route method evolution to `/iterate`, a concrete
defect to `/issue`, and publication removal through the maintenance guide.

## Infrastructure, only when affected

Read the existing port/deployment ledger and ignored secret references. Ask only for
missing or changed facts. `none` remains a valid choice for local-only work; do not
remove a live server or its data just because a new Project has no hosting need.
For initial infrastructure, perform the applicable checks in
`docs/constitution/03-infrastructure-and-secrets.md`. For a later change, reuse verified
facts and execute only the affected checks; do not replace keys, reprovision a proxy
or move unrelated services for a domain-only request. The full checklist is:
verify SSH/fingerprint, provision/reuse the dedicated key, inventory services, ask
about a domain, verify/correct its IPv4 DNS or choose a free `nip.io` hostname,
obtain publicly trusted TLS and verify renewal, and provision/reuse the authenticated
HTTP forward proxy with protected ignored credentials and native SSH forwarding.
Check authenticated HTTP/HTTPS downloads, anonymous denial and service restart when
the proxy is needed; record unneeded capabilities separately from failed checks.

Create/preserve the ignored credentials scaffold before asking the person to fill it,
following the infrastructure constitution. A missing or empty local file in a configured
workspace means missing local access, not removal of an existing server. Keep confirmed
choices and delegated recommendations distinct. Do not invent access or verification
evidence. Pending provider/account/DNS work remains explicitly pending.

Record shared non-secret facts/allocations in `docs/kandoo/living/server.md` and
Project-owned facts/allocations in `docs/projects/ID/living/server.md`. Shared
credentials stay in gitignored `docs/kandoo/secrets/credentials.md`; Project-owned
credentials stay in `docs/projects/ID/secrets/credentials.md`, never in chat, question files or non-`.md` files
referred to the participant. Generate root `kandoo/` code/configuration only if useful
for shared repeatable operations. Assess effects on the Job, shared docs/code, active
Project and inert feedback. A Project must explicitly choose its target; a new
Project-specific server never replaces the shared target or another Project's facts.

When replacing a live server, preserve old services/data and verify backups, migration,
routes and rollback before any authorized cutover. Do not redeploy existing Projects
just to finish this command.

For an added domain, record the publication origin and all supported aliases in the
selected target's owning publication/server docs. Verify DNS, the actual public reverse-proxy route,
certificate hostname coverage/renewal and HTTPS pages/assets for every supported name.
A DNS record alone is not completion. Preserve old routes unless removal was requested;
adding an alias does not imply redirecting it. Inspect the actual TLS termination layer
before editing an internal application server. These facts are available for reuse when a future Project explicitly selects this target.

## Save and resume

Record changed values in the profile and owning shared or Project server/publication
docs, with that owner's non-secret decision and verification record. Keep
credentials in ignored Markdown and report pending checks honestly. Assess effects on
the Job, shared docs/code, active Project and inert feedback; a settings change does
not reinstall the template, regenerate the Job or rebuild existing outputs.

Restore the saved Project next action after completed settings work; if an unresolved
settings review/access action remains, identify it alongside the unchanged Project
progress. End with the localized progress block and one concrete next action.
