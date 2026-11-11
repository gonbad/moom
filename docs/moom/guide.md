# Moom and a configured Kandoo

Moom is a reusable workspace template; Kandoo is a configured copy. One Job is the
current production method. Each Project is a separate instance; Asal is its deliverable.
The assistant operates tools and documents. No standalone Moom CLI installation is
part of the participant flow.

## Ownership and state

workspace.json is authoritative for selected Project, current Job, independent versions,
pending review rounds and artifact receipts. docs/index.md and Project living status
are generated views. A living explanation can describe the current result or method;
version folders preserve requests, questions and decisions. Neither replaces executable
instructions under .moom/core/ or job/NAME/.

Moom defines four distinct document classes:
1. Constitutions: Inviolable workspace invariants and boundaries. Read at start.
2. Living Docs: Current state of truth (docs/**/living/). Updated in-place with every release.
3. Version Docs: Historical immutable decision records (docs/**/versions/). Governed by the
   Historical Version Isolation Invariant: AI assistants must NEVER inspect historical version
   folders unless explicitly requested by the human creator or working on the active open version.
4. Code-Like Docs: Machine-executable SOPs, Agent Skills, and commands (job/<name>/, .moom/core/),
   kept outside the Obsidian human vault.

Projects keep inputs/, src/ and dist/ beneath projects/ID/. Shared integration and
deployment code belongs under shared/; discuss it under docs/workspace/. Keep shared
account facts under the workspace profile and credentials in ignored local files.

New version discussions use versions/VMAJOR/VMAJOR.MINOR/. A patch is nested
beneath that minor, for example versions/V1/V1.2/V1.2.1/. Review rounds are
001-review.md, 002-review.md, etc. They are not new versions. Job and Project
versions need not match Moom or each other. A draft Job iteration does not immediately
relabel or publish the working recipe.

## Start with real work

moom-start asks for missing conversation/document languages first, then missing
universal facts one at a time. moom-job captures the repeated task and the first actual
input. Read starter descriptions with `python3 moom.py catalog QUERY`, inspect only
relevant recipes, then choose/adapt one or create a new package locally. One Job is
enough; imported examples are inputs, not extra installed Jobs.

The assistant uses these mechanics, adapted to the actual task:

```sh
python3 moom.py install presentation-maker
python3 moom.py new first-deck --first --title "First actual presentation"
python3 moom.py sync
python3 moom.py verify-job --smoke scripts/check.py
python3 moom.py finish-job
```

Installation retains registry/ while the recipe is adapted, references and helpers are
checked, host commands are generated and a representative operation succeeds.
finish-job requires that verified recipe and the first Project. A failed or interrupted
setup keeps the catalog. Repeating install or moom-job resumes the active recipe;
it cannot overwrite learned improvements with the starter. After success, registry/
is removed from the Kandoo. Subsequent Projects use the current Job directly.

A custom Job follows the same flow with `install NAME --source PATH`. Author the
standard package outside registry/, include a license and a reviewed smoke helper,
then copy it into job/NAME/. No matching catalog entry is a normal setup case.

## Improve the current method

Observe the failure, diagnose its owner, fix the result, improve the reusable procedure
or helper when appropriate, verify, and record the Job revision. A project preference
does not become a shared rule automatically. Git history and released versions retain
recovery and attribution; there are no mandatory execution pins or frozen bundles.

`status` reports Projects whose observed Job differs from the current recipe.
When resuming one, inspect changed steps/helpers and adapt only affected state.
Use `adopt-job --note REASON` after that check. Do not automatically rebuild, reopen
all accepted stages, or republish previous outputs. Artifact receipts record which
recipe produced a result without forcing that recipe to execute forever.

Open a Job iteration, refine it, update metadata.version in SKILL.md, verify it and
record it with `job-revision --note REASON`. Project iterations retain a source snapshot
and their earlier review documents. A roadmap entry alone does not authorize work.

## Environment and delivery

The assistant installs needed tooling using existing runtimes, isolated environments
and user-local or portable tools first. Verify a real representative output, fonts or
exports when relevant. Surface only unavoidable OS consent or login interactions;
do not make running terminal commands a normal user task. A host permission setting
does not grant missing operating-system privileges.

Keep functional checks, fidelity to the request and human acceptance separate.
Publication uses the user's authorization for the concrete target. A local ready result
does not imply an accepted or deployed release. Keep completed outputs and ordinary
Git history. Avoid force-pushing or changing remote visibility to fix a failed push.
