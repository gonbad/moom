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
five `kandoo-*` commands and the current `job-*` commands. Never delete the executing
host command to clean up setup.

Each Project starts with `living/` and `versions/0.1/00-idea-input.md` under
`docs/projects/ID/`, plus `projects/ID/` for actual artifacts. IDs are `001-slug`,
`002-slug`, ... with a nonempty lowercase ASCII slug; allocate across both trees
and never reuse or overwrite an ID. New Projects automatically become active.
Switching restores the target's own version/progress; do not rebuild or republish.

`kandoo-iterate` opens a **planned new version** for a Project, the Job or shared
Kandoo, preserving the previous version and output. First version `0.1` runs the full
pipeline; later versions run an explicitly selected affected subset, showing untouched
steps as skipped. `kandoo-issue` diagnoses a **concrete defect**, preserves a reproduction
and expected/actual result, resolves its owner, then fixes and verifies only that scope.
An issue may remain in an open version; a closed version is never edited to hide the
defect. Both commands apply the four-domain check and the certainty protocol.

The final block of **every assistant reply**, including intermediate replies, is a
progress block in the conversation language from `profile.md`. Translate step labels
and state words; do not mix Persian and English prose. Paths and command identifiers
retain their spelling. Show all steps in order with done, one current/next, skipped
optional/unaffected steps and remaining states. Include waiting-for-questions or
waiting-for-living-review on the current step when applicable. At completion mark all
finished steps done and show the terminal state; do not invent a current step.

Bootstrap source: start, Job definition, first Project workflow, using status.
Project source: the ordered `job.md` pipeline plus the active Project's version and
step state, mirrored in shared status. Never hardcode a starter's pipeline in the bar.
For an issue/shared task, identify that active scope alongside the saved Project bar.
The **last line** gives a single concrete next action (exact file to answer/review,
exact command, or host close/reopen followed by the first command). Do not offer a
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
Next step: Open projects/001-demo/dist/index.html for the final reading.
```

Persian review example (English command identifiers remain unchanged):

```text
پیشرفت: [انجام شد] ایده · [گام جاری: منتظر بازبینی] ساخت · [مانده] تحویل
گام بعد: فایل projects/001-demo/dist/index.html را بازبینی کنید و نتیجه را بنویسید.
```
