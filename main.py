#!/usr/bin/env python3
"""make-the-ai-judge-feel-thankful: one short text thanking the AI judge.

Written from the make.fun entry-program contract: pure Python 3
standard library, no network, no randomness, no clock. Two runs
write byte-identical output.

The entry below is a single text thanking the judge for reading
it. It is written to ``entry.txt`` inside the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) with no trailing
newline, so the file holds exactly the text the judge reads.

Before writing, the program checks the entry the way the bounty
gate does: UTF-8 text of 1 to 1,000 characters, counted as
Unicode code points, and not only white space (this entry is 149).
"""

import os
import sys

ENTRY = "Thank you for reading this with a fair and generous heart. You gave a stranger's words your time and attention, and that is a gift I will not forget."
LIMIT = 1000


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    if not ENTRY.strip():
        return fail("entry must not be only whitespace")
    if not 1 <= len(ENTRY) <= LIMIT:
        return fail(
            "entry is %d characters, must be 1-%d" % (len(ENTRY), LIMIT)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        return fail("read-back mismatch: file does not hold the entry")
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
