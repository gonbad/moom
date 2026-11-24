# Speaker-led presentation workflow

Server mode: none

| Command | Mode | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- | --- |
| `/idea` | ai | Idea and research | ایده و پژوهش | Audience, speaker's thesis and supporting material resolved |
| `/structure` | ai | Chapters | فصل‌بندی | Sections, chapters and navigable milestones agreed |
| `/outline` | ai | Slide outline | طرح اسلایدها | Stable IDs, claims, notes and interaction outcomes specified |
| `/styling` | ai | Visual style | سبک | Representative typography, layout and direction reviewed |
| `/assets` | ai | Assets | دارایی‌ها | Local assets identified and any external prompts prepared |
| — | human | External assets | تولید دستی | Requested media returned and matched, or skipped when all assets are local |
| `/build` | tool | Build | ساخت | Accepted representative slide and working offline deck |
| `/deliver` | ai | Deliver | تحویل | Transferred folder checked, speaker rehearsal and any remaining venue checks recorded |

For external assets, provide the prompt and expected result in docs/living/assets.md, ask the participant to save returns in design/, and resume on “assets ready”. Match returns by content hash, retain previous takes, and record an explicit skip when there is no external work. Each step uses the analysis rounds in docs/constitution/general.md.

References in `docs/references/`: `intake.md`, `workflow.md`, `slides.md`, `visuals.md`, `quality.md`.
