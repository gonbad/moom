---
name: prd
description: Author the product requirement document with detailed user personas and boundaries.
---

# /prd

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`.

Gate: `docs/living/idea.md` exists and has a closed review. Author `docs/living/prd.md`:
1. **User Personas:** For each actor (visitor, customer, administrator, operator), write
   a concrete persona covering context, digital literacy, primary viewport (mobile vs
   desktop), Persian/Latin language habits, what success looks like in two minutes,
   anxieties (payment/privacy trust), and expected tone.
2. **Core Capabilities:** Primary journeys in this version mapped directly to the vertical
   slice in `idea.md`.
3. **Boundaries and Non-Goals:** Explicit exclusions for this version so later design and
   build stages do not drift.

Put open product questions and non-obvious tradeoffs in
`docs/versions/VERSION/NN-questions.md` in Obsidian. Once review closes, record decisions without adding a
duplicate approval round, commit if local Git is active (or record Git deferred), and
hand off to `/data-model`.
