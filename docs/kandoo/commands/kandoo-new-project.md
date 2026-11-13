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
first numbered round without blocking on a submitted blank.

Create `docs/projects/ID/living/`, `docs/projects/ID/versions/0.1/` and `projects/ID/`.
Write `versions/0.1/00-idea-input.md` using already supplied facts as editable input,
`living/idea.md` as the current summary, and `living/status.md` with the Project ID,
selected version `0.1`, Job revision, full ordered pipeline, one current first step,
remaining/optional states, review status, evidence and next action. Create only useful
input/source folders required by the actual Job, not a prescribed application scaffold.

Automatically select this Project in `docs/kandoo/living/status.md` and mirror its
state. Reuse the known languages, participant Git remote and shared server/proxy; never
copy another Project's credentials, deployment ports or private input. Assess all four
mutable domains and adapt the Job if this real work reveals a useful improvement.

Invite review/editing of the exact idea input followed by `done` / `نوشتم`, or the
actual first `job-*` command when already ready. End with the localized full-pipeline
bar and that single next action. No host reload is needed unless commands changed.
