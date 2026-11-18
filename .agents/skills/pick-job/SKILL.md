---
name: pick-job
description: Install one exact local starter and prepare its first Project.
---

# /pick-job

Read `AGENTS.md`, the four constitutions, living profile, Job and shared status.
Check lifecycle first. If configured, hand off to the saved action. If finalizing,
resume the recorded selection, reserved ID and checklist, even when invoked through
a different entry point. After catalog cleanup recover from installed files and
saved status. If setup is incomplete, retain the request and resolve or explicitly
defer remaining checks through `/start`.

Use the host’s expanded `$ARGUMENTS` or the actual invocation/skill request.
Ignore an unexpanded literal. When neither supplies an identifier, show the
verified local choices using the catalog section of `/start` and wait. Preserve
the current state. An ordinary-language request naming one starter works too.

An explicit identifier or unambiguous request to install that named starter selects
this path. Accept exactly one identifier matching an immediate local registry entry,
not a path, URL, glob, shell fragment or substring. Reject unknown identifiers and
malformed/extra arguments without changing Job/Project files or lifecycle; list the
actual available choices. Do not silently choose the nearest starter. Distinguish a
free-form custom-method request from a malformed command argument.

Before mutation, check the selected Job, its `bootstrap.md`, declared steps and references, both
`project-input/{en,fa}.md` pages, the shared Project forms, local links and
destination ownership. Apply `docs/kandoo/command-names.md` to every host.
Check that source command/reference directories contain exactly the declared
regular Markdown files and that both source and destination paths stay inside
the workspace without following symlinks. Allow replacement of the pristine
Job placeholder. Preserve existing intake pages and unrelated host procedures
on a collision and explain what needs resolving. Run file operations locally in the
current session. A named starter needs no Job-definition questions or submission.

**Reserve first.** Read the selected starter’s `bootstrap.md`. Use a supplied topic for the slug,
otherwise combine the first numeric ID with its provisional slug (e.g. `001-first-film`). Check the numeric ID across both Project
trees. Save the reserved ID, selection mode `exact starter`, identifier, revision,
source hashes (including bootstrap and both intake pages), lifecycle `finalizing` and the checklist from `docs/kandoo/finalize-job.md`
in shared status together, before installing anything. On resume use that ID, even
if only one Project root exists. Skip verified files, fill missing owned paths,
and preserve unexpected edits for resolution. After cleanup use local installed
bytes and the saved hashes. Never fetch a catalog.

**Batch-copy the method.** On a fresh, preflighted install run this block once from
the workspace root. Bind `starter` to the validated local identifier. Use native
equivalents on other shells. Treat supplied input as data. The loop needs no
sub-agent or separate tool call per file. The installed intake pages stay blank
of participant facts so later Projects can reuse them.

```sh
set -eu
src="registry/$starter"
living=docs/kandoo/living
mkdir -p "$living/commands" "$living/references" .claude/commands .opencode/commands
cp "$src/job.md" "$src/bootstrap.md" "$living/"
cp "$src"/commands/*.md "$living/commands/"
cp "$src"/references/*.md "$living/references/"
cp "$src"/commands/*.md .claude/commands/
cp "$src"/commands/*.md .opencode/commands/
for file in "$src"/commands/*.md; do
    name=${file##*/}
    skill=".agents/skills/${name%.md}"
    mkdir -p "$skill"
    cp "$file" "$skill/SKILL.md"
done
for lang in en fa; do
    cp "$src/project-input/$lang.md" "docs/kandoo/project-forms/$lang/versions/0.1/00-idea-input.md"
done
```

On PowerShell use terminating errors, `New-Item -ItemType Directory -Force` for
directories and `Copy-Item -LiteralPath` for each validated source in one batch.
On recovery compare each fixed destination with its saved source hash first. Copy
only missing owned files (or replace the original verified Job placeholder) and
verify again before advancing its checklist item. If the registry is already
gone, verify installed bytes against the saved hashes and resume local cleanup.

Continue with the shared procedure in `docs/kandoo/finalize-job.md`.
