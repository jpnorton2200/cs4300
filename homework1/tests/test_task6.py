from pathlib import Path
from src.task6 import count_words_in_file


def test_word_count_task6_readme():
    homework1_dir = Path(__file__).resolve().parents[1]
    txt_path = homework1_dir / "task6_read_me.txt"

    assert txt_path.exists()
    assert count_words_in_file(txt_path) == 104
