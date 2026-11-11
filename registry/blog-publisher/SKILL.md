---
name: blog-publisher
description: Publish an independent multi-post journal or publication site with an index, heterogeneous post layouts, offline ZIP bundles, and static deployment.
license: MIT
metadata:
  version: "0.1.0"
  author: gonbad
  origin: https://github.com/gonbad/moom
---

# Blog publisher

Use for multi-post publishing projects where each post represents an independent,
self-contained experience (an article, tutorial, academic paper, slide deck, or interactive tool)
alongside an aggregated root index.

Read [the production sequence](references/workflow.md); open only the current step's command.
The package has no external runtime dependencies beyond Python 3.10+.

The eight-step production chain:
1. [brief](commands/brief.md): Confirm inputs, thesis, and target audience.
2. [story](commands/story.md): Narrative arc and reading structure.
3. [content](commands/content.md): Core content, facts, and code examples.
4. [layout](commands/layout.md): Visual canvas, typography, and interactive components.
5. [build](commands/build.md): Minify into project dist/ and update root index.
6. [check](commands/check.md): Offline assets, links, responsiveness, and zero-leak invariant.
7. [package](commands/package.md): Standalone offline ZIP bundle.
8. [deploy](commands/deploy.md): Static sync to server origin.

Apply [the quality criteria](references/quality.md) across each stage. Distinguish source
fidelity, functional rendering, and human acceptance.
