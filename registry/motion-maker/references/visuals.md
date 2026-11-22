# Visual design, rigs and exact reuse

## Design one visual at a time

Derive the asset list from accepted scenes: identity, narrative role, appearances,
style, needed expressions/poses, transitions, attachment points and source/license.
Separate static shape from pose/state and animation behavior. A character has stable
geometry and semantic groups (body, head, arm, hand, face); colors and typography use
consistent CSS classes/tokens. A sad-to-happy transition is an authored change between
states, not permission to shake the whole character.

Write a copyable external design brief in the current version's Markdown dossier.
The participant works interactively in the current Claude Design/artifact surface
available to their account, or any capable web/desktop chatbot. A free chatbot that
can return complete HTML is a valid fallback; do not require paid Design access or
assume a particular export button. Ask it to return **one complete HTML per visual**,
embedding SVG and CSS, with buttons for every requested state/pose and transition,
play/pause/replay/seek controls, labels outside the eventual capture region, and all
required dependencies. Preserve the existing brief and acceptance criteria across
tools. If the participant prefers the coding assistant, it can prepare the same
reviewable artifact locally; never skip the review because the authoring tool changed.

The brief includes visual intent, prohibited features only when actually supplied,
frame proportions, expression/pose names, semantic SVG groups and pivot locations,
duration/easing for transitions, still holds and reduced-motion behavior. Request
readable source, no hidden remote content and no generic idle wobble. Provide feedback
on this one visual until accepted; do not generate a cast of unreviewed approximations.
The assistant imports supplied bundles from `./design/`, inventories source
files/dependencies, serves them locally and records revision/hash plus acceptance.

## SVG first, with a bounded fallback

Use SVG for suitable scalable graphics. If a focused revision still misses the desired
appearance, explain the limitation and offer (1) a precise external image-generation
prompt or (2) a participant-selected image with usable provenance/rights. Do not spend
unbounded attempts redrawing a rejected face. Agree the fallback and record it.
A raster image cannot be relabeled editable SVG; use approved whole-image transforms
or separately supplied layers/poses, with the resulting motion limits made visible.
If transitions need layers that are unavailable, simplify the story/motion explicitly
instead of pretending an illustration is rigged.

## Integrate the accepted sources

Preserve imported originals. Build the asset gallery by importing or extracting the
**same** SVG paths, group hierarchy, IDs, CSS selectors, colors and keyframes. Record
source-to-gallery and gallery-to-scene mappings in `docs/living/assets.md`; preserve hashes
of accepted originals and any derived files. Namespacing duplicate IDs/selectors is
allowed only where technically necessary, with a documented mapping and visual
equivalence checks. Do not recreate appearance from memory, use an approximate redraw
or replace a vector source with a screenshot of its preview.

Inline interactive SVG when its DOM groups/CSS must be animated; an SVG loaded as an
image does not provide the same DOM access. Test computed transform origin/transform
box and real pivot position. A waving arm rotates its arm group while body/head remain
stable; whole-body motion requires an explicit scene intention. Exercise each requested
state and both directions of relevant transitions, interruptions and reset/seek.

Serve one local gallery containing all accepted visuals. Provide per-asset state
buttons, transition playback and pause/seek; allow comparison with the original at
the same viewport, scale, pose and time. Record differences instead of calling any
working SVG a match. Accept the combined baseline before using it in scenes, then
repeat fidelity checks in context: gallery acceptance alone cannot prevent a scene
wrapper from applying a transform to the wrong element.

## Research behind this contract

This adapts a common 2D pipeline: story/timing, reviewed designs, reusable assets/rigs,
animation, then compositing. Design and rough audio may feed back into story before
final lock; the separate gallery is a lightweight browser equivalent of asset/rig
testing, not a guarantee of good acting. See [Toon Boom's workflow](https://helpcentre.toonboom.com/hc/en-ca/articles/57086503432083-About-2D-Animation-workflow-steps).

Claude's product surfaces change; verify the account's actual tools and keep the HTML
fallback usable. See [Claude artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
and [Design surface changes](https://support.claude.com/en/articles/17440474-move-from-standalone-claude-design-to-claude).
SVG [groups](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
support separate transform targets; [SVG image restrictions](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image)
explain why source embedding matters.
