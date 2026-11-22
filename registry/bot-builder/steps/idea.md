---
name: idea
description: Scope deterministic messenger bot, target platforms, core flow and external services.
---

# /idea

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `intake.md`.

Inspect `./existing/` if the participant pasted an existing codebase (a
permitted drop folder outside `docs/`). Clarify the product's core intent: a
deterministic menu/button/dialog bot on Telegram, Bale or Rubika (not an autonomous
agent loop). Identify actors, target platforms, whether payments are in scope or `not
applicable`, and external dependencies (test/live bot tokens, optional payment gateways
or notification sinks).

Cut version `0.1` to one demonstrable journey and bank secondary commands or future
features in `docs/living/roadmap.md`. Record ranked dependency fallbacks and
non-secret credential variable names in `docs/living/external-services.md`
(instructing the owner to store actual tokens only in gitignored
`docs/secrets/credentials.md`).

Always write and maintain `docs/living/idea.md`—never substitute a
version-only filename. Resolve open questions via
`docs/versions/VERSION/NN-questions.md` in Obsidian; once review closes, hand
off directly to `/prd`.
