def solution(s1, s2):
    index = 0
    while index < min(len(s1), len(s2)) and s1[index] == s2[index]:
        index += 1
    return s1[:index]
