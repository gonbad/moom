# Workflow, commands and progress

Read the current profile, Job and status before routing any task. Before setup is
complete use the bootstrap procedure recorded in status. Afterwards resolve the
active Project from status, never from the last opened file or directory listing.
Per-Project `living/status.md` retains its selected version, Job revision, progress,
review state and next action; shared status mirrors the active Project only.

Canonical workspace commands are `docs/kandoo/commands/NAME.md`; canonical Job
commands are `docs/kandoo/living/commands/job-STEP.md`. Every file begins with YAML
frontmatter containing `name: NAME` and a concise `description`, followed by Markdown.
There is one current Job, so names are short `job-STEP`, not Job-name-qualified and
never unprefixed names such as `model`. All procedure paths mean workspace-root
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
mkdir -p .claude/commands .opencode/commands .agents/skills/job-idea
cp docs/kandoo/living/commands/job-idea.md .claude/commands/job-idea.md
cp docs/kandoo/living/commands/job-idea.md .opencode/commands/job-idea.md
cp docs/kandoo/living/commands/job-idea.md .agents/skills/job-idea/SKILL.md
```

Check equality afterwards. Remove only owned obsolete command copies on a rename;
preserve unrelated user commands and resolve a collision before overwriting it.
After installing, renaming or deleting commands, instruct the person to **close and
reopen the AI host**. This is mandatory after Job definition. The `/NAME` notation
labels the workflow commands. Codex CLI uses `$NAME` or its skill picker; Codex desktop
supports slash/dollar selection. Claude Code/OpenCode use `/NAME`. Antigravity selects
or mentions the shared skill (or `/NAME` when exposed by its UI). Give the exact
invocation appropriate to the person's host when handing off.

During setup, create Project 1 and verify its state before removing registry or any
canonical bootstrap source under `docs/`. Retain the installed bootstrap host copies
as recovery entry points; on a configured workspace they route to saved status without
reading deleted canonical sources or reinstalling a catalog. Ordinary tasks use the
six `kandoo-*` commands (`kandoo-new-project`, `kandoo-switch`, `kandoo-add-idea`,
`kandoo-iterate`, `kandoo-issue`, `kandoo-server`) and the current `job-*` commands.
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
field resolve it from their selected dossier once and save the path. Follow only the
affected steps selected for an iteration, preserving the current Job's full ordered
progress display with reasons for unaffected steps.

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

`kandoo-add-idea`, `kandoo-iterate` and `kandoo-issue` accept conversational intake in
chat and resolve scope across Active Project, Kandoo/Job, or Both (creating linked
items with distinct ownership when Both applies). `kandoo-add-idea` banks ideas into
`roadmap.md` without changing the active step or implying implementation approval.
`kandoo-iterate` opens a **planned new version**, preserving the previous version and
output. First version `0.1` runs the full pipeline; later versions run an explicitly
selected affected subset, showing untouched steps as skipped. `kandoo-issue` diagnoses
a **concrete defect**, preserves reproduction and expected/actual results, resolves its
owner, then fixes and verifies only that scope; a closed version is never edited to
hide a defect. All floating commands apply the four-domain check and certainty protocol.

Give each step a brief, consistent handoff (what changed, what evidence exists, what
remains pending) without repeating long boilerplate on small turns. The final block of
**every assistant reply**, including intermediate replies, is a progress block in the
conversation language from `profile.md`. Translate step labels and state words; do not
mix Persian and English prose. Paths and command identifiers retain their spelling.
Show all steps in order with done, one current/next, skipped optional/unaffected steps
and remaining states. Include waiting-for-questions or waiting-for-living-review on the
current step when applicable. At completion mark all finished steps done and show the
terminal state; do not invent a current step.

Bootstrap source: start, Job definition, first Project workflow, using status.
Project source: the ordered `job.md` pipeline plus the active Project's version and
step state, mirrored in shared status (recording the current installed Job revision
separately from an older Project's execution revision). Never hardcode a starter's
pipeline in the bar. For an issue/shared task, identify that active scope alongside the
saved Project bar. The **last line** gives a single concrete next action (an exact `.md`
file inside `docs/` to answer/review, a live `http://` preview URL paired with its `.md`
review file in `docs/`, an exact command, or host close/reopen followed by the first
command). Never refer the participant to a non-`.md` file or a file outside `docs/`
(except pasting into `projects/ID/existing/` or `projects/ID/design/`). Do not offer a
menu of next tasks or put any prose after the block.

Before sending **each** reply, including after interruptions and context compaction,
read the saved pipeline/state and check the following mentally: all steps appear once
in order; at most one is current; pending reviews and skips match actual evidence;
all prose labels and state words use the conversation language; one final action ends
the reply. Command names, paths and identifiers alone may keep their original spelling.
Never copy an example's step names as state, omit the block on a short answer, use
`[done]`/`[current]` inside a Persian bar, or append offers/sign-offs after the action.
This is an instruction discipline, not a script or host-hook requirement.

English example:

```text
Progress: [done] Idea · [current: awaiting file answers] Plan · [todo] Build
Next step: Answer docs/projects/001-demo/versions/0.1/01-questions.md, save, then say done.
```

Persian example:

```text
پیشرفت: [انجام شد] ایده · [گام جاری: منتظر پاسخ فایل] برنامه · [مانده] ساخت
گام بعد: پاسخ‌ها را در فایل مشخص‌شده بنویسید، ذخیره کنید و بگویید «نوشتم».
```

English completed example:

```text
Progress: [done] Idea · [done] Build · [skipped: local delivery] Deploy · Complete
Next step: Read docs/projects/001-demo/living/status.md for the delivery summary and preview link.
```

Persian review example (English command identifiers and `docs/` Markdown paths remain unchanged):

```text
پیشرفت: [انجام شد] ایده · [گام جاری: منتظر بازبینی] ساخت · [مانده] تحویل
گام بعد: نتیجهٔ بازبینی را در docs/projects/001-demo/versions/0.1/02-review.md بنویسید، ذخیره کنید و بگویید «نوشتم».
```
