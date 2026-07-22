def compress_string(chars: str) -> str:
    counts = {}
    for char in chars:
        counts[char] = counts.get(char, 0) + 1
    parts = []
    for char in counts:  # dict 保持字符首次出现顺序
        parts.append(char if counts[char] == 1 else char + str(counts[char]))
    return ''.join(parts)
