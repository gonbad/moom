# Public sources, offline packages and detached builds

## Publication contract

Keep an explicit Project-owned public source directory (`src/`, `site/` or an adapted
path) separate from inputs, historical versions, secrets and private editorial notes.
Record source, public URL path, version and release selection in living Markdown.
A new Project is a draft by default and needs no `project.json` to exist or be edited.
A builder can read a small documented release table; it must skip unfinished drafts
and preview one on request without accidentally making it publicly deployable.

Generate helpers only for this Kandoo's actual publication needs. Shared publishing
code belongs in root `kandoo/`; a post-specific renderer or verifier belongs in that
Project. Do not install a workflow engine or fetch the original template at build time.
HTML/CSS/JS assets can be authored independently per post. A static build may minimize
HTML while preserving scripts, code blocks and SVG semantics. Never ship a design CDN
as an offline runtime dependency. Keep fonts/assets and their license notices local.

## Build and archive

1. Build to a staging directory. Validate every public path and reject private files,
   symlinks and traversal before copying. Avoid copying a whole Project root.
2. Check local HTML/CSS/JS references, correct RTL/LTR behavior and every download link.
   Treat a user-clicked external citation differently from a remote runtime asset.
3. Make a standalone post ZIP with its own index and all runtime assets. Adapt links
   to the publication home and online-only downloads for offline use. The ZIP never
   includes itself. Record a file inventory and SHA-256 values.
4. Extract that exact ZIP into a path with spaces; open its index with networking
   disabled. Verify interactions, print and required fonts rather than only ZIP CRCs.
5. After all checks pass replace compiled `dist/` atomically; retain rollback output.
   A deployment uploads only files in the verified release inventory, never source.

## Imported workshop downloads

A publication may distribute a template as editorial material. Import a prebuilt,
reviewed ZIP into the owning Project, record its version/hash/provenance, and commit
it or another durable offline copy. The build reads and verifies this local artifact;
it does not look for sibling source/tool directories, use a template runtime, or
silently fetch a moving branch. Keep compatibility download aliases byte-identical.
A maintainer export happens outside the Journal build. Missing or tampered material
is an actionable build failure, not a reason to reattach the publication to upstream.

## Publication and rollback

Validate the aggregate release and preview-only flag before deployment. Use only the
known authorized origin, service identity and paths. Verify HTTPS entry pages, release
hashes and offline downloads, then preserve an immutable receipt in the current shared
version dossier. Host-specific configuration is recorded in shared living docs; do
not test unrelated private services or require an organizer's network. Never relabel
a preview or a passing local check as a live publication or editorial acceptance.
