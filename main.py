#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

The program composes a single-line error message that names the real
failure in plain words, admits what the software knew, and tells the
user what to do next. It writes the line to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The failure, in plain words: what actually broke.
FAILURE = "Your file wasn't saved — the disk is full,"
# The twist: the software knew before the user even started, and
# let them do the work anyway.
CONFESSION = "and the app knew before you started typing. It let you finish the paragraph anyway."
# What to do next.
FIX = "Free some space, then save again."


def compose_error() -> str:
    """Assemble the one-line error message from its three parts.

    The parts are joined with single spaces; the punctuation inside
    each part carries the pauses, so the line reads like something
    a person would actually say out loud.
    """
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
