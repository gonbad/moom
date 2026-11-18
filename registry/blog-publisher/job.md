# blog-publisher

Publish self-contained articles, guides and papers for independent readers, with online URLs and vertical scrolling by default.

Job revision: 0.7

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea and scope | ایده و دامنه | [idea](commands/idea.md) | Adapt to actual needs |
| Editorial brief | بریف و زاویه دید | [brief](commands/brief.md) | Adapt to actual needs |
| Story structure | ساختار روایت و رئوس | [story](commands/story.md) | Adapt to actual needs |
| Content authoring | نگارش متن و محتوا | [content](commands/content.md) | Adapt to actual needs |
| Layout and styling | صفحه‌آرایی و گرافیک | [layout](commands/layout.md) | Adapt to actual needs |
| Build and verify | ساخت و بررسی | [build](commands/build.md) | Adapt to actual needs |
| Publish | انتشار | [deploy](commands/deploy.md) | Public URL by default; preserve explicit hosting deferral |

For version 0.1 follow the chosen full pipeline. Later versions use only affected
steps and prerequisites, recording skipped steps and reasons. Every command resolves
workspace-root paths, applies file review/certainty, checks the four mutable domains
and ends with dynamic localized progress plus one exact next action.

## References to install and read when relevant

- [workflow](references/workflow.md): Read for state, review and every step handoff.
- [distribution](references/distribution.md): Read for public builds, packaging and publishing.
- [infrastructure](references/infrastructure.md): Read when connecting services or deploying.
- [quality](references/quality.md): Read when defining acceptance, testing and delivering.

## Retained workshop work

The pipeline preserves the unmerged editorial stages: idea and scope in idea;
thesis and angle in brief; narrative progression and section hierarchy in story;
full prose and code listings in content; typography and visual diagrams in layout;
static compilation, link and browser validation in build; and journal
release propagation in deploy.

## Default reader and delivery contract

The page explains its argument without a live speaker. Use complete prose, embedded
explanations and ordinary vertical scrolling; avoid global slide navigation. A public
URL is the primary delivery. New work remains a private draft until publication is
selected and authorized; local preview and deferred hosting are valid during writing.
There is no default article download or ZIP procedure and no routine download question.
Add a downloadable deliverable only when explicitly requested. Intentional attachments
such as workshop kits remain editorial content. Existing hosted decks keep their own
accepted format; future speaker-led decks normally use the presentation starter.
Explicit participant choices may change these defaults per Job or Project.

## Infrastructure intake

`/deploy` owns initial hosting intake. Offer an identified existing publication target,
a new Project-specific server, or local/private deferral, using the infrastructure
Constitution. Drafting and local build need no server. A Project-specific target does
not replace the shared publication origin or move any other Project. Record an explicit
publication scope and corresponding origin before preparing a public release.

Use the [Project intake guide](bootstrap.md) to prepare a new Project and explain where to put its idea and materials.
