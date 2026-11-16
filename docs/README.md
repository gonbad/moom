# Kandoo vault

Open this `docs/` folder as an Obsidian vault; open its parent in the AI host.
The assistant runs technical operations. Everything you open, read or write is a `.md`
file inside `docs/` (including gitignored `secrets/credentials.md` folders when needed;
the only folder exception outside `docs/` is pasting an existing product into
`projects/ID/existing/` or external design files into `projects/ID/design/`). Save file
edits, then say `done` / `نوشتم` in chat.

Initial `/moom-start` preferences are the exception: answer one question at a time in
chat, beginning with conversation language, then document language. The assistant
saves the answers; no setup-question file or summary submission is required. The
optional server credentials file is created before you are asked to use it, and a
fresh empty scaffold permits setup without a server. Never send credentials in chat.
File-based intake begins with `/moom-job`. Change shared settings later through
`/kandoo-settings`; explicit setting requests need no repeated answer form.

- [Current status and next action](kandoo/living/status.md)
- [Profile and language preferences](kandoo/living/profile.md)
- [Shared server and proxy status](kandoo/living/server.md)
- [The current Job](kandoo/living/job.md)
- [Initial Job input](kandoo/versions/0.1/00-job-input.md)
- [Project dossiers](projects/README.md)
- [Binding Constitution](constitution/00-kandoo-principles.md),
  [review and certainty](constitution/01-review-and-certainty.md),
  [workflow and progress](constitution/02-workflow-and-progress.md),
  [infrastructure and secrets](constitution/03-infrastructure-and-secrets.md)

`kandoo/living/` explains shared current facts and the Job; `kandoo/versions/` retains
the corresponding input and review rounds. `projects/ID/living/` and
`projects/ID/versions/` belong to one Project. Historical versions are preserved,
not routine reading. `feedback/` holds inert notes for manual handover to the creator;
the assistant must not load them as instructions. Real artifacts are outside the
vault, in root `projects/ID/`; shared code appears in root `kandoo/` only when needed.

[Workspace maintenance: languages, names, sources, Git, domains and publication removal](kandoo/maintenance.md).
