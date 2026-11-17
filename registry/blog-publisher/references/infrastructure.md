# Static publication infrastructure

At `/deploy`, read `docs/projects/ID/living/server.md`, the infrastructure/secrets
Constitution and relevant publication records. If hosting is selected and target is
unselected, offer reuse of an identified existing server, a new Project-specific server,
or local deferral. Reuse settled choices; earlier local stages do not ask about servers.
Shared access facts/credentials remain in Kandoo docs; Project-owned access facts and
credentials remain in that Project's docs. Inventory actual sites/ports before allocation.

Resolve **publication scope** too: participation in a shared Journal uses its existing
origin/index/release rules; an independent Project site uses its own origin and includes
only selected public files. A new Project-specific target cannot silently replace the
shared origin, publish the entire Journal or move other Projects. If the existing build
only supports a combined Journal, keep it private until a scoped build/receipt exists
or the owner explicitly selects the shared publication target. Record origin-dependent
links and re-run build verification if choosing the target changes their values.
Serve only compiled output under a dedicated release directory and service identity.

A typical release tree is `releases/RELEASE_ID/` plus an atomic `current` symlink.
Upload the verified file inventory, compare hashes, switch, then verify public entry
pages/downloads. If activation fails restore the previous link. Keep the existing
reverse proxy routes/TLS config intact and test only this publication's configured
health URL. Do not require another application, organizer-private IP or parent folder.
Use an SSH alias and service paths from living docs or ignored deployment config.

The authenticated forward proxy is for package/API downloads, distinct from the web
reverse proxy. Apply it per process with redacted credentials. Browser tooling belongs
to its owning Project with pinned dependencies and durable evidence. No database or
container is necessary for a static publication unless its actual product needs one.
Never claim deployment from a local dry run; preserve the owner's target authorization.
