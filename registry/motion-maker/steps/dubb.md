---
name: dubb
description: Align selected voiceover and review final motion, captions and delivery.
---

# /dubb

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `animation.md`, `quality.md`.

Read the accepted script, preview/render identity and delivery choice. If voiceover
is selected, provide a ready-to-copy narration/pronunciation/timing brief in the current
Markdown dossier. Default to manual external recording/TTS and import the returned
audio using an attachment or assistant-managed copy. Check real voice timing and
pronunciation; do not claim the TTS service also assembled the video. Automated paid
or API access is optional and requires a deliberate choice and existing authorization.

Align/mux locally and review the actual final file. If timing changes, identify the
affected scenes and invalidate their animation/render/subtitle evidence before a
reviewed replacement. For silent or HTML-only delivery, skip audio with a reason and
perform the same final editorial checks. Inspect caption, subtitles, clean picture,
CTA facts at publication time and final output identity. Resolve placeholders; remove
internal conversation/controls. Record explicit final artifact acceptance, delivery
mode, output hashes and outstanding checks in `docs/living/delivery.md`, with caption copy
in `docs/living/caption.md`. Deliver locally by default; do not upload as a hidden side effect.
Only mark complete when the requested deliverable and required evidence exist.
