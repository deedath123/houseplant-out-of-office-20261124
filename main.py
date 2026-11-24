"""The Houseplant Out-of-Office: writes the entry line to entry.txt.

Entry (114 chars, 114 bytes, one line, no trailing newline):
Out of office: I haven't been watered since March. I ate all 214 unread
emails for moisture. Your message is next.
entry.txt sha256: 2060c3f1811ab1c22b79bac8957ed8f34e58028665dbfa43760a241d43cbe5da
"""

import os

ENTRY = "Out of office: I haven't been watered since March. I ate all 214 unread emails for moisture. Your message is next."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
