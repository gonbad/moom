"""Load authored slide fragments and verify their portable local dependencies."""
import html
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit


class Fragment(HTMLParser):
    def __init__(self, file, root):
        super().__init__(convert_charrefs=False)
        self.file, self.root, self.output = file, root, []

    def handle_starttag(self, tag, attrs):
        if tag in {"html", "head", "body", "title", "meta"}:
            return
        content = self.get_starttag_text()
        for key, value in attrs:
            if key in {"src", "href", "poster"} and value and not value.startswith("#") and not urlsplit(value).scheme and not value.startswith("//"):
                parsed = urlsplit(value)
                target = (self.file.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(self.root):
                    raise ValueError(f"Slide asset leaves input directory: {value}")
                relative = target.relative_to(self.root).as_posix()
                if parsed.fragment:
                    relative += "#" + parsed.fragment
                content = re.sub(r"\b" + key + r"\s*=\s*(['\"])(.*?)\1", lambda m: key + '="' + html.escape(relative, quote=True) + '"', content, count=1, flags=re.I)
        self.output.append(content)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag not in {"html", "head", "body", "title", "meta"}:
            self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(data)

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")


def load_fragment(file, root):
    parser = Fragment(file, root)
    parser.feed(file.read_text(encoding="utf-8"))
    return "".join(parser.output)


def validate_offline(root):
    root = root.resolve()

    def reference(value, file, asset=True):
        if not value or value.startswith(("#", "data:", "blob:")):
            return
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value.startswith("/"):
            if not asset and parsed.scheme in {"http", "https", "mailto", "tel"}:
                return
            raise ValueError(f"Offline slides need local relative assets: {value}")
        target = (file.parent / unquote(parsed.path)).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            raise ValueError(f"Missing or nonlocal presentation asset in {file.name}: {value}")

    class Assets(HTMLParser):
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "base":
                raise ValueError("Slide fragments cannot set a base URL")
            for key in ("src", "href", "poster", "xlink:href", "data" if tag == "object" else "src"):
                if key in attrs:
                    reference(attrs[key], self.file, tag != "a")
            if attrs.get("srcset") and not attrs["srcset"].startswith("data:"):
                for candidate in attrs["srcset"].split(","):
                    reference(candidate.strip().split()[0], self.file)
            if attrs.get("style"):
                css(attrs["style"], self.file)
            self.raw = tag if tag in {"style", "script"} else None

        handle_startendtag = handle_starttag

        def handle_endtag(self, tag):
            if tag == self.raw:
                self.raw = None

        def handle_data(self, data):
            if self.raw == "style":
                css(data, self.file)
            if self.raw == "script":
                js(data)

    def css(text, file):
        for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)|@import\s+(['\"])(.*?)\3", text, re.S | re.I):
            reference(match[2] if match[1] is not None else match[4], file)

    def js(text):
        if re.search(r"\b(?:fetch|XMLHttpRequest|WebSocket|EventSource|import)\s*\(", text):
            raise ValueError("Offline presentation runtime cannot fetch or import dependencies")

    for file in root.rglob("*"):
        if file.is_symlink():
            raise ValueError("Presentation output cannot contain symlinks")
        if file.suffix in {".html", ".svg"}:
            parser = Assets()
            parser.file, parser.raw = file, None
            parser.feed(file.read_text(encoding="utf-8"))
        elif file.suffix == ".css":
            css(file.read_text(encoding="utf-8"), file)
        elif file.suffix in {".js", ".mjs"}:
            js(file.read_text(encoding="utf-8"))
