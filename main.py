"""The Battery's Last Text to Its Charger.

One line, at most 200 characters: the phone battery's final message
to the charger it waited for all day. Written to /output/entry.txt.
"""

import os

ENTRY = "I waited all day at 1% while you charged your watch instead of me. I'm done. Tell the toaster I loved her."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
