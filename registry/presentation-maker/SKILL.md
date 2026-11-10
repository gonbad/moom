---
name: presentation-maker
description: Create an offline HTML slide presentation from source material. Use for a bounded presentation project with reviewable outline, content chunks and final delivery.
license: MIT
metadata:
  version: "0.1.0"
  author: gonbad
  origin: https://github.com/gonbad/moom
---

# Presentation maker

Use the actual Project's inputs, audience, intended actions and per-artifact language.
Read [the production sequence](references/workflow.md); open only the current
step's command. The package has no external runtime dependencies beyond Python 3.10+.

Start with [outline](commands/outline.md), then [draft](commands/draft.md), then
[render](commands/render.md). Keep editable slides.json under the actual Project's
src/, and build output under its dist/. The helper scripts/render.py creates a
self-contained HTML deck; scripts/check.py exercises a representative operation.

Apply [the quality criteria](references/quality.md) to small content reviews AND the
whole deck. Distinguish source fidelity, working navigation/rendering and human
acceptance. Real corrections can improve these procedures or helpers; preferences
for one presentation stay with that Project unless deliberately generalized.
