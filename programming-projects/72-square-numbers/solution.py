def solution(n):
    if n < 0:
        return 0
    digits = 1 if n == 0 else len(str(n))
    return int((n * n) % (10 ** digits) == n)
