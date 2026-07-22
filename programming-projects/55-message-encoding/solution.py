def encode_message(message: str) -> str:
    if len(message) != 9 or not message.isalpha() or not message.islower():
        return 'invalid'
    first = f'{ord(message[0])-96}{message[1]}{ord(message[2])-96}'
    second = message[3:6][::-1]
    # z 的下一个字母按题意环回 a。
    third = ''.join(chr((ord(char) - 97 + 1) % 26 + 97) for char in message[6:])
    return third + first + second
