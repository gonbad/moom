# Start or resume a Moom workspace

Read AGENTS.md, docs/moom/guide.md, docs/moom/review.md and current status.
If language preferences are unknown, ask the conversation/document language pair
first. Collect other missing universal facts one question at a time in chat, reusing
known facts. Save them under profile in workspace.json. Do not ask for accounts or a
server until the task actually needs them. Keep secrets in ignored local files.

The assistant checks Python 3.10+, writable files and Git identity/context, provisions
tools where possible, and explains opening docs/ in Obsidian. Respect an existing
parent repository and authorization; do not change remotes or visibility implicitly.
Commands are already compiled. A greeting does not require installing a package.

If a Job exists, resume selected work. Otherwise use moom-job with the real repeated
task and first input. Report actual selection, review/stage and next useful action.
