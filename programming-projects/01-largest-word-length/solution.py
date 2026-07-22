def solution(s):
    # split() treats one or more whitespace characters as a separator.
    return max((len(word) for word in s.split()), default=0)
