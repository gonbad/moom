# From a real talk to a usable presentation

Start with the actual audience, setting, duration and desired audience action. A deck
for a live speaker, a document read alone and a workshop exercise need different pacing.
Reuse supplied research and the speaker's phrasing; do not convert a request for an
argument into a catalog of definitions.

Expand three Project paths consistently from the workspace root: artifact root
`projects/ID/`, document root `docs/projects/ID/`, and selected version dossier
`docs/projects/ID/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/`; the assistant generates HTML/CSS/JS/PDF
artifacts under `projects/ID/` and serves local `http://` previews when needed.

## Authoritative four-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `job-idea` | Selected-version input recorded in `docs/projects/ID/living/status.md` | `docs/projects/ID/living/idea.md`, `roadmap.md` | `workflow.md`, `slides.md` | Audience, talk promise, format and sources resolved | `job-outline` |
| `job-outline` | `docs/projects/ID/living/idea.md` | `docs/projects/ID/living/outline.md`, `design.md` | `workflow.md`, `slides.md` | Beat sequence, timings, notes and visual system resolved | `job-build` |
| `job-build` | `docs/projects/ID/living/outline.md`, `design.md` | `projects/ID/src/`, `projects/ID/dist/`, `.md` check summary in version dossier | `workflow.md`, `slides.md`, `quality.md` | Local/offline deck built and navigation/typography verified | `job-deploy` |
| `job-deploy` | Verified deck and `docs/kandoo/living/server.md` | Delivery summary in `docs/projects/ID/living/status.md` or live receipt | `workflow.md`, `quality.md` | Speaker review resolved; local delivery or authorized hosting verified | Complete |

## Why Idea and Outline stay distinct (mini-example)

- **Idea (`idea.md`):** "20-minute Persian workshop deck for first-time builders: audience leaves able to separate one reusable Job from independent Projects; 16:9 offline HTML; recurring exam-formatting example."
- **Outline (`outline.md` + `design.md`):** "Section 1 (3 min): teacher rewriting formatting prompts every week → Section 2 (6 min): worked contrast of raw chat vs Kandoo Job → Section 3 (6 min): live exercise splitting Project vs Kandoo scope → Section 4 (5 min): Q&A and takeaway; warm paper palette, Estedad + monospace LTR code blocks."

Specification stages (`idea`, `outline`) advance once any open question round is
submitted without adding an extra approval round; a submitted question file is never
speaker acceptance of the built deck. Record speaker acceptance only for the revision
reviewed. Qualify any Git release tag by Project (`project/ID/release/VERSION`), or
record an immutable local snapshot hash when Git was deferred.

For a later iteration identify whether the request changes the audience, claim,
outline, visual system or export. Rebuild only affected artifacts while checking the
whole navigation sequence, preserving the previous delivered deck and editable source.
A participant may replace slides with a portrait story, print handout or other format;
change the Job, its commands and progress labels to match that real work.
