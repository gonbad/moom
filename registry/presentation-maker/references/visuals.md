# Presentation visuals and exact source reuse

During outline, create `docs/living/assets.md`: map each slide/beat to
its required diagram, character, photo or video; identify states, transitions, purpose,
source/license, editable format and acceptance criteria. Design only visuals the story
needs. Keep speaker notes and full narration separate from audience-facing copy.

Build begins with visual preparation, before full slide assembly. For a new reusable
visual, write a copyable Markdown prompt in the selected dossier. Support interactive
Claude Design/artifacts when available, or a free web/desktop chatbot capable of
returning HTML. Work on one visual at a time, requesting a complete HTML with embedded
SVG/CSS and buttons to view every required variant and transition. A static visual
needs only its actual states; do not add pointless animation. Give feedback until the
participant accepts that revision. The coding assistant may prepare the same reviewable
artifact locally when requested. Account/tool availability is not guaranteed; keep the
complete-HTML handoff usable across tools.

SVG is the first attempt for appropriate vector graphics. If focused iteration misses
the intent, offer an external image-generation prompt or a participant-supplied image
with usable provenance/rights. Explain raster/layer limitations; do not call an image
embedded in SVG an editable vector design. Import supplied output from
`./design/`, preserving originals and source hashes. Record the source and
approval identity in `docs/living/assets.md`; never ask for duplicate content already supplied.

Serve a local gallery with controls for the planned variants/transitions; link it from
a Markdown review in `docs/`. Verify relevant semantic groups/pivots, typography,
clipping, reduced motion and resets. Accept this baseline before integrating it into
the deck. Reuse **the exact SVG geometry, group hierarchy, IDs, CSS classes, colors
and animation behavior**. Record necessary namespacing/technical integration changes
and verify visual equivalence; do not redraw an approximation or use a screenshot of
the source. Compare the source/gallery and representative slide at matching viewport,
scale and state. A correct original can still be broken by a slide wrapper or CSS rule.

After representative-slide acceptance, assemble the full deck and review its narrative
sequence and timing. Recheck the final offline/print output: controls and speaker notes
must obey the selected delivery contract, animations need useful static print states,
and all fonts/media must be packaged locally. Previously accepted unchanged visuals
can reuse their approval evidence; changed variants need review of the actual revision.
If no new/custom visuals are required, record that fact and verify the actual reused
assets instead of manufacturing an empty gallery ritual.

See [Claude artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
for interactive output, [SVG groups](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
for transform boundaries, and [SVG-as-image restrictions](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image)
when choosing between inline source and a static image. This four-stage Job embeds
visual preparation/review in build; it does not install an extra command.
