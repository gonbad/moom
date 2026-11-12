# Convert the approved designs and verify the prototype

Read the approved design manifest and current UX. Initialize React/TypeScript with
Vite in SOURCE/frontend. Use the compatible build-time Tailwind integration (for
example tailwindcss and @tailwindcss/vite); pin dependencies in the lockfile. Translate
the exact HTML in DESIGN into components and pages. Conversion tools may assist,
but the assistant must check JSX, shared structure, responsive behavior and assets.
Extract reusable navigation, cards, controls and dialogs. Implement every UX route
and required state with replaceable mock data. Secondary views follow the approved
patterns. Preserve the design's Tailwind configuration/fonts so compilation does not
silently change its appearance. Remove preview CDN runtime dependencies from the app.

Launch the prototype under the active Project. At matched desktop/mobile viewports,
load each approved HTML source and its React route, use matching data and interaction
states, and save both screenshots under EVIDENCE. Compare layout, text, typography,
colors and interactions. Repair differences until visually equivalent; a missing
comparison or unavailable browser is a pending gate, never a pass. Review the prototype
with the person and reconcile affected specifications. Record VERSION/prototype.md
with screenshot paths and the exact owner feedback, separate from automated readiness.
