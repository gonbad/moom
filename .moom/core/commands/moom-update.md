# Update Moom while preserving the configured Kandoo

Read docs/moom/updates.md in full. The assistant fetches a specific upstream release
and resolves its commit, compares installed baseline → local → target, and handles
semantic conflicts. Use the bundled update --source PATH planner and apply helper.
Do not merge upstream main over the user's repository or replace all of .moom/.

Preserve the current Job, Projects, shared code, review history, workspace state and
unrelated edits. A configured Job prevents catalog restoration. Retain a checkpoint,
check schema/Job compatibility, run the new helper's checks, inspect the diff and scope
any authorized commit to this update. Report any unresolved conflict accurately.
