---
name: apply
description: Check a rendered project and seal the approved method.
---

# /apply

Require the reviewed mission, workflow, topology, implemented shared-code plan, floating commands and testing procedure. Resolve inline comments. Prepare a short, 15–20 line, job-specific, deletable template/docs/versions/0.1/00-user-idea-input.md in the document language. Keep 01-kandoo-interpretation.md empty. Localize project documents and labels. Preserve stable status field names, workflow identifiers and table syntax. Copy only approved context and reusable assets. Record changes and old-to-new stage mappings in template/docs/method/CHANGELOG.md.

Run `python3 scaffold.py preview NEW_TEMP_PATH` and execute the agreed checks with that directory as the working directory, including actual helper invocations and human checks. Verify relative and configured external paths, command gates, failure cases and return folders. Record results and any outstanding human acceptance. Then run `python3 scaffold.py seal VERSION`. Seal runs template Python tests inside a fresh render when tests/ exists. It publishes an immutable digest and the applied version only after checks pass. Verify the resulting render with `python3 scaffold.py render VERSION NEW_TEMP_PATH`. Record the digest, checkpoint and mark the method configured. Offer /new-project.

Verify that the project constitution carries the analysis protocol and that the first project reply will use the inherited chat language. Normal setup handoffs offer the next command; only a participant request starts it.
