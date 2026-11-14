---
name: kandoo-switch
description: Resume a chosen existing Project with its own version, progress and current Job adaptation.
---

# /kandoo-switch

Read `AGENTS.md`, all of `docs/constitution/`, living profile, shared status/server and
the installed Job. Require configured state. Use workspace-root paths throughout.

Use the requested exact Project ID; if ambiguous, list existing IDs with living titles
and ask one selection question. Never choose whichever directory sorts last. Verify
both the target dossier and artifact directory exist; diagnose a mismatch instead of
creating a new Project to conceal it. Save the former Project's status first.

Read `docs/projects/ID/living/idea.md` and `docs/projects/ID/living/status.md`, then
only its selected open version's inputs and submitted rounds needed for the resumed
step. Restore that Project's version, progress, pending questions/review and next
action into `docs/kandoo/living/status.md`, recording the current installed Job
revision separately from the Job revision under which this Project last ran. Do not
scan historical versions, rebuild outputs, republish or reset progress.

Compare the Project's recorded Job revision with the current `docs/kandoo/living/job.md`.
When the Job has added or changed stages, inspect whether the Project's existing
living docs, version rounds and artifacts already satisfy each stage: record `pending`,
`satisfied by existing evidence` or `not applicable` with concrete reasons in the open
version, and use the file-review protocol for non-obvious choices. Never
retrospectively mark newly added stages human-accepted or automatically rebuild old
posts or applications. Preserve confirmed product decisions and accepted outputs.
Evolving the Job is allowed, but a method change does not authorize a deployment.
Assess the Job, shared docs/code, this Project and append-only feedback as appropriate.

End with the restored Project's localized progress and one exact pending `.md` file
action inside `docs/` or current `job-*` command. Switching alone does not require a
host restart.
