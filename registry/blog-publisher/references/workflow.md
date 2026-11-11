# Blog production sequence

1. **Brief & Confirmation (`/brief`):**
   Capture the post's core insight, target audience, intended outcome, and source materials.
   Review uncertain requirements before implementation.

2. **Story & Structure (`/story`):**
   Outline the sequence of ideas or reading scenes. Structure into clear checkpoints.

3. **Content & Claims (`/content`):**
   Draft complete prose, code snippets, diagrams, or datasets. Ensure every factual claim
   has supporting evidence.

4. **Visual Layout (`/layout`):**
   Define the visual canvas for the post. Each post is autonomous:
   - Articles use comfortable reading widths, clean typography, and callouts.
   - Slide decks use 16:9 horizontal canvases with keyboard and touch navigation.
   - Academic papers use formal A4 layout, two-column text, and theorem callouts.
   - Interactive tools embed runnable client-side widgets.

5. **Build & Minify (`/build`):**
   Compile the post into a minimized, self-contained `dist/` directory. Update the root
   publication index with a new card.

6. **Check & Verify (`/check`):**
   Verify responsiveness, keyboard navigation, broken internal links, and enforce the
   Zero-Remote-Leak invariant (no unverified external CDN fonts, scripts, or styles).

7. **Offline Package (`/package`):**
   Assemble a standalone offline ZIP archive containing the post's complete offline runtime.

8. **Deploy (`/deploy`):**
   Transfer the compiled static `dist/` tree to the configured static web server origin.
