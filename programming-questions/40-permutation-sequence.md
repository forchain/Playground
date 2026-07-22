# 40. Permutation Sequence

> 难度与建议用时：Expert-1 45 mins

string

permutation

math

## Problem Statement

Given an integer `n` and an integer `k`, return the `k`th permutation sequence of the set `[1, 2, 3, ..., n]`. The permutations are ordered lexicographically.

## Input & Output

### Input Format

- An integer `n` (1 ≤ n ≤ 9), representing the size of the set.
- An integer `k` (1 ≤ k ≤ n!), representing the index of the permutation sequence to return.

### Input Constraints

- `n` will be between 1 and 9 inclusive.
- `k` will be between 1 and `n!` inclusive.

### Output Format

- A string representing the `k`th permutation sequence.

## Examples

### Example 1

#### Input

```
3
3
```

#### Output

```
213
```

#### Explanation

The permutations of `[1, 2, 3]` in lexicographical order are:

1. 123
2. 132
3. 213
4. 231
5. 312
6. 321 The 3rd permutation is `213`.

### Example 2

#### Input

```
4
9
```

#### Output

```
2314
```

#### Explanation

The permutations of `[1, 2, 3, 4]` in lexicographical order are:

1. 1234
2. 1243
3. 1324
4. 1342
5. 1423
6. 1432
7. 2134
8. 2143
9. 2314 The 9th permutation is `2314`.

### Example 3

#### Input

```
2
2
```

#### Output

```
21
```

#### Explanation

The permutations of `[1, 2]` in lexicographical order are:

1. 12
2. 21 The 2nd permutation is `21`.

## User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.
