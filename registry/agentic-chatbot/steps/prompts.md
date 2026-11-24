---
name: prompts
description: Author Project-scoped runtime prompts, persona rules and synthetic dialogue examples.
---

# /prompts

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `authority.md`.

Gate: `docs/living/edge-cases.md` exists and has a closed review. Author the reviewed prompt specifications as Markdown inside the Project's
document root `docs/living/prompts/` (never unscoped `docs/prompts/`):
1. **System Prompt (`docs/living/prompts/system.md`):** Role identity, SOP
   enforcement, tool invocation boundaries, `[h_*]` opaque handle rules (never guessing
   or requesting raw vaulted secrets), and untrusted-data boundaries.
2. **Persona & Linguistic Tone (`docs/living/prompts/persona.md`):** Natural,
   clear Persian/chosen language guidelines, conciseness and polite out-of-scope refusals.
3. **Synthetic Dialogue Examples (`docs/living/prompts/examples.md`):**
   Multi-turn examples matching the exact policies chosen in `capabilities.md`:
   - `read` + `none` and `direct` + `none` tool calls.
   - `direct` + `soft` conversational offer, refusal/correction and confirmed execution.
   - `confirm` + `hard` proposal emission (`propose_<action>`) awaiting independent
     out-of-band/UI approval.
   - Refusal of prompt injection and out-of-scope requests.

Invite review or non-obvious question resolution via
`docs/versions/VERSION/NN-analysis-prompts.md` in Obsidian; once review closes, hand
off to `/architecture`.
