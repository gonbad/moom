---
name: sops
description: Specify Standard Operating Procedures, stage-by-stage conversational workflows and validation rules.
---

# /sops

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`.

Gate: `docs/living/tools.md` exists and has a closed review. Author `docs/living/sops.md`:
1. **Stage Progression:** For each multi-step capability, define ordered stages
   (discovery → slot collection → parameter validation → policy-gated tool invocation →
   outcome summary).
2. **Information Gathering & Deterministic Validation:** Specify required facts and
   deterministic format/domain checks before any tool call.
3. **Conversational Recovery:** Rules for disambiguating vague requests, handling
   corrections or topic switches, and canceling an in-progress workflow cleanly.

Resolve open questions via `docs/versions/VERSION/NN-questions.md` in
Obsidian; once review closes, hand off to `/data-model`.
