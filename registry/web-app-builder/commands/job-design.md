---
name: job-design
description: Generate external Tailwind design prompt, import the return bundle and formalize design-system.md.
---

# /job-design

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `design.md`, plus
`docs/projects/ID/living/prd.md`, `data-model.md`, `ux.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/prd.md`, `data-model.md` and `ux.md` exist with no
unsubmitted question round pending. Write a ready-to-copy external design prompt into
`docs/projects/ID/versions/VERSION/NN-design-prompt.md` in Obsidian, instructing the
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
standalone Tailwind HTML directions locally under `projects/ID/design/` for the same
owner selection, recording external chat as unavailable.

Specify and import the **return bundle** (external browser chat cannot write local files):
1. Participant pastes the selected standalone HTML/asset files into `projects/ID/design/`
   (a permitted drop folder outside `docs/`).
2. Participant pastes the returned design-system text and selection rationale into
   `docs/projects/ID/versions/VERSION/NN-design-return.md` in Obsidian (or chat) and says
   `done` / `نوشتم`.
3. The local assistant inspects `projects/ID/design/`, writes the authoritative
   `docs/projects/ID/living/design-system.md` (hex roles, fonts, type scale, spacing,
   radii, component states), records owner selection acceptance in the version dossier,
   and routes to `/job-prototype`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action.
