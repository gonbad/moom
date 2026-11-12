# External design handover

Confirm that this Project's PRD, data-model and UX are ready for design. Present one
short prompt and the actual three files at LIVING/prd.md, LIVING/data-model.md and
LIVING/ux.md. Explain the resolved DESIGN directory before the person leaves for
Claude Web Chat or Claude Design. Keep all exploration in one conversation/project.
Do not require a compiled prompt document or ask the participant to write the prompt.

```text
I attached prd.md, data-model.md and ux.md for my web app.
Use Tailwind CSS; external CDN scripts are allowed in these preview HTML artifacts.
First generate three visually distinct interactive HTML designs for the primary
screen identified in ux.md. Wait for my choice or blend request to establish the
design system. Then create complete standalone HTML pages for 3–5 other important
screens in those documents, consistently using the selected design. Keep the same
conversation and provide the HTML and necessary assets for download.
```

The person selects/refines the designs and places approved originals and assets in
DESIGN. Record the choice and file manifest in VERSION/design.md. Preserve original
HTML as the comparison baseline. Return to the person for missing files rather than
inventing an approved design. Remaining secondary screens are extrapolated in prototype.
