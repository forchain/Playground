# 16. String Compression

> 难度与建议用时：Medium-2 30 mins

string

two pointer

## Problem Statement

You are given a string consisting of lowercase English letters. Your task is to compress the string into a new format where consecutive repeated characters are replaced with the character followed by the count of its repetitions. If a character appears only once, it should just appear as it is.

## Input & Output

### Input Format

- A string `s` containing only lowercase English letters.

### Input Constraints

- `1 <= len(s) <= 100`

### Output Format

- A string representing the compressed version of the input.

## Examples

### Example 1

#### Input

```
aaaabbbcca
```

#### Output

```
a4b3c2a1
```

#### Explanation

The character `a` appears 4 times consecutively, followed by `b` three times, then `c` twice, and finally `a` once.

### Example 2

#### Input

```
abcccdeeeeffff
```

#### Output

```
ab1c3d1e4f4
```

#### Explanation

All single characters are followed by `1`, while consecutive characters are followed by their counts.

## User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.
