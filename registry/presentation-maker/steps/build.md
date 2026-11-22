---
name: build
description: Build and verify the selected presentation with local assets.
---

# /build

Read the project constitution and current status. Use the following references from `docs/references/`: `slides.md`, `workflow.md`, `visuals.md`, `quality.md`.

Gate: `docs/living/outline.md` and `design.md` exist with a closed review. Follow `visuals.md` first: prepare one visual at a time,
support external interactive HTML/SVG design, review its states/transitions, then serve
and accept the required asset gallery. Preserve originals and exact SVG/CSS source
identities. Build and compare one representative slide before assembling the full deck;
never redraw an accepted asset. Record reused evidence or no-new-assets conditions.

Generate editable source under `./src/` and deliverable
output under `./dist/` for the chosen format; author genuine layouts and
diagrams rather than forcing every beat into one bullet template. Bundle fonts, media
and licenses locally under `./` with zero runtime CDN dependency. If a font or
package download is blocked, use the configured proxy or a clean local system fallback
font and record the fallback honestly.

For HTML, default to horizontal slides and left/right navigation, then implement
stable slide IDs, keyboard/touch navigation, focus restoration,
overview/deep links and browser history without marking skipped slides visited or
trapping keys inside inputs. Check mixed Persian/LTR text, reduced motion, desktop/mobile
overflow, notes, print/PDF export and network-disabled opening from a path with spaces.
Serve a local `http://127.0.0.1` preview for the speaker and record technical check
results, artifact hashes and review prompts in a `.md` file under
`docs/versions/VERSION/`; never refer the participant to open or edit raw
non-`.md` files outside `docs/`. Keep speaker acceptance pending until given for this
revision, and route to `/deploy`.
