# Check: verify links, rendering, and offline isolation

Inspect the built post in a browser:
1. Verify responsiveness and layout fidelity.
2. Confirm all internal links and media resolve locally.
3. Validate zero remote network calls (`http://` or `https://` in assets).
4. Run `python3 moom.py run scripts/check.py`.
