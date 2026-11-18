# Moom → your Kandoo

Moom is a Markdown template for turning repeated work into your own evolving Job.
A configured workspace is a Kandoo: one current method, several independent Projects.
There is no bundled runtime, Python CLI, script installer or machine-readable state.
The coding assistant reads the procedures and works with your computer's native tools.

1. On [the template](https://github.com/gonbad/moom), choose **Use this template →
   Create a new repository** under your account. Choose public or private visibility
   (private is a useful default for unpublished work), then clone **your new repository's
   HTTPS URL** into a fresh folder. Public HTTPS clones need no repository login;
   private clones and pushes use supported authentication, such as a credential
   manager or GitHub CLI with browser login. SSH keys are not a prerequisite, and
   your GitHub account password cannot authenticate Git. See
   [GitHub's credential setup](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).
   Existing forks remain valid. Alternatively, extract the workshop ZIP and let setup
   initialize Git and connect your repository. Offline/local-only work can continue
   with backup pending, and you can explicitly skip any setup step.
2. Open that folder in Claude Code, OpenCode, Codex or Antigravity. Open its `docs/`
   subfolder as an Obsidian vault; [the vault home](docs/README.md) explains the layout.
   Every file you read or write lives as Markdown inside `docs/` (the only folder
   exception is pasting an existing codebase or external design files when requested).
3. Run `/start` (Codex CLI: `$start`; desktop slash/dollar picker;
   Antigravity: select or mention the skill). Ordinary language
   also works. Answer setup preferences **in chat, one question at a time**: first
   conversation language in English/Persian (English recommended), then document
   language in your chosen chat language. The assistant detects tools and reuses Git
   identity/access; you need not choose a single AI host. Setup finishes by listing
   the actual available starters with their exact selection commands. Server intake
   belongs only to the Job stage that needs it; local content work needs none.
4. Choose a prepared Job directly, for example `/pick-job motion-maker` or
   `/pick-job presentation-maker` (Codex: `$pick-job motion-maker`). This installs the exact
   starter without Job-definition questions. Or run `/create-job`
   to describe repeated work in the provided Markdown input, save it and say
   `done` / `نوشتم`. That custom path can use, adapt or replace any
   [starter](registry/README.md), with confirmed choices and provisional delegation.
5. The assistant installs your Job, creates and verifies Project 1 from your input,
   removes the catalog and canonical bootstrap documents, and replaces this README with
   your Kandoo's guide. Use the idea page and optional material locations it shows
   you. Once saved, close and reopen the same workspace, then run the first Job step.

Claude Code and OpenCode read `.claude/commands/NAME.md` and
`.opencode/commands/NAME.md`. Codex and Antigravity share
`.agents/skills/NAME/SKILL.md`. These are identical copies of canonical Markdown,
including `name` and `description` frontmatter. The six permanent workspace commands
are pre-synced too, and become usable when setup is complete. Job commands are installed
at finalization. Codex CLI uses `$NAME`, and Codex desktop accepts slash/dollar selection.
Claude Code/OpenCode use `/NAME`. Antigravity uses skill selection or mentions, with
`/NAME` where its UI exposes the skill. Retained bootstrap host entries become local
recovery handoffs and never reinstall the catalog.
You may perform different steps in different hosts. Each session resumes the saved
preferences and Project state; it does not repeat setup or regenerate the Job.

Later, `/new-project` creates and selects the next independent Project;
`/switch-project` resumes one; `/add-idea` banks an idea for the Project, Kandoo
or both without interrupting work; `/iterate` opens a planned version;
`/issue` handles a defect; `/preferences` changes languages, workspace
preferences, Git backup or shared infrastructure while preserving Project progress.
Commands are unprefixed; [reserved names](docs/kandoo/command-names.md) prevent
collisions with host commands. `/architecture` is a technical planning step and
`/visuals` is visual design; host-native commands keep their own meanings.
The Job can evolve during real work. Every response has progress and one next action.

This source contains only Markdown and a root `.gitignore`, apart from Git metadata.
Maintainer tooling lives in the parent Workshop repository, outside the participant
template. It validates and packages the source; participants never need that tooling.
After setup there is no upstream update, publish or source-repository dependency.

Host discovery references: [Claude Code](https://code.claude.com/docs/en/slash-commands),
[OpenCode](https://opencode.ai/docs/commands/), [Codex skills](https://learn.chatgpt.com/docs/build-skills),
and [Antigravity skills](https://antigravity.google/docs/skills/).

[License](LICENSE.md)

[Workspace maintenance](docs/kandoo/maintenance.md) explains naming, existing-material
intake, shared settings, Git remote changes, domains, unlisting and unpublishing.
