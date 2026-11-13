---
name: moom-job
description: Define an adaptable Job from file intake, install commands and detach into an independent Kandoo.
---

# /moom-job

Read `AGENTS.md`, all of `docs/constitution/` and the living profile, server, status
and Job. Use workspace-root paths and the universal review/certainty/progress rules.
If configured, continue the current Job; never repeat setup or restore a catalog.
If finalizing, resume its saved checklist before intake or catalog reading. If start
is pending, preserve intake and resolve or explicitly defer its missing checks; honor
the user's instruction to skip any setup step without claiming it was verified.

## Intake and review

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
submitted blank. Once the specification choices are resolved, finalize these outputs.

## Five finalization outputs

1. **Living Job.** Write `docs/kandoo/living/job.md` with the selected method, outputs,
   revision, ordered pipeline, optional steps, quality criteria and iteration rules.
   Copy/adapt every required reference into `docs/kandoo/living/references/` and route
   its reading from the Job. Do not leave a path into the bootstrap registry or an
   outside repository. This is the single current Job, not an immutable installation.
2. **Canonical commands and all host copies.** Write the short `job-STEP.md` procedures
   under `docs/kandoo/living/commands/`, with matching `name` and `description`
   frontmatter. Every step reads the Constitution, installed Job, shared server and
   active Project state, applies file reviews and four-domain updates, and persists
   its progress plus one next action. Create directories and `cp` each canonical
   file byte-for-byte into `.claude/commands/`, `.opencode/commands/`, and
   `.agents/skills/NAME/SKILL.md` (shared by Codex and Antigravity). Do the same for
   the five permanent `kandoo-*` commands in `docs/kandoo/commands/`. Detect collisions
   and preserve unrelated user procedures. Check all copies for equality.
3. **Project 1, before cleanup.** Persist lifecycle `finalizing` and a restart-safe
   checklist in shared status: installed Job/references, command equality, Project 1
   paths and prefilled input, local reference/remote cleanup, final consistency check,
   canonical bootstrap removal, host restart and actual first Job command. Update
   each item as it completes. Retain the registry and all command files at this stage.
   Allocate `001-<slug>` across both Project trees without overwriting
   anything. If resuming interrupted finalization reuse the already-created first
   Project instead of allocating a duplicate. Create `docs/projects/ID/living/`,
   `docs/projects/ID/versions/0.1/` and `projects/ID/`. Prefill
   `versions/0.1/00-idea-input.md` with **all first-project information already supplied**
   in intake/rounds, clearly separating facts from unresolved or delegated choices;
   invite edits rather than asking for the same story again. Write `living/idea.md`
   and `living/status.md` (version `0.1`, current Job revision, ordered step states,
   current first step, pending review, readiness/acceptance/deployment evidence and
   one next action). Select this Project in shared status automatically. No separate
   new-project command is needed. Append a sanitized feedback note if useful.
4. **Verify, then detach.** First verify Project 1 paths, prefilled facts, selected
   status, Constitution pointers and byte equality of every installed Job/permanent
   command. Verify that Job references are local and self-contained. Rewrite the
   README and living onboarding for this Kandoo. Remove template upstream remotes
   (SSH/HTTPS/fetch/push variants), preserving participant remotes, branches and work;
   pending or user-skipped remote backup is allowed. Keep Git history and license.
   Resolve active upstream paths/URLs and stale references; retain historical inputs
   and answers as records rather than erasing work to pass a scan.
   Only after these checks pass, replace installed `moom-start` and `moom-job` host
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
   Job command (usually `/job-idea`; Codex CLI `$job-idea`, desktop slash/dollar picker;
   Antigravity select/mention the skill). Do not assume hot discovery
   or run the first step silently before the requested restart.

If an interrupted run deleted the registry already, recover from the installed Job
and saved participant docs; never restore or download the template. End every reply
with the dynamic localized bar and one exact next file action or restart/first-command
handoff. After completion it is the Project's Job pipeline, not a bootstrap-only bar.
