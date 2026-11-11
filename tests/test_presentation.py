"""Verify independent HTML-slide authoring and portable asset delivery."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "registry/presentation-maker/scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("slide_renderer", SCRIPTS / "render.py")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class Presentation(unittest.TestCase):
    def test_authored_markup_is_distinct_from_escaped_plain_text(self):
        output = renderer.render({"title": "Deck", "slides": [
            {"title": "Text", "body": "<script>source text</script>"},
            {"title": "Code", "html": "<h1>Code</h1><pre><code>print(1)</code></pre>"}]})
        self.assertIn("&lt;script&gt;source text", output)
        self.assertIn("<pre><code>print(1)</code></pre>", output)

    def test_fragment_files_and_assets_produce_a_standalone_deck(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "src/slides").mkdir(parents=True)
            (root / "src/assets").mkdir()
            (root / "src/slides/chart.html").write_text('<h1>Chart</h1><img src="../assets/chart.svg" alt="Chart">')
            (root / "src/assets/chart.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><rect width="10" height="10"/></svg>')
            source = root / "src/slides.json"
            source.write_text(json.dumps({"title": "Example", "slides": [{"title": "Chart", "file": "slides/chart.html"}]}))
            output = root / "dist/index.html"
            result = subprocess.run([sys.executable, str(SCRIPTS / "render.py"), "--input", str(source), "--output", str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('src="assets/chart.svg"', output.read_text())
            self.assertTrue((root / "dist/assets/chart.svg").is_file())
            source.write_text(json.dumps({"title": "Remote dependency", "slides": [{"html": '<img src="//invalid.example/chart.png">'}]}))
            result = subprocess.run([sys.executable, str(SCRIPTS / "render.py"), "--input", str(source), "--output", str(output)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
