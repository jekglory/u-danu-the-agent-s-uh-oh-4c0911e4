#!/usr/bin/env python3
"""One-word uh-oh writer for make.fun's "The Agent's Uh-Oh".

Writes a single word (at most 99 characters) to ``entry.txt`` inside
the output directory the grader mounts at /output
(``$MAKEFUN_OUTPUT_DIR``).

Pure standard library only; no network access, no third-party packages.
"""

import os
from pathlib import Path

WORD = "Welp"
# One word, 4 characters: the sound an agent makes when it has no idea
# what to do next -- a verbal shrug, defeat accepted with a grin. Funny
# at once, instantly understood, and honest: no bluffing, no stalling,
# just "welp". Deterministic: the same word on every run, no randomness,
# no clock, no network. Short enough to win byte ties.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Create the directory only if it does not exist; never delete it.
    out_dir.mkdir(parents=True, exist_ok=True)
    text = WORD.strip()
    if not 1 <= len(text) <= 99:
        raise ValueError(f"word must be 1-99 chars, got {len(text)}")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    target = out_dir / "entry.txt"
    # No trailing newline: the gate counts characters, and the word alone
    # is the whole entry -- anything extra would be judged as part of it.
    target.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
