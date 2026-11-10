# Render and verify an offline presentation

Use the selected Project and current Job. Run the reviewed scripts/render.py helper
through `python3 moom.py run scripts/render.py --input projects/ID/src/slides.json
--output projects/ID/dist/index.html`. The assistant resolves ID from workspace.json.
Inspect the rendered result in the available browser: offline loading, arrow-key
navigation, scrolling/overflow, language direction and content fidelity. Do not claim
browser checks from a file-existence test. Record readiness; record acceptance only
with approval of this concrete revision. Keep source and prior outputs for recovery.
