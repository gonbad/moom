# Presentation craft, HTML behavior and delivery

## Prompt and storyboard

Use a concrete brief such as:

> Create a 20-minute Persian workshop for first-time builders. The audience should
> finish able to separate a repeatable method from one output. Use one recurring
> example, a failed attempt and an improved attempt. Propose the argument and slide
> beats before choosing layouts. Include speaker notes and a five-minute exercise.

For each beat write its claim, supporting evidence/example, audience activity and
visual treatment. Use assertion titles and diagrams where spatial relations explain
more than text. A chart needs axes, units, data source and a stated takeaway. Never
invent numerical evidence. Show real code at readable size with a visible explanation.
Alternate comparison, process, demonstration and reflection rather than repeating a
single title-and-bullets layout. Keep speaker notes separate from audience text.

## Build the chosen format

HTML example structure, generated in the Project only when appropriate:

```text
src/index.html        semantic sections and slide IDs
src/deck.css          theme tokens, RTL, mobile and print styles
src/deck.js           navigation and local interaction state
src/assets/           fonts, images and their licenses
```

Use stable slide IDs in the URL hash. Arrow/Page keys move predictably; Home/End and
an overview permit seeking. Ignore navigation keystrokes in inputs/dialogs. Closing
an overlay restores focus. Direct seeking must not mark skipped sections visited.
Back/forward navigation, reload and touch controls restore the same selected slide.
Show where the audience is without making navigation depend on finishing animations.
For RTL prose set `lang`/`dir`; isolate code, formulas and paths as LTR. Test actual
Persian font shaping, mixed-script wrapping, long names and small screens. Respect
reduced motion and avoid scroll/keyboard traps. Do not promise fullscreen in contexts
where the browser disallows it; retain a working ordinary viewport.

For print/PDF hide navigation, preserve diagrams and page breaks, and check an actual
export for clipping and missing fonts. For offline delivery load by `file://` from a
path with spaces and Persian characters while network access is disabled. Bundle
runtime fonts, scripts and images locally; navigation must not require fetch of local
JSON under file restrictions. A single-file artifact can inline assets when useful.
Offer editable source and the chosen viewing/export format, not a forced JSON schema.
