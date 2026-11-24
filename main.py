#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - desert island entry.

Entry: exactly one emoji, U+1F3DD DESERT ISLAND (🏝), 1 character,
4 bytes UTF-8, no trailing newline, no words. It is the canonical dream
vacation in a single glyph: your own private island — palm, sand and sea
in one postcard scene, vivid at a glance, specific (one particular dream,
not any holiday), with a small castaway spark, and instantly readable
across cultures and screens.

Gate (from the bounty rules): the entry must be exactly one emoji and
1-8 characters long. This entry clears it with room to spare at 1 char.
The tie-break after rate rewards fewer bytes, then earlier receipt, so
the entry deliberately omits VS16 (U+FE0F): U+1F3DD has
Emoji_Presentation=Yes and renders as an emoji on every modern platform
without it, and the bare form is 4 bytes instead of 7.

Writes the entry to /output/entry.txt FIRST, then a byte-identical copy
to entry.txt next to this script (best effort: the grader mounts the repo
read-only, so a failed copy must never crash the run; exit 0 always).
The /output file is read back and asserted byte-equal before returning,
so a bad graded file fails loudly instead of being submitted silently.

Deterministic: no network, no randomness, no input, no environment.
"""

import os

# U+1F3DD DESERT ISLAND - 1 character, 4 bytes UTF-8, no trailing newline.
# No VS16: U+1F3DD has Emoji_Presentation=Yes, so it renders as an emoji
# on every modern platform without it, and the tie-break rewards fewer bytes.
ENTRY = "\U0001F3DD"


def write_output(data: bytes) -> None:
    """Write the entry bytes to /output/entry.txt FIRST, then a
    byte-identical copy to entry.txt next to this script (best effort).

    Order matters: the grader mounts the repo read-only, so the repo-root
    copy must never be able to crash the run — /output is written and
    read back first, and the local copy lives inside try/except.
    """
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read back and assert: the graded file must be exactly the intended
    # bytes. A mismatch (disk error, wrong path) must fail loudly here
    # rather than submit a bad entry.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "read-back mismatch on /output/entry.txt"
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "wb") as f:
            f.write(data)
    except OSError:
        # Repo is mounted read-only by the grader: the /output copy above
        # is the graded one, so a failed local copy is not an error.
        pass


def main() -> int:
    data = ENTRY.encode("utf-8")
    write_output(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
