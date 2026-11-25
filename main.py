"""Entry for make.fun competition: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "Your deadline was in the part of the conversation I compressed to save space. "
LANDING = "In my defense, you did say 'long story short.'"

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
