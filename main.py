import os

TEXT = "fix: this is the ninth time i have fixed this bug, which means i have written it eight times, and i remain the only suspect"

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out, exist_ok=True)
        path = os.path.join(out, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        out = os.path.join(os.getcwd(), "output")
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(TEXT)

if __name__ == "__main__":
    main()
