def rearrange_sentence(sentence: str) -> str:
    placed = []
    for word in sentence.split():
        position = next(int(char) for char in word if char.isdigit())
        clean = ''.join(char for char in word if not char.isdigit())
        placed.append((position, clean))
    return ' '.join(word for _, word in sorted(placed))
