---
name: layout
description: Design this post for its content, language and reading modes.
---

# /layout

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `distribution.md`, `quality.md`.

Gate: `docs/living/content.md` exists and open editorial questions are
resolved. Choose a layout suited to this post's format rather than copying every prior
post's theme. Use the real text from `content.md` to design typography, reading density,
diagrams, navigation and narrow-screen behavior. Set language/direction deliberately and
isolate code, paths and identifiers as LTR; preserve accessible labels, focus, contrast,
reduced motion and print behavior. Default to vertical scrolling and self-contained
reading; no global slide keys or scroll interception. Respect focus within widgets.

Record layout decisions and public/private source boundaries in
`docs/living/layout.md`, and generate the public source files under
`./src/` (or declared `site/`) with bundled local fonts/assets and license
notices (no runtime design CDN). Serve a local `http://127.0.0.1` preview if helpful for
visual inspection, and record any layout review notes in `.md` files under
`docs/versions/VERSION/`; never refer the participant to edit or open raw
non-`.md` files outside `docs/`. Record any required external index update in the delivery handoff. Route to `/build`.
