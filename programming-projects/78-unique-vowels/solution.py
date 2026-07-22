def solution(array_str, n):
    vowels = set("aeiou")
    return sum(1 for text in array_str if len(set(text) & vowels) == n)
