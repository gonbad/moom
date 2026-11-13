---
name: moom-job
description: Define an adaptable Job from file intake, install commands and detach into an independent Kandoo.
---

# /moom-job

Read `AGENTS.md`, all of `docs/constitution/` and the living profile, server, status
and Job. Use workspace-root paths and the universal review/certainty/progress rules.
If configured, continue the current Job; never repeat setup or restore a catalog.
If start is pending, preserve any supplied intake and complete its missing prerequisite.

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
3. **Remove bootstrap and detach completely.** First verify the installed Job,
   commands and references are self-contained; if interrupted, resume from status
   and do not delete the only remaining input. Before removing these instructions,
   persist lifecycle `finalizing` and a restart-safe checklist in shared status:
   installed command equality, remote/reference cleanup, Project 1 paths and prefilled
   input, configured-state verification, host restart and the actual first Job command.
   Use permanent Kandoo names there; update each item as it completes so an interrupted
   session can finish using status without fetching any bootstrap source.
   Then delete `registry/` completely.
   Remove `moom-start` and `moom-job` from all host locations **and** their canonical
   sources in `docs/kandoo/commands/` (read this procedure fully before removing it).
   Remove any old `moom-*` command/update/publish leftovers. Rewrite root `README.md`
   for this Kandoo, its Job, paths and commands. Update status and any retained
   onboarding text to the new identity. Remove all remotes/fetch/push URLs targeting
   `gonbad/moom`, including SSH and HTTPS variants, retaining the verified participant
   remote. A participant fork remains valid even if its repository name contains the
   original template name; use a neutral local remote alias and no upstream dependency.
   Inspect every remaining working file, command name and local path for Moom
   references, stale registry paths, template URLs or relative source dependencies;
   resolve them before declaring detachment. Keep the license and participant inputs,
   answers, decisions and project facts; do not erase work to make a scan pass.
   Git object history is retained, not rewritten. Nothing at runtime reads/fetches
   upstream or uses feedback as input. Root `kandoo/` is created later only if shared
   code is needed; do not create it as a bootstrap scaffold.
4. **Project 1.** Allocate `001-<slug>` across both Project trees without overwriting
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
5. **Restart and first step.** Recheck the participant remote, absence of registry and
   bootstrap commands/references, installed command equality, Constitution pointers,
   Project 1 paths/idea facts and saved status. Mark lifecycle `configured`, record
   the installed Job revision and actual evidence; preserve participant Git backup.
   Tell the person to **close and reopen their AI host**, then invoke the actual first
   Job command (usually `/job-idea`, Codex `$job-idea`). Do not assume hot discovery
   or run the first step silently before the requested restart.

If an interrupted run deleted the registry already, recover from the installed Job
and saved participant docs; never restore or download the template. End every reply
with the dynamic localized bar and one exact next file action or restart/first-command
handoff. After completion it is the Project's Job pipeline, not a bootstrap-only bar.
