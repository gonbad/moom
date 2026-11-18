# Command names and collision checks

Reviewed 2026-11-17. This reference remains installed after the bootstrap registry is
removed. It is a conservative denylist of documented native names, aliases, built-in
skills and compatibility names, not a claim that every feature appears in every account.
New host versions and user/plugin commands can add names; inspect the current host's
actual command/skill catalog as well. Availability in one host never permits a collision
in another supported host.

## Native names by host

Identifiers omit the leading slash. The table is also read by the Workshop maintainer
audit; keep each host's identifier list on one table row.

| Host | Reserved identifiers | Primary source |
| --- | --- | --- |
| Claude Code | `add-dir`, `advisor`, `agents`, `allowed-tools`, `android`, `app`, `artifact-capabilities`, `artifact-diagramming`, `artifacts`, `auto-mode-setup`, `autocompact`, `autofix-pr`, `background`, `bashes`, `batch`, `bg`, `branch`, `btw`, `bug`, `cd`, `checkpoint`, `checkup`, `chrome`, `claude-api`, `claude-in-chrome`, `clear`, `code-review`, `color`, `compact`, `config`, `context`, `continue`, `copy`, `cost`, `dataviz`, `debug`, `deep-research`, `design`, `design-login`, `design-sync`, `desktop`, `diff`, `doctor`, `effort`, `exit`, `export`, `fast`, `feedback`, `fewer-permission-prompts`, `focus`, `fork`, `goal`, `heapdump`, `help`, `hooks`, `ide`, `import`, `init`, `insights`, `install-github-app`, `install-slack-app`, `ios`, `keybindings`, `list-agents`, `login`, `logout`, `loop`, `mcp`, `memory`, `mobile`, `model`, `new`, `output-style`, `passes`, `peers`, `permissions`, `plan`, `plugin`, `plugin-authoring`, `powerup`, `pr-comments`, `privacy-settings`, `proactive`, `quit`, `radio`, `rate-limit-options`, `rc`, `recap`, `release-notes`, `reload-plugins`, `reload-skills`, `remote-control`, `remote-env`, `rename`, `reset`, `restart`, `resume`, `review`, `rewind`, `routines`, `run`, `run-skill-generator`, `sandbox`, `schedule`, `scroll-speed`, `security-review`, `settings`, `setup-bedrock`, `setup-vertex`, `share`, `simplify`, `skill-doctor`, `skills`, `slides`, `stats`, `status`, `statusline`, `stickers`, `stop`, `subtask`, `tasks`, `team-onboarding`, `teleport`, `terminal-setup`, `theme`, `tp`, `tui`, `ultraplan`, `ultrareview`, `undo`, `update`, `update-config`, `upgrade`, `usage`, `verify`, `vim` | [Official command catalog](https://code.claude.com/docs/en/commands) |
| Codex CLI | `agents`, `app`, `approve`, `apps`, `archive`, `btw`, `cd`, `clean`, `clear`, `compact`, `config`, `copy`, `cwd`, `daemon`, `daybreak`, `debug-config`, `delete`, `diff`, `exit`, `experimental`, `export`, `fast`, `feedback`, `fork`, `goal`, `hooks`, `ide`, `import`, `init`, `keymap`, `logout`, `mcp`, `memories`, `mention`, `model`, `new`, `permissions`, `pet`, `pets`, `plan`, `plugins`, `presets`, `ps`, `pwd`, `quit`, `raw`, `recap`, `rename`, `resume`, `review`, `setup-default-sandbox`, `side`, `skills`, `status`, `statusline`, `stop`, `subagents`, `theme`, `title`, `tui`, `usage`, `vim`, `voice`, `warnings`, `worktree` | [Official developer commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) |
| Codex desktop / IDE | `cloud`, `cloud-environment`, `ide-context`, `local`, `project`, `reasoning` | [App commands](https://developers.openai.com/codex/app/commands), [IDE commands](https://developers.openai.com/codex/ide/slash-commands) |
| OpenCode | `agents`, `btw`, `clear`, `compact`, `connect`, `continue`, `editor`, `exit`, `export`, `help`, `highlights`, `init`, `models`, `new`, `q`, `quit`, `redo`, `resume`, `sessions`, `summarize`, `themes`, `thinking`, `undo`, `update` | [Current TUI](https://opencode.ai/docs/cli/tui/), [V1 compatibility](https://opencode.ai/v1/docs/tui/) |
| Antigravity | `agents`, `agy-customizations`, `antigravity-guide`, `automation`, `boost`, `browser`, `btw`, `changelog`, `codesearch`, `context`, `credits`, `diff`, `effort`, `generative_ui`, `goal`, `grill-me`, `learn`, `migrate-workflows`, `permissions`, `plan`, `plugin`, `resume`, `run-workflow`, `schedule`, `statusline`, `swarm`, `teamwork`, `title`, `usage`, `voice` | [Official catalog](https://antigravity.google/docs/slash-commands/), [workflow migration](https://antigravity.google/docs/ide/workflows) |

## Core workspace names

These nine names are also unavailable to Job commands, including after bootstrap
detachment: `start`, `pick-job`, `create-job`, `new-project`, `switch-project`, `iterate`, `issue`,
`preferences`, `add-idea`. The first three remain host-only recovery entry points.

## Authoring and installation procedure

1. Derive short descriptive names from the method. Use lowercase ASCII words separated
   by hyphens, at most 64 characters. Do not add a framework or Job prefix.
2. Compare every proposed name against the union of the native table, all nine core
   names and other proposed names. Inspect existing canonical files, all supported host
   locations, and available plugin/user catalogs. Reserve names case-insensitively.
   Do not run a native command just to test whether a name is free.
3. Prefer meaningful alternatives: `architecture` for technical planning,
   `visuals` for visual design, `preferences` for workspace settings. Never overwrite
   a native command or unrelated procedure. Similar purpose does not confer ownership.
4. For a custom Job, record the chosen stage-to-command mapping in its living Job;
   update pipeline links, frontmatter, next actions and all installed copies together.
   A safe rename does not authorize changes to the method's purpose or acceptance gates.
5. An exact named-starter install must pass this check before mutation. If an unrelated
   command already occupies a name, explain the specific collision and preserve files.
   Resolve ownership or explicitly choose a custom mapping; never silently adapt bytes
   while claiming an exact installation. On a verified resume, update only owned files
   according to the saved checklist; preserve unexpected edits for review.
6. Check equality of canonical and host copies. Remove only verified owned obsolete
   files on a rename, preserve other commands, update saved next actions, and request a
   host close/reopen when discovery changes. Retain recovery entries after detachment.

Native catalogs can change independently of Moom. During later authoring, refresh only
the relevant official documentation when local evidence is insufficient, record the
date and any new reserved names here, then check the whole Job mapping again. This is
host compatibility research, not a dependency on the upstream Moom template. If current
discovery cannot be checked, record that limit and use ordinary-language invocation
until a host rehearsal verifies the name; do not claim native compatibility was tested.

