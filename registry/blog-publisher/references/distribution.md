# Publication and offline distribution

Choose the actual output/hosting contract; no fixed JSON or shared theme is required.
Each post owns its design and explicit public source. Keep drafts unpublished by
default; private inputs, version history, secrets and source-only files never enter
public output. Record shared origin, index/discovery policy and deliberate downloads
in shared docs, with Project-specific paths and metadata in its own docs. If a manifest
is useful, generate it with every new Project and verify it rather than assuming one
exists. Keep the index up to date when adding posts; automate discovery if chosen.

Generate an appropriate local build/check mechanism as real code when needed, in the
Project or shared Kandoo domain, not a dependency on an outside starter. Stage builds
before replacing working output, preserve code/pre whitespace when minimizing HTML,
and never silently rewrite JavaScript. Verify local references, CSS/JS dependencies,
images/fonts, interactive states and browser routes. Package each selected artifact
for offline reading, with a verified file/hash inventory and all deliberate downloads.
Test extracted output with networking disabled; compare it to the public-source design.

Deploy only verified public output to the participant's authorized target, inheriting
shared server/proxy facts. No hardcoded organizer servers, unrelated service health
checks or external parent paths are allowed. Preserve earlier posts/releases with a
rollback procedure. Verify live routes, downloads, trusted HTTPS and hashes. Technical
readiness, publication state and human editorial acceptance remain independent.
