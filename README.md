# Moom → your Kandoo

Moom is a Markdown template for turning repeated work into your own evolving Job.
A configured workspace is a Kandoo: one current method, several independent Projects.
There is no bundled runtime, Python CLI, script installer or machine-readable state.
The coding assistant reads the procedures and works with your computer's native tools.

1. Fork [the template](https://github.com/gonbad/moom), clone your fork into a fresh
   folder, or extract the workshop ZIP and choose your own repository during setup.
   A participant-owned Git remote is recommended; offline/local-only work can start
   with local Git and pending backup. You can explicitly skip any setup step.
2. Open that folder in Claude Code, OpenCode, Codex or Antigravity. Open its `docs/`
   subfolder as an Obsidian vault; [the vault home](docs/README.md) explains the layout.
   Every file you read or write lives as Markdown inside `docs/` (the only folder
   exception is pasting an existing codebase or external design files when requested).
3. Run `/moom-start` (Codex CLI: `$moom-start`; desktop slash/dollar picker;
   Antigravity: select or mention the skill). Ordinary language
   also works. The assistant collects languages, checks Git and backup, and asks
   about a server immediately. No server is a valid answer. With one, setup verifies
   SSH, a domain or free `nip.io` hostname, public HTTPS and an authenticated proxy.
4. Run `/moom-job`. Describe your repeated work in the provided file, save it, then
   say `done` / `نوشتم`. Use, adapt or replace any [starter](registry/README.md).
   Question rounds distinguish your confirmed choices from provisional delegation.
5. The assistant installs your Job, creates and verifies Project 1 from your input,
   removes the catalog and canonical bootstrap documents, and replaces this README with
   your Kandoo's guide. Close and reopen the AI host, then run its first `job-*` step.

Claude Code and OpenCode read `.claude/commands/NAME.md` and
`.opencode/commands/NAME.md`. Codex and Antigravity share
`.agents/skills/NAME/SKILL.md`. These are identical copies of canonical Markdown,
including `name` and `description` frontmatter. The six `kandoo-*` workspace commands
are pre-synced too, and become usable when setup is complete. Job commands are installed
at finalization. Codex CLI uses `$NAME`, and Codex desktop accepts slash/dollar selection.
Claude Code/OpenCode use `/NAME`. Antigravity uses skill selection or mentions, with
`/NAME` where its UI exposes the skill. Retained bootstrap host entries become local
recovery handoffs and never reinstall the catalog.

Later, `/kandoo-new-project` creates and selects the next independent Project;
`/kandoo-switch` resumes one; `/kandoo-add-idea` banks an idea for the Project, Kandoo
or both without interrupting work; `/kandoo-iterate` opens a planned version;
`/kandoo-issue` handles a defect; `/kandoo-server` adds or changes shared infrastructure.
The Job can evolve during real work. Every response has progress and one next action.

This source contains only Markdown and a root `.gitignore`, apart from Git metadata.
Maintainer tooling lives in the parent Workshop repository, outside the participant
template. It validates and packages the source; participants never need that tooling.
After setup there is no upstream update, publish or source-repository dependency.

Host discovery references: [Claude Code](https://code.claude.com/docs/en/slash-commands),
[OpenCode](https://opencode.ai/docs/commands/), [Codex skills](https://learn.chatgpt.com/docs/build-skills),
and [Antigravity skills](https://antigravity.google/docs/skills/).

[License](LICENSE.md)
