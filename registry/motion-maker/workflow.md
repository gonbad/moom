# motion-maker workflow

Server mode: none

Work locally through delivery. This workflow has no infrastructure intake.

| Command | Mode | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- | --- |
| `/idea` | ai | Idea and audience | ایده و مخاطب | Audience, purpose, output and factual constraints resolved |
| `/outline` | ai | Narrative outline | طرح روایت | Ordered beats, pacing, visual needs and closing action |
| `/story` | ai | Scene story and timing | داستان و زمان‌بندی صحنه‌ها | Accepted narrative; scene contract and rough spoken/animatic timing |
| `/visuals` | ai | Individual visual design | طراحی تک‌تک عناصر بصری | Per-visual HTML with variants/transitions, exact source identity and explicit acceptance |
| `/assets` | ai | Asset gallery and transitions | گالری عناصر و گذارها | Local integrated gallery, rig/transition checks and accepted baseline |
| `/animate` | ai | Local animation | ساخت و بازبینی موشن | Representative scene then accepted complete HTML preview with source identity |
| `/render` | tool | Silent video render | رندر ویدئوی بی‌صدا | Verified silent export or honestly pending/skipped state |
| — | human | Return voice recording | تحویل صدا | For a dubbed edition, record the accepted script, drop the audio in the declared return folder and run /dubb. Record a skip for silent delivery. |
| `/dubb` | tool | Dubbing and final delivery | صداگذاری و تحویل نهایی | Audio alignment if selected, final review and delivered artifact identity |

For the initial version follow these stages in order. Read each installed procedure for its inputs, outputs and exit evidence. Review only affected stages and prerequisites during later iterations.

References in `docs/references/`: `animation.md`, `intake.md`, `quality.md`, `visuals.md`, `workflow.md`.
