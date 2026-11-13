---
name: kandoo-iterate
description: Open a planned new version for the active Project, installed Job or shared Kandoo.
---

# /kandoo-iterate

Read `AGENTS.md`, all of `docs/constitution/`, profile, server, shared status and Job.
Resolve paths from the workspace root; require configured state. This command is for
planned new scope/version work. A concrete defect routes to `kandoo-issue` instead.

Determine the owner from the request and current docs: active Project, Job or shared
Kandoo. Ask one routing question only if still ambiguous. Project versions belong in
`docs/projects/ID/versions/`; Job/shared versions in `docs/kandoo/versions/`. Keep Job
revision and Project/shared version independent; never version every Project when the
method changes. If another version is open, preserve it and resolve whether to finish
or explicitly supersede it before opening a successor.

Allocate the next unused version (normally `0.2`, `0.3`, ...), never overwrite one.
Record a stable summary and output/source snapshot or Git commit for the previous
version without reading unrelated history. Write the new `00-iteration-input.md`
with the supplied goal, retained constraints, change scope and acceptance criteria.
Use numbered question files for choices and non-obvious proposed decisions, preserving
Confirmed versus Delegated certainty on submission.

Assess effects on the four domains. Select only affected Job steps and their
prerequisites for this version; show unaffected steps as skipped with reasons. Do not
rerun the complete first-version intake or discard previous choices. Edit current
living docs and implementations in place while retaining previous version evidence.
For Job changes, update the living method/revision and canonical `job-*` commands,
copy changed commands to every host, and remove only owned obsolete copies. Record
which existing Projects need an adaptation check without rebuilding them.

Persist the owning status, affected scope, review state and single next action. Keep
the active Project selected while working on Job/shared changes. End with the
localized scoped iteration bar and exact input/review/command action. Require host
close/reopen if command discovery changed, with the precise resumed command.
