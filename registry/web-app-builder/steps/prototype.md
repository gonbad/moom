---
name: prototype
description: Convert approved HTML into React with bundled Tailwind, verify HTML-to-React fidelity and freeze the prototype.
---

# /prototype

Read the project constitution and current status. Use the following references from `docs/references/`: `design.md`, `workflow.md`, `quality.md`.

Gate: `docs/living/design-system.md` and approved HTML files in
`./design/` exist with owner selection recorded. Build the interactive frontend
under `./frontend/` on an allocated free local port (`http://127.0.0.1:PORT`):
1. **Direct HTML-to-React Conversion:** Transcribe the exact DOM structure, layout and
   Tailwind utility classes of the approved HTML files in `./design/` into React
   components. Derive any secondary screens in `ux.md` strictly from `design-system.md`
   tokens and shells rather than requiring every screen to be externally generated or
   inventing unrelated layouts.
2. **Locally Bundled Tailwind & Fonts:** Compile Tailwind and required fonts locally inside
   `./frontend/` (`@tailwindcss/vite` or PostCSS), removing the preview CDN
   script so the prototype works identically offline. If package downloads are blocked,
   use the configured proxy or record the dependency block honestly.
3. **Mock API Seam (`./frontend/src/api/`):** Route all screen data through one
   typed mock seam returning realistic synthetic fixtures shaped like `data-model.md`; UI
   components do not scatter raw `fetch` calls.
4. **First Visual Fidelity Gate (HTML vs React):** Compare the authoritative HTML screens
   with the running React prototype at matching desktop/mobile viewports, fonts, synthetic
   data and empty/loading/error/filled states. Record comparison results in
   `docs/versions/VERSION/NN-analysis-prototype.md` and apply owner refinements
   until the owner explicitly accepts the prototype; never refer the participant to edit
   non-`.md` files outside `docs/`.
5. **Freeze Project-Qualified Baseline:** Fold any agreed UX/field refinements back into
   `prd.md`, `data-model.md` and `ux.md`. Freeze the accepted prototype with a
   project-qualified Git tag `project/prototype/VERSION` (never overwriting an existing
   tag silently); if Git was deferred, save an immutable copy under
   `./.snapshots/prototype-VERSION/` with SHA-256 hashes recorded in the version
   dossier and mark Git tagging deferred. Record the exact baseline tag or snapshot path,
   content hashes and acceptance-evidence path in `docs/living/status.md`.
   Stop the dev server and route to `/scenarios`.
