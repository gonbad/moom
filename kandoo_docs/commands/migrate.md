---
name: migrate
description: Preview and apply a reviewed method update to explicitly named projects.
---

# /migrate

Resolve the named slug(s) or explicit all in the project ledger. Check the applied and installed Kandoo versions and the project’s own product version. Run `python3 scaffold.py migrate SLUG VERSION` for a read-only old/local/new comparison. Inspect local drift, renames, completed stages and the next step. Record whether new requirements are already satisfied, pending or explicitly skipped. Preserve participant inputs, deliveries, history and secrets.

Review the diff and capture a clean local Git checkpoint before applying it. Resolve each conflict explicitly with --keep PATH or --take PATH. Use --completed STAGE for an added stage satisfied by existing evidence. Use --current STAGE when a renamed or removed active stage requires a successor. Repeat the preview with those choices. After confirmation run the same command with --apply. The helper applies the plan in a disposable Git worktree, preserves a backup ref and fast-forwards only the checked project. Verify the project status, host commands and fresh-session progress, then record the result and exact next action.
