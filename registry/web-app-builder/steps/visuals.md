---
name: visuals
description: Generate external Tailwind design prompt, import the return bundle and formalize design-system.md.
---

# /visuals

Read the project constitution and current status. Use the following references from `docs/references/`: `design.md`, `workflow.md`.

Gate: `docs/living/prd.md`, `data-model.md` and `ux.md` exist with a closed review. Write a ready-to-copy external design prompt into
`docs/versions/VERSION/NN-design-prompt.md` in Obsidian, instructing the
participant to attach `prd.md`, `data-model.md` and `ux.md` in Claude Web Chat or Claude
Design using the strongest suitable model and high-effort mode available to them (never
freezing an obsolete model name, and never sending secrets or personal data):
- Require standard Tailwind CSS utility classes throughout (allowing the standalone
  preview CDN `<script src="https://cdn.tailwindcss.com"></script>` only in these preview
  HTML files for browser inspection).
- Request three distinct directions (A, B, C) of the primary key screen in `ux.md` with
  realistic Persian content and RTL typography, then—after the owner selects or combines
  them in that chat—a complete Markdown design-system text plus 3–5 connected key screens
  as standalone HTML files covering empty, loading, error and validation states.

If external design-chat access is unavailable, fall back to generating three distinct
standalone Tailwind HTML directions locally under `./design/` for the same
owner selection, recording external chat as unavailable.

Specify and import the **return bundle** (external browser chat cannot write local files):
1. Participant pastes the selected standalone HTML/asset files into `./design/`
   (a permitted drop folder outside `docs/`).
2. Participant pastes the returned design-system text and selection rationale into
   `docs/versions/VERSION/NN-design-return.md` in Obsidian (or chat) and says
   `done` / `نوشتم`.
3. The local assistant inspects `./design/`, writes the authoritative
   `docs/living/design-system.md` (hex roles, fonts, type scale, spacing,
   radii, component states), records owner selection acceptance in the version dossier,
   and routes to `/prototype`.
