---
name: shared-code
description: Scope, plan, implement and exercise reusable helpers.
---

# /shared-code

Inspect workflow inputs and example outputs. For each helper propose purpose and scope, consumers, input/output contract, failure behavior, dependencies, location, Git owner, version pin, implementation tasks and test cases. Compare per-project template, shared sibling or host tool, and Kandoo-local utility according to who actually invokes it. Record the selected plan in the current dossier and its durable location and invocation under the heading `## Shared code` in living/workflow.md. A routine with no helper records that decision.

After review, implement each required helper at its agreed location and wire it into the calling stage. Install or document dependencies. Exercise representative and failing inputs from the consumer’s working directory, including shared location resolution. Record the exact command, tool version, evidence and limits. Keep unresolved implementation work open. On change repeat the affected checks. Continue to /floating-commands.
