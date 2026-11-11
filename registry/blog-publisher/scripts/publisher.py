"""Static publication assembly and verification. Python 3.10+, standard library only."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

PRIVATE = {"inputs", "secrets", "versions", ".git", ".venv", "node_modules", "__pycache__", "docs"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def workspace(explicit=None):
    root = Path(explicit or os.environ.get("MOOM_WORKSPACE") or Path(__file__).resolve().parents[3]).resolve()
    if not (root / "projects").is_dir() or not (root / "publication.json").is_file():
        raise ValueError(f"Publication workspace needs projects/ and publication.json: {root}")
    return root


def confined(root, name):
    raw = root / name
    if any(part in PRIVATE or part.startswith(".env") for part in Path(name).parts):
        raise ValueError(f"Private path is not a publication asset: {name}")
    for path in [raw, *raw.parents]:
        if path == root.parent:
            break
        if path.is_symlink():
            raise ValueError(f"Publication paths cannot contain symlinks: {name}")
    path = raw.resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path leaves publication: {name}")
    return path


class MinifiedHTML(HTMLParser):
    """Collapse HTML formatting whitespace without rewriting code or preformatted text."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output, self.protected = [], []

    def handle_starttag(self, tag, attrs):
        self.output.append(self.get_starttag_text())
        if tag in {"pre", "code", "textarea", "script", "style", "svg", "math"}:
            self.protected.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.output.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")
        if self.protected and self.protected[-1] == tag:
            self.protected.pop()

    def handle_data(self, data):
        self.output.append(data if self.protected else re.sub(r"\s+", " ", data))

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")

    def handle_decl(self, decl):
        self.output.append(f"<!{decl}>")

    def handle_comment(self, data):
        if self.protected or data.startswith("[if"):
            self.output.append(f"<!--{data}-->")


def minify_html(text):
    parser = MinifiedHTML()
    parser.feed(text)
    parser.close()
    return "".join(parser.output).strip() + "\n"


def public_tree(source, target):
    if not (source / "index.html").is_file():
        raise ValueError(f"Explicit public source needs index.html: {source}")
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        confined(source, relative)
        if any(part.startswith(".") for part in relative.parts):
            raise ValueError(f"Hidden working file in public source: {path}")
        if not path.is_file() or path.suffix in {".py", ".pyc", ".map", ".pem", ".key"}:
            continue
        if path.suffix == ".md" and "downloads" not in relative.parts:
            continue
        if path.name in {"project.json", "workspace.json"}:
            raise ValueError(f"Working metadata in public source: {path}")
        dest = target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix.lower() in {".html", ".htm"}:
            dest.write_text(minify_html(path.read_text(encoding="utf-8")), encoding="utf-8")
        else:
            shutil.copy2(path, dest)


def validate_url(value, file, root, *, asset=True):
    value = value.strip()
    if not value or value.startswith("#"):
        return
    parsed = urlsplit(value)
    if parsed.scheme in {"data", "blob"}:
        return
    if parsed.scheme or parsed.netloc or value.startswith("//"):
        if not asset and parsed.scheme in {"http", "https", "mailto", "tel"}:
            return
        raise ValueError(f"Remote or unsupported runtime reference in {file.relative_to(root)}: {value}")
    if value.startswith("/"):
        raise ValueError(f"Use file-portable relative references in {file.relative_to(root)}: {value}")
    target = (file.parent / unquote(parsed.path)).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Reference leaves output in {file.relative_to(root)}: {value}")
    if target.is_dir():
        target /= "index.html"
    if not target.is_file():
        raise ValueError(f"Missing local reference in {file.relative_to(root)}: {value}")


def check_css(text, file, root):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", text, re.S | re.I):
        validate_url(match[2], file, root)
    for match in re.finditer(r"@import\s+(['\"])(.*?)\1", text, re.I):
        validate_url(match[2], file, root)


def check_js(text, file, root):
    for match in re.finditer(r"\b(?:fetch|import|Worker|WebSocket|EventSource|sendBeacon)\s*\(\s*(['\"])([^'\"]+)\1", text):
        validate_url(match[2], file, root)
    for match in re.finditer(r"\b(?:import|export)\s+[^;\n]*?\sfrom\s*(['\"])([^'\"]+)\1", text):
        validate_url(match[2], file, root)


class References(HTMLParser):
    def __init__(self, file, root, offline=False):
        super().__init__()
        self.file, self.root, self.offline = file, root, offline
        self.raw = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "base":
            raise ValueError(f"Base URLs break standalone output: {self.file}")
        for key in ("src", "href", "poster", "data" if tag == "object" else "xlink:href"):
            if key not in attrs:
                continue
            if self.offline and tag == "a" and ("data-online-only" in attrs or "data-home-link" in attrs):
                continue
            validate_url(attrs[key] or "", self.file, self.root, asset=tag != "a")
        if attrs.get("srcset") and not attrs["srcset"].startswith("data:"):
            for entry in attrs["srcset"].split(","):
                validate_url(entry.strip().split()[0], self.file, self.root)
        if attrs.get("style"):
            check_css(attrs["style"], self.file, self.root)
        if tag in {"style", "script"}:
            self.raw = tag

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == self.raw:
            self.raw = None

    def handle_data(self, data):
        if self.raw == "style":
            check_css(data, self.file, self.root)
        elif self.raw == "script":
            check_js(data, self.file, self.root)


def check_tree(root, *, offline=False):
    if not (root / "index.html").is_file():
        raise ValueError(f"Output needs index.html: {root}")
    count = 0
    for file in sorted(root.rglob("*")):
        if file.is_symlink():
            raise ValueError(f"Symlink in output: {file}")
        if not file.is_file():
            continue
        if any(part in PRIVATE or part.startswith(".env") for part in file.relative_to(root).parts):
            raise ValueError(f"Private working content in output: {file}")
        if file.suffix.lower() in {".html", ".htm", ".svg"}:
            parser = References(file, root, offline)
            parser.feed(file.read_text(encoding="utf-8"))
            parser.close()
        elif file.suffix == ".css":
            check_css(file.read_text(encoding="utf-8"), file, root)
        elif file.suffix in {".js", ".mjs"}:
            check_js(file.read_text(encoding="utf-8"), file, root)
        count += 1
    return count


def package(post, metadata, temporary):
    offline = temporary / (metadata["id"] + "-offline")
    shutil.copytree(post, offline)
    entry = offline / "index.html"
    entry.write_text(entry.read_text(encoding="utf-8").replace('data-delivery="online"', 'data-delivery="offline"'), encoding="utf-8")
    checksums = {p.relative_to(offline).as_posix(): digest(p) for p in sorted(offline.rglob("*")) if p.is_file()}
    write_json(offline / "offline-manifest.json", {"project": metadata["id"], "version": metadata["version"], "sha256": checksums})
    names = [metadata.get("archive", f"{metadata['id']}-v{metadata['version']}.zip"), *metadata.get("archive_aliases", [])]
    for name in names:
        if Path(name).name != name or not name.endswith(".zip"):
            raise ValueError(f"Archive must be a ZIP filename: {name}")
    archive = post / "downloads" / names[0]
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for file in sorted(offline.rglob("*")):
            if file.is_file():
                relative = file.relative_to(offline).as_posix()
                if relative in {"downloads/" + n for n in names}:
                    raise ValueError("Offline archive cannot contain itself")
                info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                bundle.writestr(info, file.read_bytes())
    for alias in names[1:]:
        shutil.copy2(archive, archive.parent / alias)
    return names[0]


def check_archive(archive):
    with zipfile.ZipFile(archive) as bundle, tempfile.TemporaryDirectory(prefix="offline-check-") as temp:
        root = Path(temp)
        for name in bundle.namelist():
            confined(root, name)
        if bundle.testzip():
            raise ValueError(f"Corrupt archive: {archive}")
        bundle.extractall(root)
        manifest = json.loads((root / "offline-manifest.json").read_text(encoding="utf-8"))
        check_hashes(root, manifest)
        return check_tree(root, offline=True)


def check_hashes(root, manifest):
    expected = manifest["sha256"]
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    excluded = {"release.json"} if (root / "release.json").is_file() else {"offline-manifest.json"}
    if actual - excluded != set(expected):
        raise ValueError("Output file inventory differs from its manifest; rebuild the release")
    for name, checksum in expected.items():
        if digest(confined(root, name)) != checksum:
            raise ValueError(f"Output checksum differs: {name}")


def check_release(output):
    manifest = json.loads((output / "release.json").read_text(encoding="utf-8"))
    check_hashes(output, manifest)
    count = check_tree(output)
    archives = 0
    for record in manifest["projects"].values():
        if record["kind"] == "post":
            check_archive(confined(output, record["targets"]["offline"]))
            archives += 1
    return {"ok": True, "files": count, "offline_archives": archives, "projects": list(manifest["projects"])}


def replace_tree(staged, destination):
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise ValueError(f"Refusing to replace non-directory output: {destination}")
    backup = destination.with_name(destination.name + ".previous")
    if backup.exists():
        raise ValueError(f"Recover previous interrupted build before replacing {backup}")
    if destination.exists():
        destination.rename(backup)
    try:
        staged.rename(destination)
    except BaseException:
        if backup.exists():
            backup.rename(destination)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def fold_calendar(text):
    lines = []
    for line in text.splitlines():
        fragment = ""
        for char in line:
            if len((fragment + char).encode("utf-8")) > 75:
                lines.append(fragment)
                fragment = " "
            fragment += char
        lines.append(fragment)
    return ("\r\n".join(lines) + "\r\n").encode("utf-8")


def build(root, output=None, preview=None):
    output = Path(output) if output else root / "dist"
    if output.is_symlink():
        raise ValueError("Refusing symlinked output")
    output = output.resolve()
    if output == root or root.is_relative_to(output) or output.is_relative_to(root / "projects"):
        raise ValueError("Aggregate output must be separate from the workspace and Project source")
    settings = json.loads((root / "publication.json").read_text(encoding="utf-8"))
    origin = settings["origin"].rstrip("/")
    parsed = urlsplit(origin)
    if parsed.scheme != "https" or not parsed.hostname or parsed.path or parsed.query or parsed.fragment or parsed.username:
        raise ValueError("Select an HTTPS publication origin without a path")
    available = []
    for folder in sorted((root / "projects").iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue
        meta_file = folder / "project.json"
        if not meta_file.is_file():
            raise ValueError(f"Declare public source, kind, version and publish in {meta_file}")
        metadata = json.loads(meta_file.read_text(encoding="utf-8"))
        if not isinstance(metadata.get("publish"), bool):
            raise ValueError(f"Project publish must be an explicit true/false: {meta_file}")
        if metadata["id"] != folder.name or metadata.get("kind") not in {"index", "post"}:
            raise ValueError(f"Invalid Project identity or kind: {meta_file}")
        if not metadata.get("publish") and metadata.get("published_snapshot") and folder.name != preview:
            identifier = metadata["id"]
            snapshot = (folder / metadata["published_snapshot"]).resolve()
            if not snapshot.is_relative_to(folder.resolve()):
                raise ValueError("Published snapshot leaves Project")
            folder = snapshot
            metadata = json.loads((folder / "project.json").read_text(encoding="utf-8"))
            if metadata.get("id") != identifier:
                raise ValueError("Published snapshot must belong to the same Project")
        available.append((folder, metadata))
    if preview and not any(meta["id"] == preview for _, meta in available):
        raise ValueError(f"Unknown preview Project: {preview}")
    selected = [(folder, meta) for folder, meta in available if meta.get("publish") or meta["id"] == preview]
    selected.sort(key=lambda item: item[1]["kind"] != "index")
    if sum(meta["kind"] == "index" for _, meta in selected) != 1:
        raise ValueError("Exactly one explicitly authored publication index is required")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="publication-build-", dir=output.parent) as temp:
        temporary = Path(temp)
        staged = temporary / "site"
        staged.mkdir()
        records, project_outputs, destinations = {}, {}, set()
        for folder, meta in selected:
            public_path = meta.get("public_path", "" if meta["kind"] == "index" else meta["id"])
            if public_path and (Path(public_path).is_absolute() or Path(public_path).as_posix() != public_path or any(part in {".", ".."} or part.startswith(".") for part in Path(public_path).parts)):
                raise ValueError(f"Use a canonical relative public path: {public_path}")
            if (meta["kind"] == "index" and public_path) or (meta["kind"] == "post" and not public_path):
                raise ValueError("Index must own the root and each post must own a subdirectory")
            if any(public_path == old or (old and public_path.startswith(old + "/")) or (public_path and old.startswith(public_path + "/")) for old in destinations):
                raise ValueError(f"Overlapping public paths: {public_path}")
            destinations.add(public_path)
            target = confined(staged, public_path)
            if meta["kind"] == "post" and target.exists():
                raise ValueError(f"Post overlaps the index's public assets: {public_path}")
            source = confined(folder, meta["source"])
            if source == folder.resolve():
                raise ValueError("Project root is private; select its explicit public source directory")
            if meta.get("build_command"):
                command = meta["build_command"]
                if not isinstance(command, list) or not command or not all(isinstance(s, str) for s in command):
                    raise ValueError("build_command must be a reviewed argv list")
                subprocess.run(command, cwd=folder, stdout=sys.stderr, check=True)
            public_tree(source, target)
            for material in meta.get("materials", []):
                resource = confined(folder, material["source"])
                destination = confined(target, material["target"])
                if not resource.is_file():
                    raise ValueError(f"Prepare declared material before build: {resource}")
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(resource, destination)
            for calendar in target.rglob("*.ics"):
                calendar.write_bytes(fold_calendar(calendar.read_text(encoding="utf-8").replace("URL:https://blog.kiloapp.ir/", f"URL:{origin}/")))
            entry = target / "index.html"
            entry.write_text(entry.read_text(encoding="utf-8").replace('<meta name="journal-origin" content="https://blog.kiloapp.ir">', f'<meta name="journal-origin" content="{origin}">'), encoding="utf-8")
            record = {"source": folder.relative_to(root).as_posix(), "kind": meta["kind"], "version": meta["version"], "public_path": public_path}
            if meta["kind"] == "post":
                archive = package(target, meta, temporary)
                record["targets"] = {"web": f"{public_path}/index.html", "offline": f"{public_path}/downloads/{archive}"}
            records[meta["id"]] = record
            local_output = temporary / (meta["id"] + "-dist")
            shutil.copytree(target, local_output)
            project_outputs[meta["id"]] = local_output
        posts = [key for key, value in records.items() if value["kind"] == "post"]
        active = os.environ.get("MOOM_PROJECT")
        primary = active if active in posts else (posts[-1] if posts else None)
        manifest = {"version": records[primary]["version"] if primary else "0.1", "origin": origin,
                    "post": records[primary]["public_path"] if primary else None, "preview_only": bool(preview),
                    "projects": records, "targets": records[primary]["targets"] if primary else {},
                    "sha256": {p.relative_to(staged).as_posix(): digest(p) for p in sorted(staged.rglob("*")) if p.is_file()}}
        write_json(staged / "release.json", manifest)
        result = check_release(staged)
        for identifier, local_output in project_outputs.items():
            destination = root / "projects" / identifier / "dist"
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix="project-build-", dir=destination.parent) as local_temp:
                local_staged = Path(local_temp) / "dist"
                shutil.copytree(local_output, local_staged)
                replace_tree(local_staged, destination)
        replace_tree(staged, output)
    return {**result, "built": str(output), "preview_only": bool(preview)}
