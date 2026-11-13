# External design and implementation fidelity

Produce Project-owned `prd.md`, `data-model.md` and `ux.md` first. The design handoff
is one prompt plus these three files for Claude Web Chat or Claude Design. Explain
the main view, users, routes, states and constraints. In the same design conversation
request three main-view alternatives, let the owner select/combine them, then obtain
3–5 key screens and their approved HTML. Record source and confirmed choices.

Bring those files into the Project's design folder. Convert their actual appearance
to React (or the explicitly adapted stack) under assistant supervision; do not replace
the approved design with a fresh generic theme. Compare corresponding source HTML and
prototype screenshots at matched viewports and states; review mismatches with the
person before connecting APIs. A conversion tool is optional and its result is reviewed.
Preview CDNs may help design exploration; production Tailwind, fonts, scripts and other
runtime assets must be bundled locally. Preserve deep-link SPA routing, error/loading/
empty states, RTL behavior and accessibility through integration.
