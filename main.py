#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

The program composes a single-line error message that names the real
failure in plain words, admits what the software knew, and tells the
user what to do next. It writes the line to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The failure, in plain words: what actually broke.
FAILURE = "Your file wasn't saved — the disk is full"
# The twist: the software knew and said nothing.
CONFESSION = "and the app knew all along. It just let you keep typing."
# What to do next.
FIX = "Free some space, then save again."


def compose_error() -> str:
    """Assemble the one-line error message from its three parts."""
    parts = [FAILURE, CONFESSION, FIX]
    line = " ".join(part.strip() for part in parts)
    return line.strip()


def main() -> None:
    line = compose_error()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
