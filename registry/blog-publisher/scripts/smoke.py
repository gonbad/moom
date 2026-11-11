#!/usr/bin/env python3
"""Exercise assembly, packaging, and validation in an isolated sample workspace."""
import json
import tempfile
from pathlib import Path
from publisher import build, write_json

with tempfile.TemporaryDirectory(prefix="blog-publisher-smoke-") as temp:
    root = Path(temp)
    write_json(root / "publication.json", {"origin": "https://example.invalid"})
    for identifier, kind, content in [("000-index", "index", '<a href="001-post/">Post</a>'), ("001-post", "post", "<h1>Offline example</h1>")]:
        folder = root / "projects" / identifier
        (folder / "src").mkdir(parents=True)
        (folder / "src/index.html").write_text("<!doctype html><html><body>" + content + "</body></html>")
        write_json(folder / "project.json", {"id": identifier, "kind": kind, "version": "0.1.0", "source": "src", "publish": True})
    print(json.dumps(build(root)))
