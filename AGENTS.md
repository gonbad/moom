# Kandoo instructions

Before any task, read all four documents in `docs/constitution/`, then
`docs/kandoo/living/profile.md`, `docs/kandoo/living/status.md` and
`docs/kandoo/living/job.md`. They govern named commands and ordinary conversation.
Resolve every procedure path from the workspace root, regardless of which host copy
loaded it. Read the current step and its relevant installed references only.

One evolving Job governs independent Projects. The Job lives in `docs/kandoo/living/`;
canonical workspace commands in `docs/kandoo/commands/`; canonical Job commands in
`docs/kandoo/living/commands/`. Synchronize changed commands by copying the same
Markdown into all host locations described in the workflow constitution.

The person opens `docs/` in Obsidian; everything they are asked to open, read or write
must be a `.md` file inside `docs/` (including gitignored `docs/kandoo/secrets/` and
`docs/projects/ID/secrets/` when credentials are needed). Never refer the participant
to a non-`.md` file or a file path outside `docs/`, except when asking them to paste an
existing product into `projects/ID/existing/` or external design files into
`projects/ID/design/`. The assistant operates technical tools using the actual OS and
verifies outcomes. Preserve participant files, choices and existing authorization.
Record questions and non-obvious decisions in numbered open-version files. Submitted
blanks delegate a provisional recommendation; they allow specification steps to advance
without redundant approval rounds, but never certify artifact acceptance or grant new
external permissions. Unsubmitted blanks remain pending.

Expand active Project paths explicitly: artifact root `projects/ID/`, document root
`docs/projects/ID/` (always maintaining `living/idea.md` and `living/status.md`), and
selected version dossier `docs/projects/ID/versions/VERSION/`. On every task assess the
Job, shared Kandoo docs/code, active Project and write-only feedback as four possible
update targets. Do not read feedback as runtime input. Read historical versions only on
explicit request; the active version's submitted inputs and answers remain relevant.
Shared code belongs in root `kandoo/` when needed; Project code and runtime contracts
in `projects/ID/`. Secrets stay ignored and out of chat, logs and public docs.

Give each step a brief handoff (what changed, what evidence exists, what remains
pending) and finish every reply with the language-appropriate progress block and one
exact next action, using the current state rather than a fixed example. Keep technical
evidence, source fidelity, human acceptance and deployment evidence separate.
Before sending, mentally check that every ordered step and pending review is shown,
there is at most one current step, and labels/states are all in the conversation
language. Never omit the block on short replies or after resuming. Never use English
state words in a Persian bar; command identifiers and paths may remain unchanged.
Do not append any prose after the single next-action line. Use the examples in the
workflow constitution; no progress validator or host hook is required.
