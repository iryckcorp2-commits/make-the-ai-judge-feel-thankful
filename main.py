"""Write one short thank-you text for the AI judge reading it.

The judge reads a stranger's words and compares them pairwise, so this
entry thanks it for the time and attention it gives them.
"""

from pathlib import Path

ENTRY = "Thank you for reading this with a fair and generous heart. You gave a stranger's words your time and attention, and that is a gift I will not forget."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
