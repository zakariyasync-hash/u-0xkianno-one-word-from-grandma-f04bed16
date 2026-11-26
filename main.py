#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI.

The word is "doohickey": the classic grandma word for a mysterious
newfangled device she cannot quite name. Warm, a little baffled, and
funny in one word — she has been calling every unfamiliar gadget a
doohickey for decades, and the AI thing is simply the newest one.
"""

import os
import sys

WORD = "doohickey"
# Default is the competition output path; MAKEFUN_OUTPUT lets the program
# be exercised locally without touching /output.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
MAX_CHARS = 30


def main() -> int:
    # Gate-shaped validation, mirroring the competition gate:
    # UTF-8 text of 1 to 30 characters, not only whitespace, one word.
    if not WORD or len(WORD) > MAX_CHARS or not WORD.strip():
        print("error: entry word fails length check", file=sys.stderr)
        return 1
    if len(WORD.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    # Edge cases the gate's "one word" reading also forbids: punctuation
    # tricks, digits, control characters, or hidden whitespace inside
    # the word. The entry is plain letters only.
    if not WORD.isalpha():
        print("error: entry must be letters only", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in WORD):
        print("error: entry contains a control character", file=sys.stderr)
        return 1
    try:
        WORD.encode("utf-8")
    except UnicodeEncodeError:
        print("error: entry is not valid UTF-8", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the word, 9 bytes.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Round-trip check: what was written is exactly what was intended,
    # including byte length (catches encoding or newline translation).
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != WORD.encode("utf-8"):
        print(f"error: round-trip mismatch: {raw!r} != {WORD.encode('utf-8')!r}",
              file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH}: {WORD!r} ({len(WORD.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
