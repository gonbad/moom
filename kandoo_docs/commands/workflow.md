---
name: workflow
description: Define ordered stages, actors, handoffs and delivery criteria.
---

# /workflow

Analyze the proposed workflow from the reviewed mission. Write living/workflow.md after convergence. Preserve explicit exclusions. Offer omission for optional terminal actions. A manual upload outside the agreed deliverable goes on the roadmap. Use this table format, with /idea first. Older four-column tables imply ai.

| Command | Mode | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- | --- |
| `/idea` | ai | Brief | ایده | Accepted input |
| — | human | External generation | تولید دستی | Returned media verified |
| `/produce` | tool | Produce | تولید | Verified delivery |

Use ai, tool, human and api. Each command has a complete living/steps/NAME.md body with YAML name and description. A human row has a unique stage label, a handoff specifying exact outbound files, external action, return folder, and resume cue. Detect a single new matching return by name and hash since the prior take. Ask when several match. For an API record provider, inputs, result, credential scope, retry and error behavior. Give each stage inputs, output, prerequisites and observable exit evidence. Add domain and server facts to living/context/. Keep starter reference paths usable under docs/references/. Record one Server mode line (none, shared or dedicated). Review each optional stage and respect the latest explicit edits. Offer /topology.

For media routines write raw/ and intermediate file patterns in template/docs/method/project-ignore.md, one Git ignore pattern per line. Record filenames and digests in receipts. Keep small reviewed final deliveries and reusable assets tracked under the agreed policy.

For version one use an available free API when it implements the agreed task promptly. When realistic images or video are inexpensive to obtain manually, provide the prompt, return folder and exact resume cue as a human stage. Record paid integrations and later browser automation on the method roadmap, with the manual step they would replace.
