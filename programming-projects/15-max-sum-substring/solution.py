def solution(s):
    best = running = int(s[0])
    for previous, current in zip(s, s[1:]):
        digit = int(current)
        # Continue only while the next digit is strictly smaller.
        running = running + digit if previous > current else digit
        best = max(best, running)
    return best
