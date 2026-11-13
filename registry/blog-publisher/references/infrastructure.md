# Static publication infrastructure

Read shared `docs/kandoo/living/server.md` and the infrastructure/secrets Constitution.
Local-only delivery requires no server. For hosting, reuse verified SSH identity, DNS,
HTTPS and proxy facts; record only this publication's allocations and overrides.
Inventory existing sites first. Use a dedicated release directory and service identity;
serve only compiled public output with a known origin and immutable release receipts.

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
