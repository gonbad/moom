# Moom / Kandoo

This is a Moom template until workspace.json selects a Job; a configured copy is a Kandoo.
Read docs/moom/guide.md and docs/moom/review.md. For a named command, read
.moom/core/commands/moom-NAME.md in full. Plain-language requests route the same way.
Use `python3 moom.py status` for actual state. The assistant runs technical commands;
the person does not need to install a Moom CLI. Windows may use `py -3`.

There is exactly one current, evolving Job at job/NAME/. Its instructions, commands,
scripts and assets govern every Project when resumed. Resolve its procedures with
`python3 moom.py procedure STEP`. Check adaptation when the recipe has changed;
record that check with adopt-job. Do not rebuild or republish old outputs automatically.
Job revisions, Project versions, Moom releases and review-round numbers are independent.

Human requests, answers, reviews and living explanations belong in docs/; executable
instructions belong in .moom/core/ or job/; actual artifacts belong in projects/.
Open docs/ as the Obsidian vault. Shared integration code belongs in shared/.

Before creating a question file, resolve its owning entity. If unknown, ask in chat or
through the host question tool. If the owner also cannot locate it, use
docs/workspace/intake/ and route it after diagnosis. Once scoped, use numbered
Markdown rounds under that entity's current version; preserve all submitted answers.
Read version inputs in numeric order, including COMMENT/نظر, with later decisions
overriding earlier ones. Check source fidelity separately from functioning output.
Do not infer acceptance from silence, generated documents or passing tests.

Native wrappers are generated copies. Edit canonical procedures, then sync; preserve
local edits and resolve command collisions. Publication needs the user's authorization.
Do not include credentials, project inputs or local environments in reusable exports.

When developing THIS public template, keep workspace.json pristine and test in temporary
copies. Its development discussions live in the parent Workshop, outside this repository.
Run `python3 -m unittest discover -s tests -v` and `python3 tools/release.py --check`.
