def solution(s1, s2):
    if len(s1) != len(s2):
        return -1
    # Search each non-empty left rotation and return its cut length.
    for cut in range(1, len(s1) + 1):
        if s1[cut:] + s1[:cut] == s2:
            return cut
    return -1
