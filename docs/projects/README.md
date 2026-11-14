# Independent Project dossiers

The first Project is created and selected automatically when the Job is installed.
Use `kandoo-new-project` for later instances and `kandoo-switch` to resume another.

Each `ID` owns document root `docs/projects/ID/` (`living/`, selected version dossier
`versions/VERSION/` starting at `versions/0.1/00-idea-input.md`, and gitignored
`secrets/credentials.md` when needed) plus artifact root `projects/ID/` outside this
vault for code, pasted `existing/` or `design/` bundles, data and compiled outputs.
`living/status.md` retains selected version, recorded Job revision, ordered step states,
pending review and one next action; `living/idea.md` is always maintained with current
understood scope. Never reuse another Project's input, prompts, contracts, credentials,
Git tags, deployment ports or output. Shared server details belong to Kandoo unless
this Project overrides them.
