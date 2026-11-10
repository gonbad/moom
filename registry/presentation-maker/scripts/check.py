#!/usr/bin/env python3
"""Exercise the standalone renderer from the active, copied Job."""

import importlib.util
from html.parser import HTMLParser
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "presentation_renderer", Path(__file__).with_name("render.py")
)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class Deck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = 0
        self.remote_assets = []
        self.executables = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.slides += tag == "section"
        self.executables += tag == "script"
        for key in ("src", "href"):
            if attrs.get(key, "").startswith(("https:", "http:", "//")):
                self.remote_assets.append(attrs[key])


output = renderer.render(
    {
        "title": "Representative operation",
        "language": "fa",
        "direction": "rtl",
        "slides": [
            {"title": "First", "body": "<script>untrusted source text</script>"},
            {"title": "Second", "body": "A complete offline result."},
        ],
    }
)
deck = Deck()
deck.feed(output)
assert deck.slides == 2 and deck.executables == 1 and not deck.remote_assets
assert 'dir="rtl"' in output and "&lt;script&gt;" in output
print(
    "Rendered two offline slides; checked direction, escaping, structure and local assets. Browser/human review remains separate."
)
