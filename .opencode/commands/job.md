---
name: job
description: Install an exact named starter immediately, or define an evolving Job through file intake.
---

# /job [starter-id]

Host argument slot: `$ARGUMENTS` when the host expands it. Otherwise read the actual
invocation/skill request. An unresolved literal `$ARGUMENTS` is not a starter identifier;
use the person's request, with the no-argument path when no identifier was supplied.

Read `AGENTS.md`, all of `docs/constitution/` and the living profile, server, status
and Job. Use workspace-root paths and the universal review/certainty/progress rules.
If configured, continue the current Job; never repeat setup or restore a catalog.
If finalizing, resume its saved checklist before intake or catalog reading. If start
is pending, preserve intake and resolve or explicitly defer its missing checks; honor
the user's instruction to skip any setup step without claiming it was verified.

## Named starter fast path

Inspect lifecycle before interpreting an argument. Configured workspaces always resume
their saved action, even if a starter identifier is supplied. Finalizing workspaces
resume the saved selection/checklist; never switch method mid-finalization or allocate
a second first Project. Resolve or explicitly defer any missing language/Git setup
through `/start`, retaining the supplied starter request. No server question belongs
to either bootstrap command.

An explicit identifier or unambiguous request to install that named starter selects
this path. Accept exactly one identifier matching an immediate local registry entry,
not a path, URL, glob, shell fragment or substring. Reject unknown identifiers and
malformed/extra arguments without changing Job/Project files or lifecycle; list the
actual available choices. Do not silently choose the nearest starter. Distinguish a
free-form custom-method request from a malformed command argument.

Before mutation, check the selected Job, declared steps and references, both
`project-input/{en,fa}.md` pages, the shared Project forms, local links and
destination ownership. Apply `docs/kandoo/command-names.md` to every host.
Check that source command/reference directories contain exactly the declared
regular Markdown files and that both source and destination paths stay inside
the workspace without following symlinks. Allow replacement of the pristine
Job placeholder. Preserve existing intake pages and unrelated host procedures
on a collision and explain what needs resolving. Run file operations locally in the
current session. A named starter needs no Job-definition questions or submission.

**Reserve first.** Use a supplied topic for the slug or the provisional
`001-first-project` when none was given. Check the numeric ID across both Project
trees. Save the reserved ID, selection mode `exact starter`, identifier, revision,
source hashes (including both intake pages), lifecycle `finalizing` and checklist
in shared status together, before installing anything. On resume use that ID, even
if only one Project root exists. Skip verified files, fill missing owned paths,
and preserve unexpected edits for resolution. After cleanup use local installed
bytes and the saved hashes. Never fetch a catalog.

**Batch-copy the method.** On a fresh, preflighted install run this block once from
the workspace root. Bind `starter` to the validated local identifier. Use native
equivalents on other shells. Treat supplied input as data. The loop needs no
sub-agent or separate tool call per file. The installed intake pages stay blank
of participant facts so later Projects can reuse them.

```sh
set -eu
src="registry/$starter"
living=docs/kandoo/living
mkdir -p "$living/commands" "$living/references" .claude/commands .opencode/commands
cp "$src/job.md" "$living/job.md"
cp "$src"/commands/*.md "$living/commands/"
cp "$src"/references/*.md "$living/references/"
cp "$src"/commands/*.md .claude/commands/
cp "$src"/commands/*.md .opencode/commands/
for file in "$src"/commands/*.md; do
    name=${file##*/}
    skill=".agents/skills/${name%.md}"
    mkdir -p "$skill"
    cp "$file" "$skill/SKILL.md"
done
for lang in en fa; do
    cp "$src/project-input/$lang.md" "docs/kandoo/project-forms/$lang/versions/0.1/00-idea-input.md"
done
```

On PowerShell use terminating errors, `New-Item -ItemType Directory -Force` for
directories and `Copy-Item -LiteralPath` for each validated source in one batch.
On recovery compare each fixed destination with its saved source hash first. Copy
only missing owned files (or replace the original verified Job placeholder) and
verify again before advancing its checklist item. If the registry is already
gone, verify installed bytes against the saved hashes and resume local cleanup.

**Create the first Project** using the reserved ID and the “Initialize the dossier”
section of the permanent `docs/kandoo/commands/new-project.md` procedure. Execute
only that section here. Finish verification, detachment and restart below before
the participant's first Job command.

## Custom intake and review (no starter argument)

Invite the person to write or voice-transcribe repeated work and their real first
example in `docs/kandoo/versions/0.1/00-job-input.md`, save it and say `done` / `نوشتم`.
Preserve anything already written. Do not replace intake with a chat questionnaire.
After submission read the intake and current version's numbered rounds in order,
including `COMMENT` / `نظر`, without scanning older versions.

Read `registry/README.md` and relevant candidates. Offer **three equal paths**:
use a fitting starter; use the nearest starter **only as an initial base**, freely
changing style, formats, steps and rules; or author a new Job. Never reject a valid
need because it differs from a starter (portrait slides are a simple example).

Use consecutive numbered question files in the same `0.1` folder for missing choices
and non-obvious AI decisions. Every item has context, concrete options, an explicit
AI Recommendation and a blank answer field. Submitted explicit choices are Confirmed
(`قطعی`); submitted blanks apply the recommendation immediately as Delegated /
Provisional (`پیش‌فرض موقت`). Unsubmitted blanks remain pending. Preserve resolution
evidence and carry confirmed versus delegated choices into living summaries.

Keep the workflow useful for the actual work. Decide deliverables, ordered steps,
translated display labels, optional conditions, quality criteria, first-project facts,
and later-version adaptation. Change the base without friction during definition or
later real Projects. Do not infer human acceptance or external permission from a
submitted blank. Once the specification choices are resolved, validate command names against
`docs/kandoo/command-names.md`, record selection mode `custom`, enter `finalizing`
and save the first Project ID (checked across both trees) and complete checklist
before writing the installed method. Then finalize these outputs.

## Five finalization outputs

1. **Living Job.** Verify the exact path's installed Job and references. For a
   custom Job, write its agreed method, revision, ordered steps, optional conditions
   and quality criteria in `docs/kandoo/living/job.md`. Install its self-contained
   references under `references/`. Prepare reusable intake pages at
   `docs/kandoo/project-forms/{en,fa}/versions/0.1/00-idea-input.md` from the chosen
   starter or the custom method. Keep the real first example in its Project.
2. **Canonical and host commands.** Exact copies are already installed by the batch.
   For a custom Job write the agreed step procedures in `docs/kandoo/living/commands/`
   with matching name/description frontmatter, state reads, reviews, four-domain
   updates and one next action. Copy their bytes to the same three host layouts.
   For both paths compare canonical and host bytes in one batch, including the six
   permanent workspace commands. Repair only missing or changed owned permanent
   copies. Preserve unrelated commands and skip matching copies.
3. **Selected Project 1.** Verify the named install's initialized dossier. For a
   custom Job, use the same “Initialize the dossier” procedure with the reserved
   ID and the agreed method. Preserve prefilled facts, submitted material and edits on
   resume. Shared profile, roadmap, setup history and server documents already live
   in place. Update shared status with the selected Project, version, Job revisions
   and its real next action. Persist each completed phase in the checklist (Job and
   references, command equality, Project paths and input, reference/remote checks,
   recovery copies, registry and canonical bootstrap removal, final check and host
   restart handoff). Keep the registry until the installed method and Project pass
   verification. A sanitized feedback note is optional.
4. **Verify, then detach.** First verify Project 1 paths, prefilled facts, selected
   status, Constitution pointers and byte equality of every installed Job/permanent
   command. Verify that Job references are local and self-contained. For exact installation,
   compare the installed Job, commands, references and reusable intake pages with the saved source hashes and all
   remaining source bytes; recovery after catalog removal uses the saved hashes.
   Verify the saved command list and first action do not depend on registry paths. Rewrite the
   README and living onboarding for this Kandoo, linking `docs/kandoo/maintenance.md`.
   Remove template upstream remotes
   (SSH/HTTPS/fetch/push variants), preserving participant remotes, branches and work;
   pending or user-skipped remote backup is allowed. Keep Git history and license.
   Resolve active template-source/update paths/URLs and stale references; retain
   selected product/API dependency references, which are not template dependencies.
   Retain historical inputs
   and answers as records rather than erasing work to pass a scan.
   Only after these checks pass, replace installed `start` and `job` host
   copies with small, host-only **recovery procedures**, preserving their names and
   frontmatter. Those procedures read `AGENTS.md` and living status directly: configured
   means hand off to its saved next action; finalizing means resume the saved checklist;
   never fetch a template or read a deleted canonical source. Keep these files in
   `.claude/commands/`, `.opencode/commands/` and `.agents/skills/`; do not delete the
   executing command or require its canonical source for recovery.
   As the final cleanup remove `registry/` and the two canonical bootstrap sources
   from `docs/kandoo/commands/`. Record each cleanup independently so interruption
   between them is recoverable. Remove only other owned obsolete bootstrap commands,
   preserving unrelated host commands. Root `kandoo/` is created only for real shared
   code needs. Nothing at runtime reads upstream or feedback as input.
5. **Restart and first step.** Recheck configured paths, command equality (host-only
   recovery copies compare to each other), the saved Project and completed checklist.
   Mark lifecycle `configured`, recording the Job revision and actual evidence;
   preserve backup evidence and pending/skipped checks separately.
   Tell the person to **close and reopen their AI host**, then invoke the actual first
   Job command (usually `/idea`; Codex CLI `$idea`, desktop slash/dollar picker;
   Antigravity select/mention the skill). Do not assume hot discovery
   or run the first step silently before the requested restart.

If an interrupted run deleted the registry already, recover from the installed Job
and saved participant docs; never restore or download the template. End every reply
with the dynamic localized bar and one exact next file action or restart/first-command
handoff. After completion it is the Project's Job pipeline, not a bootstrap-only bar.
