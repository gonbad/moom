"""Observable publishing boundaries and complete offline releases in temporary workspaces."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "registry/blog-publisher/scripts"
sys.path.insert(0, str(SCRIPTS))
import publisher


class Publishing(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="publication-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "workspace"
        publisher.write_json(self.root / "publication.json", {"origin": "https://example.invalid"})
        self.project("000-index", "index", '<a href="001-post/">Read</a>')
        self.post = self.project("001-post", "post", '<h1>Example</h1><p>Complete offline content.</p>')

    def project(self, identifier, kind, html, publish=True):
        folder = self.root / "projects" / identifier
        (folder / "src").mkdir(parents=True)
        (folder / "src/index.html").write_text("<!doctype html>\n<html><body>\n  " + html + "\n</body></html>")
        publisher.write_json(folder / "project.json", {"id": identifier, "kind": kind, "source": "src", "version": "0.1.0", "publish": publish})
        return folder

    def test_release_has_materials_packages_and_no_private_or_draft_content(self):
        self.project("002-draft", "post", "UNPUBLISHED", False)
        for name in ["inputs/private.txt", "secrets/test.key", "versions/V0.1/source.md"]:
            p = self.post / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("SYNTHETIC_PRIVATE_MARKER")
        material = self.post / "materials/worksheet.txt"
        material.parent.mkdir()
        material.write_text("Public worksheet")
        meta = json.loads((self.post / "project.json").read_text())
        meta["materials"] = [{"source": "materials/worksheet.txt", "target": "downloads/worksheet.txt"}]
        publisher.write_json(self.post / "project.json", meta)
        result = publisher.build(self.root)
        self.assertEqual(result["offline_archives"], 1)
        self.assertFalse((self.root / "dist/002-draft").exists())
        manifest = json.loads((self.root / "dist/release.json").read_text())
        archive = self.root / "dist" / manifest["projects"]["001-post"]["targets"]["offline"]
        with zipfile.ZipFile(archive) as bundle:
            self.assertEqual(bundle.read("downloads/worksheet.txt"), b"Public worksheet")
            self.assertIn("offline-manifest.json", bundle.namelist())
            self.assertFalse(any("secrets" in n or "inputs" in n or "versions" in n for n in bundle.namelist()))
        self.assertTrue((self.post / "dist/index.html").is_file())

    def test_root_private_and_symlink_sources_are_rejected(self):
        meta_path = self.post / "project.json"
        original = json.loads(meta_path.read_text())
        for source in [".", "inputs"]:
            publisher.write_json(meta_path, {**original, "source": source})
            with self.assertRaises(ValueError):
                publisher.build(self.root)
        publisher.write_json(meta_path, original)
        (self.post / "src/linked.txt").symlink_to(self.post / "project.json")
        with self.assertRaisesRegex(ValueError, "symlink"):
            publisher.build(self.root)

    def test_deleted_files_and_projects_are_removed_on_rebuild(self):
        old = self.post / "src/withdrawn.html"
        old.write_text("Withdrawn")
        extra = self.project("002-other", "post", "Old post")
        publisher.build(self.root)
        old.unlink()
        shutil.rmtree(extra)
        publisher.build(self.root)
        self.assertFalse((self.root / "dist/001-post/withdrawn.html").exists())
        self.assertFalse((self.root / "dist/002-other").exists())

    def test_failed_validation_keeps_previous_release(self):
        publisher.build(self.root)
        before = (self.root / "dist/release.json").read_bytes()
        (self.post / "src/index.html").write_text('<script src="//invalid.example/remote.js"></script>')
        with self.assertRaises(ValueError):
            publisher.build(self.root)
        self.assertEqual((self.root / "dist/release.json").read_bytes(), before)

    def test_checks_reject_actual_remote_and_missing_dependencies(self):
        for content in ['<script src="//invalid.example/code.js"></script>',
                        '<style>@font-face{font-family:x;src:url(https://invalid.example/a.woff2)}</style>',
                        '<link rel="stylesheet" href="missing.css">',
                        '<img src="missing.png">', '<iframe src="https://invalid.example"></iframe>']:
            (self.post / "src/index.html").write_text(content)
            with self.assertRaises(ValueError):
                publisher.build(self.root)

    def test_html_minification_preserves_code_and_preformatted_data(self):
        content = '<html>\n  <p>A   B</p>\n<pre>  x\n    y</pre><script>const x = "a  b";\n// keep this\n</script></html>'
        result = publisher.minify_html(content)
        self.assertLess(len(result), len(content))
        self.assertIn('<pre>  x\n    y</pre>', result)
        self.assertIn('const x = "a  b";\n// keep this\n', result)

    def test_installed_cli_resolves_workspace_from_an_unrelated_directory(self):
        scripts = self.root / "job/blog-publisher/scripts"
        shutil.copytree(SCRIPTS, scripts, ignore=shutil.ignore_patterns("__pycache__"))
        output = Path(self.temp.name) / "built"
        result = subprocess.run([sys.executable, str(scripts / "build.py"), "--output", str(output)], cwd=Path(self.temp.name), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((output / "release.json").is_file())
        (output / "001-post/index.html").write_text("corrupted after build")
        result = subprocess.run([sys.executable, str(scripts / "check.py"), "--output", str(output)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

    def test_draft_preview_is_distinct_from_a_production_release(self):
        self.project("002-draft", "post", "Local preview", False)
        publisher.build(self.root, preview="002-draft")
        manifest = json.loads((self.root / "dist/release.json").read_text())
        self.assertTrue(manifest["preview_only"])
        self.assertIn("002-draft", manifest["projects"])

    def test_ambiguous_paths_and_symlink_outputs_are_rejected(self):
        meta = json.loads((self.post / "project.json").read_text())
        for public_path in [".", "a/../b", "/absolute"]:
            publisher.write_json(self.post / "project.json", {**meta, "public_path": public_path})
            with self.assertRaises(ValueError):
                publisher.build(self.root)
        publisher.write_json(self.post / "project.json", meta)
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        link = self.root / "linked-dist"
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            publisher.build(self.root, link)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
