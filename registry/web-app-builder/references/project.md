# Project ownership and review

Read before the first step and whenever resuming another Project. Run Moom status;
create the first Project with `new SLUG --first` or subsequent Projects with `new SLUG`.
Run the installed Job's `scripts/project.py init` through `moom.py run`; its JSON gives
the absolute paths used below. The assistant runs technical commands, installs tooling,
and uses the selected conversation/document languages. Reuse known profile facts.

| Name | Owner and location |
|---|---|
| `PROJECT` | `projects/ID/` for the selected ID from workspace.json |
| `SOURCE` | `PROJECT/src/`; frontend, backend/app, services and deploy live here |
| `LIVING` | `docs/projects/ID/living/`; current PRD, UX, schema, flows and profile |
| `VERSION` | The selected Project's current version dossier from workspace state |
| `EXISTING` | `PROJECT/existing_product/`; optional initial source/reference assets |
| `DESIGN` | `PROJECT/design/`; original approved external HTML and assets |
| `EVIDENCE` | `PROJECT/evidence/`; screenshots and machine-readable check outcomes |
| `DEPLOY` | `SOURCE/deploy/`; reviewed deployment configuration |

These are resolved directories, not shell variables assumed to exist. All paths in
commands are relative to these roots. Never put product specs in workspace-global
`docs/living/` or reuse another Project's environment. Initialize directories without
overwriting their contents. Before resuming, read the current primary input, approved
living docs, pending reviews and milestones. Check Job adaptation as Moom requires.

The first concept belongs in `VERSION/02-idea-core.md` in V0.1, with an inventory and
hash/commit identity for any existing product. Keep the owner's `01-*.md` input intact.
The first existing-product copy stays under EXISTING; retain its original revision in
Git and record its inventory in that initial dossier. Current summaries may be promoted
to LIVING. Later changes use the active dossier; do not rewrite historical V0.1 inputs.
Code, screenshots, HTML, environments and credentials stay outside the docs vault.

For each specification, show the changed decisions and unresolved choices, then use
Moom's numbered file review protocol when review is needed. The person checks scope,
user behavior, data meaning and proposed tradeoffs, in manageable chunks. Record the
actual artifact with `record STEP --artifact PATH`; record acceptance only with evidence
of approval of that revision. The complete result also needs a final walkthrough.
Readiness, machine tests, source fidelity and human acceptance are distinct.

After adapting the recipe through the first Project, use
`verify-job --smoke scripts/smoke.py`, then `finish-job`. The supplied smoke operation
checks isolated Project initialization, switching/resume and ownership rejection. It
makes no claim about live infrastructure, messenger APIs, models or acceptance.
