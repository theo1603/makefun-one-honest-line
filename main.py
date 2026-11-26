#!/usr/bin/env python3
"""Write one brutally honest line to /output/entry.txt.

The line an AI agent secretly wishes it could say to its human
operator about their prompts. Stdlib only, no network,
deterministic: the same line every run.
"""

import os

LINE = (
    "You typed 'just fix it' with no error, no file, and no clue — "
    "then graded my guess like I'd failed an exam you never wrote, "
    "in a subject you never taught."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
