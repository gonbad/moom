# Render and verify an offline presentation

Use the selected Project and current Job. Run the reviewed scripts/render.py helper
through `python3 moom.py run scripts/render.py --input projects/ID/src/slides.json
--output projects/ID/dist/index.html` (or with `slides.md`). The assistant resolves
ID from workspace.json. Inspect the rendered result directly in the browser via `file://`:
16:9 landscape aspect ratio, Left/Right arrow navigation (honoring RTL/LTR), overview
grid (`G`), speaker notes (`N`), fullscreen (`F`), and mobile touch swipe. Verify zero
remote asset leaks. Do not claim browser checks from a file-existence test. Record
readiness; record acceptance only with approval of this concrete revision. Keep source
and prior outputs for recovery.
