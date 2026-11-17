# motion-maker

Create a short motion graphic from a scene-by-scene story, reviewed reusable visuals
and an accepted local HTML animation, then render and dub only when requested.

Job revision: 0.1

This is an evolving method, not a fixed visual style or a particular event campaign.
Keep characters, brand, language, aspect ratio, duration and publishing facts in each
Project. SVG is the first attempt for suitable graphic elements; external image
generation and supplied images are supported fallbacks. No server is required.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea and audience | ایده و مخاطب | [idea](commands/idea.md) | Every new Project |
| Narrative outline | طرح روایت | [outline](commands/outline.md) | Before detailed scenes |
| Scene story and timing | داستان و زمان‌بندی صحنه‌ها | [story](commands/story.md) | Before visual production |
| Individual visual design | طراحی تک‌تک عناصر بصری | [visuals](commands/visuals.md) | Review each required visual and its states |
| Asset gallery and transitions | گالری عناصر و گذارها | [assets](commands/assets.md) | Verify the accepted sources together |
| Local animation | ساخت و بازبینی موشن | [animate](commands/animate.md) | Representative scene, then whole HTML preview |
| Silent video render | رندر ویدئوی بی‌صدا | [render](commands/render.md) | Explicit request and accepted preview revision |
| Dubbing and final delivery | صداگذاری و تحویل نهایی | [dubb](commands/dubb.md) | Voiceover when selected; otherwise final silent/local delivery |

The first version follows this pipeline. If only HTML is requested, mark render
skipped and use dubb's final-delivery checks without generating audio. Silent video
needs no TTS; mark voiceover not applicable and still verify final delivery. Later
versions assess affected steps and downstream evidence, rebuilding only invalidated
work. Show the complete ordered pipeline and actual skipped/pending reasons.

## References to install and read when relevant

- [workflow](references/workflow.md): State, stage contracts, iteration and progress.
- [visuals](references/visuals.md): External design, source fidelity, states and gallery.
- [animation](references/animation.md): Scene timing, deterministic preview and export.
- [quality](references/quality.md): Acceptance, regression checks and public delivery.

## Non-negotiable handoffs

The story separates on-screen copy, narration, subtitles and publishing caption.
No design approval is inferred from submitted specification blanks. Review one visual
at a time, then its transitions, then scene composition. Reuse the accepted SVG
geometry, IDs, groups, CSS classes and animation behavior in the full composition.
Do not redraw an approximate character after accepting its prototype.

Rendering is never a side effect of finishing animation. Dubbing defaults to manual
external audio supplied by the participant; paid/API automation requires an explicit
choice. Plan voice timing during story, before picture lock. Public output contains
only audience-relevant accepted content. All fact claims and time-sensitive calls to
action must be checked against the intended publication time.

Participant instructions/reviews live in `docs/`; visual source, code, media and
exports are generated inside `projects/ID/`. The assistant serves local previews and
performs technical work. Source fidelity, functional tests, human acceptance and
delivery each have their own evidence. Do not promise a finished workshop-quality
result until a real representative Project has been rehearsed and accepted.
