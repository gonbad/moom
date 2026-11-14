---
name: kandoo-issue
description: Diagnose, fix and verify a concrete defect in the active Project, Job or shared Kandoo.
---

# /kandoo-issue

Read `AGENTS.md`, all of `docs/constitution/`, current profile, status, server and Job.
Resolve workspace-root paths; require configured state. This command handles an
observed defect; planned feature/version work belongs to `kandoo-iterate`.

Capture expected versus actual result, reproduction input/steps, affected output and
available evidence through conversational chat intake. Diagnose ownership using current
files: Active Project, reusable Job/shared Kandoo, or Both (with linked distinct issue
records when Both applies). The person reports the symptom; do not require them to
identify its technical cause. If ownership remains genuinely unclear, ask one concise
routing question in chat before creating the issue dossier.

In the owner's current open version under `docs/` create the next unused `NN-issue.md`,
preserving the supplied report and subsequent findings. If its last version is closed,
open a new repair version, retaining the closed evidence and last working output. Use
numbered `.md` question rounds inside `docs/` for material uncertainties and non-obvious
proposed fixes, with context/options/AI recommendation/blank answer and the certainty
protocol; never refer the participant to non-`.md` files or paths outside `docs/`.
For a newly opened repair version, record the issue's full path as `Current input` in
its owning status. In an existing open version, retain its input and link this issue
as the current repair context. Never manufacture a new `00-idea-input.md` to resume a fix.

Reproduce before fixing where feasible, implement the focused fix, and verify the
original failure plus relevant regression behavior. Assess all four domains: repair
the reusable method if that caused the defect, update shared docs/code if needed,
repair only affected Project work and append sanitized creator feedback when useful.
A Job edit is normal evolution; no reinstall, upstream fetch or forced migration is
needed. Copy changed canonical commands to every host and preserve unrelated commands.
Do not mutate earlier accepted outputs or publish a fix without target authorization.

Record diagnosis, changed scope, evidence and unresolved limits in the issue file and
living state. Restore the interrupted workflow's Project selection/progress or mark
the affected step current if its result was invalidated. End with localized progress,
repair status and one exact next action (review/retest/resume); require close/reopen
if command names or discovery changed. Passing regression checks are not human acceptance.
