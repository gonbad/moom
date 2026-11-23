# film-maker workflow

Server mode: none

Work locally through delivery. This workflow has no infrastructure intake.

| Command | Mode | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- | --- |
| `/idea` | ai | Idea | ایده | edit the whole story in prose, confirm who speaks and record the title. |
| `/story` | ai | Story | داستان | adapt the accepted prose into scenes with camera positions and a shot ID for each speaking turn. |
| `/narration-prompt` | ai | Narration prompt | راهنمای صدا | review one document per sequence, with copyable style and speech for each performance and a folder for the takes. |
| — | human | Record performances | ضبط اجرا | Use the approved sequence prompt sheets. Record or generate audio, drop new takes in the designated sequence folder, then run /narrate. |
| `/narrate` | tool | Narrate | ضبط | record separate voices by uninterrupted speaking turn, actors performing together by scene, and continuous solo narration by sequence. |
| `/storyboard` | ai | Storyboard | استوری‌بورد | time the pictures to the chosen performance. |
| `/visuals` | ai | Visuals | تصاویر | establish the cast and finish one telling shot. |
| `/animate` | ai | Animate | پویانمایی | finish the action, then mix sound for each sequence. |
| `/render` | tool | Render | خروجی | assemble, inspect and deliver the film. |

For the initial version follow these stages in order. Read each installed procedure for its inputs, outputs and exit evidence. Review only affected stages and prerequisites during later iterations.

References in `docs/references/`: `intake.md`, `production.md`.
