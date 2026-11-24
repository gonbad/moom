---
name: inspect
description: Diagnose method friction using evidence from one registered project.
---

# /inspect

Resolve one registered slug (ask if missing), its installed version, the applicable sealed baseline, method notes and relevant output. Compare the observed result with the accepted rule. Record expected and observed behavior, cost and evidence. Key each receipt in living/projects.md by slug, filename and content hash. Resume pending work from its dossier and reuse a completed receipt when the same note returns. Leave inaccessible evidence pending.

- Route a project-specific repair to its /issue. Record local exceptions in the receipt.
- For a reproducible method bug with an already agreed rule, this invocation owns the fix through verification. Check whether the current applied method still has the defect. If already fixed, link the verified version. Otherwise open a patch dossier for the current applied method (0.1 to 0.1.1, then 0.1.2). When a feature revision is open, use a separate clean Git worktree rooted at the commit for the applied method. Carry only verified patch files into the method and reconcile the open feature dossier against that patch. Preserve the participant’s pending edits. Record the rule, affected sources, failing check and remedy. Correct the reusable source and template. Reuse the /apply preview, fresh-render checks and seal procedure. Create a disposable project from the repaired seal in an isolated copy of the Kandoo and check its installed commands and output there. Exercise the original failure on the old and repaired outputs before recording the applied version, digest and test result. On failure retain a pending receipt and resume the same patch. Report the outcome directly; no second /new-version invocation is required.
- When the desired behavior needs a new choice, open numbered analysis in the method dossier. After convergence this inspection resumes the agreed work. Route elective future enhancements to the roadmap with their disposition.

Keep existing projects pinned until the participant selects a migration. Process domain facts and reusable assets with their provenance and receipt.
