# Workflow, commands and progress

Read the current profile, Job and status before routing any task. Before setup is
complete use the bootstrap procedure recorded in status. Afterwards resolve the
active Project from status, never from the last opened file or directory listing.
Per-Project `living/status.md` retains its selected version, Job revision, progress,
review state and next action; shared status mirrors the active Project only.

Canonical workspace commands are `docs/kandoo/commands/NAME.md`; canonical Job
commands are `docs/kandoo/living/commands/STEP.md`. Every file begins with YAML
frontmatter containing `name: NAME` and a concise `description`, followed by Markdown.
There is one current Job, so commands have descriptive unprefixed names such as
`idea`, `visuals` and `architecture`. Do not add a framework or Job prefix.
Before creating or renaming a command, read `docs/kandoo/command-names.md`: exclude
the union of all supported hosts' native names, all core workspace names and installed
user/plugin commands. `model`, `plan`, `design` and `settings` are reserved collisions,
not valid Job names. Save any chosen safe mapping in the living Job. All procedure paths mean workspace-root
paths, independent of the host file's directory. Route supporting references through
the installed Job so copying commands does not break relative links.

For every new, renamed or changed command, create directories and copy the exact
canonical bytes to all these locations, even if the person currently uses one host:

| Host | Installed path |
| --- | --- |
| Claude Code | `.claude/commands/NAME.md` |
| OpenCode | `.opencode/commands/NAME.md` |
| Codex | `.agents/skills/NAME/SKILL.md` |
| Antigravity | `.agents/skills/NAME/SKILL.md` (same shared copy) |

The assistant runs native `mkdir` and `cp` or `New-Item` / `Copy-Item` equivalents;
no wrapper generator is needed. For example, from the workspace root:

```sh
mkdir -p .claude/commands .opencode/commands .agents/skills/idea
cp docs/kandoo/living/commands/idea.md .claude/commands/idea.md
cp docs/kandoo/living/commands/idea.md .opencode/commands/idea.md
cp docs/kandoo/living/commands/idea.md .agents/skills/idea/SKILL.md
```

Check equality afterwards; keep already identical files unchanged. Synchronize only
missing or changed owned copies. Remove only owned obsolete command copies on a rename;
preserve unrelated user commands and resolve a collision before overwriting it.
After installing, renaming or deleting commands, instruct the person to **close and
reopen the AI host**. At Job installation show the material locations first so
the participant can save their initial input before the required restart. The `/NAME` notation
labels the workflow commands. Codex CLI uses `$NAME` or its skill picker; Codex desktop
supports slash/dollar selection. Claude Code/OpenCode use `/NAME`. Antigravity selects
or mentions the shared skill (or `/NAME` when exposed by its UI). Give the exact
invocation appropriate to the current host when handing off. Detect it from the session;
never ask the person to commit to one host or install only that host's commands. A
profile's detected-host field is advisory and may be stale. On a host switch, read the
same saved preferences, pending setup question and Project progress without restarting.

During setup, create Project 1 and verify its state before removing registry or any
canonical bootstrap source under `docs/`. Retain the installed bootstrap host copies
as recovery entry points; on a configured workspace they route to saved status without
reading deleted canonical sources or reinstalling a catalog. Ordinary tasks use the
six permanent workspace commands (`new-project`, `switch-project`, `add-idea`,
`iterate`, `issue`, `preferences`) and the current Job step commands.
Never delete the executing host command to clean up setup.

Expand three plain-language path aliases consistently for every active Project:
- **Active artifact root** `projects/ID/`: Project code, frontend/backend apps, build
  outputs, executable service contracts, local data, and pasted `existing/` or `design/`
  bundles.
- **Active document root** `docs/projects/ID/`: `living/` specifications (always
  maintaining `living/idea.md` and `living/status.md`) plus gitignored
  `secrets/credentials.md` when Project credentials are needed.
- **Selected version dossier** `docs/projects/ID/versions/VERSION/`: raw inputs
  (`00-idea-input.md` or `00-iteration-input.md`), numbered question/test/issue rounds,
  and verification or deployment notes.

Never write Project prompts, contracts, secrets or code into unscoped root paths such
as `docs/prompts/`, `docs/contracts/`, `docs/secrets/`, `frontend/` or `backend/`.
IDs are `001-slug`, `002-slug`, ... with a nonempty lowercase ASCII slug; allocate
across both trees and never reuse or overwrite an ID. New Projects automatically become
active. Switching restores the target's own version/progress; do not rebuild or republish.

Record the selected version's **Current input** path in its owning status. First
Projects use `00-idea-input.md`; planned iterations use `00-iteration-input.md`; a new
repair version may use its `NN-issue.md`. Job commands read that recorded input and
the current living summaries, never require a first-version input file in a later
version, and never scan closed versions to find one. Existing versions without this
field resolve it from their selected dossier once and save the path. Follow the affected steps selected for an iteration and assess each downstream
dependency before reusing it. Record `invalidated`, `satisfied by existing evidence`
or `not applicable` with reasons; rebuild only invalidated work. Preserve the full
ordered progress display with reasons for unaffected steps. A method change reports
the changed rule/revision, affected Project(s), invalidated evidence and next action;
it does not imply rebuilding other Projects or erasing their accepted outputs.

Qualify Git prototype and release tags by Project and version (for example
`project/001-demo/prototype/0.1` and `project/001-demo/release/0.1`) and never replace
an existing tag silently. When Git is unavailable or deferred during setup, record an
immutable local snapshot path and SHA-256 identity in the open version dossier and mark
Git tagging deferred rather than blocking the workflow. Run side-by-side comparisons
from separate copies or worktrees on free ports instead of checking out over active work.
For a prototype, record the exact current baseline tag or snapshot path and content
hashes in Project status, with its acceptance evidence. If refinement creates a new
baseline, update that record after acceptance; later comparisons resolve this record
instead of constructing a tag from the Project version or using an earlier baseline.

`add-idea`, `iterate` and `issue` accept conversational intake in
chat and resolve scope across Active Project, Kandoo/Job, or Both (creating linked
items with distinct ownership when Both applies). `add-idea` banks ideas into
`roadmap.md` without changing the active step or implying implementation approval.
`iterate` opens a **planned new version**, preserving the previous version and
output. First version `0.1` runs the full pipeline; later versions run an explicitly
selected affected subset, showing untouched steps as skipped. `issue` diagnoses
a **concrete defect**, preserves reproduction and expected/actual results, resolves its
owner, then fixes and verifies only that scope; a closed version is never edited to
hide a defect. All floating commands apply the four-domain check and certainty protocol.

`preferences` handles shared preferences, Git and explicitly scoped infrastructure using existing
facts and only affected checks. Apply explicit requests directly; unresolved non-obvious
choices use the shared file-review protocol. Preserve the active Project and its
pipeline, and resume its saved action after the settings work.

Give each step a brief, consistent handoff (what changed, what evidence exists, what
remains pending) without repeating long boilerplate on small turns. The final block of
**every assistant reply**, including intermediate replies, is a progress block in the
conversation language from `profile.md`. Translate step labels and state words; do not
mix Persian and English prose. Paths and command identifiers retain their spelling.
Before a language is selected, the first setup question and short bootstrap progress
labels may be bilingual English/Persian. After the answer, use only the chosen language.
Use visual states: ✅ completed, 🔵 current, ⬜ remaining and ⏭️ skipped. Show
all steps once in order; add a short localized waiting/review/skip reason when needed.
Use ordinary Markdown with readable wrapping, not bracketed `[todo]` state words or
a clickable-checkbox dependency. Keep at most one current/next step. Include waiting-for-questions or waiting-for-living-review on the
current step when applicable. At completion mark all finished steps done and show the
terminal state; do not invent a current step.

Bootstrap source: start, Job definition, first Project workflow, using status.
Project source: the ordered `job.md` pipeline plus the active Project's version and
step state, mirrored in shared status (recording the current installed Job revision
separately from an older Project's execution revision). Never hardcode a starter's
pipeline in the bar. For an issue/shared task, identify that active scope alongside the
saved Project bar. The **last line** gives a single concrete next action (an exact `.md`
file inside `docs/` to answer/review, a reply to the single setup chat question,
an unavoidable account/access action, a live `http://` preview URL paired with its `.md`
review file in `docs/`, an exact command, or an initial idea-file handoff with restart and the first command
after saving). Never refer the participant to a non-`.md` file or a file outside `docs/`
(except pasting into `projects/ID/existing/` or `projects/ID/design/`). Do not offer a
menu of next tasks or put any prose after the block.

Before sending **each** reply, including after interruptions and context compaction,
read the saved pipeline/state and check the following mentally: all steps appear once
in order; at most one is current; pending reviews and skips match actual evidence;
all prose labels and state words use the conversation language; one final action ends
the reply. Command names, paths and identifiers alone may keep their original spelling.
Never copy an example's step names as state, omit the block on a short answer, use
bracketed English state words inside a Persian bar, or append offers/sign-offs after the action.
This is an instruction discipline, not a script or host-hook requirement.

English example (use the actual saved steps and state):

> **Progress:** ✅ Idea · 🔵 Plan (waiting for answers) · ⬜ Build
>
> **Next step:** Answer `docs/projects/001-demo/versions/0.1/02-questions.md`, save, then say `done`.

Persian example:

> **پیشرفت:** ✅ ایده · 🔵 برنامه (منتظر پاسخ فایل) · ⬜ ساخت
>
> **گام بعد:** پاسخ‌ها را در فایل مشخص‌شده بنویسید، ذخیره کنید و بگویید «نوشتم».

Completed example:

> **Progress:** ✅ Idea · ✅ Build · ⏭️ Deploy (local delivery) · Complete
>
> **Next step:** Read `docs/projects/001-demo/living/status.md` for the delivery summary.

Review example:

> **پیشرفت:** ✅ ایده · 🔵 ساخت (منتظر بازبینی) · ⬜ تحویل
>
> **گام بعد:** نتیجهٔ بازبینی را در فایل بازبینی مشخص‌شده بنویسید، ذخیره کنید و بگویید «نوشتم».

## Project naming and material intake

Apply this contract both when bootstrap creates Project 1 and for every later Project.
Use a supplied topic/name immediately; accept it alongside a command or in ordinary
conversation. For example: `new-project — an interactive astronomy article`.
If no topic is known, use a provisional slug and explain in the first handoff that
idea review will resolve it. Keep the numeric prefix stable and record the display
title separately. During `/idea`, finalize the Project slug before handing off. If the existing slug is provisional, derive a descriptive ASCII slug from the reviewed title or topic and apply the rename; review only
non-obvious choices in the existing question round. Before renaming, check collisions
across both trees. Update both roots, current input/status, living references and
relevant tools together; preserve submitted records with an old-to-new mapping.
A published URL needs an explicit compatibility decision before a rename changes it.

The idea input must explain where existing work goes. Create or reuse a Markdown
source note under the selected dossier (normally `sources/notes.md`) and an inventory
in `docs/projects/ID/living/sources.md`. Link supplied material there instead of asking
for a duplicate paste. Explain `projects/ID/existing/` for an existing product or
binary bundle; prepare each offered folder before displaying its path. This folder is the permitted participant drop
exception outside `docs/`. Keep raw inputs separate from public source. Inspect the
active document/artifact roots and current dossier before asking editorial questions;
read relevant user-created sources, while unsubmitted review answers remain pending.
The first handoff explains the provisional/final name and source locations, then gives
one exact next action. Do not require another approval just to provide intake folders.

## Read the first Project input

On the first invocation, read the active Project’s recorded input, supplied chat
facts, living idea, source notes/inventory and relevant files in the offered drop
folder. Use the installed Job’s bootstrap for the types of material to expect.
An empty folder, copied prompts, headings, bound paths, a provisional slug or a
starter default supply no premise. If all you find is scaffolding, give the exact
idea page, invite one free-form description and wait. Keep the first step current.
Do not open a numbered questionnaire or recommend creative choices at that point.

When material exists, carry explicit constraints forward and work from it. If an
artifact alone leaves the requested goal ambiguous, ask one focused question about
that artifact. With enough information, begin the first step immediately. Invoking
the command requests reading initial input. It never submits an open numbered
review, delegates unanswered choices or records human acceptance. On later versions
use the recorded current input and existing facts instead of restarting intake.

## Shared maintenance

Use [the maintenance guide](../kandoo/maintenance.md) to route Git remote changes,
languages, domains, method changes and publication removal. `/preferences` handles
preferences, Git and infrastructure; ordinary language is also sufficient.
Shared work preserves the selected Project and its saved pipeline; only affected
checks and artifacts are changed. Previously granted authorization remains valid.

## Setup catalog exception

At the end of `/start`, show the actual available named-starter invocations and the
custom `/create-job` option. This selection menu is required and precedes the progress block;
the single last action asks the person to select one. Other handoffs retain one concrete
next action. Never list planned starters or restore a registry after finalization.
