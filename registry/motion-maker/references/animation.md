# Scene timing, preview and export

## Scene contract before production

For each stable scene ID record start/duration, narrative purpose, visible assets and
placement, exact short on-screen copy, narration, subtitle text/policy, entry state,
actions/holds, exit state and transition to the next scene. Keep narration out of
on-screen paragraphs unless deliberately chosen. Publishing captions live separately;
speaker/recording notes and controls are not content. A scene may intentionally be still.
Every movement needs a communicative purpose, target group, pivot, duration and easing.

Read narration aloud or use an explicitly selected temporary voice track during story.
Try a rough timed storyboard/animatic with placeholders before polishing assets. Test
reading time, emphasis, breathing room and the closing hold. A word-count estimate is
a provisional budget, not proven voice timing. Rough audio and visual tests can revise
the story; final dubbing still follows accepted picture. Do not promise automatic lip
sync unless it is separately scoped and tested.

## One deterministic scene clock

Build a representative short scene (normally about 5–8 seconds) using the accepted
asset sources. Include the hardest required gesture/state transition and text layout.
Compare it with the gallery at matching states before building the rest. Preserve
approved paths/classes/keyframes and record any necessary timing integration changes.

Define one explicit scene/composition time and a seek operation. Derive scene selection,
SVG transforms, text visibility and all animation phases from it. For CSS/Web Animations,
pause autonomous playback and set animation `currentTime` (or equivalent deterministic
state); for procedural transforms, derive values from the same clock. Preserve approved
easing/geometry. Wall-clock CSS animations, timers, random jitter and uncontrolled media
playback must not compete with the composition clock. Seeking repeatedly to time T,
or reaching it after a pause/restart, must give the same visual result. See
[Animation.currentTime](https://developer.mozilla.org/en-US/docs/Web/API/Animation/currentTime).

Serve HTML locally. Provide play/pause, replay, seek and scene selection, with narration
or recording guidance outside the clean composition. Verify behavior at exact cuts,
mid-transition, first and last frames, interrupted playback and backward seeking. Avoid
continual bobbing, unsupported emotional claims, arbitrary motion and unreadable moving
text. Respect reduced motion in interactive previews without changing the chosen export
unexpectedly. Test Persian shaping, RTL and font loading when applicable.

## Render only the accepted revision

`/render` requires both explicit rendering intent and acceptance of the current HTML
preview, identified by source revision/hashes, viewport, frame rate and duration. The
command itself supplies render intent but cannot silently accept unseen changes. Do
not start frame capture merely because the preview compiles or a review form was submitted.

The assistant checks local dependencies and prepares a short representative render
sample before the full encode. Wait for fonts, images and composition readiness; seek
each frame at an explicit time and await a stable painted frame. Capture only the
composition, excluding buttons, debug overlays, teleprompter/narration text, timers and
decorative audio bars. Subtitles appear only according to the approved output contract.
Account for exact duration and frame count; inspect scene boundaries and final hold.

Use bounded memory/disk and a streaming or staged encoding path. Handle encoder errors,
stdin backpressure, cancellation, closed pipes and process cleanup; a partial file must
never replace a previous accepted export. Write a temporary/new output, check exit
status and probe the actual encoded dimensions, codec, frame rate and duration before
promoting it. Compare selected encoded frames with the accepted HTML, then watch the
complete result. Record real elapsed stages when a slow capture/encode needs diagnosis.

## Voice and final timing

Default to a manual external recording or TTS workflow: give the approved narration,
pronunciation notes and per-scene timing targets in Markdown; import the resulting
audio, check rights/voice consent when relevant and align it locally. TTS returns
audio; it does not itself assemble or synchronize a final film. See
[Gemini speech generation](https://ai.google.dev/gemini-api/docs/speech-generation).

Do not silently buy access or automate an API. Reuse explicit authorization if the
participant selects automation. Listen to the complete voice track and verify names,
numbers, Persian pronunciation if applicable, leading/trailing silence, clipping,
scene alignment and ending. Mux/review locally. If real speech needs a timing change,
invalidate affected preview/render/subtitle evidence, return to animation and review
the changed revision before replacing the export. Avoid compressing speech until it
is unintelligible just to preserve an arbitrary picture duration.
