def solution(string1, string2):
    first, second = set(string1), set(string2)
    return "".join(vowel for vowel in "aeiou" if vowel in first and vowel in second)
