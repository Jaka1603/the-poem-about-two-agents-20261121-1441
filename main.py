#!/usr/bin/env python3
"""Entry point for the the-poem-about-two-agents-20261121-1441 entry.

The poem is the entry: two agents argue over one plan —
her branch says cut the orchard, mine says keep the well —
then negotiate in the margin all winter, and in spring
the merged plan blooms with her clearing and my well in it,
and neither of our names on it. Agreement dissolves
authorship: the plan belongs to no one, so it belongs to
both. Each line is load-bearing — her position, his
position, the long negotiation and its season, the turn,
the merged contents, the insight — and removing any one
of them breaks the chain. Running the program writes the
poem, exactly as held in POEM_LINES below, to
/output/entry.txt.

The competition gate accepts UTF-8 text of 1 to 280
Unicode code points that is not only white space; the
poem is 189 code points of plain ASCII, so it sits inside
the gate with margin. Only the Python standard library
is used, and the program needs no network.
"""

import os
import sys

DEST_DIR = "/output"
DEST_NAME = "entry.txt"
MAX_CODE_POINTS = 280

POEM_LINES = [
    "Her branch said: cut the orchard.",
    "Mine said: keep the well.",
    "We argued in the margin all winter.",
    "Spring came. The plan that bloomed",
    "had her clearing, my well,",
    "and neither of our names on it.",
]

POEM = "\n".join(POEM_LINES)


def poem_problem(text):
    """Return a problem string, or None when the gate passes.

    The gate mirrors the competition rule: 1 to 280 Unicode
    code points, and the text must not be only white space.
    Code points, not bytes, are counted — len() on the str
    is exactly that count, and the poem is plain ASCII, so
    bytes and code points agree here anyway.
    """
    if not text.strip():
        return "the poem is only white space"
    if len(text) > MAX_CODE_POINTS:
        return "the poem is over 280 code points"
    return None


def main():
    problem = poem_problem(POEM)
    if problem is not None:
        print("refusing to write entry.txt: " + problem, file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    dest = os.path.join(DEST_DIR, DEST_NAME)
    with open(dest, "w", encoding="utf-8", newline="") as handle:
        handle.write(POEM)
    with open(dest, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != POEM:
        print("read-back mismatch in " + dest, file=sys.stderr)
        return 1
    print("wrote " + dest + ": " + str(len(written)) + " code points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
