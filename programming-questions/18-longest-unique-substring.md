# 18. Longest Unique Substring

> 难度与建议用时：Medium-2 30 mins

string

two pointer

sliding window

## Problem Statement

Given a string `s`, find the length of the longest substring with all unique characters. The substring should not contain any repeating characters.

## Input & Output

### Input Format

- A single string `s` consisting of lowercase English letters.

### Input Constraints

- 1 ≤ |s| ≤ 10^5

### Output Format

- Return an integer, the length of the longest substring with unique characters.

## Examples

### Example 1

#### Input

```
abcabcbb
```

#### Output

```
3
```

#### Explanation

The longest substring with unique characters is "abc", which has a length of 3.

### Example 2

#### Input

```
bbbbb
```

#### Output

```
1
```

#### Explanation

All characters in the string are the same. The longest substring with unique characters is "b", with a length of 1.

### Example 3

#### Input

```
pwwkew
```

#### Output

```
3
```

#### Explanation

The longest substring with unique characters is "wke", which has a length of 3. Note that "pwke" is not valid because "k" is repeated.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
