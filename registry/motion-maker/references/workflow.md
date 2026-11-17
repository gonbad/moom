# Motion workflow and state

Resolve the active Project and selected open version from living status. Read its
recorded Current input and submitted rounds, including COMMENT/نظر, before asking
questions. Do not rescan closed versions or require first-version input in an iteration.
All paths are relative to the workspace root. Participant-facing documents are Markdown
inside `docs/`; the assistant creates technical artifacts and serves preview URLs.

## Stage contracts

| Command | Principal input | Output in Project living docs | Artifact / exit evidence |
| --- | --- | --- | --- |
| `idea` | Selected input and supplied sources | `idea.md`, `sources.md`, `roadmap.md` | Audience, purpose, output and factual constraints resolved |
| `outline` | Idea and evidence | `outline.md` | Ordered beats, pacing, visual needs and closing action |
| `story` | Outline | `story.md`, `assets.md`, `caption.md` | Accepted narrative; scene contract and rough spoken/animatic timing |
| `visuals` | Story and asset plan | `visuals.md`, `assets.md` | Per-visual HTML with variants/transitions, exact source identity and explicit acceptance |
| `assets` | Accepted per-visual source | `assets.md` | Local integrated gallery, rig/transition checks and accepted baseline |
| `animate` | Story plus asset baseline | `animation.md` | Representative scene then accepted complete HTML preview with source identity |
| `render` | Accepted preview and explicit render request | `render.md` | Verified silent export or honestly pending/skipped state |
| `dubb` | Script, chosen delivery and reviewed picture | `delivery.md`, `caption.md` | Audio alignment if selected, final review and delivered artifact identity |

Put review instructions and check evidence in the current version dossier, using its
next unused numeric prefix for each question/review/issue round. Link local `http://`
previews from those Markdown files; do not ask the participant to inspect source files
outside the vault. External design output may be dropped into `projects/ID/design/`.
For audio/media supplied later, provide an attachment workflow or an assistant import
from a participant-supplied location; do not invent another required non-vault editing
task. Record the imported identity and provenance in Markdown.

## Iteration and method evolution

`/add-idea` records a future idea without changing the current step. `/iterate` plans
a new version; `/issue` handles an observed defect. A request can address the Project,
the reusable Job, or Both. Honor an explicit scope without re-asking. When a scene
defect exposes a general method gap, propose/apply the authorized method fix and link
its own issue to the Project repair. Keep Project-specific story facts out of the Job.

After a change, record the revised rule, affected outputs, invalidated acceptance and
next action. A story timing change may invalidate scene animation, rendered picture,
subtitles and audio alignment; a caption correction may need no new picture. Walk the
downstream dependency chain and reuse unchanged evidence with reasons. Preserve the
previous accepted release. Do not rebuild other Projects when evolving this Job.

Use short stage handoffs with actual evidence, pending review and one next action.
Maintain Project `living/status.md` and shared active status, distinguishing installed
Job revision from the revision under which a Project ran. Show all ordered localized
steps, at most one current step, and deliberate skipped states. No automatic render,
external publishing, host-session creation or infrastructure provisioning is hidden
in the handoff. Record slow operations by purpose, start/end and result when diagnosing
latency; do not infer network or model causes from wall time alone.
