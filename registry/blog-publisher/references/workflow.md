# An authored publication, one Project per post

A post may be an article, handbook, paper, presentation or interactive explanation.
Ask what the reader should understand or do, the evidence available, language, desired
format and delivery route. Preserve the creator's actual actor/action sequence: an
article about what the reader does must not quietly become instructions to an AI.

Expand three Project paths consistently from the workspace root: artifact root
`projects/ID/`, document root `docs/projects/ID/`, and selected version dossier
`docs/projects/ID/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/`; the assistant manages HTML/CSS/JS/ZIP build
files under `projects/ID/` and serves local `http://` previews when needed.

## Authoritative seven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `job-idea` | Selected-version input recorded in `docs/projects/ID/living/status.md` | `docs/projects/ID/living/idea.md`, `roadmap.md` | `workflow.md`, `distribution.md` | Scope, reader problem and source boundaries resolved | `job-brief` |
| `job-brief` | `docs/projects/ID/living/idea.md` | `docs/projects/ID/living/brief.md` | `workflow.md`, `quality.md` | Audience, thesis, angle and constraints resolved | `job-story` |
| `job-story` | `docs/projects/ID/living/brief.md` | `docs/projects/ID/living/story.md` | `workflow.md`, `quality.md` | Ordered section hierarchy, actor sequence and evidence map resolved | `job-content` |
| `job-content` | `docs/projects/ID/living/story.md`, `brief.md`, `idea.md` | `docs/projects/ID/living/content.md` | `workflow.md`, `quality.md` | Complete narrative written with claim-to-source traceability | `job-layout` |
| `job-layout` | `docs/projects/ID/living/content.md` | `docs/projects/ID/living/layout.md`, `projects/ID/src/` | `workflow.md`, `distribution.md`, `quality.md` | Typography, RTL/LTR isolation and layout built on real text | `job-build` |
| `job-build` | `docs/projects/ID/living/layout.md`, `projects/ID/src/` | Compiled output, standalone ZIP, `.md` verification note in version dossier | `workflow.md`, `distribution.md`, `quality.md` | Local build, links, hashes and network-disabled ZIP verified | `job-deploy` |
| `job-deploy` | Verified output and `docs/kandoo/living/server.md` | Delivery summary in `docs/projects/ID/living/status.md` or live receipt | `workflow.md`, `distribution.md`, `infrastructure.md`, `quality.md` | Local delivery recorded or authorized public release verified | Complete |

## Why Idea, Brief, Story and Content stay distinct (mini-example)

- **Idea (`idea.md`):** "Write a short private Persian guide for workshop participants whose server is unavailable, using only this Kandoo's verified local-workflow rules; exclude unverified cloud workarounds."
- **Brief (`brief.md`):** "Reader: non-developer builder on laptop without VPS. Outcome: finish specifications, prototype and offline review cleanly while keeping live server checks marked pending. Tone: calm, practical, zero hype."
- **Story (`story.md`):** "1. Recognize the trap (faking a pass vs freezing everything) → 2. Record `server: none` honestly in setup → 3. Complete local specs and preview → 4. What waits for `/kandoo-server` later, with table mapping each claim to its constitution rule."
- **Content (`content.md`):** The full Persian prose implementing those exact four sections in order, with concrete examples and source traceability.

Keep living summaries in `docs/projects/ID/living/` and raw requests plus numbered
review rounds in `docs/projects/ID/versions/VERSION/`. Specification steps (`idea`,
`brief`, `story`) advance once any open question round is submitted without adding an
extra approval ceremony; editorial narrative acceptance, browser verification and live
deployment remain separate facts. New posts start private/draft and need no machine
manifest or upstream repository.

A shared authored index is its own Project; update it deliberately only when discovery
is in scope. Describe the current installed Job revision separately from the revision
under which an older Project last ran. On a deliberate resume of an older Project,
inspect whether its existing files already satisfy `brief` or `story` and record
`pending`, `satisfied by existing evidence` or `not applicable` with reasons. Never
retrospectively mark new steps accepted or rebuild/republish old posts automatically.
