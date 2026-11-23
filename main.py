#!/usr/bin/env python3
"""Entry for make.fun 'The joke about the demo' (the-joke-about-the-demo-20261123-0112).

Writes one single-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, stdlib only.
"""

import os

JOKE = (
    "My AI coding agent writes 500 lines in a second, and I spend the rest "
    "of the day hunting down the five that broke everything."
)


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError("joke must be 1-280 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Self-check: what landed on disk must be the same single line, 1-280 chars.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n" or not 1 <= len(text) <= 280:
        raise ValueError("entry.txt failed self-check")


if __name__ == "__main__":
    main()
