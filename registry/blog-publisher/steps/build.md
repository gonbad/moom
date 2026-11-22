---
name: build
description: Assemble and verify the web publication and any intentional materials.
---

# /build

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `distribution.md`, `quality.md`.

Gate: `docs/living/layout.md` and public source under `./` are
ready. Use project-local build helpers when needed. Stage public files strictly from the allowlisted source directory, excluding
inputs, secrets, `docs/` and version history. Unfinished unrelated drafts must never
break a build; a draft preview build remains marked preview-only and undeployable.
An unselected publication target permits local preview. Do not ask for a server here;
record unresolved origin-dependent links and re-verify them after `/deploy` selects
its target. A Project-specific site must have a scoped build, not an accidental copy
of the shared Journal.

Imported materials are local checksum-pinned artifacts; never invoke sibling template
sources, parent maintainer tools or network fetches during a build. Produce compiled web
output and SHA-256 inventories. Check web links, assets, RTL/mobile reading and actual
interactive behavior. Do not create a post ZIP by default. Validate any explicitly
selected downloads as part of the release. Run browser checks
with Project-owned dependencies under `./checks/` when available; if a browser
binary or package download is unavailable, preserve the verified static output,
use the prepared local check fallback and record blocked browser evidence honestly in a
`.md` verification report under `docs/versions/VERSION/`. Never refer the
participant to non-`.md` files outside `docs/`. Route to `/deploy` with separate
technical build, source fidelity and human acceptance states.
