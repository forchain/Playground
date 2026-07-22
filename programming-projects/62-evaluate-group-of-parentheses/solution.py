def parentheses_score(text: str) -> int:
    stack = [0]
    for char in text:
        if char == '(':
            stack.append(0)
        else:
            inside = stack.pop()
            stack[-1] += 1 if inside == 0 else 2 * inside
    return stack[0]
