#!/usr/bin/env python3
"""Render presentation slides into a standalone, offline, zero-CORS horizontal HTML deck."""

import argparse
import html
import json
import re
from pathlib import Path


def render(value):
    title = value.get("title")
    slides = value.get("slides")
    language = value.get("language", "en")
    direction = value.get("direction", "ltr")
    if (
        not isinstance(title, str)
        or not title.strip()
        or not isinstance(slides, list)
        or not slides
    ):
        raise ValueError("A presentation deck needs a title and a nonempty slides list")
    if (
        not isinstance(language, str)
        or not re.fullmatch(r"[a-zA-Z]{2,8}(?:-[a-zA-Z0-9]{1,8})*", language)
        or direction not in ("ltr", "rtl")
    ):
        raise ValueError("Use a valid language tag and ltr/rtl direction")

    slide_sections = []
    grid_tiles = []
    for number, slide in enumerate(slides, 1):
        if not isinstance(slide, dict):
            raise TypeError("Each slide must be an object")
        stitle = str(slide.get("title", f"Slide {number}"))
        sbody = str(slide.get("body", ""))
        snote = str(slide.get("speaker_notes") or slide.get("source_note") or "")

        esc_title = html.escape(stitle)
        esc_body = html.escape(sbody)
        esc_note = html.escape(snote)

        note_attr = f' data-notes="{esc_note}"' if esc_note else ""
        slide_sections.append(
            f'<section class="slide" id="slide-{number}" data-index="{number - 1}"{note_attr} tabindex="0">'
            f'<header class="slide-header"><span class="slide-num">{number} / {len(slides)}</span></header>'
            f'<div class="slide-content">'
            f'<h1>{esc_title}</h1>'
            f'<div class="slide-body">{esc_body}</div>'
            f'</div>'
            f'</section>'
        )

        grid_tiles.append(
            f'<button type="button" class="grid-card" data-goto="{number - 1}">'
            f'<span class="grid-num">{number}</span>'
            f'<span class="grid-title">{esc_title}</span>'
            f'</button>'
        )

    # Icons and labels depending on direction
    prev_icon = "→" if direction == "rtl" else "←"
    next_icon = "←" if direction == "rtl" else "→"

    return f"""<!doctype html>
<html lang="{language}" dir="{direction}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{
  --bg-deck: #0f172a;
  --bg-slide: #1e293b;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --accent: #38bdf8;
  --accent-gold: #f59e0b;
  --border-card: #334155;
  --font-stack: system-ui, -apple-system, "Segoe UI", Roboto, Vazirmatn, Tahoma, sans-serif;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 100%; height: 100%;
  background: var(--bg-deck);
  color: var(--text-main);
  font-family: var(--font-stack);
  overflow: hidden;
  user-select: none;
}}
.deck-stage {{
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2vmin;
}}
.deck-canvas {{
  width: min(94vw, 167.1vmin);
  height: min(52.88vw, 94vmin);
  aspect-ratio: 16 / 9;
  background: var(--bg-slide);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}}
.slide {{
  display: none;
  width: 100%; height: 100%;
  padding: 5% 6%;
  flex-direction: column;
  justify-content: space-between;
  outline: none;
}}
.slide.active {{
  display: flex;
  animation: fadeIn 0.15s ease-out;
}}
@keyframes fadeIn {{
  from {{ opacity: 0.6; transform: scale(0.995); }}
  to {{ opacity: 1; transform: scale(1); }}
}}
.slide-header {{
  display: flex;
  justify-content: flex-end;
  font-size: clamp(12px, 1.4vmin, 16px);
  color: var(--text-muted);
  font-weight: 600;
}}
.slide-content {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2vmin;
}}
.slide-content h1 {{
  font-size: clamp(24px, 4.2vmin, 52px);
  line-height: 1.25;
  color: var(--accent);
  font-weight: 700;
  max-width: 25ch;
}}
.slide-body {{
  font-size: clamp(16px, 2.4vmin, 28px);
  line-height: 1.6;
  color: var(--text-main);
  white-space: pre-wrap;
  max-width: 55ch;
}}
.deck-controls {{
  position: fixed;
  bottom: 1.5vmin;
  right: 2vmin;
  display: flex;
  gap: 0.6vmin;
  z-index: 100;
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(8px);
  padding: 0.5vmin 0.8vmin;
  border-radius: 8px;
  border: 1px solid var(--border-card);
}}
[dir="rtl"] .deck-controls {{ right: auto; left: 2vmin; }}
.btn {{
  background: #334155;
  color: var(--text-main);
  border: none;
  border-radius: 6px;
  font-family: inherit;
  font-size: clamp(12px, 1.5vmin, 15px);
  padding: 0.6vmin 1vmin;
  cursor: pointer;
  transition: background 0.15s;
}}
.btn:hover {{ background: #475569; }}
.progress-bar {{
  position: absolute;
  bottom: 0; left: 0;
  height: 4px;
  background: var(--accent);
  transition: width 0.2s ease;
}}
.rotation-hint {{
  display: none;
  position: fixed;
  top: 1vmin; left: 50%;
  transform: translateX(-50%);
  background: rgba(245, 158, 11, 0.9);
  color: #000;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
  z-index: 1000;
}}
@media (orientation: portrait) {{
  .rotation-hint {{ display: block; }}
}}
.modal {{
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.92);
  backdrop-filter: blur(12px);
  z-index: 200;
  display: flex;
  flex-direction: column;
  padding: 4vmin;
}}
.modal.hidden {{ display: none; }}
.modal-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2vmin;
  padding-bottom: 1vmin;
  border-bottom: 1px solid var(--border-card);
}}
.modal-title {{ font-size: 20px; font-weight: bold; color: var(--accent); }}
.grid-container {{
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1.5vmin;
  overflow-y: auto;
  padding-right: 1vmin;
}}
.grid-card {{
  aspect-ratio: 16 / 9;
  background: var(--bg-slide);
  border: 1px solid var(--border-card);
  border-radius: 8px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: inherit;
  color: var(--text-main);
  cursor: pointer;
  transition: transform 0.15s, border-color 0.15s;
}}
.grid-card:hover, .grid-card.current {{
  border-color: var(--accent);
  transform: translateY(-2px);
}}
.grid-card.current {{ border-width: 2px; }}
.grid-num {{ font-size: 11px; color: var(--text-muted); font-weight: bold; }}
.grid-title {{ font-size: 13px; font-weight: 600; line-height: 1.3; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }}
.notes-drawer {{
  position: fixed;
  bottom: 0; left: 0; right: 0;
  max-height: 40vh;
  background: #1e293b;
  border-top: 2px solid var(--accent);
  padding: 2vmin 3vmin;
  z-index: 150;
  overflow-y: auto;
  box-shadow: 0 -10px 25px rgba(0,0,0,0.5);
}}
.notes-drawer.hidden {{ display: none; }}
.notes-text {{ font-size: 16px; line-height: 1.6; color: #e2e8f0; white-space: pre-wrap; }}
@media print {{
  html, body {{ overflow: visible; height: auto; background: #fff; color: #000; }}
  .deck-stage {{ position: static; display: block; padding: 0; }}
  .deck-canvas {{ width: 100% !important; height: auto !important; aspect-ratio: auto; border: none; box-shadow: none; }}
  .slide {{ display: block !important; page-break-after: always; height: 100vh; padding: 40px; }}
  .deck-controls, .rotation-hint, .modal, .notes-drawer {{ display: none !important; }}
}}
</style>
</head>
<body>
<div class="rotation-hint">↻ Rotate device / جهت نمایش بهتر بچرخانید</div>
<div class="deck-stage">
  <main class="deck-canvas">
    {"".join(slide_sections)}
    <div class="progress-bar" id="progress"></div>
  </main>
</div>
<nav class="deck-controls" aria-label="Presentation Controls">
  <button type="button" class="btn" id="btn-prev" title="Previous Slide ({prev_icon})">{prev_icon}</button>
  <button type="button" class="btn" id="btn-next" title="Next Slide ({next_icon})">{next_icon}</button>
  <button type="button" class="btn" id="btn-grid" title="Slide Overview (G)">⊞ G</button>
  <button type="button" class="btn" id="btn-notes" title="Speaker Notes (N)">✎ N</button>
  <button type="button" class="btn" id="btn-fs" title="Fullscreen (F)">⛶ F</button>
</nav>
<div id="overview-modal" class="modal hidden">
  <div class="modal-header">
    <span class="modal-title">Slide Overview / فهرست اسلایدها</span>
    <button type="button" class="btn" id="btn-close-grid">✕ Close</button>
  </div>
  <div class="grid-container">
    {"".join(grid_tiles)}
  </div>
</div>
<aside id="notes-modal" class="notes-drawer hidden">
  <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
    <strong style="color:var(--accent);">Speaker Notes / یادداشت سخنران</strong>
    <button type="button" class="btn" id="btn-close-notes">✕</button>
  </div>
  <div id="notes-content" class="notes-text"></div>
</aside>
<script>
(function() {{
  const slides = Array.from(document.querySelectorAll('.slide'));
  const total = slides.length;
  const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
  let currentIndex = 0;

  const progress = document.getElementById('progress');
  const overviewModal = document.getElementById('overview-modal');
  const notesModal = document.getElementById('notes-modal');
  const notesContent = document.getElementById('notes-content');
  const gridCards = Array.from(document.querySelectorAll('.grid-card'));

  function showSlide(index) {{
    if (index < 0) index = 0;
    if (index >= total) index = total - 1;
    currentIndex = index;

    slides.forEach((s, i) => {{
      s.classList.toggle('active', i === currentIndex);
    }});
    gridCards.forEach((c, i) => {{
      c.classList.toggle('current', i === currentIndex);
    }});

    const pct = ((currentIndex + 1) / total) * 100;
    progress.style.width = pct + '%';

    const curSlide = slides[currentIndex];
    const notes = curSlide.getAttribute('data-notes') || 'No notes for this slide.';
    notesContent.textContent = notes;
    window.location.hash = 'slide-' + (currentIndex + 1);
  }}

  function next() {{ showSlide(currentIndex + 1); }}
  function prev() {{ showSlide(currentIndex - 1); }}

  function toggleGrid() {{
    overviewModal.classList.toggle('hidden');
    if (!overviewModal.classList.contains('hidden')) {{
      const curCard = gridCards[currentIndex];
      if (curCard) curCard.scrollIntoView({{ block: 'nearest' }});
    }}
  }}

  function toggleNotes() {{
    notesModal.classList.toggle('hidden');
  }}

  function toggleFullscreen() {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen().catch(() => {{}});
    }} else {{
      document.exitFullscreen().catch(() => {{}});
    }}
  }}

  document.getElementById('btn-next').onclick = next;
  document.getElementById('btn-prev').onclick = prev;
  document.getElementById('btn-grid').onclick = toggleGrid;
  document.getElementById('btn-close-grid').onclick = toggleGrid;
  document.getElementById('btn-notes').onclick = toggleNotes;
  document.getElementById('btn-close-notes').onclick = toggleNotes;
  document.getElementById('btn-fs').onclick = toggleFullscreen;

  gridCards.forEach(card => {{
    card.onclick = () => {{
      const idx = parseInt(card.getAttribute('data-goto'), 10);
      showSlide(idx);
      toggleGrid();
    }};
  }});

  document.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    if (e.key === 'Escape') {{
      overviewModal.classList.add('hidden');
      notesModal.classList.add('hidden');
      return;
    }}
    if (e.key === 'g' || e.key === 'G') {{
      e.preventDefault();
      toggleGrid();
      return;
    }}
    if (e.key === 'n' || e.key === 'N') {{
      e.preventDefault();
      toggleNotes();
      return;
    }}
    if (e.key === 'f' || e.key === 'F') {{
      e.preventDefault();
      toggleFullscreen();
      return;
    }}

    // Spatial navigation honoring direction
    if (isRtl) {{
      if (e.key === 'ArrowLeft' || e.key === 'PageDown' || e.key === ' ') {{
        e.preventDefault(); next();
      }} else if (e.key === 'ArrowRight' || e.key === 'PageUp') {{
        e.preventDefault(); prev();
      }}
    }} else {{
      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {{
        e.preventDefault(); next();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault(); prev();
      }}
    }}
  }});

  // Touch Swipe Support
  let touchStartX = 0;
  document.addEventListener('touchstart', (e) => {{
    touchStartX = e.changedTouches[0].screenX;
  }}, {{ passive: true }});

  document.addEventListener('touchend', (e) => {{
    const diff = e.changedTouches[0].screenX - touchStartX;
    if (Math.abs(diff) > 40) {{
      if (isRtl) {{
        if (diff > 0) prev(); else next();
      }} else {{
        if (diff < 0) next(); else prev();
      }}
    }}
  }}, {{ passive: true }});

  // Hash jump on load
  const match = window.location.hash.match(/^#slide-(\\d+)$/);
  if (match) {{
    showSlide(parseInt(match[1], 10) - 1);
  }} else {{
    showSlide(0);
  }}
}})();
</script>
</body>
</html>"""


def parse_input(path):
    text = path.read_text(encoding="utf-8").strip()
    if path.suffix == ".json" or text.startswith("{"):
        return json.loads(text)
    # Parse markdown slides separated by ---
    slides = []
    lines = text.splitlines()
    title = path.stem.replace("-", " ").title()
    cur_title = ""
    cur_body = []
    cur_notes = []
    in_notes = False

    def push_slide():
        nonlocal cur_title, cur_body, cur_notes, in_notes
        if cur_title or cur_body:
            slides.append({
                "title": cur_title or f"Slide {len(slides) + 1}",
                "body": "\n".join(cur_body).strip(),
                "speaker_notes": "\n".join(cur_notes).strip()
            })
        cur_title = ""
        cur_body = []
        cur_notes = []
        in_notes = False

    for line in lines:
        if line.strip() == "---":
            push_slide()
            continue
        if line.strip().startswith("???"):
            in_notes = True
            continue
        if in_notes:
            cur_notes.append(line)
        elif line.startswith("# ") and not cur_title:
            cur_title = line[2:].strip()
            if not title or title == path.stem.replace("-", " ").title():
                title = cur_title
        elif line.startswith("## ") and not cur_title:
            cur_title = line[3:].strip()
        else:
            cur_body.append(line)
    push_slide()

    return {
        "title": title or "Presentation",
        "slides": slides or [{"title": "Title", "body": "Content"}]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = parse_input(args.input)
    output = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(
        json.dumps({"artifact": str(args.output), "bytes": args.output.stat().st_size})
    )


if __name__ == "__main__":
    main()
