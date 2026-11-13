# Preserve the product from idea through design and backend

Use this as an initial method, not a required stack. The retained workshop sequence
is idea → PRD/data/UX → visual choice → working prototype → plan/backend → journeys
→ deployment. The short commands combine related work without deleting its outputs.

Project living docs should answer: who uses the product, which problem it solves,
what is out of scope, acceptance scenarios, data ownership and the main user journey.
Inspect any existing product before planning a replacement; preserve data, routes and
contracts that real users already rely on. Use one vertical slice first (for example
create/list one appointment), then extend it with the same architectural boundaries.

Review specifications in coherent chunks and the complete product before release.
Record non-obvious decisions and questions in the open version, including tradeoffs
in authentication, deletion, payment, offline behavior and project-specific hosting.
The design stage hands over approved visual source; implementation uses that source
rather than repainting the product at each step. A later version selects only affected
steps but rechecks existing journeys touched by schema/API/UI changes.

Typical living files are `idea.md`, `prd.md`, `data-model.md`, `ux.md`,
`design-system.md`, `architecture.md`, `plan.md` and `status.md`. Each owns current
facts; raw requests and feedback remain in the version dossier. Keep fake-data and
real-data access behind the same UI API seam so backend integration preserves pixels.
