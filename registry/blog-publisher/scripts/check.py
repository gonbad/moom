#!/usr/bin/env python3
"""Exercise the blog publisher checks on local posts."""

from html.parser import HTMLParser
from pathlib import Path


class AssetChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.remote_assets = []
        self.tags = 0

    def handle_starttag(self, tag, attrs):
        self.tags += 1
        attrs = dict(attrs)
        for key in ("src", "href"):
            val = attrs.get(key, "")
            if val.startswith(("https://", "http://", "//")) and not val.startswith("//"):
                # Ignore ordinary external <a> links, only catch assets (script, link, img, audio, video)
                if tag in ("script", "link", "img", "audio", "video", "source"):
                    self.remote_assets.append((tag, val))


def check_html(content):
    checker = AssetChecker()
    checker.feed(content)
    if checker.remote_assets:
        raise ValueError(f"Found remote asset leak: {checker.remote_assets}")
    return checker.tags > 0


sample_html = """<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>نمونه پست کارگاه</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <h1>عنوان پست</h1>
  <p>متن کامل و بدون وابستگی به CDN خارجی.</p>
  <a href="https://example.com">لینک معتبر به منبع خارجی</a>
  <script src="assets/app.js"></script>
</body>
</html>"""

assert check_html(sample_html)
print("Blog publisher smoke check: zero remote asset leaks verified.")
