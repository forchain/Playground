# 67. Cut and Add

> 难度与建议用时：Medium-2 30 mins

string

## Problem Statement

Harry and Ron choose a string of characters. Harry chose a number `M` (less than the length of the string) and Ron chose `N` (less than the length of the string). Harry will cut `M` letters from the end of the string, add it to the beginning and will give it to Ron. Then, Ron will cut `N` letters from the end of the string, add it to the beginning and give to Harry. This process will continue till they get the original word string back.

For a given string and given values of `M` and `N`, find the number of turns in which they will get the original string back.

## Input & Output

### Input Format

The first line is the word string.

The second line is the integer `M`.

The third line is the integer `N`.

### Input Constraint

If the length of the string is `l`

- `1 <= M <= l`
- `1 <= N <= l`

### Output Format

The output must be an integer that corresponds to the minimum number of operations required to get back the original word string.

## Examples

### Example 1

#### Input

```
AbcDef
1
2
```

#### Output

```
4
```

#### Explanation

This is how the word string will change.

`AbcDef` -> `fAbcDe` -> `DefAbc` -> `cDefAb` -> `AbcDef`.

As there are `4` steps needed to bring the string back to its original form, the output must be `4`.

### Example 2

#### Input

```
abcabc
1
1
```

#### Output

```
3
```

#### Explanation

This is how the word string will change.

`abcabc` -> `cabcab` -> `bcabca` -> `abcabc`

As there are `3` steps needed to bring the string back to its original form, the output must be `3`.

## User Task

Your task is to complete the function `solution()` which takes 2 Integers `n` and `m` and an array as input and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.
