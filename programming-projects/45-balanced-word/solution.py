def balanced_word(word: str) -> int:
    if len(word) % 2:
        return -1
    middle = len(word) // 2
    value = lambda part: sum(ord(ch) - ord('a') + 1 for ch in part)
    return int(value(word[:middle]) == value(word[middle:]))
