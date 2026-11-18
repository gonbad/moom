---
name: new-project
description: Create and select the next independent Project using the installed Job.
---

# /new-project

Read `AGENTS.md`, all of `docs/constitution/`, profile, server, status and the installed
`docs/kandoo/living/job.md`. Resolve paths from the workspace root. Require a configured
Job for a standalone invocation. During Job finalization the caller uses only
“Initialize the dossier” below with the saved reservation. Otherwise continue
the recorded setup step, preserving any new input.

Save the previous Project's current progress. Determine the next unused numeric ID
from **both** `docs/projects/` and `projects/` (including gaps, using maximum + 1),
with a nonempty lowercase ASCII slug derived from the person's request. Never reuse
an ID or overwrite a folder. Surface non-obvious scope/slug choices in the new version's
first numbered round without blocking on a submitted blank. Apply the naming and
material-intake contract in the workflow constitution: use a supplied topic immediately,
otherwise explain the provisional name and revisit it at idea review with the same number.

## Initialize the dossier

Use the already chosen ID (the saved reservation during Job finalization). Select
`docs/kandoo/project-forms/en/` or `fa/` from the saved **document language**.
For another requested language, use the English layout and translate the new
participant-facing pages. The forms stay in this Kandoo for the next Project.

For a fresh Project with verified free paths, create both roots and copy the
selected form tree in one local tool call. Bind `id` and `lang` to the checked ID
and form language. In a configured older Kandoo without a form tree, create the
pages listed below from the installed method. Stop if a root already exists and inspect ownership. On a
verified resume use the reserved roots and copy **only missing files**. Keep any
filled input, notes or edits. Use native directory/copy operations on other shells.

```sh
set -eu
mkdir -p docs/projects projects
mkdir "docs/projects/$id"
mkdir "projects/$id"
cp -R "docs/kandoo/project-forms/$lang/." "docs/projects/$id/"
```

Fill the copied forms in place. Replace their marked fields only in the new
dossier, keeping reusable forms pristine.

- In `versions/0.1/00-idea-input.md` carry forward supplied facts, constraints
  and existing material, preserving confirmed, delegated and unresolved choices.
  In `living/idea.md` summarize only known scope. With no topic, leave the idea
  open for the actual first step. Keep the Project's audience and output language
  open unless supplied. Explain provisional naming where applicable.
- In `living/status.md` fill `{{project_id}}`, `{{job_revision}}`, `{{pipeline}}`,
  `{{first_step}}` and `{{next_action}}` from the selected ID and current installed
  Job. List its full ordered steps with one current step. Record version 0.1, the
  current input path, review state and actual evidence. Fill `{{project_id}}` in
  the idea input's existing-product path too. Use the real host invocation for
  the first step, including restart only for a newly installed Job.
- Fill `{{server_selection}}` in `living/server.md` with `unselected` for a
  hosting-capable Job or `none (local Job)` for a wholly local Job. Keep the
  Project roadmap for deferred ideas. Use `versions/0.1/sources/notes.md` and
  `living/sources.md` for supplied sources. Inventory existing files before asking
  questions and create `projects/ID/existing/` only when needed.

Verify both roots, the current input path and local source pointers. Check the
copied fields are resolved and Project status reflects this Job and the supplied
facts. Return to finalization if called from `/job`.

## Select and hand off

Automatically select this Project in `docs/kandoo/living/status.md` and mirror its
state, recording both the installed Job revision and the active Project's Job revision.
Reuse the known languages and participant Git remote. Do not ask infrastructure questions or create credentials here.
At the Job's declared stage, offer an identified existing target or a new Project-specific
server, plus local deferral. Never infer target selection from another Project, and
never copy its credentials, prompts, contracts, ports or private input.
Assess all four mutable domains and adapt the Job if this real work reveals a useful
improvement.

Invite review/editing of `docs/projects/ID/versions/0.1/00-idea-input.md` in Obsidian
followed by `done` / `نوشتم`, or the actual first Job command when already ready.
Explain the name and source-intake locations before that single next action. The only
file-boundary exceptions are the existing-product/design drop folders. End with the
localized full-pipeline bar and that single next action. No host reload is needed unless
commands changed.
