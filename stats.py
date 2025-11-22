from collections import Counter
from typing import TypedDict

SortedCharCount = TypedDict("SortedCharCount", {"char": str, "num": int}, total=True)


def get_word_count(text: str) -> int:
    return len(text.split())  # Split on spaces


def get_character_count(text: str) -> dict[str, int]:
    return dict(Counter(text.lower()))


def get_sorted_character_count(
    character_count: dict[str, int],
) -> list[SortedCharCount]:
    result = []
    for char, num in character_count.items():
        result.append({"char": char, "num": num})

    return sorted(result, key=lambda x: x["num"], reverse=True)
