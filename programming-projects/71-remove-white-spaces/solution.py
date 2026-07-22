def solution(text):
    result = []
    for character in text:
        if character != " ":
            result.append(character)
    return "".join(result)
