#!/usr/bin/env python3
"""Render reviewed slide data to a standalone HTML file, without dependencies."""

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
        raise ValueError("A deck needs a title and a nonempty slides list")
    if (
        not isinstance(language, str)
        or not re.fullmatch(r"[a-zA-Z]{2,8}(?:-[a-zA-Z0-9]{1,8})*", language)
        or direction not in ("ltr", "rtl")
    ):
        raise ValueError("Use a valid language tag and ltr/rtl direction")
    sections = []
    for number, slide in enumerate(slides, 1):
        if (
            not isinstance(slide, dict)
            or not isinstance(slide.get("title"), str)
            or not isinstance(slide.get("body"), str)
            or not isinstance(slide.get("source_note", ""), str)
        ):
            raise TypeError(
                "Each slide needs title and body strings, with an optional source_note string"
            )
        note = (
            f"<footer>{html.escape(slide['source_note'])}</footer>"
            if slide.get("source_note")
            else ""
        )
        sections.append(
            f'<section id="slide-{number}" tabindex="0"><small>{number} / {len(slides)}</small><h1>{html.escape(slide["title"])}</h1><p>{html.escape(slide["body"])}</p>{note}</section>'
        )
    return f'''<!doctype html>
<html lang="{language}" dir="{direction}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#142e2a;color:#f6f0df;font:clamp(18px,2.3vw,32px)/1.65 system-ui,sans-serif}}section{{min-height:100vh;padding:8vh 8vw;scroll-margin:0}}h1{{max-width:24ch;font-size:clamp(32px,5vw,72px);line-height:1.2;color:#edbd76}}p{{max-width:65ch;white-space:pre-wrap;overflow-wrap:anywhere}}small,footer{{font-size:16px;opacity:.8}}footer{{margin-top:3rem}}html{{scroll-snap-type:y proximity}}section{{scroll-snap-align:start}}nav{{position:fixed;bottom:1rem;right:1rem;display:flex;gap:.5rem}}button{{font:inherit;font-size:16px;padding:.5rem 1rem;cursor:pointer}}@media print{{section{{break-after:page;min-height:auto}}nav{{display:none}}}}</style></head>
<body>{"".join(sections)}<nav aria-label="Slide navigation"><button type="button" id="previous" aria-label="Previous slide">↑</button><button type="button" id="next" aria-label="Next slide">↓</button></nav>
<script>const slides=[...document.querySelectorAll('section')];function move(delta){{let current=slides.reduce((best,s,i)=>Math.abs(s.getBoundingClientRect().top)<Math.abs(slides[best].getBoundingClientRect().top)?i:best,0);slides[Math.max(0,Math.min(slides.length-1,current+delta))].scrollIntoView();}}document.querySelector('#previous').onclick=()=>move(-1);document.querySelector('#next').onclick=()=>move(1);document.addEventListener('keydown',e=>{{if(['ArrowDown','ArrowRight','PageDown'].includes(e.key)){{e.preventDefault();move(1);}}else if(['ArrowUp','ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();move(-1);}}}});</script></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = render(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(
        json.dumps({"artifact": str(args.output), "bytes": args.output.stat().st_size})
    )


if __name__ == "__main__":
    main()
