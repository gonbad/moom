---
name: idea
description: Assess agent suitability, explain cost/security risks, scope core capability and boundaries.
---

# /idea

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `intake.md`.

Inspect `./existing/` if the participant pasted an existing codebase (a
permitted drop folder outside `docs/`). **Suitability Gate:** Explain the tradeoffs of
model-directed tool loops versus a deterministic bot (`bot-builder`) or ordinary web app
(`web-app-builder`): latency, recurring token cost, semantic mistakes and prompt
injection risk. Confirm with the owner via `NN-questions.md` that autonomous tool
selection genuinely adds value here.

Identify the narrow version `0.1` capability, caller personas, channel (messenger, web
or scheduled job), whether payments apply or are `not applicable`, and external systems.
Bank secondary tools and future scope in `docs/living/roadmap.md`.

Always write and maintain `docs/living/idea.md`—never substitute a
version-only filename. Resolve open questions via
`docs/versions/VERSION/NN-questions.md` in Obsidian; once review closes, hand
off directly to `/prd`.
