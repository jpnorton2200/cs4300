from pathlib import Path

def count_words_in_file(path: str | Path) -> int:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    return len(text.split())
