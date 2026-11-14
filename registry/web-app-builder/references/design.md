# External design prompt, return bundle and two-stage visual fidelity

## Three specifications and one external prompt

Write `docs/projects/ID/living/prd.md`, `data-model.md` and `ux.md` before design. The
PRD names users, problem, scope, rich personas, journeys and acceptance criteria. The
 conceptual data model names entities, fields, relationships and invariants without SQL.
UX names every screen, empty/loading/error states and the single primary key screen.

Write the ready-to-paste prompt into `docs/projects/ID/versions/VERSION/NN-design-prompt.md`
so the participant can copy it from Obsidian and attach those three `.md` files in
Claude Web Chat or Claude Design using the strongest suitable model and high-effort
mode available on their account (never hardcoding an obsolete model version):

> Use the attached `prd.md`, `data-model.md` and `ux.md` as the contract. First propose
> three clearly distinct visual directions (A, B, C) of the primary key screen using the
> same realistic Persian content. Vary layout, RTL Persian typography and color/shape
> palette for the target viewport. Use standard Tailwind CSS utility classes throughout
> (a `<script src="https://cdn.tailwindcss.com"></script>` tag is permitted in standalone
> preview HTML so files open directly in a browser). Explain each direction briefly.
> After I choose or combine directions, output: (1) a complete Markdown design-system
> specification (hex color roles, font families, type scale, spacing, radii and
> focus/hover/disabled/error states), and (2) 3–5 connected key screens as standalone
> HTML files including empty, loading, error and validation states.

Never send secrets or real personal data. If external design chat is unavailable, fall
back to generating three distinct standalone Tailwind HTML directions locally under
`projects/ID/design/` for the same human choice, recording external chat as unavailable.

## Return bundle and local import

External browser chat cannot write local workspace files directly. Define a concrete
four-part return bundle:
1. **Selected HTML screens and assets** pasted by the participant into `projects/ID/design/`
   (one of the permitted non-`docs/` drop folders).
2. **Design-system Markdown text** pasted by the participant into
   `docs/projects/ID/versions/VERSION/NN-design-return.md` (or chat).
3. **Selection rationale** (which direction or combination won and why).
4. **Local assistant import:** the assistant inspects the HTML files, writes the
   authoritative `docs/projects/ID/living/design-system.md`, and records the imported
   inventory in the open version dossier.

## Prototype conversion and two separate visual comparisons

Convert the approved HTML DOM structure and Tailwind utility classes directly into React
components under `projects/ID/frontend/` using locally compiled Tailwind (Vite +
`@tailwindcss/vite` or PostCSS—removing the preview CDN from the React app):

```sh
mkdir -p projects/ID
npm create vite@latest projects/ID/frontend -- --template react-ts
npm --prefix projects/ID/frontend install
npm --prefix projects/ID/frontend install tailwindcss @tailwindcss/vite
```

Derive secondary screens listed in `ux.md` from the same `design-system.md` tokens and
shell components rather than requiring every screen to be externally generated or
inventing new styles. Route all UI data through `projects/ID/frontend/src/api/` returning
realistic synthetic fixtures shaped like `data-model.md`.

Maintain **two distinct visual fidelity gates** with separate `.md` evidence records:
1. **Gate 1 (`job-prototype`, HTML → React):** Compare authoritative HTML in
   `projects/ID/design/` with the running React prototype at matching desktop/mobile
   viewports, local fonts, data and empty/error/filled states before freezing
   `project/ID/prototype/VERSION` (or an immutable local snapshot if Git is deferred).
2. **Gate 2 (`job-test`, Frozen Prototype → Integrated Application):** Run the frozen
   prototype from a separate worktree/copy on a free port beside the integrated app and
   verify pixel/layout parity plus zero runtime CDN requests.

References: [Vite](https://vite.dev/guide/),
[Tailwind installation](https://tailwindcss.com/docs/installation/).

Later comparisons use the exact accepted prototype baseline recorded in
`docs/projects/ID/living/status.md`, including any revised tag or snapshot created
during scenarios. Never infer the baseline from the Project version alone.
