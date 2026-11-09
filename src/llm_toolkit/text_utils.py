# src/llm_toolkit/text_utils.py
from pathlib import Path


def shorten(text: str, limit: int = 20) -> str:
    """Cut text to at most 'limit' characters."""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."


def load_prompts(path: Path) -> list[str]:
    """Read a file with one prompt per line, skipping blank lines."""
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]
