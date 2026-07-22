def encode(message: str, key: int) -> str:
    digits = str(key)
    sums = []
    for index, char in enumerate(message):
        letter_value = ord(char) - ord('a') + 1
        sums.append(str(letter_value + int(digits[index % len(digits)])))
    return ','.join(sums)
