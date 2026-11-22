# Public web sources and detached builds

## Publication contract

Keep a Project-owned public source directory (`./src/`, `./site/`
or an adapted path) separate from inputs, version records, secrets and editorial
notes. Record source, public URL path, version and release selection in living Markdown.
A new Project is private by default and needs no machine manifest. Skip incomplete
unselected drafts; an explicit draft preview must remain undeployable.

A blog's default deliverable is a web page that explains itself, uses vertical scrolling
and is shared by URL. Do not create a standalone post ZIP or a download procedure by
default. An explicit request may add one later. Intentional editorial materials, such
as a workshop kit, remain independently selected content.

Keep publishing helpers, renderers and checks in the project. Build without fetching the source template
or reading sibling maintainer tools. Keep source and runtime assets explicit. Bundled
assets and license notices are useful for reliable web delivery; removing article ZIPs
is not a request to introduce external runtime dependencies.

## Build and verify

1. Stage only the declared public source and intentional materials. Reject private
   files, symlinks and traversal before copying; never copy the entire Project root.
2. Verify HTML/CSS/JS references, RTL/mobile reading, actual interactions, the authored
   index and every provided material link. Separate external citations from runtime assets.
3. Record the exact file inventory and SHA-256 values. Static structure checks, browser
   interaction, source fidelity and human acceptance are separate evidence.
4. Replace compiled output only after verification, retaining known rollback output.
   Deployment uploads only the verified release inventory.

## Intentional workshop downloads

A post may distribute a reviewed template or other editorial material. Import it into
the owning Project and record version, checksum and provenance in living Markdown.
Commit the required public artifact or another durable local copy. Ordinary builds
verify and consume that copy without locating the template source or fetching a moving
branch. Retained versioned kits keep their original bytes and checksum pins; only an
explicitly rolling compatibility alias follows the current kit. Missing or tampered
material is an actionable failure, not permission to rebuild it from upstream.

## Publication and rollback

Resolve the explicitly selected publication scope and server target. A shared Journal
uses its authorized shared origin/index and release selection; an independent Project
site uses its own origin and only its verified public inventory. Never deploy the whole
Journal to a new Project-specific server or overwrite the shared origin implicitly.
Use the selected origin and supported aliases, service identity and paths.
Verify public HTTPS pages, assets, release hashes and intentional downloads at every
supported hostname; preserve an immutable receipt in the owning Project dossier.
Record DNS, routing and TLS changes with the selected target's owner. If choosing the
target changes canonical URLs or build selection, rebuild and verify before activation.
Do not treat a preview or
local check as live deployment or human acceptance. An explicit hosting deferral is
valid and retains the working local preview. Unlisting, unpublishing and deleting
source are distinct operations described in the project publication record.
