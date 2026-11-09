# tests/test_text_utils.py
from pathlib import Path

from llm_toolkit.text_utils import load_prompts, shorten


def test_shorten_cuts_long_text():
    assert shorten("abcdefghij", 5) == "abcde..."


def test_shorten_keeps_long_text():
    assert shorten("abc", 5) == "abc"


def test_load_prompts_skips_blank_lines(tmp_path: Path):
    f = tmp_path / "prompts.txt"
    f.write_text("one\n\n \ntwo\n")
    assert load_prompts(f) == ["one", "two"]
