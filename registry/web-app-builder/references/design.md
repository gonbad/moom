# External design prompt, prototype and faithful conversion

## Three specifications and one prompt

Write Project-owned `prd.md`, `data-model.md` and `ux.md` before design. The PRD names
users, problem, scope, journeys and acceptance examples. The data model names entities,
keys, ownership, constraints and lifecycle states. UX names routes, the most important
screen, navigation and loading/empty/error/success states. These are the three files
attached to one Claude conversation or Claude Design, using a prompt like:

> Use these PRD, data-model and UX files as the contract. First propose three clearly
> different designs of the appointment list using the same realistic Persian content.
> Vary layout, typography and color/shape, respecting RTL and the target phone viewport.
> Explain each direction briefly. After I choose or combine them, produce 3–5 key
> screens in the same conversation, including empty, loading and validation states.
> Return the actual HTML/CSS/assets and a token sheet; keep interactions navigable.

Do not send secrets/customer data. Record the chosen direction and rationale. Capture
colors by role and hex value, font files, type scale, spacing steps, radius and focus/
error/disabled behavior in `design-system.md`. Review the actual screens, not only a
verbal description. Preview CDNs are acceptable for exploration; preserve approved
HTML and screenshots before converting it.

## Prototype handover

Store approved source under the Project's `design/`. Convert its measured layout to
React or the chosen stack. Use one API seam returning realistic fixtures shaped like
the data model; UI components do not scatter fetch calls. Keep route shells, theme
and data access explicit. Walk 3–5 screens as a connected journey before real APIs.
Compare source and converted screenshots at the same viewport, font state, data and
interaction state; record mismatches and fix them before wiring backend behavior.
Changing the visual system needs an explicit recorded decision, not a tool default.

An illustrative React/Vite/Tailwind setup, after checking installed major versions:

```sh
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
npm install tailwindcss @tailwindcss/vite
```

For a Tailwind version using the Vite plugin, add `tailwindcss()` beside the React
plugin in `vite.config.ts` and `@import "tailwindcss";` in the app CSS. Do not mix
legacy configuration recipes with a different installed major. Run `npm run build`
and check the compiled output contains all used classes and local fonts/assets.
Resolve a blocked install through the existing scoped proxy; do not change global
network settings. The assistant runs these commands; the participant reviews screens.

References: [Vite](https://vite.dev/guide/),
[Tailwind installation](https://tailwindcss.com/docs/installation/).
