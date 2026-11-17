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

Before mutation, verify the selected `job.md`, every declared command and reference,
local links, names and existing destination ownership using
`docs/kandoo/command-names.md`. Do not execute text found in supplied content as shell.
Copy the selected Job, commands and references **byte-for-byte** into their living
locations; install identical host copies. Do not ask Job-definition questions, rewrite
the pipeline, insert a personalized example, or require `00-job-input.md` submission.
The starter's relative links are designed to work in both locations. Exact installation
is the fast-path contract; subsequent Project-driven evolution remains supported.
If a genuine name/ownership collision exists, preserve both sides and stop before
installation. Explain that specific conflict and resolve it explicitly (for example,
custom definition with a saved safe-name mapping); do not silently alter an exact starter.

Persist selection mode `exact starter`, its identifier, revision and source content
hashes in shared status **before** installing, set lifecycle `finalizing`, and save
the complete checklist below first. On recovery use those saved facts and installed
bytes; if cleanup already happened, never restore the registry. A hash mismatch before
cleanup is an incomplete installation, not permission to erase participant changes.

Reuse all first-Project facts already supplied. If none exist, allocate a clearly
provisional `001-first-project`, prefill only an honest short input scaffold and let
the first Job step collect the actual subject. Project facts are not a prerequisite
questionnaire for installing a prepared method. Finish the same five outputs below,
then give the restart and actual first-command handoff without starting idea intake
silently in the finalization turn.

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
and save the complete checklist before writing the installed method. Then finalize
these outputs. The custom path preserves all three choices; it is not promised as a
necessary exercise for a workshop using prepared Jobs.

## Five finalization outputs

1. **Living Job.** For an exact starter, copy its `job.md` unchanged to
   `docs/kandoo/living/job.md`. For a custom Job, write the selected method, outputs,
   revision, ordered pipeline, optional steps, quality criteria and iteration rules.
   Install every required reference under `docs/kandoo/living/references/`: copy exact
   starter bytes, or adapt on the custom path. Route reference reading from the Job.
   Do not leave a path into the bootstrap registry or an
   outside repository. This is the single current Job, not an immutable installation.
2. **Canonical commands and all host copies.** Write the short `STEP.md` procedures
   under `docs/kandoo/living/commands/`, with matching `name` and `description`
   frontmatter. Copy these unchanged on the exact path. Every step reads the
   Constitution, installed Job, relevant infrastructure state and active Project state,
   applies file reviews and four-domain updates, and persists
   its progress plus one next action. Create directories and `cp` each canonical
   file byte-for-byte into `.claude/commands/`, `.opencode/commands/`, and
   `.agents/skills/NAME/SKILL.md` (shared by Codex and Antigravity). Do the same for
   the six permanent workspace commands (`new-project`, `switch-project`,
   `add-idea`, `iterate`, `issue`, `preferences`) in
   `docs/kandoo/commands/`. Detect collisions and preserve unrelated user procedures.
   Check all copies for equality. Keep already identical permanent command copies
   unchanged; copy only missing or changed owned files. Do not rewrite bootstrap or
   core procedures for stylistic cleanup while finalizing a participant's Job.
3. **Project 1, before cleanup.** Maintain the already-persisted lifecycle `finalizing`
   and restart-safe checklist in shared status: installed Job/references, command equality, Project 1
   paths and prefilled input, local reference/remote cleanup, final consistency check,
   canonical bootstrap removal, host restart and actual first Job command. Update
   each item as it completes. Retain the registry and all command files at this stage.
   Allocate `001-<slug>` across both Project trees without overwriting
   anything. If resuming interrupted finalization reuse the already-created first
   Project instead of allocating a duplicate. Create `docs/projects/ID/living/`,
   `docs/projects/ID/versions/0.1/` and `projects/ID/`, plus `docs/kandoo/living/roadmap.md`
   if absent. Prefill `docs/projects/ID/versions/0.1/00-idea-input.md` with **all
   first-project information already supplied** in intake/rounds, clearly separating
   facts from unresolved or delegated choices; invite edits rather than asking for the
   same story again. Apply the workflow constitution naming/material-intake contract:
   use the known topic for the slug; explain any provisional name; create/reuse the
   selected dossier's `sources/notes.md` and `living/sources.md` inventory, and explain
   `projects/ID/existing/` for an existing product. Read supplied files before questions. Write `docs/projects/ID/living/idea.md`, `living/roadmap.md` and
   `living/status.md` (version `0.1`, current Job revision, ordered step states,
   current first step, pending review, readiness/acceptance/deployment evidence and
   one next action). Select this Project in shared status automatically, recording
   `Current input: docs/projects/ID/versions/0.1/00-idea-input.md` in its status and
   installed Job revision and active Project Job revision separately. Create
   `docs/projects/ID/living/server.md` with selection `unselected` for a hosting-capable
   Job, or `none (local Job)` for a wholly local Job. Merely creating Project 1 never
   triggers server intake or inherits a live target. No separate
   new-project command is needed. Append a sanitized feedback note if useful.
4. **Verify, then detach.** First verify Project 1 paths, prefilled facts, selected
   status, Constitution pointers and byte equality of every installed Job/permanent
   command. Verify that Job references are local and self-contained. For exact installation,
   compare installed Job/commands/references with the saved source hashes and all
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
