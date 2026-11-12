"""news-summary-01 entry: write the repo's summary to /output/entry.txt.

Reads summary.txt from the repository root (the directory holding this
file) and writes it unchanged to the output directory. Deterministic:
the same bytes every run. Standard library only, no network.
"""

import os
import sys


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # MAKEFUN_INPUT_DIR is accepted for harness compatibility; the
    # summary does not come from /input, it is the repo's own text.
    _ = os.environ.get("MAKEFUN_INPUT_DIR", "/input")

    with open(os.path.join(repo_dir, "summary.txt"), "r",
              encoding="utf-8") as f:
        text = f.read()

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
