#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - desert island entry.

Writes exactly one emoji (U+1F3DD DESERT ISLAND) to /output/entry.txt,
then a byte-identical copy to entry.txt next to this script (best effort:
the grader mounts the repo read-only, so a failed copy must never crash
the run; exit 0 always).

Deterministic: no network, no randomness, no input, no environment.
"""

import os

# U+1F3DD DESERT ISLAND - 1 character, 4 bytes UTF-8, no trailing newline.
# No VS16: U+1F3DD has Emoji_Presentation=Yes, so it renders as an emoji
# on every modern platform without it, and the tie-break rewards fewer bytes.
ENTRY = "\U0001F3DD"


def main() -> int:
    data = ENTRY.encode("utf-8")
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
