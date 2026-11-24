#!/usr/bin/env python3
"""Dad Joke Showdown — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is one dad joke, at most 200 characters.
"""

import os
import sys

ENTRY = "I explained taxes to my kids by eating half their fries. Now they call me their fry-nance minister."


def self_check(entry: str) -> None:
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 200:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-200")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
