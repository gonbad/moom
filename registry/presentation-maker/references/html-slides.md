# Independently authored HTML slides

Use separate fragment files for different slide compositions:

```json
{"title":"Demo","language":"en","direction":"ltr","assets":"assets",
 "slides":[{"title":"A chart","file":"slides/chart.html"},
           {"title":"Code","html":"<h1>Example</h1><pre><code>print(1)</code></pre>"}]}
```

src/slides/chart.html can contain `<h1>Results</h1><img src="../assets/chart.svg" alt="Results">`.
The renderer rebases that asset path, copies the declared assets directory into dist/,
and verifies local dependencies. Scope custom CSS to a slide or a specific class.
Keep private inputs outside the assets directory. Plain `body` remains escaped text;
use authored HTML deliberately instead of disabling escaping for imported source text.

Run scripts/render.py through Moom with --input and --output. Deliver the entire output
folder (or a ZIP made from its contents); open index.html directly with networking off.
Landscape is the default. Small screens can scroll slide content vertically; horizontal
swipes navigate, and vertical gestures keep reading the current slide. The overview
supports Tab, Space/Enter selection, spatial arrows, G and Escape. Test these behaviors
in the actual browser, together with notes, fullscreen, RTL and browser back/forward.
