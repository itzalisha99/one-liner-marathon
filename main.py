#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one one-line comedy joke (1-280 chars, UTF-8) to /output/entry.txt.
"""

import os

LINE = "My printer only works when I don't need it. It's not broken, it's just unionised."


def validate(text):
    """Mirror the bounty gate: 1-280 chars, UTF-8, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
