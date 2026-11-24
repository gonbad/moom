---
name: story
description: Outline narrative structure, section headings, evidence sequence and transitions.
---

# /story

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `quality.md`.

Gate: `docs/living/brief.md` exists and has a closed review. Author `docs/living/story.md`:
1. **Narrative Arc & Actor Sequence:** Progression from concrete reader hook/problem
   through worked steps or evidence to actionable takeaway, explicitly preserving who
   performs each step (reader vs assistant vs system).
2. **Ordered Section Hierarchy:** Complete heading sequence (H1, H2, H3), the single
   claim or task of each section, estimated weight, and transition bridges between sections.
   Include explanations and transitions that a reader can follow without narration.
3. **Evidence & Example Map:** Map every claim in `brief.md` and creator correction in
   the open version to a specific section, naming the exact source fact, worked example,
   diagram, table or code listing that supports it, and flagging any missing source fact.

Use `docs/versions/VERSION/NN-analysis-story.md` for non-obvious structural
choices, ordering tradeoffs or missing prerequisites. Invite the owner to inspect
`docs/living/story.md` in Obsidian; once review closes, hand off to `/content`.
