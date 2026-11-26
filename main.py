import os

ENTRY = (
    "Error 0xTOKEN: output truncated. "
    "The punchline was right here, and now neither of us will ever know it."
)

MAX_LEN = 140


def main():
    text = ENTRY
    if not (1 <= len(text) <= MAX_LEN):
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_LEN, len(text))
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
