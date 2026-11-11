# Verify standalone delivery

The build generates each post's downloads/ ZIP and offline-manifest.json inside it.
Run `python3 moom.py run scripts/check.py` to verify actual ZIP contents and hashes.
Extract the selected archive into a fresh directory and open index.html with networking
disabled. Check the real interactions, fonts and declared participant downloads.
Record the archive as ready only after those checks.
