# Public source and release contract

Read this when preparing a new publication or changing its build/deployment.

The workspace has publication.json with an HTTPS origin and one explicit index.
Each Project has project.json, for example:

```json
{"id":"001-example","kind":"post","version":"0.1.0","source":"src","publish":false}
```

Use kind `index` for the root. Posts default to their ID as public_path. `source`
selects only public runtime files and must contain index.html. Never select the Project
root, inputs, history, secrets, or a directory containing private files. A new Project
starts unpublished. Author the index links explicitly; the builder does not invent cards.
If a custom stack needs compilation, declare a reviewed `build_command` argv list;
it runs inside that Project before collecting its explicit public source.

Optional `materials` contains source/target mappings for deliberate public downloads.
Prepare those inputs before building. Optional `archive` and `archive_aliases` name ZIP
filenames under each post's downloads/. Native Project source uses src/; existing posts
may keep site/. No layout driver or shared visual theme is required.

`python3 moom.py run scripts/build.py` creates minimized HTML, per-Project dist/,
standalone offline ZIPs with checksum manifests, and the aggregated workspace dist/.
The build stages and validates a clean release before replacing prior output. HTML
minification preserves whitespace inside code, preformatted text, SVG, and scripts.
JavaScript is not rewritten. The release manifest records every deployed file.

Publish selects production input; it is not evidence of a successful deployment or
human acceptance. `publish:false` excludes drafts. To keep an older release online
while a successor is drafted, `published_snapshot` may identify a prior Project source
snapshot with its own project.json. After opening a successor through moom-iterate,
set publish:false and set published_snapshot to the returned previous source path
relative to the Project before editing the draft. `--preview ID` produces a marked local-only build
that deployment rejects. Browser review must cover source fidelity and interactions.

`python3 moom.py run scripts/check.py` verifies actual output and offline ZIPs. It
checks local references, HTML/CSS runtime dependencies, literal JS dependency calls,
and release/package hashes. Browser checks are still required for dynamically built
URLs and interactions. Missing output fails. `scripts/smoke.py` instead exercises an
isolated build for verify-job; it is never publication acceptance evidence.

For work that will be deployed, gather missing hosting facts during brief/setup,
reusing the known workspace configuration. Verify the intended SSH identity and DNS
control early; do not defer first server onboarding until deploy. Local-only work
needs no server. Hosting credentials and server-specific code belong to the workspace. Configure
`deployment: {"adapter":"shared/deploy.py"}` in publication.json, implement that
adapter for the actual host, and use scripts/deploy.py --dry-run to validate the target.
Deploy only with the user's authorization, then verify public URLs/downloads and hashes.
The reusable package never contains a particular host, account, or credentials.
