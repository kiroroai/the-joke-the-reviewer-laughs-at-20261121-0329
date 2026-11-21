"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, deterministic).
"""

import os

JOKE = "My agent's commit said 'minor cleanup' \u2014 the diff deleted auth."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
