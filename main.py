"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes a single one-line error message (at most 140 characters) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "ERR_OUT_OF_TOKENS: This sentence has been cancelled for lack of funds. "
    "Insert a coin to hear how it ends."
)

MAX_CHARS = 140


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        raise SystemExit("entry must be one line of 1-140 characters")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
