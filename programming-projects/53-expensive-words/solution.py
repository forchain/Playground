def expensive_words(sentence: str) -> int:
    total = 0
    for token in sentence.split():
        letters = [char for char in token if char.isalpha()]
        value = sum(ord(char.lower()) - ord('a') + 1 for char in letters)
        # 标点不参与大小写判断；剩余字母全部大写才翻倍。
        if letters and all(char.isupper() for char in letters):
            value *= 2
        total += value
    return total
