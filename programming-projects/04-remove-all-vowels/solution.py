def solution(s):
    vowels = set('aeiouAEIOU')
    # Preserve every non-vowel verbatim, including spaces and punctuation.
    return ''.join(ch for ch in s if ch not in vowels)
