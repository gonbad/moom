# An authored publication, one Project per post

A post is normally an article, handbook, paper or interactive explanation that a
reader understands without a speaker. Default to vertical scrolling and an online URL.
Existing or explicitly adapted formats remain valid. No default article ZIP is produced.
Ask what the reader should understand or do, the evidence available, language, desired
format and delivery route. Preserve the creator's actual actor/action sequence: an
article about what the reader does must not quietly become instructions to an AI.

Expand three Project paths consistently from the workspace root: artifact root
`./`, document root `docs/`, and selected version dossier
`docs/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/`; the assistant manages HTML/CSS/JS/ZIP build
files under `./` and serves local `http://` previews when needed.

## Authoritative seven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `idea` | Selected-version input recorded in `docs/living/status.md` | `docs/living/idea.md`, `roadmap.md` | `workflow.md`, `distribution.md` | Scope, reader problem and source boundaries resolved | `brief` |
| `brief` | `docs/living/idea.md` | `docs/living/brief.md` | `workflow.md`, `quality.md` | Audience, thesis, angle and constraints resolved | `story` |
| `story` | `docs/living/brief.md` | `docs/living/story.md` | `workflow.md`, `quality.md` | Ordered section hierarchy, actor sequence and evidence map resolved | `content` |
| `content` | `docs/living/story.md`, `brief.md`, `idea.md` | `docs/living/content.md` | `workflow.md`, `quality.md` | Complete narrative written with claim-to-source traceability | `layout` |
| `layout` | `docs/living/content.md` | `docs/living/layout.md`, `./src/` | `workflow.md`, `distribution.md`, `quality.md` | Typography, RTL/LTR isolation and layout built on real text | `build` |
| `build` | `docs/living/layout.md`, `./src/` | Verified web output, `.md` verification note in version dossier | `workflow.md`, `distribution.md`, `quality.md` | Web build, links, hashes and browser behavior verified | `deploy` |
| `deploy` | Verified output and `docs/living/server.md` | Delivery summary in `docs/living/status.md` or live receipt | `workflow.md`, `distribution.md`, `infrastructure.md`, `quality.md` | Public origin/aliases verified or explicit hosting deferral recorded | Complete |

## Why Idea, Brief, Story and Content stay distinct (mini-example)

- **Idea (`idea.md`):** "Write a short private Persian guide for workshop participants whose server is unavailable, using only this Kandoo's verified local-workflow rules; exclude unverified cloud workarounds."
- **Brief (`brief.md`):** "Reader: non-developer builder on laptop without VPS. Outcome: finish specifications, prototype and offline review cleanly while keeping live server checks marked pending. Tone: calm, practical, zero hype."
- **Story (`story.md`):** "1. Identify the reader's local task → 2. Complete local specs and preview → 3. Record explicit deferral when the Job reaches infrastructure intake → 4. Which delivery checks remain pending, with each claim tied to its constitution rule."
- **Content (`content.md`):** The full Persian prose implementing those exact four sections in order, with concrete examples and source traceability.

Keep living summaries in `docs/living/` and raw requests plus numbered
review rounds in `docs/versions/VERSION/`. Specification steps (`idea`,
`brief`, `story`) advance once review closes without adding an
extra approval ceremony; editorial narrative acceptance, browser verification and live
deployment remain separate facts. New posts start private/draft and need no machine
manifest or upstream repository.

A shared authored index is its own Project; update it deliberately only when discovery
is in scope. Describe the current installed Job revision separately from the revision
under which an older Project last ran. On a deliberate resume of an older Project,
inspect whether its existing files already satisfy `brief` or `story` and record
`pending`, `satisfied by existing evidence` or `not applicable` with reasons. Never
retrospectively mark new steps accepted or rebuild/republish old posts automatically.
