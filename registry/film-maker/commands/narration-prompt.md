---
name: narration-prompt
description: Review one sequence of editable recording prompts.
---

# /narration-prompt

Read AGENTS.md, the four documents in docs/constitution/, the installed profile, Job and status in docs/kandoo/living/, and its references/production.md. Resolve the selected Project, open version, current input and submitted reviews. Work under projects/ID/ for media and docs/projects/ID/ for living notes and versioned Markdown reviews.

Use the explicitly or softly confirmed script and voice plan. Write one numbered review document for the sequence. List prompts in script order and choose their scope from how the voices will be recorded.

- **Separate voices or TTS.** Write one independently copyable prompt per uninterrupted speaking turn, including each narrator passage in a mixed scene. Keep consecutive sentences or questions together when the speaker carries one thought through them. Link the turn to its dialogue shot and any reaction shots it spans.
- **Actors performing together.** Give them one scene prompt containing the speaker-labelled exchange and cues for pauses, interruptions and overlap. Keep the individual turns linked to their shot IDs for editing.
- **Continuous solo narration.** Give the narrator one prompt for the voiced sequence, even when the pictures cross scene boundaries.

Skip silent beats. For an intentional replay of a recording, identify the original take or planned source and the excerpt to use. A picture cut can fall inside any of these performances.

Label each prompt with its sequence, relevant scene and shot IDs, speaker or cast, and revision. Give the performer directions for tone, pace, pauses and pronunciation separately from a copyable block containing only the exact spoken words in the chosen language. Keep a consistent voice for each speaker. Subtitles and directions stay outside the speech input.

Give each new recording two clearly labelled, independently copyable blocks: **Style instructions** and **Spoken text**. Write the style as a short direction the actor can perform or paste into a TTS style field. Include the speaker’s established voice, language or dialect, pace, and the emotional change at this beat. For a joint take, describe how the actors listen and respond. If a tool only accepts spoken text, use the style as a performance or voice-selection guide.

Before handing over the prompts, create a sequence folder under `projects/ID/existing/voices/` (for example `sequence-01/`). Put its actual path and a working folder link near the top of the review sheet. Give a suggested filename beside each new take, including the prompt ID, speaker or cast and take number. Keep the actual audio extension and increment the take number for retries. For shared takes or playback, identify the file that covers those cues. In the chat handoff give the destination, a brief style cue and the review sheet link. When the files are ready, the participant can run /narrate.

Show the draft before sending the participant to record. Ask “Would you like to change the words or how they’re read?” They can edit either part directly in Markdown, leave comments below the block or in chat, or use it as written. On submission, reread their actual edits. Preserve their wording, apply requested revisions, and show the resulting copyable prompt for use or further edits. Keep submitted drafts and comments identifiable by revision. When the participant selects a draft for recording, save that exact text and update living/script.md if the words changed. A request for changes leaves this sequence in prompt review. Resume here until they choose a version or provide the take they made from it.

Record evidence, pending review and next action in Project and shared status. Apply the four-domain check and show the localized pipeline. Keep human acceptance separate from technical checks.
