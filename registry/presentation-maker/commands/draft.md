# Draft the agreed slides

Keep src/slides.json with title, language, direction and slides. Plain slides use title
and body strings, which are escaped as text. For authored layouts use a slide's `html`
string or `file` path to a separate HTML fragment, relative to slides.json. Title remains
the overview label; an HTML slide supplies its own visible headings/composition.
Put public images, styles, fonts and scripts under src/assets/ (or declare an assets
folder in JSON). Relative src/href paths in fragment files are rebased to the deck root.
Use local assets and classic scripts, without fetch, module imports, or a server.
Read ../references/html-slides.md for an example. Review source fidelity in manageable
chunks and check coverage, language and order across the complete deck.
