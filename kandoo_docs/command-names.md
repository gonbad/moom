# Command names and collision checks

Reviewed 2026-11-17. The local registry is permanent. It is a conservative denylist of documented native names, aliases, built-in
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

Reserve these Kandoo names: `start`, `job`, `topology`, `shared-code`, `floating-commands`, `testing`, `mission`, `workflow`, `apply`, `new-project`, `inspect`, `new-version`, `migrate`, `report-moom`.

## Authoring

Also reserve project utilities `iterate`, `issue`, `add-idea`, `method-note` and the conditional `server` procedure. Check names case-insensitively against this catalog, existing host files and installed user/plugin commands. Preserve unrelated entries. Use unprefixed lowercase ASCII words separated by hyphens, maximum 64 characters. Each source has YAML name and description. Claude Code and OpenCode take command files. Codex and Antigravity share the skills directory. Reopen the project session after changing its installed commands.
