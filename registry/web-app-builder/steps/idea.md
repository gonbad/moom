---
name: idea
description: Scope the product, benchmark competitors, identify unfair advantage and external fallbacks.
---

# /idea

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `intake.md`.

If the participant has an existing codebase, they may paste it into
`./existing/` (one of the permitted non-`docs/` drop folders); inspect models,
schemas, routes and business rules thoroughly before proposing changes. Contrast the
product with 2–3 realistic alternatives (competitors, domestic platforms such as Divar,
Bale or Snapp, or manual Excel/paper habits) and isolate the decisive unfair advantage.

Cut version `0.1` to one demonstrable vertical slice and bank deferred features in
`docs/living/roadmap.md`. For every external service dependency, document a
ranked fallback chain (primary, secondary and zero-dependency local fallback) plus
non-secret credential variable names in `docs/living/external-services.md`
(recording domestic versus foreign network constraints and instructing the owner to
store actual keys only in gitignored `docs/secrets/credentials.md`).

Always write and maintain `docs/living/idea.md` with actors, problem,
differentiator, fallbacks and the `0.1` boundary—never use an alternative version-only
filename instead of `docs/living/idea.md`. Resolve open choices via
`docs/versions/VERSION/NN-questions.md` in Obsidian; once review closes, hand
off directly to `/prd`.
