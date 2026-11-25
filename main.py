#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout.

Standard library only.
"""

import os

JOKE = "I told my boss I was burned out and he gave me a candle, a mindfulness app, and another deadline."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the joke, nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print(JOKE)

if __name__ == "__main__":
    main()
