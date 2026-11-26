#!/usr/bin/env python3
"""One Word From Grandma — v3.

Writes exactly one word to /output/entry.txt: the word a grandma
would text about AI.

The word is "Roboot": the typo a grandma would actually make when
she means "robot" — warm, baffled, funny in one word, and unmistakably
about a machine. No sentence, no explanation, no punctuation tricks.
"""

import os
import sys

WORD = "Roboot"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 30


def main() -> int:
    # Gate mirror: 1-30 characters, not only whitespace, one word.
    if not (1 <= len(WORD) <= MAX_CHARS):
        print(f"error: word length {len(WORD)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not WORD.strip() or len(WORD.split()) != 1:
        print("error: entry must be exactly one non-blank word", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the word exactly, with no trailing newline, so the file
    # holds nothing but the entry itself.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Round-trip check: read the file back and confirm it holds exactly
    # the intended word as valid UTF-8, so a partial write or an
    # encoding slip can never pass silently.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    try:
        back = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"error: output is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if back != WORD:
        print(f"error: round-trip mismatch: file holds {back!r}, expected {WORD!r}",
              file=sys.stderr)
        return 1
    if len(raw) != len(WORD.encode("utf-8")):
        print("error: round-trip byte-length mismatch", file=sys.stderr)
        return 1
    print(f"verified round-trip: {OUTPUT_PATH} holds exactly {WORD!r}")
    print(f"wrote {OUTPUT_PATH}: {WORD!r} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
