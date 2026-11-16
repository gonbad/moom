---
name: kandoo-new-project
description: Create and select the next independent Project using the installed Job.
---

# /kandoo-new-project

Read `AGENTS.md`, all of `docs/constitution/`, profile, server, status and the installed
`docs/kandoo/living/job.md`. Resolve paths from the workspace root. Require a configured
Job; otherwise continue the recorded setup step, preserving any new input.

Save the previous Project's current progress. Determine the next unused numeric ID
from **both** `docs/projects/` and `projects/` (including gaps, using maximum + 1),
with a nonempty lowercase ASCII slug derived from the person's request. Never reuse
an ID or overwrite a folder. Surface non-obvious scope/slug choices in the new version's
first numbered round without blocking on a submitted blank. Apply the naming and
material-intake contract in the workflow constitution: use a supplied topic immediately,
otherwise explain the provisional name and revisit it at idea review with the same number.

Create `docs/projects/ID/living/`, `docs/projects/ID/versions/0.1/` and `projects/ID/`.
Write `docs/projects/ID/versions/0.1/00-idea-input.md` using already supplied facts as
editable input, `docs/projects/ID/living/idea.md` as the current scope summary,
`docs/projects/ID/living/roadmap.md` for deferred Project ideas, and
`docs/projects/ID/living/status.md` with the Project ID, selected version `0.1`,
current Job revision, full ordered pipeline from `docs/kandoo/living/job.md`, one
current first step, remaining/optional states, review status, evidence and next action.
Record `Current input: docs/projects/ID/versions/0.1/00-idea-input.md` in that status.
Create/reuse `docs/projects/ID/versions/0.1/sources/notes.md` and
`docs/projects/ID/living/sources.md` for existing notes, links and source pointers.
Explain these in the idea input together with `projects/ID/existing/` for a supplied
product/binary bundle; create that drop folder when needed. Inventory existing files
before writing or asking questions, and preserve user-created material. Create only
useful Job folders, not an application scaffold.

Automatically select this Project in `docs/kandoo/living/status.md` and mirror its
state, recording both the installed Job revision and the active Project's Job revision.
Reuse the known languages, participant Git remote and shared server/proxy; never copy
another Project's credentials, prompts, contracts, deployment ports or private input.
Assess all four mutable domains and adapt the Job if this real work reveals a useful
improvement.

Invite review/editing of `docs/projects/ID/versions/0.1/00-idea-input.md` in Obsidian
followed by `done` / `نوشتم`, or the actual first `job-*` command when already ready.
Explain the name and source-intake locations before that single next action. The only
file-boundary exceptions are the existing-product/design drop folders. End with the
localized full-pipeline bar and that single next action. No host reload is needed unless
commands changed.
