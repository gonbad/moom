# presentation-maker

Create speaker-led, horizontal presentations with left/right navigation and downloadable offline delivery by default; hosting is optional.

Job revision: 0.5

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea | ایده | [idea](commands/idea.md) | Adapt to actual needs |
| Outline | طرح ارائه | [outline](commands/outline.md) | Adapt to actual needs |
| Build | ساخت | [build](commands/build.md) | Adapt to actual needs |
| Deliver | تحویل | [deploy](commands/deploy.md) | Adapt to actual needs |

For version 0.1 follow the chosen full pipeline. Later versions use only affected
steps and prerequisites, recording skipped steps and reasons. Every command resolves
workspace-root paths, applies file review/certainty, checks the four mutable domains
and ends with dynamic localized progress plus one exact next action.

## References to install and read when relevant

- [workflow](references/workflow.md): Read for state, review and every step handoff.
- [visuals](references/visuals.md): Read for per-visual design, gallery review and exact source reuse.
- [slides](references/slides.md): Read for the chosen presentation format and interactions.
- [quality](references/quality.md): Read when defining acceptance, testing and delivering.

## Retained workshop work

The idea/outline/build/delivery commands retain narrative planning, editable visual
source, interactive navigation, offline exports and speaker review within those steps.
There is no separate review command.

## Default audience and delivery contract

Assume a live speaker supplies part of the explanation. Use horizontal slides with
left/right navigation and speaker notes; deliver a downloadable artifact that works
without the network. Hosting is secondary and explicitly selected. Keep navigation
out of focused inputs/dialogs and verify the actual download. Portrait layouts,
self-guided formats or other delivery modes remain valid explicit overrides.

## Visual and infrastructure handoffs

Outline maps required assets to slide beats. Build starts with per-visual interactive
design and an accepted gallery, then a representative slide, then the whole deck.
Keep the four visible stages; visual preparation is explicit work inside build.
Reuse accepted SVG/CSS exactly and verify source-to-slide fidelity. No server intake
belongs to idea, outline or local build/delivery. Only an explicit hosting choice at
`/deploy` invokes the scoped infrastructure procedure.
