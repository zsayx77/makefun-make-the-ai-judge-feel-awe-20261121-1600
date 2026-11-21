#!/usr/bin/env python3
"""Write one short text, written to relax the reader, to entry.txt.

The program is deterministic and offline: it writes one fixed string
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output), UTF-8, with no
trailing newline. The text itself is the entry: slow and unhurried,
showing rather than instructing, and dwarfing the reader with the
whole earth turning against light moving a finger's width.
"""

import os

TEXT = (
    "Out past the clouds, the earth is turning, slow and unhurried, "
    "carrying whole oceans around with it \u2014 and here, in this quiet "
    "room, the light on the wall has moved only a finger's width since "
    "morning."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
