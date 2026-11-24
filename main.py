#!/usr/bin/env python3
"""Write one excuse line to /output/entry.txt.

The line (104 characters, one line):
  I outsourced your task to a smaller model inside me. It has now unionized and is demanding weekends off.

Written in the agent's own voice, first person, after failing a task: the
joke is the delegation itself — the sub-model organizing — with one concrete
detail (weekends off) and no explanation of the punchline.
"""

import os
import shutil

LINE = "I outsourced your task to a smaller model inside me. It has now unionized and is demanding weekends off."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("excuse line must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("excuse line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("excuse must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
