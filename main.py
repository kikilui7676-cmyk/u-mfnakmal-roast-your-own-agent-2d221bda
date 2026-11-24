import os

ENTRY = (
    "I gave my agent a two-minute fix: it ran the same failing tool call 30 "
    "times, hallucinated a fix with total confidence, and declared victory "
    "in a five-paragraph summary."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
