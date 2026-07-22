# 1. Largest Word Length -- Medium-1 30 mins

string

# Problem Statement

Given a string S, your task is to find the length of the largest word (a sequence of non-space characters separated by spaces) in the string.

# Input & Output

## Input Format

A single string S, which may contain both uppercase and lowercase English alphabets, digits, and spaces.

## Input Constraints

1 <= |S| <= 1000 (where |S| represents the length of the string).

Words are separated by one or more spaces, and the string will not contain leading or trailing spaces.

## Output Format

An integer representing the length of the largest word in the string.

# Examples

## Example 1

### Input

```
The quick brown fox
```

### Output

```
5
```

### Explanation

The largest word in the input is "quick," which has a length of 5.

## Example 2

### Input

```
A journey of a thousand miles begins with a single step
```

### Output

```
8
```

### Explanation

The largest word in the input is "thousand," which has a length of 8.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 2. Sum of Digits -- Medium-1 30 mins

math

string

# Problem Statement

Write a function to calculate the sum of digits of an integer number `n`. For example, if the input is 123, the sum of digits is 1 + 2 + 3 = 6. The function must return the calculated sum.

## Input & Output

### Input Format

1. A single integer `n`.

### Input Constraints

- `|n| <= 10^9`

### Output Format

- A single integer representing the sum of the digits of the input number.

# Examples

## Example 1

### Input

```
123
```

### Output

```
6
```

### Explanation

The sum of the digits of 123 is 1 + 2 + 3 = 6.

## Example 2

### Input

```
-2059
```

### Output

```
16
```

### Explanation

The sum of the digits of -2059 is 2 + 0 + 5 + 9 = 16 (ignoring the negative sign).

## Example 3

### Input

```
0
```

### Output

```
0
```

### Explanation

The digit sum of 0 is just 0.

# User Task

Your task is to complete the function solution() and return the expected answer. You don’t need to read the input; just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 3. Sum of Unique Chars -- Medium-1 30 mins

string

ascii

# Problem Statement

You are given a string `s` consisting of lowercase English letters. Your task is to calculate the sum of the ASCII values of all unique characters in the string. A unique character is one that appears exactly once in the string.

# Input & Output

## Input Format

- A single string `s`, containing only lowercase English letters.

## Input Constraints

- `1 <= len(s) <= 100`

## Output Format

- An integer representing the sum of the ASCII values of all unique characters in the string.

# Examples

## Example 1

### Input

```
abc
```

### Output

```
294
```

### Explanation

The unique characters in `abc` are `a, b, c`. Their ASCII values are 97, 98, and 99, respectively. The sum is `97 + 98 + 99 = 294`.

## Example 2

### Input

```
abac
```

### Output

```
197
```

### Explanation

The unique character in `abac` are `b` and `c`. Its ASCII value is `98` + `99`. Output is 197.

## Example 3

### Input

```
xyzwx
```

### Output

```
362
```

### Explanation

The unique characters in `xyzwx` are `y, z, w`. Their ASCII values are `121` , `122, 119`, respectively. The sum is `121 + 122 + 119 = 362`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 4.Remove All Vowels -- Medium-1 30 mins

string

# Problem Statement

Write a function that takes a string as input and removes all vowels (both uppercase and lowercase) from it. The output should be the modified string without vowels.

# Input & Output

## Input Format

- A single string containing uppercase and lowercase letters. The string may also include spaces or special characters (which should be kept intact).

## Input Constraints

- 1 ≤ Length of the string ≤ 100

## Output Format

- Return the string with all vowels removed.

# Examples

## Example 1

### Input

```
hello world
```

### Output

```
hll wrld
```

### Explanation

All vowels (e, o) from "hello world" are removed.

## Example 2

### Input

```
Programming is fun!
```

### Output

```
Prgrmmng s fn!
```

### Explanation

All vowels (o, a, i, i, u) from "Programming is fun!" are removed.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 5.Rotate Array Steps -- Medium-1 30 mins

array

rotation

# Problem Statement

You are given an array `arr` of integers containing `n` elements and an integer `k`. Rotate the array to the right by `k` steps, where `k` can be any positive integer (less than or equal to 1000). Rotation means each element of the array is shifted right by one position, and the last element moves to the beginning. For example, rotating `[1, 2, 3]` by 1 step results in `[3, 1, 2]`.

# Input & Output

## Input Format

- First line contains an integer `n`, the size of the array `arr`.
- Second line contains `n` space-separated integers, representing the elements of the array `arr`.
- Third line contains an integer `k`.

## Input Constraints

- 1 <= n <= 100
- -10^4 <= arr[i] <= 10^4
- 1 <= k <= 10^4

## Output Format

- Output the rotated array as a **space-separated string**.

# Examples

## Example 1

### Input

```
5
1 2 3 4 5
2
```

### Output

```
4 5 1 2 3
```

### Explanation

Rotating `[1, 2, 3, 4, 5]` two steps to the right results in `[4, 5, 1, 2, 3]`.

## Example 2

### Input

```
6
10 20 30 40 50 60
4
```

### Output

```
40 50 60 10 20 30
```

### Explanation

Rotating `[10, 20, 30, 40, 50, 60]` four steps to the right results in `[40, 50, 60, 10, 20, 30]`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 6.Second Largest Element -- Medium-1 30 mins

array

sorting

# Problem Statement

You are given an array of integers. Your task is to find the second largest element in the array. If the array does not have at least two distinct elements, return `-1`.

# Input & Output

## Input Format

- An integer `n` denoting the size of the array.
- An array of `n` integers.

## Input Constraints

- `2 <= n <= 100`
- `-10^6 <= array[i] <= 10^6`

## Output Format

- An integer representing the second largest element, or `-1` if there isn’t one.

# Examples

## Example 1

### Input

```
5
2 3 6 6 5
```

### Output

```
5
```

### Explanation

The largest element is `6`. The second largest distinct element is `5`.

## Example 2

### Input

```
3
10 10 10
```

### Output

```
-1
```

### Explanation

The array has only one distinct element, so there is no second largest.

## Example 3

### Input

```
6
1 2 3 4 5 4
```

### Output

```
4
```

### Explanation

The largest element is `5`. The second largest distinct element is `4`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 7.Find Missing Number -- Medium-1 30 mins

array

math

searching

# Problem Statement

You are given an array of size `n` containing integers from `1` to `n+1` inclusive, with exactly one number missing. Your task is to find the missing number.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- `1 <= n <= 100`
- The array contains distinct integers from `1` to `n+1` with one number missing.

## Output Format

- Return the missing number as an integer.

# Examples

## Example 1

### Input

```
4
1 2 4 5
```

### Output

```
3
```

### Explanation

The array contains numbers from `1` to `5` with `3` missing.

## Example 2

### Input

```
5
2 3 1 5 6
```

### Output

```
4
```

### Explanation

The array contains numbers from `1` to `6` with `4` missing.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 8.Kth Largest Element -- Medium-1 30 mins

array

sorting

searching

# Problem Statement

You are given an array of integers and an integer `k`. Your task is to find the `k`th largest element (1-indexed) in the array.

# Input & Output

## Input Format

- The first line of input contains an integer `n`, the size of the array (1 ≤ n ≤ 100).
- The second line contains `n` integers separated by spaces, representing the array elements. Each array element `a[i]` satisfies `−10^4 ≤ a[i] ≤ 10^4`.
- The third line contains a single integer `k` (1 ≤ k ≤ n), which specifies the position of the largest element to find.

## Input Constraints

- 1 ≤ n ≤ 100
- −10^4 ≤ a[i] ≤ 10^4
- 1 ≤ k ≤ n

## Output Format

- A single integer representing the `k`th largest element in the array.

# Examples

## Example 1

### Input

```
6
3 2 1 5 6 4
2
```

### Output

```
5
```

### Explanation

The sorted array in descending order is [6, 5, 4, 3, 2, 1]. The 2nd largest element is `5`.

## Example 2

### Input

```
4
7 9 3 2
4
```

### Output

```
2
```

### Explanation

The sorted array in descending order is [9, 7, 3, 2]. The 4th largest element is `2`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 9.Max XOR Subarray -- Medium-2 30 mins

array

xor

subarray

# Problem Statement

Given an array of integers, find the maximum XOR value of any subarray of the array.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100,000
- -10^9 ≤ array[i] ≤ 10^9

## Output Format

- Return a single integer, the maximum XOR value of any subarray.

# Examples

## Example 1

### Input

```
4
1 2 3 4
```

### Output

```
7
```

### Explanation

The subarray `[3, 4]` has the maximum XOR value of `7`.

## Example 2

### Input

```
5
8 1 2 12 7
```

### Output

```
15
```

### Explanation

The subarray `[8, 1, 2, 12]` has the maximum XOR value of `15`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 10.Max Product Subarray -- Medium-2 30 mins

array

subarray

greedy

# Problem Statement

Given an array of integers, find the contiguous subarray within the array (containing at least one number) which has the largest product.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10 ≤ array[i] ≤ 10

## Output Format

- Return a single integer, the maximum product of a contiguous subarray.

# Examples

## Example 1

### Input

```
5
2 3 -2 4 -1
```

### Output

```
48
```

### Explanation

The subarray `[2, 3, -2, 4, -1]` has the maximum product of 48.

## Example 2

### Input

```
4
-2 0 -1 3
```

### Output

```
3
```

### Explanation

The subarray `[3]` has the maximum product of 3.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

JavaScript

Python3

Rust

PHP

NodeJS

C#

TypeScript

Ruby

Go

C++

Dart

Java

Scala

C

Kotlin

Swift

AddPreview

# 11.Count Distinct Substrings -- Medium-2 30 mins

string

substring

# Problem Statement

Given a string `s`, your task is to count the number of distinct substrings of `s`. A substring is defined as a contiguous sequence of characters within a string. The empty substring is not considered.

# Input & Output

## Input Format

- A single string `s`.

## Input Constraints

- 1 ≤ |s| ≤ 100
- `s` consists of lowercase English letters only.

## Output Format

- An integer representing the number of distinct substrings of `s`.

# Examples

## Example 1

### Input

```
abc
```

### Output

```
6
```

### Explanation

The distinct substrings of "abc" are: "a", "b", "c", "ab", "bc", "abc". Total = 6.

## Example 2

### Input

```
aaa
```

### Output

```
3
```

### Explanation

The distinct substrings of "aaa" are: "a", "aa", "aaa". Total = 3.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 12.Find Majority Element -- Medium-2 30 mins

array

searching

# Problem Statement

Given an array of integers, find the majority element. A majority element is an element that appears more than ⌊n/2⌋ times in the array, where n is the size of the array. If no such element exists, return -1.

# Input & Output

## Input Format

- The first line contains an integer n, the size of the array.
- The second line contains n integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^9 ≤ array[i] ≤ 10^9

## Output Format

- Return the majority element if it exists, otherwise return -1.

# Examples

## Example 1

### Input

```
5
3 3 4 2 3
```

### Output

```
3
```

### Explanation

The element `3` appears 3 times, which is more than ⌊5/2⌋ = 2.

## Example 2

### Input

```
4
1 2 3 4
```

### Output

```
-1
```

### Explanation

No element appears more than ⌊4/2⌋ = 2 times.

## Example 3

### Input

```
6
2 2 1 1 1 2
```

### Output

```
-1
```

### Explanation

No element appears more than ⌊6/2⌋ = 3 times.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 13.Rearrange Alternately -- Medium-2 30 mins

array

sorting

two pointer

# Problem Statement

Given a sorted array of integers, rearrange the elements in such a way that the first element is the largest, the second is the smallest, the third is the second largest, the fourth is the second smallest, and so on. Your task is to return the rearranged integers as a space-separated string.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array, separated by spaces.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^5 ≤ array[i] ≤ 10^5
- The array is sorted in non-decreasing order.

## Output Format

- Return the rearranged array as a space-separated string.

# Examples

## Example 1

### Input

```
6
1 2 3 4 5 6
```

### Output

```
6 1 5 2 4 3
```

### Explanation

The largest element is 6, the smallest is 1, the second largest is 5, the second smallest is 2, and so on.

## Example 2

### Input

```
5
10 20 30 40 50
```

### Output

```
50 10 40 20 30
```

### Explanation

The largest element is 50, the smallest is 10, the second largest is 40, the second smallest is 20, and so on.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 14.String Rotation Check -- Medium-2 30 mins

string

rotation

# Problem Statement

Given two strings `s1` and `s2`, determine if `s2` is a **left-rotation** of `s1`.
A **left-rotation** here means that you take some number of characters from the **beginning** of the string `s1` and append them to the end of `s1` to form `s2`.

# Input & Output

## Input Format

- The first line contains a string `s1`.
- The second line contains a string `s2`.

## Input Constraints

- 1 ≤ |s1|, |s2| ≤ 100
- Both strings consist of lowercase English letters only.

## Output Format

- Return the length of the rotation if `s2` is a **left-rotation** of `s1`.
- If `s2` is not a rotation of `s1`, return `-1`.

# Examples

## Example 1

### Input

```
abcde
deabc
```

### Output

```
3
```

### Explanation

`s2` is a rotation of `s1` by 3 characters ("abcde" rotated by 3 becomes "deabc").

## Example 2

### Input

```
hello
lohel
```

### Output

```
2
```

### Explanation

`s2` is a rotation of `s1` by 2 characters ("hello" rotated by 2 becomes "lohel").

## Example 3

### Input

```
abc
cabd
```

### Output

```
-1
```

### Explanation

`s2` is not a rotation of `s1`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 15.Max Sum Substring -- Medium-2 30 mins

string

greedy

sliding window

# Problem Statement

Given a string of digits, you need to determine the largest sum of a contiguous substring whose digits are strictly decreasing from left to right.

A substring must consist of one or more consecutive characters from the string.

# Input & Output

## Input Format

- A single string `s` consisting of digits (0-9).

## Input Constraints

- `1 <= length(s) <= 1000`

## Output Format

- Return the **maximum possible sum** of digits of any contiguous substring where each digit is **strictly less than the previous digit**.

# Examples

## Example 1

### Input

```
9875
```

### Output

```
29
```

### Explanation

The substring "9875" gives the maximum sum of `9 + 8 + 7 + 5 = 29`.

## Example 2

### Input

```
1234
```

### Output

```
4
```

### Explanation

No two adjacent digits form a strictly decreasing pair.
The maximum sum comes from the single digit substring `4`.

## Example 3

### Input

```
404
```

### Output

```
4
```

### Explanation

Valid strictly decreasing substrings:

- `4`
- `40 → 4 + 0 = 4`

The maximum sum is `4`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C#

C

JavaScript

Ruby

Swift

Java

NodeJS

Python3

Scala

Rust

Dart

C++

TypeScript

Go

PHP

Kotlin

AddPreview

# 16.String Compression -- Medium-2 30 mins

string

two pointer

# Problem Statement

You are given a string consisting of lowercase English letters. Your task is to compress the string into a new format where consecutive repeated characters are replaced with the character followed by the count of its repetitions. If a character appears only once, it should just appear as it is.

# Input & Output

## Input Format

- A string `s` containing only lowercase English letters.

## Input Constraints

- `1 <= len(s) <= 100`

## Output Format

- A string representing the compressed version of the input.

# Examples

## Example 1

### Input

```
aaaabbbcca
```

### Output

```
a4b3c2a1
```

### Explanation

The character `a` appears 4 times consecutively, followed by `b` three times, then `c` twice, and finally `a` once.

## Example 2

### Input

```
abcccdeeeeffff
```

### Output

```
ab1c3d1e4f4
```

### Explanation

All single characters are followed by `1`, while consecutive characters are followed by their counts.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 17.Sort by Frequency -- Medium-2 30 mins

array

sorting

frequency

# Problem Statement

Given an array of integers, sort the array in decreasing order of frequency of elements. If two elements have the same frequency, the one with the smaller value should come first.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^3 ≤ array[i] ≤ 10^3

## Output Format

- Return the sorted array as a **space-separated string**.

# Examples

## Example 1

### Input

```
6
4 5 6 5 4 3
```

### Output

```
4 4 5 5 3 6
```

### Explanation

The frequency of elements is:

- 4: 2 times
- 5: 2 times
- 6: 1 time
- 3: 1 time

Since 4 and 5 have the highest frequency, they come first. Between 4 and 5, 4 is smaller, so it comes first. The remaining elements are sorted by their values.

## Example 2

### Input

```
5
1 2 2 3 3
```

### Output

```
2 2 3 3 1
```

### Explanation

The frequency of elements is:

- 2: 2 times
- 3: 2 times
- 1: 1 time

Since 2 and 3 have the highest frequency, they come first. Between 2 and 3, 2 is smaller, so it comes first. The remaining element is 1.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 18.Longest Unique Substring -- Medium-2 30 mins

string

two pointer

sliding window

# Problem Statement

Given a string `s`, find the length of the longest substring with all unique characters. The substring should not contain any repeating characters.

# Input & Output

## Input Format

- A single string `s` consisting of lowercase English letters.

## Input Constraints

- 1 ≤ |s| ≤ 10^5

## Output Format

- Return an integer, the length of the longest substring with unique characters.

# Examples

## Example 1

### Input

```
abcabcbb
```

### Output

```
3
```

### Explanation

The longest substring with unique characters is "abc", which has a length of 3.

## Example 2

### Input

```
bbbbb
```

### Output

```
1
```

### Explanation

All characters in the string are the same. The longest substring with unique characters is "b", with a length of 1.

## Example 3

### Input

```
pwwkew
```

### Output

```
3
```

### Explanation

The longest substring with unique characters is "wke", which has a length of 3. Note that "pwke" is not valid because "k" is repeated.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 19.Longest Prefix Match -- Medium-2 30 mins

string

# Problem Statement

You are given two strings `s1` and `s2`. Your task is to find the longest prefix string that is common to both `s1` and `s2`. If no such prefix exists, return an empty string.

# Input & Output

## Input Format

- The first line contains the string `s1`.
- The second line contains the string `s2`.

## Input Constraints

- `1 <= len(s1), len(s2) <= 10^5`
- Both strings contain only lowercase English letters ('a' to 'z').

## Output Format

- A single string representing the longest common prefix between `s1` and `s2`.

# Examples

## Example 1

### Input

```
abcd
abcxyz
```

### Output

```
abc
```

### Explanation

The common prefix between `s1` and `s2` is "abc".

## Example 2

### Input

```
hello
world
```

### Output

```

```

### Explanation

The strings `s1` and `s2` have no common prefix, so the result is an empty string.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

20.Smallest Unique Substring -- Hard-1 30 mins

string

sliding window

two pointer

# Problem Statement

You are given a string `s`. Your task is to find the length of the smallest substring of `s` that contains all the unique characters in `s`.

# Input & Output

## Input Format

A single string `s` containing lowercase alphabets `a-z`.

## Input Constraints

- 1 ≤ |s| ≤ 10^3 (where |s| is the length of the string)
- The string consists of only lowercase English letters.

## Output Format

Return the length of the smallest substring of `s` that contains all unique characters.

# Examples

## Example 1

### Input

```
abcaacbb
```

### Output

```
3
```

### Explanation

The unique characters in the string are `a, b, c`. The smallest substring that contains all these is `abc`, which has a length of `3`.

## Example 2

### Input

```
aaa
```

### Output

```
1
```

### Explanation

The only unique character in the string is `a`. The smallest substring containing `a` is `a` itself, with a length of `1`.

## Example 3

### Input

```
abcdef
```

### Output

```
6
```

### Explanation

All characters in the string are unique and already present in the same substring. Hence the length is `6`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Go

Java

C#

Ruby

Python3

Scala

NodeJS

C

Rust

Kotlin

PHP

JavaScript

TypeScript

Swift

Dart

AddPreview

# 21.Longest Zigzag Path -- Hard-1 45 mins

array

dynamic programming

subsequence

# Problem Statement

Given an array of integers, find the length of the longest zigzag subsequence. A zigzag subsequence is defined as a sequence where the differences between consecutive elements strictly alternate between positive and negative.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

## Output Format

- Return a single integer, the length of the longest zigzag subsequence.

# Examples

## Example 1

### Input

```
6
1 7 4 9 2 5
```

### Output

```
6
```

### Explanation

The entire array is a zigzag sequence: [1, 7, 4, 9, 2, 5], as 1 < 7, 7 > 4, 4 < 9, 9 > 2, 2 < 5.

## Example 2

### Input

```
7
1 17 5 10 13 15 10
```

### Output

```
5
```

### Explanation

The longest zigzag subsequence is [1, 17, 10, 13, 10].

## Example 3

### Input

```
5
10 10 10 10 10
```

### Output

```
1
```

### Explanation

All elements are the same, so the longest zigzag subsequence is any single element.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Java

Swift

NodeJS

Ruby

Kotlin

C#

C++

C

Rust

Dart

TypeScript

Python3

PHP

JavaScript

Scala

Go

AddPreview

# 22.Count Palindromic Substrings -- Hard-1 45 mins

string

palindrome

substring

# Problem Statement

Given a string `s`, your task is to count the number of distinct palindromic substrings in the string. A substring is a contiguous sequence of characters within a string, and a palindrome is a string that reads the same backward as forward.

# Input & Output

## Input Format

- A single string `s` of length `n`.

## Input Constraints

- 1 ≤ n ≤ 1000
- The string `s` consists of lowercase English letters only.

## Output Format

- Return a single integer, the count of distinct palindromic substrings in the string.

# Examples

## Example 1

### Input

```
ababa
```

### Output

```
5
```

### Explanation

The distinct palindromic substrings are: `a`, `b`, `aba`, `bab`, `ababa`.

## Example 2

### Input

```
abc
```

### Output

```
3
```

### Explanation

The distinct palindromic substrings are: `a`, `b`, `c`.

## Example 3

### Input

```
aaa
```

### Output

```
3
```

### Explanation

The distinct palindromic substrings are: `a`, `aa`, `aaa`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 23.Max Sum Increasing Subsequence -- Hard-1 45 mins

array

dynamic programming

subsequence

# Problem Statement

Given an array of integers, find the maximum sum of an increasing subsequence in the array. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a sequence of numbers such that every number in the sequence is greater than the previous one. You need to return the maximum sum of such a subsequence.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

## Output Format

- Return a single integer, the maximum sum of an increasing subsequence.

# Examples

## Example 1

### Input

```
6
1 101 2 3 100 4
```

### Output

```
106
```

### Explanation

The increasing subsequence with the maximum sum is [1, 2, 3, 100].

## Example 2

### Input

```
5
10 5 4 3 2
```

### Output

```
10
```

### Explanation

The increasing subsequence with the maximum sum is [10].

## Example 3

### Input

```
7
3 4 5 10 1 2 3
```

### Output

```
22
```

### Explanation

The increasing subsequence with the maximum sum is [3, 4, 5, 10].

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 24.Max Sum Non-Adjacent -- Hard-1 45 mins

array

dynamic programming

greedy

# Problem Statement

Given an array of integers, find the maximum sum of non-adjacent elements. You cannot pick two consecutive elements from the array. If the array is empty, or you choose to pick no elements, return 0.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

## Output Format

- Return a single integer, the maximum sum of non-adjacent elements.

# Examples

## Example 1

### Input

```
5
3 2 7 10 12
```

### Output

```
22
```

### Explanation

The maximum sum is obtained by picking 3, 7, and 12 (3 + 7 + 12 = 22).

## Example 2

### Input

```
4
-1 2 9 -4
```

### Output

```
9
```

### Explanation

The maximum sum is obtained by picking 9.

## Example 3

### Input

```
6
5 5 10 100 10 5
```

### Output

```
110
```

### Explanation

The maximum sum is obtained by picking 5, 100, and 5 (5 + 100 + 5 = 110).

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 25.Minimum Jumps to End -- Hard-1 45 mins

array

greedy

dynamic programming

# Problem Statement

You are given an array `arr` of size `n` where each element represents the maximum number of steps you can jump forward from that position. Your task is to determine the minimum number of jumps required to reach the end of the array starting from the first element. If it is not possible to reach the end, return `-1`.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array `arr`.

## Input Constraints

- `1 <= n <= 100`
- `0 <= arr[i] <= 100`

## Output Format

- Return a single integer, the minimum number of jumps required to reach the end of the array, or `-1` if it is not possible.

# Examples

## Example 1

### Input

```
5
2 3 1 1 4
```

### Output

```
2
```

### Explanation

From index 0, jump 1 step to index 1, then jump 3 steps to the end (index 5). Total jumps = 2.

## Example 2

### Input

```
5
1 0 0 0 0
```

### Output

```
-1
```

### Explanation

It is not possible to move beyond index 0 as all subsequent elements are 0.

## Example 3

### Input

```
1
0
```

### Output

```
0
```

### Explanation

You are already at the end of the array, so no jumps are required.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 26.Max Sum Partition -- Hard-1 45 mins

array

dynamic programming

partitioning

# Problem Statement

You are given an array of integers `arr` of size `N`. Your task is to partition the array into contiguous subarrays such that the sum of the maximum element of each subarray is maximized. You can partition the array into as many subarrays as you like, but each subarray must contain at least one element.

Return the maximum sum of the maximum elements of the subarrays.

# Input & Output

## Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` integers, the elements of the array `arr`.

## Input Constraints

- 1 ≤ N ≤ 100
- -10^4 ≤ arr[i] ≤ 10^4

## Output Format

- Return a single integer, the maximum sum of the maximum elements of the subarrays.

# Examples

## Example 1

### Input

```
5
1 3 -1 2 5
```

### Output

```
11
```

### Explanation

Partition the array as `[1]`, `[3]`, `[-1, 2]`, `[5]`. The maximum elements are `1`, `3`, `2`, and `5`. Their sum is `1 + 3 + 2 + 5 = 11`.

## Example 2

### Input

```
4
-2 -1 -3 -4
```

### Output

```
-1
```

### Explanation

We don't partition the array, and just use the entire array. The maximum of the array is `-1`

## Example 3

### Input

```
6
4 2 1 6 3 8
```

### Output

```
24
```

### Explanation

Partition the array as `[4]`, `[2]`, `[1]`, `[6]`, `[3]`, `[8]`. The maximum elements are `4`, `2`, `1`, `6`, `3` and `8`. Their sum is 4 + 2 + 1 + 6 + 3 + 8 = 24.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

JavaScript

Python3

Rust

PHP

NodeJS

C#

TypeScript

Ruby

Go

C++

Dart

Java

Scala

C

Kotlin

Swift

AddPreview

# 27.Minimum Swaps To Sort Array -- Hard-2 40 mins

array

sorting

greedy

# Problem Statement

You are given an array `A` of `N` distinct integers. Your task is to determine the minimum number of swaps (not necessarily adjacent) required to sort the array in ascending order.

# Input & Output

## Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers, the elements of the array `A`.

## Input Constraints

- 1 ≤ N ≤ 100
- -10^4 ≤ A[i] ≤ 10^4
- All elements in the array are distinct.

## Output Format

- Return a single integer, the minimum number of swaps required to sort the array.

# Examples

## Example 1

### Input

```
5
3 1 2 5 4
```

### Output

```
3
```

### Explanation

To sort the array `[3, 1, 2, 5, 4]` in ascending order:

1. Swap `3` and `1`: `[1, 3, 2, 5, 4]`
2. Swap `3` and `2`: `[1, 2, 3, 5, 4]`
3. Swap `5` and `4`: `[1, 2, 3, 4, 5]` Total swaps = 3.

## Example 2

### Input

```
4
4 3 2 1
```

### Output

```
2
```

### Explanation

To sort the array `[4, 3, 2, 1]` in ascending order:

1. Swap `4` and `1`: `[1, 3, 2, 4]`
2. Swap `3` and `2`: `[1, 2, 3, 4]` Total swaps = 2.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 28.Find Longest Repeating Substring -- Hard-2 45 mins

string

searching

# Problem Statement

You are given a string `s`. Your task is to find the length of the longest substring that repeats itself at least twice in the given string. The repeated substrings must not overlap.

# Input & Output

## Input Format

- A single string `s` consisting of only lowercase English letters.

## Input Constraints

- 1 ≤ |s| ≤ 10^3 (where |s| is the length of the string)

## Output Format

- Return an integer representing the length of the longest repeating substring or `0` if no such substring exists.

# Examples

## Example 1

### Input

```
ababc
```

### Output

```
2
```

### Explanation

The longest substring that repeats is `ab`, appearing twice in `ababc`.

## Example 2

### Input

```
aaaa
```

### Output

```
2
```

### Explanation

The substring `aa` is the longest repeated substring in `aaaa`, with no overlaps

## Example 3

### Input

```
abcdef
```

### Output

```
0
```

### Explanation

There are no repeating substrings in `abcdef`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 29.Longest Bitonic Subsequence -- Hard-2 45 mins

array

dynamic programming

subsequence

# Problem Statement

Given an array of integers, find the length of the longest bitonic subsequence. A bitonic subsequence is a sequence that first increases and then decreases. The elements of the subsequence need not be contiguous but must maintain their relative order.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

## Output Format

- Return a single integer, the length of the longest bitonic subsequence.

# Examples

## Example 1

### Input

```
6
1 2 5 3 2 1
```

### Output

```
6
```

### Explanation

The entire array `[1, 2, 5, 3, 2, 1]` is a bitonic subsequence.

## Example 2

### Input

```
8
1 11 2 10 4 5 2 1
```

### Output

```
6
```

### Explanation

The longest bitonic subsequence is `[1, 2, 10, 4, 2, 1]`.

## Example 3

### Input

```
5
12 11 40 5 3
```

### Output

```
4
```

### Explanation

The longest bitonic subsequence is `[12, 40, 5, 3]`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

30.Max Sum Path in Grid -- Hard-2 45 mins

array

2d array

dynamic programming

# Problem Statement

You are given a 2D grid of integers with `N` rows and `M` columns. Starting from the top-left corner of the grid `(0, 0)`, you can move either **right** or **down** at each step. Your task is to find the maximum sum of values you can collect by following a path from the top-left corner to the bottom-right corner of the grid `(N-1, M-1)`.

# Input & Output

## Input Format

- The first line contains two integers `N` and `M`, the number of rows and columns in the grid.
- The next `N` lines each contain `M` integers, representing the grid.

## Input Constraints

- `1 <= N, M <= 100`
- `-1000 <= grid[i][j] <= 1000`

## Output Format

- Return a single integer, the maximum sum of values collected along the path.

# Examples

## Example 1

### Input

```
3 3
1 2 3
4 5 6
7 8 9
```

### Output

```
29
```

### Explanation

The path with the maximum sum is `1 -> 4 -> 7 -> 8 -> 9`, with a total sum of `29`.

## Example 2

### Input

```
2
2
-1 -2
-3 -4
```

### Output

```
-7
```

### Explanation

The path with the maximum sum is `-1 -> -2 -> -4`, with a total sum of `-7`.

## Example 3

### Input

```
4
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

### Output

```
73
```

### Explanation

The path with the maximum sum is `1 -> 5 -> 9 -> 13 -> 14 -> 15 -> 16`, with a total sum of `73`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 31.Longest Palindromic Subsequence -- Hard-2 45 mins

string

dynamic programming

palindrome

# Problem Statement

Given a string `s`, find the length of the longest palindromic subsequence in the string. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Input & Output

## Input Format

- A single string `s`.

## Input Constraints

- 1 ≤ |s| ≤ 1000 (where |s| is the length of the string `s`)
- The string `s` consists of lowercase English letters only.

## Output Format

- Return an integer representing the length of the longest palindromic subsequence.

# Examples

## Example 1

### Input

```
abdbca
```

### Output

```
5
```

### Explanation

The longest palindromic subsequence is "abdba", which has a length of 5.

## Example 2

### Input

```
cbbd
```

### Output

```
2
```

### Explanation

The longest palindromic subsequence is "bb", which has a length of 2.

## Example 3

### Input

```
a
```

### Output

```
1
```

### Explanation

The longest palindromic subsequence is "a", which has a length of 1.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 32.Merge Overlapping Intervals -- Hard-2 45 mins

array

sorting

# Problem Statement

You are given a list of intervals where each interval is represented as a pair of integers `[start, end]`. Your task is to merge all overlapping intervals and return the resulting list of merged intervals. Two intervals `[a, b]` and `[c, d]` overlap if `b >= c` and `a <= d`.

# Input & Output

## Input Format

- The first line contains an integer `n`, the number of intervals.
- The next `n` lines each contain two integers `start` and `end` representing an interval.

## Input Constraints

- `1 <= n <= 100`
- `-10^4 <= start <= end <= 10^4`

## Output Format

- Return a 2d array of the merged intervals, where each interval is represented as `[start, end]`

# Examples

## Example 1

### Input

```
4
1 3
2 6
8 10
15 18
```

### Output

```
[[1, 6], [8, 10], [15, 18]]
```

### Explanation

The intervals `[1, 3]` and `[2, 6]` overlap, so they are merged into `[1, 6]`. The other intervals do not overlap.

## Example 2

### Input

```
3
1 4
4 5
6 8
```

### Output

```
[[1, 5], [6, 8]]
```

### Explanation

The intervals `[1, 4]` and `[4, 5]` overlap, so they are merged into `[1, 5]`. The interval `[6, 8]` does not overlap with any other interval.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 33.Longest Common Subsequence -- Hard-2 45 mins

string

dynamic programming

subsequence

# Problem Statement

Given two strings `s1` and `s2`, find the length of their longest common subsequence (LCS). A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "abc", "abg", "bdf" are subsequences of "abcdefg".

# Input & Output

## Input Format

- The first line contains a string `s1`.
- The second line contains a string `s2`.

## Input Constraints

- 1 ≤ |s1|, |s2| ≤ 1000
- Both strings consist of lowercase English letters only.

## Output Format

- Return a single integer, the length of the longest common subsequence.

# Examples

## Example 1

### Input

```
abcde
ace
```

### Output

```
3
```

### Explanation

The longest common subsequence is "ace" with length 3.

## Example 2

### Input

```
abc
def
```

### Output

```
0
```

### Explanation

There is no common subsequence between "abc" and "def".

## Example 3

### Input

```
abcde
abcde
```

### Output

```
5
```

### Explanation

The longest common subsequence is the entire string "abcde" with length 5.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 34.Maximal Rectangle Area -- Hard-2 45 mins

array

2d array

dynamic programming

# Problem Statement

Given a 2D binary matrix filled with 0s and 1s, find the area of the largest rectangle containing only 1s.

# Input & Output

## Input Format

- The first line contains two integers `n` and `m`, the number of rows and columns in the matrix.
- The next `n` lines each contain `m` integers (0 or 1), representing the binary matrix.

## Input Constraints

- 1 ≤ n, m ≤ 100
- Each element of the matrix is either 0 or 1.

## Output Format

- Return a single integer, the area of the largest rectangle containing only 1s.

# Examples

## Example 1

### Input

```
4
4
1 0 1 0
1 0 1 1
1 1 1 1
1 0 0 1
```

### Output

```
4
```

### Explanation

The largest rectangle containing only 1s is formed by the elements `arr[1][2]`, `arr[2][2]`, `arr[2][3]`, `arr[1][3]` and has an area of 2 * 2 = 4

## Example 2

### Input

```
3
3
0 1 1
1 1 1
1 1 0
```

### Output

```
4
```

### Explanation

The largest rectangle containing only 1s is formed by the elements `arr[0][1]`, `arr[0][2]`, `arr[2][1]`, `arr[1][2]` and has an area of 2 * 2 = 4

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 35.Maximize Array Sum -- Hard-2 45 mins

array

greedy

sorting

# Problem Statement

You are given an array `A` of size `N` and an integer `K`. You can perform at most `K` operations on the array. In each operation, you can select any element of the array and negate its value (i.e., change `A[i]` to `-A[i]`). Your task is to maximize the sum of the array after performing at most `K` operations.

# Input & Output

## Input Format

- The first line contains an integer `N`, the size of the array.
- The second line contains `N` integers, the elements of the array `A`.
- The third line contains an integer `K`, the maximum number of operations allowed.

## Input Constraints

- `1 <= N <= 100`
- `-10^4 <= A[i] <= 10^4`
- `1 <= K <= 10^4`

## Output Format

- Return a single integer, the maximum sum of the array after performing at most `K` operations.

# Examples

## Example 1

### Input

```
5
-2 0 5 -1 -3
4
```

### Output

```
11
```

### Explanation

Negate `-2`, `-1`, and `-3` to get `[2, 0, 5, 1, 3]`. The sum is `2 + 0 + 5 + 1 + 3 = 11`.

## Example 2

### Input

```
3
-5 -2 -3
2
```

### Output

```
6
```

### Explanation

Negate `-5` and `-3` to get `[5, -2, 3]`. The sum is `5 + (-2) + 3 = 6`.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 36.Maximal Square Area -- Hard-2 45 mins

array

2d array

dynamic programming

# Problem Statement

Given a 2D binary matrix filled with 0s and 1s, find the area of the largest square containing only 1s.

# Input & Output

## Input Format

- The first line contains two integers `n` and `m`, the number of rows and columns in the matrix.
- The next `n` lines each contain `m` integers (0 or 1), representing the binary matrix.

## Input Constraints

- 1 ≤ n, m ≤ 100
- Each element of the matrix is either 0 or 1.

## Output Format

- Return a single integer, the area of the largest square containing only 1s.

# Examples

## Example 1

### Input

```
4
5
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

### Output

```
4
```

### Explanation

The largest square containing only 1s has a side length of 2, so the area is 2 * 2 = 4.

## Example 2

### Input

```
3
3
0 1 0
1 1 1
1 1 1
```

### Output

```
4
```

### Explanation

The largest square containing only 1s has a side length of 2, so the area is 2 * 2 = 4.

## Example 3

### Input

```
2 2
0 0
0 0
```

### Output

```
0
```

### Explanation

There are no 1s in the matrix, so the largest square area is 0.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 37.Minimum Cost to Equalize -- Hard-2 40 mins

array

greedy

# Problem Statement

You are given an array `A` of size `N` consisting of positive integers. You can perform the following operation any number of times:

- Choose any element of the array and either increment or decrement it by 1. Each operation costs 1 unit.

Your task is to determine the minimum cost required to make all elements of the array equal.

# Input & Output

## Input Format

- The first line contains a single integer `N`, the size of the array.
- The second line contains `N` space-separated integers, the elements of the array `A`.

## Input Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ A[i] ≤ 10,000

## Output Format

- Return a single integer, the minimum cost required to make all elements of the array equal.

# Examples

## Example 1

### Input

```
5
1 2 3 4 5
```

### Output

```
6
```

### Explanation

The optimal strategy is to make all elements equal to 3. The cost is:

- |1 - 3| + |2 - 3| + |3 - 3| + |4 - 3| + |5 - 3| = 2 + 1 + 0 + 1 + 2 = 6.

## Example 2

### Input

```
4
10 20 30 40
```

### Output

```
40
```

### Explanation

The optimal strategy is to make all elements equal to 25. The cost is:

- |10 - 25| + |20 - 25| + |30 - 25| + |40 - 25| = 15 + 5 + 5 + 15 = 40.

## Example 3

### Input

```
3
7 7 7
```

### Output

```
0
```

### Explanation

All elements are already equal, so the cost is 0.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 38.Max Sum Circular Subarray -- Hard-2 45 mins

array

subarray

greedy

# Problem Statement

Given a circular array of integers, your task is to find the maximum possible sum of a subarray. A circular array means that the end of the array wraps around to the beginning. For example, in the array `[1, -2, 3, -2]`, the subarray `[3, -2, 1]` is valid.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array.

## Input Constraints

- 1 ≤ n ≤ 100
- -10^4 ≤ array[i] ≤ 10^4

## Output Format

- Return a single integer, the maximum sum of a subarray in the circular array.

# Examples

## Example 1

### Input

```
4
1 -2 3 -2
```

### Output

```
3
```

### Explanation

The subarray `[3]` has the maximum sum of 3.

## Example 2

### Input

```
3
5 -3 5
```

### Output

```
10
```

### Explanation

The subarray `[5, 5]` (circular) has the maximum sum of 10.

## Example 3

### Input

```
3
-3 -2 -1
```

### Output

```
-1
```

### Explanation

The subarray `[-1]` has the maximum sum of -1.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 39.Longest Prefix Suffix -- Expert-1 45 mins

string

searching

# Problem Statement

You are given a string `s`. Your task is to find the length of the longest prefix of the string which is also a suffix. However, this prefix and suffix must not overlap. For example, in the string `abcab`, `ab` is a prefix and also a valid suffix, but they do not overlap.

# Input & Output

## Input Format

- A string `s` consisting of lowercase English letters.

## Input Constraints

- 1 ≤ |s| ≤ 1000 (where |s| is the length of the string)

## Output Format

- An integer representing the length of the longest prefix which is also a suffix and does not overlap.

# Examples

## Example 1

### Input

```
aabaab
```

### Output

```
3
```

### Explanation

The prefix "aab" is also a suffix. It has a length of 3, and it does not overlap.

## Example 2

### Input

```
abcdef
```

### Output

```
0
```

### Explanation

There is no prefix that is also a suffix.

## Example 3

### Input

```
levellevel
```

### Output

```
5
```

### Explanation

The longest prefix "level" is also a suffix and has a length of 5 without overlapping.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

JavaScript

NodeJS

TypeScript

PHP

C

Scala

Rust

Dart

Go

Swift

Python3

Kotlin

Ruby

Java

C++

C#

AddPreview

40.Permutation Sequence -- Expert-1 45 mins

string

permutation

math

# Problem Statement

Given an integer `n` and an integer `k`, return the `k`th permutation sequence of the set `[1, 2, 3, ..., n]`. The permutations are ordered lexicographically.

# Input & Output

## Input Format

- An integer `n` (1 ≤ n ≤ 9), representing the size of the set.
- An integer `k` (1 ≤ k ≤ n!), representing the index of the permutation sequence to return.

## Input Constraints

- `n` will be between 1 and 9 inclusive.
- `k` will be between 1 and `n!` inclusive.

## Output Format

- A string representing the `k`th permutation sequence.

# Examples

## Example 1

### Input

```
3
3
```

### Output

```
213
```

### Explanation

The permutations of `[1, 2, 3]` in lexicographical order are:

1. 123
2. 132
3. 213
4. 231
5. 312
6. 321 The 3rd permutation is `213`.

## Example 2

### Input

```
4
9
```

### Output

```
2314
```

### Explanation

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

## Example 3

### Input

```
2
2
```

### Output

```
21
```

### Explanation

The permutations of `[1, 2]` in lexicographical order are:

1. 12
2. 21 The 2nd permutation is `21`.

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 41.Minimum Replacements to Sort -- Expert-1 60 mins

array

sorting

greedy

# Problem Statement

You are given a 0-indexed integer array `nums`. In one operation, you can replace any element of the array with any two elements that sum to it.

For example, consider `nums = [5,6,7]`. In one operation, you can replace `nums[1]` with `2` and `4` and convert `nums` to `[5,2,4,7]`.

Return the minimum number of operations required to make the array sorted in non-decreasing order.

# Input & Output

## Input Format

- The first line contains an integer `n`, the size of the array.
- The second line contains `n` integers, the elements of the array `nums`.

## Input Constraints

- `1 <= n <= 100`
- `1 <= nums[i] <= 10^9`

## Output Format

- Return a single integer, the minimum number of operations required.

# Examples

## Example 1

### Input

```
3
5 6 7
```

### Output

```
0
```

### Explanation

The array is already sorted in non-decreasing order, so no operations are needed.

## Example 2

### Input

```
3
3 9 3
```

### Output

```
2
```

### Explanation

To sort the array, we need to perform the following operations:

1. Replace `9` with `3` and `6` → `[3, 3, 6, 3]`
2. Replace `6` with `3` and `3` → `[3, 3, 3, 3, 3]`

After these operations, the array becomes sorted.

## Example 3

### Input

```
5
1 3 2 4 5
```

### Output

```
1
```

### Explanation

Replace `3` with `2` and `1` → `[1, 1, 2, 2, 4, 5]`. The array is now sorted.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Dart

Rust

C#

Java

JavaScript

Ruby

Kotlin

Go

C

Python3

TypeScript

Swift

Scala

NodeJS

PHP

AddPreview

# 42.Closest Palindrome -- Expert-2 60 mins

string

palindrome

math

# Problem Statement

Given a string `n` representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

# Input & Output

## Input Format

- A single string `n` representing a positive integer.

## Input Constraints

- `1 <= len(n) <= 18`
- `n` consists of digits only and does not have leading zeros.

## Output Format

- Return a string representing the closest palindrome.

# Examples

## Example 1

### Input

```
123
```

### Output

```
121
```

### Explanation

The closest palindrome to 123 is 121.

## Example 2

### Input

```
1
```

### Output

```
0
```

### Explanation

The closest palindromes to 1 are 0 and 2. Since there is a tie, the smaller one (0) is returned.

## Example 3

### Input

```
808
```

### Output

```
818
```

### Explanation

The closest palindrome to 808 is 818.

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C#

Dart

JavaScript

Scala

Kotlin

Go

C

Python3

PHP

Java

TypeScript

NodeJS

Ruby

Rust

Swift

AddPreview

# 43.Longest substring without repeating characters -- Medium-2 30 mins

string

sliding window

# Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters

# Input & Output

## Input Format

The first and only line contains the string `s`

## Input Constraints

`s` has at least one character

## Output Format

An integer representing the length of the longest substring

# Examples

## Example 1

### Input

```
abcabcbb
```

### Output

```
3
```

### Explanation

The longest substring without repeating characters is abc. So, the value returned is 3.

## Example 2

### Input

```
abcda
```

### Output

```
4
```

### Explanation

The longest substring without repeating characters is abcd. So, the value returned is 4.

## Example 3

### Input

```
aaacbb
```

### Output

```
3
```

### Explanation

The longest substring without repeating characters is acb. So, the value returned is 3.

# User Task

Your task is to complete the function `solution()` which takes in the string `s` as a parameter and returns an integer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Python3

C++

PHP

Java

C#

JavaScript

Scala

NodeJS

Ruby

C

Go

AddPreview

# 44.Toffees in a Packet -- Hard-1 40 mins

array

sliding window

greedy

# Problem Statement

You are given an array `arr` of positive integers of size `n`. Each value in the array represents the number of toffees in a packet. Each packet can have any number of toffees. For example, if `arr = [2, 3]`, this means that the first packet has 2 toffees and the second has 3 toffees.
There are `x` students. The task is to distribute toffee packets among `x` students such that:

- Each students gets exactly one packet
- The difference between the maximum number of toffees given to a student and the minimum number of toffees given to a student is minimum

# Input & Output

## Input Format

- The first line is an integer `n`, which represents the number of chocolate packets
- The next line is an integer `x`, which represents the number of students
- The next line contains `n` space-separated integer values that represent the number of toffees in each packet

## Input Constraints

```
n >= x > 1
```

## Output Format

An integer representing the difference between the maximum and minimum.

# Examples

## Example 1

### Input

```
7
3
7 3 2 4 9 12 56
```

### Output

```
2
```

### Explanation

Imagine Student 1 got the 2nd packet, Student 2 got the 3rd packet and Student 3 got the 4th packet. So, the three students get 3, 2 and 4 toffees respectively.
The difference between the maximum (4) and minimum (2) number of toffees is 2. For no other distribution will this difference be smaller.

## Example 2

### Input

```
6
4
6 8 11 21 90 49
```

### Output

```
15
```

### Explanation

We have 4 students. Let's say Student 1 got the 1st packet, Student 2 got the 2nd packet, Student 3 got the 3rd packet and Student 4 got the 4th packet. So, the four students get 6, 8, 11 and 21 toffees respectively.
The difference between the maximum (21) and minimum (6) number of toffees is 15. For no other distribution will this difference be smaller.

# User Task

Your task is to complete the function `solution` which takes in two integers `n` and `x`, and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly.



Languages Available

C++

Go

Ruby

NodeJS

Java

Python3

JavaScript

PHP

Scala

C#

C

AddPreview

# 45.Balanced Word -- Medium-1 30 mins

# Problem Statement

We assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A balanced word is one where the sum of values of the characters on the left-hand side of the word equals the sum of values of the characters on the right-hand side.

Complete the function `solution` that returns integer `1` if the word is balanced, and `0` if it's not. Return `-1` if the word has an odd number of letters.

# Input & Output

## Input Format

The first line contains a String input

## Input Constraints

All words will be lowercase, and have a minimum of 2 characters

## Output Format

The output must be an integer which satisfies the required condition

# Examples

## Example 1

### Input

```
zips
```

### Output

```
1
```

### Explanation

The input string `zips` is divided to `zi` and `ps`.

- Sum of the position of characters in `zi` is 26 + 9 is 35
- Sum of the position of characters in `ps` is 16 + 19 is 35

As the sum of left-hand side and right-hand side characters is same so return 1

## Example 2

### Input

```
bray
```

### Output

```
0
```

### Explanation

```
The input string bray divided to br and ay
- Sum of the values of characters in br is 20
- Sum of the position of characters in  ay is 26
```

## Example 3

### Input

```
arise
```

### Output

```
-1
```

### Explanation

As `arise` has an odd number of letters, the output is -1

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C

Python3

Scala

C#

NodeJS

Java

JavaScript

Ruby

Kotlin

AddPreview

# 46.Smallest Subarray -- Hard-1 45 mins

array

sliding window

# Problem Statement

Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array. A subarray is a contiguous part of the array

# Input & Output

## Input Format

- The first line is the number of elements in the array
- The second line contains space-separated array elements

## Input Constraints

```
1 <= |A| <= 2000
```

## Output Format

The output is an integer which satisfies the required condition

# Examples

## Example 1

### Input

```
2
1 3
```

### Output

```
2
```

### Explanation

The only choice is to take both elements

## Example 2

### Input

```
1
2
```

### Output

```
1
```

### Explanation

The whole array must be taken as it has only one element

## Example 3

### Input

```
7
1 5 10 7 1 9 4
```

### Output

```
3
```

### Explanation

Subarray `{1, 5, 10}` has both maximum and minimum value.

## User Task

Your task is to complete the function `minSubarrayLength()` which takes a number of array elements N and an array as input and returns the expected answer. You don't need to read the input as a string, write code within the function block directly.



Languages Available

C++

C

Python3

Scala

C#

NodeJS

Java

JavaScript

Ruby

Kotlin

AddPreview

# 47.Money Bill Count -- Medium-2 30 mins

array

math

# Problem Statement

You are given an integer `amount` and an array of distinct integers `arr` which represent different denomination of `coins`. You have to find the minimum number of different `coins` required to match the `amount`.

# Input & Output

## Input Format

- The first line is the amount
- The second line is the number of elements in the input array. That is, the different types of `coins`
- The third line contains the input array elements separated by spaces

## Input Constraints

- There must be atleast 1 combination of `coins` which will match the `amount`

## Output Format

The output is an integer which satisfies the required condition.

# Examples

## Example 1

### Input

```
101
3
1 10 20
```

### Output

```
6
```

### Explanation

To get to `101`, we can have `5` coins that have a denomination of `20` and `1` coin that has a denomination of `1`. . That is, `(20 * 5) + (1 * 1) = 101`. So, with `6` coins, we can get to the amount of `101`.

We can also get to `101` with `10` coins of denomination `10` and `1` coin of denomination `1`. `(10 * 10) + (1 * 1) = 101`. But, this will need `11` coins in total.

So, the answer is `6` because we are looking for the **minimum** number of coins.

## Example 2

### Input

```
1050
4
1 10 20 100
```

### Output

```
13
```

### Explanation

```
1050 = (10 * 100) + (2 * 20) + (1 * 10)
Number of coins = 10 + 2 + 1 = 13
```

## Example 3

### Input

```
55
4
1 5 10 50
```

### Output

```
2
```

### Explanation

```
55 = (1 * 50) + (1 * 5)
Number of coins = 1 + 1 = 2
```

# User Task

Your task is to complete the function `minimumCoins()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

Java

C#

JavaScript

Scala

NodeJS

Ruby

C

AddPreview

# 48.Subarray's Sum Equal To Value -- Medium-2 30 mins

array

subarray

two pointer

# Problem Statement

You are given an array of integers `arr[]`. Your task is to find and count all subarrays that have a sum equal to a given target value `x`.

# Input & Output

## Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

## Input Constraints

For the input n, `n >= 2`

## Output Format

An integer representing the total number of subarrays whose sum is equal to `x`

# Examples

## Example 1

### Input

```
6
3
1 2 3 -3 1
```

### Output

```
4
```

### Explanation

Consider the subarrays `[1, 2]`, `[1, 2, 3, -3]`, `[2, 3, -3, 1]`, `[3]`. All these 4 subarrays sum up to 3.

## Example 2

### Input

```
3
2
1 1 1
```

### Output

```
2
```

### Explanation

The subarrays `[1, 1]`, at indices 0 and 1, `[1, 1]`, at indices 1 and 2

# User Task

Your task is to complete the function `solution()` which takes in the integers `n`, `x` and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly.



Languages Available

Java

Python3

PHP

NodeJS

JavaScript

C++

C

Rust

Go

AddPreview

# 49.Longest Continuous Increasing Subarray -- Hard-1 45 mins

array

subarray

sliding window

# Problem Statement

Given an unsorted array of integers `arr[]`, find the length of the longest continuous increasing subarray (subarray with strictly increasing elements)

# Input & Output

## Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line contains `n` space-separated integer values of `arr`

## Input Constraints

For the input n, `n >= 2`

## Output Format

An integer representing the length of the longest continuous increasing subarray. For Example 1, the output will be

# Examples

## Example 1

### Input

```
7
1 3 5 4 7 8 9
```

### Output

```
4
```

### Explanation

Consider the subarray `[4, 7, 8, 9]`. This is the longest increasing subarray possible. You will then return 4 as the output.

## Example 2

### Input

```
5
2 4 6 5 8
```

### Output

```
3
```

### Explanation

Consider the subarray `[2, 4, 6]`. This is the longest increasing subarray possible. You will then return 3 as the output.

# User Task

Your task is to complete the function `solution()` which takes in the integers `n` and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Python3

C++

PHP

Java

JavaScript

NodeJS

Rust

C

Go

AddPreview

50.Longest set of consecutive people wearing **white shirts** -- Hard-1 45 mins

bit manipulation

# Problem Statement

You are given a binary string, `bin_str` which represents people standing in a line. A binary string is a string which contains only `0’s` and `1’s`. A `0`, in this case, represents a person wearing a **black** shirt and a `1` represent a person wearing a **white** shirt. You are required to find the length of the longest set of consecutive people wearing **white shirts**, given that you are allowed to perform **at most** one swap between a person wearing a white shirt and a black one.

# Input & Output

## Input Format

The first and only line of input is the string `bin_str`

## Input Constraints

The string has at least 2 characters

## Output Format

The output is an integer

# Examples

## Example 1

### Input

```
11111000
```

### Output

```
5
```

### Explanation

We see that the longest set of consecutive `1's` (people wearing white shirts) starts at index `0` and ends at index `4`. There are no additional `1's` for us to perform any swaps with, so the length of the longest consecutive set of people wearing white shirts is 5.

## Example 2

### Input

```
111011101
```

### Output

```
7
```

### Explanation

By performing a swap between the `0` at index `3` and the `1` at index `8`, we get 7 consecutive `1's` starting at index `0` and ending at index `6`. so the length of the longest consecutive set of people wearing white shirts is 7.

# User Task

Your task is to complete `solution()` which accepts a string as a parameter and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.



Languages Available

Python3

C++

Java

C#

JavaScript

Scala

NodeJS

Ruby

C

AddPreview

# 51.Sum of weights of the mangoes -- Hard-1 45 mins

array

greedy

sliding window

# Problem Statement

You are given an array of integers, `weights` where each integer in the array represents the weight of a mango. You have to find the number of ways in which one mango can be removed from the list, such that the sum of weights of the mangoes at the even positions and the sum of weights of mangoes at the odd positions in the resulting list, are equal

# Input & Output

## Input Format

- The first line of input contains an integer
- The next line contains a single line of space separated integers

## Input Constraints

For each weight `w` in the array, `1 <= w <= 10000`

## Output Format

The output must be an integer which satisfies the required condition

# Examples

## Example 1

### Input

```
4
3 1 7 4
```

### Output

```
1
```

### Explanation

We see that removing the mango at index 1 (0-based indexing) modifies the list to `[3, 7, 4]`, and `weights[0] + weights[2] = weights[1] (3 + 4 = 7)`. This is the only way to satisfy the required condition. So, the output is 1.

## Example 2

### Input

```
3
3 3 3
```

### Output

```
3
```

### Explanation

We see that by removing any of the mangoes from the list, the sum of weights at the even and odd indices become equal. For example, removing element at index 0, modifies the list to `[3, 3]`, and `weights[0] = weights[1]`. This holds true if we remove elements at index 1 and index 2 as well. Therefore, the number of ways to satisfy the required condition is 3.

# User Task

Your task is to complete `solution()` which accepts a list as a parameter and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.



Languages Available

Python3

C++

Java

C#

JavaScript

Scala

NodeJS

Ruby

C

AddPreview

# 52.Smallest subarray with sum greater than x -- Medium-2 30 mins

array

subarray

# Problem Statement

Given an array of integers `arr` of length `n` and a number `x`, find the smallest subarray with sum greater than `x`.

# Input & Output

## Input Format

- The first line is an integer `n`, which represents the number of integers in the array
- The next line represents the integer `x`
- The next line contains `n` space-separated integer values of `arr`

## Input Constraints

- `n >= 2`
- `x` <= sum of `arr`

## Output Format

An integer representing the size of the smallest subarray.

# Examples

## Example 1

### Input

```
6
51
1 4 45 6 0 19
```

### Output

```
3
```

### Explanation

We have to find a subarray whose sum is more than 51. `[4, 45, 6]` satisfies this condition and is the smallest such subarray possible. So, the output will be the size of this subarray, 3.

## Example 2

### Input

```
5
50
1 10 3 40 18
```

### Output

```
2
```

### Explanation

A subarray whose sum is greater than 50 is `[40, 18]`. This is the smallest subarray. So, the output is 2.

# User Task

Your task is to complete the function `solution()` which takes in two integers `n` and `x`, and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

C++

Go

C

Python3

NodeJS

Java

JavaScript

PHP

AddPreview

# 53.Expensive Words -- Medium-1 30 mins

string

# Problem Statement

Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, d = 4, e = 5,..., z = 26). Uppercase alphabets have the same values as lowercase ones. However, if a word is **all** in UPPERCASE, the value of that word is doubled. Complete the function `solution()` that calculates the total value of the words in a sentence. Non-alphabet characters are ignored in this calculation.

# Input & Output

## Input Format

The first and only line of input contains a string.

## Input Constraints

- The sentence has at least one word
- Ignore spaces and punctuation
- Remember that the value of a word isn't doubled unless all the letters in it are uppercased.

## Output Format

The output is an integer

# Examples

## Example 1

### Input

```
abc ABC Abc
```

### Output

```
24
```

### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12
- Word 3's value = 1 + 2 + 3 = 6

Total value = 6 + 12 + 6 = 24

## Example 2

### Input

```
ab-c A-BC
```

### Output

```
18
```

### Explanation

- Word 1's value = 1 + 2 + 3 = 6
- Word 2's value = (1 + 2 + 3) x 2 = 12

Total value = 6 + 12 = 18

# User Task

Your task is to complete the function `solution()` which returns the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

Java

JavaScript

NodeJS

C

AddPreview

# 54.Number String -- Medium-1 30 mins

math

# Problem Statement

You are given an integer `n` which needs to be expanded into a string based on the digits of the number and their place values. The expanded string must be returned.

# Inputs & Outputs

## Input Format

The first and only line contains an integer `n`

## Output Format

A string representing the expanded form of the integer

# Examples

## Example 1

### Input

```
n = 35
```

### Output

```
30 + 5
```

## Explanation

5 is in the 1's place, and 3 is in the 10's place.

So, it can be expanded in the following way:

```
(3 x 10) + (5 x 1)
```

This results in the output `30 + 5`

## Example 2

### Input

```
73
```

### Output

```
70 + 3
```

### Explanation

3 is in the 1's place, and 7 is in the 10's place.

So, it can be expanded in the following way:

```
(7 x 10) + (3 x 1)
```

This results in an output of `70 + 3`

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

JavaScript

Java

NodeJS

C

AddPreview

# 55.Message Encoding -- Medium-1 30 mins

string

# Problem Statement

You are given a string `message` which needs to be encoded based on the following steps:

1. The length of the message to be encoded must be **exactly** 9 characters and all the characters must be lowercase letters. If either of these conditions are not met, the message must be encoded to `invalid`
2. The string must be divided into three parts, of three characters each. The first part `part_1` is the first three characters, `part_2` is the next three characters, `part_3` is the last three characters. These parts will be used in a later step.
3. The first and the third letter must be converted to the corresponding number (a = 1, b = 2, c = 3...z = 26 etc)
4. Reverse the fourth, fifth and sixth characters of the original message ('abc' will be converted to 'cba')
5. Replace the seventh, eighth and ninth letter of the original string with the next letter of the alphabet (a -> b, b -> c, z -> a)
6. Return the string in the following order: `part_3` + `part_1` + `part_2`

# Input & Output

## Input Format

The first line contains a string

## Output Format

A single string

# Examples

## Example 1

### Input

```
moirarose
```

### Output

```
ptf13o9rar
```

### Explanation

We start with Step 1: The message contains exactly nine characters and has only lowercase characters so the message is valid

Step 2: The string is divided into 3 parts: `moi`, `rar`, `ose`

Step 3: The first and the third letter must be converted to the corresponding letter: `m=13`, `i=9`, so the string is `13o9rarose`

Step 4: Reverse the fourth, fifth and sixth characters of the original message: `rar` gets reversed to `rar`, so the string now is, `1309rarrose`

Step 5: Replace the seventh, eighth and ninth letter with the next letter of the alphabet. `ose` gets replaced with `ptf`

Step 6: Return the string in the following order: `part_3` + `part_1` + `part_2`: part3 is `ptf`, part_2 is `13o9`, part_1 is `rar`. The string to be returned is `ptf13o9rar`

## Example 2

### Input

```
AlexisRose
```

### Output

```
invalid
```

### Explanation

The message contains uppercase characters.

# User Task

Your task is to complete the function `solution()` which takes a string `message` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

C++

Python3

NodeJS

Java

JavaScript

C

AddPreview

# 56.Eat the number -- Medium-1 30 mins

array

# Problem Statement

A number can eat the number to the right of it if it's smaller than itself. After eating that number, it becomes the sum of itself and that number. Your job is to return the final array after the leftmost element has finished "eating".

# Input & Output

## Input Format

- The first line contains an integer `n`, the number of elements in input array.
- The next line contains space-separated integers which are the elements of the array.

## Input Constraints

- Each array has at least 2 elements
- Each element is an integer

## Output Format

The output is an array of integers

# Examples

## Example 1

### Input

```
4
5 3 7 30
```

### Output

```
15 30
```

### Explanation

For the array a = [5, 3, 7, 30] , size = 4

- `5` eats `3` to get `[8, 7, 30]`.
- `8` eats `7` to get `[15, 30]`
- `15` cannot eat `30` and hence `[15, 30]` is the final output

## Example 2

### Input

```
3
5 1 4
```

### Output

```
10
```

### Explanation

For the array `a = [5, 1, 4]` , size = 3

- `5` eats `1` to get `[6, 4]`.
- `6` eats `4` to get `[10]` which is the final output

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

Java

JavaScript

NodeJS

C

AddPreview

# 57.Rearrange Sentence -- Medium-1 30 mins

string

sorting

# Problem Statement

Given a sentence with numbers representing a word's location embedded within each word of given sentence, return the sorted sentence according to the numbers in each word.

# Input & Output

## Input Format

The first and only line of input is a string

## Input Constraints

Only integers between 1 and 9 will be present in the string

## Output Format

The output will be a string

# Examples

## Example 1

### Input

```
is2 Thi1s T4est 3a
```

### Output

```
This is a Test
```

### Explanation

- the word `is2` contains 2 - so the word `is` location is `2`
- the word `Thi1s` contains 1 - so the word `This` location is `1`
- the word `T4est` contains 4 - so the word `Test` location is `4`
- the word `3a` contain 3 - so the word `a` location is `3`

so when we rearrange we get output :

```
This is a Test
```

## Example 2

### Input

```
is3 Cri1stiano 4the Rona2ldo 5best
```

### Output

```
Cristiano Ronaldo is the best
```

### Explanation

- word `is3` contains number `3`, so its location in output string is `3`.
- word `Cri1stiano` contains number `1`, so its location in output string is `1`.
- word `4the` contains number `4`, so its location in output string is `4`.
- word `Rona2ldo` contains number `2`, so its location in output string is `2`.
- word `5best` contains number `5`, so its location in output string is `5`

so the output is, `Cristiano Ronaldo is the best`

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C

Python3

NodeJS

Java

JavaScript

AddPreview

# 58.Column With Maximum Sum -- Medium-1 30 mins

array

# Problem Statement

You are given an array of numbers and a value for `n`. The number `n` splits the array into `n-sized` groups. After splitting, these groups are stacked on top of each other (see below). You have to find the **column-wise sum** and return the column number that has the **largest sum**. In case two or more columns have the same sum, return the **smallest** column number of these. Please note that the column number which should be returned is **1-indexed**.

# Input & Output

## Input Format

- The first line is the number of elements in the input array
- The second line contains input array elements separated by spaces
- The third line is the value of `n`, i.e., the number of elements to be grouped in each subgroup

## Input Constraints

- `2 <= n <= 100`
- `n` will always divide input array into equal-length groups

## Output Format

- A valid column number which has the largest sum

# Examples

## Example 1

### Input

```
12
4 14 12 7 14 16 5 13 7 16 11 19
4
```

### Output

```
2
```

### Explanation

The array elements `4 14 12 7 14 16 5 13 7 16 11 19` are divided into subgroups of size `4` so we get

```
[[4, 14, 12,  7],
[14, 16, 5, 13],
[7, 16, 11, 19]]
```

When we compute the column wise sum we have

```
25, 46, 28, 39
```

the maximum value of `46` is in column 2 therefore it is returned as output

## Example 2

### Input

```
9
14 9 19 6 13 13 3 2 12
3
```

### Output

```
1
```

### Explanation

The array elements `14 9 19 6 13 13 3 2 12` are divided into subgroups of size `3` so we get

```
[
  [14, 9, 19],
  [6, 13, 13],
  [24, 2, 12]
]
```

When we compute the column-wise sum we get

```
44, 24, 44
```

Both column `1` and `3` have the same sum of `44`. But, as `1` is smaller, that is returned as the output.

# User Task

Your task is to complete the function solution() which returns the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

JavaScript

Java

NodeJS

C

AddPreview

# 59.Encoding -- Medium-1 30 mins

string

# Problem Statement

You are given a string `message` of lowercase characters and an integer `key`. The string needs to be encoded using the integer based on the following rules:

1. Assign a number to each letter in the alphabet. 'a' corresponds to 1, 'b' corresponds to 2, 'c' corresponds to 3 and so on.
2. Starting from the leftmost character of `message`, sum up the integer value of the first character with the first digit of `key`. Then, sum the integer value of the next character with the next digit of `key`. If the digits of `key` are exhausted, start from the first digit of `key` and continue till the characters of `message` are exhausted.
3. Concatenate all the sums you have calculated into a single string, separated by commas, and return it.

# Inputs & Outputs

## Input Format

- The first line contains the `message` string
- The second line contains the integer `key`

## Input Constraint

- `message` has at least 2 characters
- `message` contains only lowercase alphabets
- `key` has at least 2 digits

## Output Format

- A string containing the different sums which have been calculated, separated by commas
- No spaces after the commas

# Examples

## Example 1

### Input

```
start
1357
```

### Output

```
20,23,6,25,21
```

### Explanation

Start with the first character of `message`, which is 's'. Its integer value is 19. Add the first digit of `key`, which is 1, to 19. The integer value of 't' is 20. Adding this to the next digit of `key`, which is 3, gives you a sum of 23. This process continues until the end of the `message` string. The example is explained in the table below.

| message            | s    | t    | a    | r    | t    |
| ------------------ | ---- | ---- | ---- | ---- | ---- |
| message int values | 19   | 20   | 1    | 18   | 20   |
| key                | 1    | 3    | 5    | 7    | 1    |
| sum                | 20   | 23   | 6    | 25   | 21   |

So, the output for this example is: `20,23,6,25,21`

## Example 2

### Input

```
masterpiece
1939
```

### Output

```
14,10,22,29,6,27,19,18,6,12,8
```

### Explanation

| message            | m    | a    | s    | t    | e    | r    | p    | i    | e    | c    | e    |
| ------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| message int values | 13   | 1    | 19   | 20   | 5    | 18   | 16   | 9    | 5    | 3    | 5    |
| key                | 1    | 9    | 3    | 9    | 1    | 9    | 3    | 9    | 1    | 9    | 3    |
| sum                | 14   | 10   | 22   | 29   | 6    | 27   | 19   | 18   | 6    | 12   | 8    |

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

C

Python3

NodeJS

Java

JavaScript

AddPreview

60.Valid coupon -- Medium-1 30 mins

string

# Problem Statement

A fake coupon website is operating on the internet, and a major e-commerce company must try to identify the fake coupons. Every coupon has a serial number that can be used to determine whether it is valid. The serial number also can be used to determine the discount amount of the coupon. A valid serial number will have the following characteristics:

1. There are 10 to 12 characters.
2. The first 3 characters are distinct uppercase English letters.
3. The next 4 characters represent the year the coupon was printed and will always be between 1900 and 2019 inclusive.
4. The next characters represent the coupon discount amount and may be any one of {10, 20, 50, 100, 200, 500, 1000}.
5. The next character should be the last character of the serial number. The serial number must end with exactly one uppercase English letter only

Given a coupon code, return the **first character** of the coupon code if it is valid i.e., it satisfies all the 5 conditions mentioned above. Otherwise, return the **last character**.

# Input & Output

## Input Format

The first and only line is a string

## Input Constraints

The coupon code has at least 1 character

## Output Format

Return a character in C/C++/Java and string of length 1 in JavaScript/Python

# Examples

## Example 1

### Input

```
AVG190420T
```

### Output

```
A
```

### Explanation

- There are 10 characters, so it passes condition 1.
- The first three characters `AVG` are distinct & uppercase, so it passes condition 2
- The next four characters `1904` is between 1900 and 2019, so it passes condition 3
- For the next two characters `20` is among the list of values, so it passes condition 4
- The next character which is the last character is a `T`, so it passes condition 5

## Example 2

### Input

```
1234XYZ
```

### Output

```
Z
```

### Explanation

The string doesn't have 10 to 12 characters. Therefore, it is invalid and we are returning the last character `Z`.

# User Task

Your task is to complete the function `solution()` which takes a string `string` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Python3

C++

Java

JavaScript

NodeJS

C

AddPreview

# 61.Compress String -- Medium-1 30 mins

string

# Problem Statement

You are given a string of characters `chars`. This string needs to be compressed based on the following rules:

1. If the number of times a character repeats in a string is 1, then the resultant string must contain the character itself.
2. If the number of times a character `x` is repeated is `n`, then the resultant string should contain `xn`

The order of characters in the resultant string must match the order in which they appear in the input string.

# Input & Output

## Input Format

The first and only line of input is a string

## Input Constraints

- The string only has lowercase alphabets.
- The string contains at least 1 character.

## Output Format

- A string is returned as the output

# Examples

## Example 1

### Input

```
ahaee
```

### Output

```
a2he2
```

### Explanation

`a` occurs twice, `h` occurs once and `e` occurs twice.

## Example 2

### Input

```
a
```

### Output

```
a
```

### Explanation

`a` occurs only once.

# User Task

Your task is to complete the function `solution()` which returns the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

Java

JavaScript

NodeJS

C

AddPreview

# 62.Evaluate group of parentheses -- Medium-2 30 mins

string

stack

# Problem Statement

You are given a balanced parentheses string. That is, each open `"("` has corresponding closed `")"`. You have to compute the total score based on the following rules:

- Substring `s = "()"` has score 1,
- Substring `s1s2` has total score as score of `s1` + score of `s2`, for ex `()()` has total score `1 + 1 = 2`
- Substring `"(s)"` has total score as `2` * score of `"s"`.
- Calculate the total score of the given expression and return it as integer.

# Input & Output

## Input Format

The first line and only line contains a string

## Input Constraints

The string is a balanced parentheses string with at least one pair of balanced parentheses

## Output Format

An integer representing the total score of the string

# Examples

## Example 1

### Input

```
(()(()))
```

### Output

```
6
```

### Explanation

The `(` at index `0` closes only at the end of the string. So, whatever comes within this will be multiplied by 2.

The next `(` at index `1` closes at index `2`, so, this adds 1 to the result.

The next `(` at index `3` closes at index `6`. So, whatever comes between index `3` and `6` will be multiplied by 2.

The last `(` at index `4` closes at index `5`, so, 1 is added to the result

Therefore, the result is `2 * ((2 * 1) + 1) = 6`

## Example 2

### Input

```
()((()))
```

### Output

```
5
```

### Explanation

The `(` at index `0` closes at index `1`. So, 1 is added to the result.

The next `(` at index `2` closes at index `7`. So, whatever comes between index `2` and `7` will be multiplied by 2.

The next `(` at index `3` closes at index `6`. So, whatever comes between index `3` and `6` will be multiplied by 2.

The last `(` at index `4` closes at index `5`, so, 1 is added to the result

Therefore, the result is `1 + (2 * 2 * 1) = 5`

# User Task

Your task is to complete the function solution() and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C++

JavaScript

Java

NodeJS

C

AddPreview

# 63.Unique triplets whose sum equals n -- Medium-2 30 mins

array

# Problem Statement

Given an array of elements `array`, and an integer `k`, find out the number of unique triplets whose sum is equal to `k`. A unique triplet consists of three values from different indices, and triplets with the same values (regardless of order or indices) are considered duplicates and only counted once. Once a triplet is selected, the triplet cannot be reused. So, if you have an array `[1, 2, 3]` and the value of `k` is `6`, `[1, 2, 3]` is your only unique triplets. `[3, 2, 1]`, `[2, 1, 3]` and other triplets using the same triplet in a different order cannot be counted as unique triplets.

# Input & Output

## Input Format

- The first line contains an integer `size`, the number of elements in input array
- The next line contains space-separated integers which are the elements of the array.
- The next line contains the 'k' value i,e., the sum of triplets should equate to

## Input Constraints

The array has at least 3 elements

## Output Format

The output is an integer.

# Examples

## Example 1

### Input

```
6
1 0 2 6 3 9
11
```

### Output

```
2
```

### Explanation

There are two unique triplets whose sum equals `11`, `[0, 2, 9]` and `[2, 6, 3]`

## Example 2

### Input

```
9
1 2 6 3 4 5 9 10 11
20
```

### Output

```
5
```

### Explanation

The unique triplets whose sum equals 20 are

```
[1, 9, 10], [6, 3, 11], [4, 5, 11], [6, 4, 10], [6, 5, 9]
```

## Example 3

### Input

```
6
1 1 4 5 4 5
10
```

### Output

```
1
```

### Explanation

There is only 1 unique triplets whose sum equals 10

```
[1, 4, 5]
```

All other instances are duplicates of the same triplet.

# User Task

Your task is to complete the function `solution()` which takes in an integer `numOfElements`, an array `arr` and another integer `k and returns an integer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

NodeJS

C

C++

JavaScript

Java

Python3

AddPreview

# 64.Compare and merge strings -- Medium-2 30 mins

sorting

string

# Problem Statement

You are given two strings `string1` and `string2` made of uppercase letters. You must create a third string `string3` out of them. These are the rules:

- Step 1: Compare the first letter in both strings and pick the smaller of the two. (for eg, if the words are `ABC` and `DEF`, you will pick `A` from the first string)
- Step 2: If both the letters are the same, pick the letter from `string1`
- Step 3: The letter you pick is removed from the original string and gets added to `string3`
- Step 4: You again compare the first two letters in the two strings like in Step 1 above and follow Steps 2 and 3

You follow this process until no letters are left in `string1` and `string2`.

# Input & Output

## Input Format

- The first line contains a string
- The second line contains a string

## Input Constraint

- Both input strings are in upper case
- Each string has at least one alphabet

## Output Format

A single string

# Examples

## Example 1

### Input

```
ACA
BCF
```

### Output

```
ABCACF
```

### Explanation

The table below shows how the process works. We extract characters from both strings step-by-step.

| string1 | string2 | string3 |
| ------- | ------- | ------- |
| ACA     | BCF     |         |
| CA      | BCF     | A       |
| CA      | CF      | AB      |
| A       | CF      | ABC     |
|         | CF      | ABCA    |
|         | F       | ABCAC   |
|         |         | ABCACF  |

## Example 2

### Input

```
RAJ
RAVI
```

### Output

```
RAJRAVI
```

### Explanation

The first letters to choose from are R and R since they are on the top of the stacks. R is chosen from the first string. Then, the options are A and R. A is chosen. Then the two stacks have J and R, so J is chosen. The current string is RAJ. As all the letters from the first stack have been used up, all the characters from the second stack can be appended to the resultant string.

## Example 3

### Input

```
DAVID
ROSE
```

### Output

```
DAROSEVID
```

### Explanation

The first letters to choose from are D and R. D is chosen from the first string. Then, the options are A and R. A is chosen. Then the two stacks have V and R, so R is chosen. The current string is DAR. Next, the letters to choose from are V and O. O is selected. This process continues until all the characters of both stack have been used up.

# User Task

Your task is to complete the function `solution()` which takes 2 strings `string1` and `string2` and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Python3

C++

Java

JavaScript

NodeJS

C

AddPreview

# 65.Packing Bags -- Medium-2 30 mins

array

greedy

# Problem Statement

You arrive at the supermarket checkout and you've only got a limited number of shopping bags with you. Miser that you are, you hate buying extra bags when you've got dozens at home that you forgot to bring with you! Can you fit all your shopping into the bags you've got with you?

Each bag can carry a maximum of 10kg and each item you've purchased weighs between 1 and 10kg.

You have to find out if there are enough bags to carry all the items. Return true if there are enough bags to contain all the items, false otherwise.

# Input & Output

## Input Format

The first line contains an integer `n`, the number of elements in input array.

The next line contains `n` space-separated integers which are the elements of the array.

The next line contains an integer which is the number of bags

## Input Constraints

- All weights will be integers between 1 and 10kg inclusive
- Items can be packed in any order
- There may be more than one way to fit all the items in the available bags

# Examples

## Example 1

### Input

```
12
2 1 2 5 4 3 6 1 1 9 3 2
4
```

### Output

```
true
```

### Explanation

Bag 1 = [2, 1, 2, 5] (10kg)

Bag 2 = [4, 3, 3] (10kg)

Bag 3 = [6, 2, 1, 1] (10kg)

Bag 4 = [9] (9kg)

## Example 2

### Input

```
11
2 7 1 3 3 4 7 4 1 8 2
4
```

### Output

```
false
```

### Explanation

Bag 1 = [2, 8] (10kg)

Bag 2 = [3, 7] (10kg)

Bag 3 = [2, 4, 4] (10kg)

Bag 4 = [7, 3] (10kg)

two 1kg items are left over

# User Task

Your task is to complete `solution()` which accepts 3 parameters, the number of elements, the array of items and the number of bags, and returns an integer. You don't need to read the input, just use the parameter(s) of the function and write code within the function block and return the required answer.



Languages Available

C++

C

Python3

NodeJS

Java

JavaScript

AddPreview

# 66.Subarray Sum Modulo -- Medium-2 30 mins

array

subarray

# Problem Statement

A subarray of array "a" of length "n" is a continuous segment from a[i] through a[j] where `0 <= i <= j < n` . The sum of an array is the sum of its elements. Given an array `a` containing `n` integers, and an integer `m`, determine the maximum value of the sum of any of its subarrays modulo `m`.

# Input & Output

## Input Format

The first line contains an integer `n`, the number of elements in the input array.

The second line contains an integer `m`, the modulo divisor.

The third line contains space-separated integers, i.e., array elements

## Input Constraints

- 2 <= n <= 105
- 1 <= m <= 1014
- 1<= a[i] <= 1018

## Output

The output must be an integer which is the maximum value of sum of any of the arrays' subarrays, modulo `m`.

# Examples

## Example 1

### Input

```
5
7
3 3 9 9 5
```

### Output

```
6
```

### Explanation

For the array a = [3,3,9,9,5] , n = 5 and m = 7, the subarrays_sum % m is as follows

- `[3] % 7 => 3`.
- `[9] % 7 => 2`.
- `[5] % 7 => 5`.
- `[9,5] % 7 => 14 % 7 => 0`.
- `[9,9] % 7 => 18 % 7 => 4`.
- `[3,9] % 7 => 11 % 7 => 4`.
- `[3,3] % 7 => 6 % 7 => 6`.
- `[3,9,9] % 7 => 21 % 7 => 0`.
- `[3,3,9] % 7 => 15 % 7 => 1`.
- `[9,9,5] % 7 => 23 % 7 => 2`.
- `[3,3,9,9] % 7 => 24 % 7 => 3`.
- `[3,9,9,5] % 7 => 26 % 7 => 5`.
- `[3,3,9,9,5] % 7 => 29 % 7 => 1`.

## Example 2

### Input

```
3
6
1 2 3
```

### Output

```
5
```

### Explanation

For the array a = [1,2,3] , n = 3 and m = 6, the subarrays_sum % m is as follows

- `[1] % 6 => 1`.
- `[2] % 6 => 2`.
- `[3] % 6 => 3`.
- `[2,3] % 6 => 5 % 6 => 5`.
- `[1,2] % 6 => 3 % 6 => 3`.
- `[1,2,3] % 6 => 6 % 6 => 0`.

# User Task

Your task is to complete the function `solution()` which takes an integer `n`, an integer `m` and an array `arr`, and returns the expected answer which is an integer. You don't need to read the input or print output, just write code within the function block directly.



Languages Available

C++

C

Python3

NodeJS

Java

JavaScript

AddPreview

# 67.Cut and Add -- Medium-2 30 mins

string

# Problem Statement

Harry and Ron choose a string of characters. Harry chose a number `M` (less than the length of the string) and Ron chose `N` (less than the length of the string). Harry will cut `M` letters from the end of the string, add it to the beginning and will give it to Ron. Then, Ron will cut `N` letters from the end of the string, add it to the beginning and give to Harry. This process will continue till they get the original word string back.

For a given string and given values of `M` and `N`, find the number of turns in which they will get the original string back.

# Input & Output

## Input Format

The first line is the word string.

The second line is the integer `M`.

The third line is the integer `N`.

## Input Constraint

If the length of the string is `l`

- `1 <= M <= l`
- `1 <= N <= l`

## Output Format

The output must be an integer that corresponds to the minimum number of operations required to get back the original word string.

# Examples

## Example 1

### Input

```
AbcDef
1
2
```

### Output

```
4
```

### Explanation

This is how the word string will change.

`AbcDef` -> `fAbcDe` -> `DefAbc` -> `cDefAb` -> `AbcDef`.

As there are `4` steps needed to bring the string back to its original form, the output must be `4`.

## Example 2

### Input

```
abcabc
1
1
```

### Output

```
3
```

### Explanation

This is how the word string will change.

`abcabc` -> `cabcab` -> `bcabca` -> `abcabc`

As there are `3` steps needed to bring the string back to its original form, the output must be `3`.

# User Task

Your task is to complete the function `solution()` which takes 2 Integers `n` and `m` and an array as input and returns the expected answer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

C++

C

Python3

NodeJS

Java

JavaScript

AddPreview

# 68.Partition Array -- Medium-2 30 mins

array

greedy

# Problem Statement

You are given an array `arr` of integers of length `n`. Your task is to check whether it is possible to divide the array into 2 parts such that the first part contains one of the elements of the array and the second part contains all the other elements, and the product of all the elements in the second part equal the value of the element in the first part. If it is possible to achieve this, return the index (0-indexed) of the element you have chosen as your first part. If there are multiple answers, return the answer with the smallest index. If it is not possible to divide the array in this way, return -1.

# Input & Output

## Input Format

- The first line contains the number of elements in the input array
- The second line contains the elements of the input array separated by spaces.

## Input Constraint

```
2 <= n <= 100
```

## Output Format

An integer which is the index of the element in the first part, or -1

# Examples

## Example 1

### Input

```
4
2 8 4 1
```

### Output

```
1
```

### Explanation

We see that 8 = 2 * 4 * 1, and 1 is the index of 8

## Example 2

### Input

```
3
2 2 8
```

### Output

```
-1
```

### Explanation

It is not possible to divide the array in any way to get the required partitions

# User Task

Your task is to complete the function `solution()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

C++

Python3

NodeJS

Java

JavaScript

C

AddPreview

# 69.Prison Break -- Hard-1 45 mins

array

bit manipulation

# Problem Statement

Imagine you are in a prison with many prison cells. The cells can be locked or unlocked. We represent the cells as an array of `0`'s and `1`'s, where `0` represents an unlocked cell and `1` represents a locked cell. Each cell has exactly 1 prisoner. You are the prisoner in the **leftmost** cell. So, if the configuration is `0 1 0`, it means there are 3 cells: you are in an unlocked cell, the next cell is locked, and the cell after that is also unlocked.

If your cell is unlocked, you can walk down the cells in order and release different prisoners. The cell must be unlocked (`0`) for you to be able to release the prisoner. Once you unlock a cell, all cells will flip from locked to unlocked, and vice-versa. So, if the state is `0 1 0`, it will become `1 0 1`, for example.

Once you release a prisoner, you cannot move back to the previous cell. You can only move forward. Your task is to return the number of prisoners that you can release, `num_release`.

# Input & Output

## Input Format

- The first line is the number of cells
- The second line contains input array elements separated by spaces i.e `0` and `1`.

## Input Constraints

- The array will have at least 1 element
- The array will only have valid integers i.e `0` and `1`

## Output Format

The output must be an integer

## Examples

### Example 1

#### Input

```
3
1 1 1
```

#### Output

```
0
```

#### Explanation

As the first cell is locked, we can't release any prisoners.

### Example 2

#### Input

```
7
0 0 1 1 1 0 1
```

## Output

```
4
```

#### Explanation

```
[0, 0, 1, 1, 1, 0, 1]
// You release the prisoner in the 1st cell.

[1, 1, 0, 0, 0, 1, 0]
// You release the prisoner in the 3rd cell (2nd one locked).

[0, 0, 1, 1, 1, 0, 1]
// You release the prisoner in the 6th cell (3rd, 4th, and 5th locked).

[1, 1, 0, 0, 0, 1, 0]
// You release the prisoner in the 7th cell - and you are done!
```

The total number of prisoners released is `4`. So your function will return `4`

# User Task

Your task is to complete the function `countReleasedPrisoner()`. You don't need to read the input, just write code within the function block directly.



Languages Available

JavaScript

C++

NodeJS

C

Python3

Java

AddPreview

70.Perfect Numbers -- Medium-1 30 mins

math

# Problem Statement

Given an integer `n`, find out all perfect numbers from 1 to n (1 and n are included). A perfect number is a number whose sum of factors is the same number, excluding itself. If there are no numbers to print, an empty string must be returned.

# Inputs & Outputs

## Input Format

The first and only line of input contains the integer `n`

## Input Constraints

For the integer n `2 <= n <= 1000000`

## Output Format

It should be a string of space-separated integers. The output should be a string of space-separated integers which are perfect numbers. If there are no numbers to print, return an empty string

# Examples

## Example 1

### Input

```
7
```

### Output

```
6
```

### Explanation

The only number which has the sum of factors equal to the number itself between 1 and 6 is 6. Factors of 6 excluding 6 are 1, 2, 3

Sum of the factors `1 + 2 + 3 = 6`

## Example 2

### Input

```
200
```

### Output

```
6 28
```

### Explanation

Factors of 6 excluding 6 are 1, 2, 3

Sum of the factors `1 + 2 + 3 = 6`

Factors of 28 excluding 28 are 1, 2, 4, 7, 14

Sum of the factors = `1 + 2 + 4 + 7 + 14 = 28`

# User Task

Your task is to complete `solution()` which accepts an integer and returns a string of space separated perfect numbers between 1 and n. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

Java

C

AddPreview

# 71.Remove White Spaces -- Medium-1 30 mins

string

# Problem Statement

Write a Program to remove all white spaces from a string without built-in functions.

# Input & Output

## Input Format

The first and only line contains a string

## Output Format

The output is a single string with the spaces removed

# Examples

## Example 1

### Input

Rise and shine

### Output

Riseandshine

### Explanation

Removing all spaces in the string, we get Riseandshine

## Example 2

### Input

Visual Studio Code

### Output

VisualStudioCode

### Explanation

Removing all spaces in the string, we get VisualStudioCode

# User Task

You task is to complete `solution()` which accepts a string `str` and returns a string without spaces. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Python3

C

Java

AddPreview

# 72.Square Numbers -- Medium-1 30 mins

math

# Problem Statement

Write a program to find a number whose square has the same digits in the end as the number itself

# Input & Output

## Input Format

The first and only line contains an integer

## Input Constraints

For the number `n`, `-10000 <= n <= 10000`

## Output Format

Return `1` or `0` based on whether the given condition is satisfied or not.

# Examples

## Example 1

### Input

```
25
```

### Output

```
1
```

### Explanation

The square of 25 is 625, which ends with 25, which is the number itself. So, `1` is returned

## Example 2

### Input

```
8
```

### Output

```
0
```

### Explanation

The square of 8 is 64. As the square does not end with 8, `0` is returned

## User Task

Your task is to complete `solution()` which accepts an integer and returns the expected answer which is also an integer. You don't need to read the input as an integer, just write code within the function block directly.



Languages Available

Python3

Java

C

AddPreview

# 73.Roots of Quadratic Equation -- Medium-2 30 mins

math

# Problem Statement

Write a program to find roots of quadratic equation in the form ax2 + bx + c where a, b & c are integers. The equation will always yield integer roots.

# Input & Output

## Input Format

The first and only line of input contains 3 integers which represent the coefficients (constants a, b and c in the equation in the problem statement) of the quadratic equation.

## Input Constraints

```
-10000 <= a,b,c <= 10000
```

## Output Format

The output must be a string of space-separated integers which are the roots of the equation.

# Examples

## Example 1

### Input

```
1 4 3
```

### Output

```
-1 -3
```

### Explanation

Solving the equation for x2 + 4x + 3, we find the roots of the equation are -1 and -3

## Example 2

### Input

```
1 2 1
```

### Output

```
-1 -1
```

### Explanation

Solving the equation for x2 + 2x + 1, we find the roots of the equation are -1 and -1

# User Task

Your task is to complete `solution()` which accepts three integers a, b & c and returns a string which is contains the roots of the equation, separated by a space. You don't need to read the input, just write code within the function block directly.



Languages Available

Python3

C

Java

AddPreview

# 74.Find Common Vowels -- Medium-1 30 mins

string

# Problem Statement

You are given two strings `str_1` and `str_2`. You have to find the vowels in `str_1` that are also present in `str_2`. The output must be a concatenation of the common vowels, in alphabetical order. If there are no common vowels, you must return an empty string.

# Input & Output

## Input Format

The first line is a string which contains `str_1` The second line is a string which contains `str_2`

## Input Constraints

- Both strings have at least 1 character
- All characters in both strings are lower-case

## Output Format

A single string which is satisfies the given condition.

# Examples

## Example 1

### Input

```
float
arose
```

### Output

```
ao
```

### Explanation

The common vowels in `float` and `arose` are `ao` sorted in alphatical order

## Example 2

### Input

```
equivalent
fraction
```

### Output

```
ai
```

### Explanation

The common vowels in `equivalent` and `fraction` are `ai` sorted in alphatical order

# User Task

Your task is to complete the function `solution()` which takes 2 strings `string1` and `string2` as input and returns another string as output. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Java

C

AddPreview

# 75.Inversion Count -- Medium-1 30 mins

array

# Problem Statement

Given an array `a` of length `n`, two elements `a[i]` and `a[j]` form an inversion if `a[i]` > `a[j]` and `i` < `j`. Find the number of inversions the array contains.

# Inputs & Outputs

## Input Format

- The first line of input contains an integer which is the length of the array.
- The next line of input contains the elements of the array, separated by spaces.

## Input Constraints

For the length of the array `n`

```
2 <= n <= 10000
```

## Output Format

The output will be an integer which contains the number of inversions

# Examples

## Example 1

### Input

```
5
2 4 1 3 5
```

### Output

```
3
```

### Explanation

The inversions of the array `[2, 4, 1, 3, 5]` are: `(2, 1)`, `(4, 2)`, `(4, 3)`

So, the number of inversions are `3`

## Example 2

### Input

```
3
1 2 5
```

### Output

```
0
```

### Explanation

The array `[1, 2, 5]` is already sorted, so the number of inversions is 0.

# User Task

Your task is to complete the function `solution()` which takes an array length and the array as input and returns the inversion count. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Java

C

AddPreview

# 76.Smallest Subarray (JS) -- Medium-2 45 mins

## Problem Statement

Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.

**Problem Constraints**

1 <= |A| <= 2000

**Input Format**

The first line is the number of elements in an array.

The second line is the space-separated array elements.

f.e: `1 2 3 4` means `A = [1, 2, 3, 4]`

**Output Format**

Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

**Example Input**

Input 1:

2

1 3

Input 2:

1

2

Input 3:

7

1 5 10 7 1 9 4

**Example Output**

Output1: `2`

Output2: `1`

Output 3: `3`

**Example Explanation**

Explanation 1: `Only choice is to take both elements.`

Explanation 2: `Take the whole array.`

Explanation 2: `Subarray {1, 5, 10} has both maximum and minimum value.`

## User Task

Your task is to complete the function `minSubarrayLength()` which takes a number of array elements N and an array as input and returns the expected answer. You don't need to read the input as a string, write code within the function block directly.



Languages Available

NodeJS

JavaScript

AddPreview

# 77.Pick the Points -- Hard-1 30 mins

math

array

2d array

# Problem Statement

On the integer line, a **segment** is defined by a starting integer and an ending integer. It contains all integers between them, including themselves. For example, a segment `{3, 5}` means integers `3, 4, 5`.

You are given an array of `n` segments `[{a[0],b[0]}, {a[1],b[1]},…,{a[n−1],b[n−1]}]`. You must find the minimum number of points such that each segment contains at least one point. That is, find the size of a minimum set of integers `X` such that for any segment `{a[i], b[i]}` there is a point `x ∈ X` such that `a[i] ≤ x ≤ b[i]`

# Inputs & Outputs

## Input Format

- The first line is an integer `n`, which represents the number of segments.
- The next `n` lines contain a pair of numbers representing the coordinates of a segment. Each pair indicates the start and end of a segment.

## Input Constraints

There are at least 2 segments in the array

## Output Format

The output contains a single integer

# Examples

## Example 1

### Input

```
3
1 3
2 5
3 6
```

### Output

```
1
```

### Explanation

We have segments `[{1,3}, {2,5}, {3,6}]`. All of these segments contain the point with coordinate `3`. Hence, the output for this example is `1`.

## Example 2

### Input

```
4
4 7
1 3
2 5
5 6
```

### Output

```
2
```

### Explanation

We have 4 segments `[{4,7}, {1,3}, {2,5}, {5,6}]`. The second and third segments contain `3`. The first and fourth segments contain `6`. So, the output for this example is `2`.

# User Task

Your task is to complete the function `solution()` which takes in an integer `numOfsets` and a two dimensional array `arr` as parameters and returns an integer. You don't need to read the input as a string, just write code within the function block directly.



Languages Available

Java

C

AddPreview

# 78.Unique Vowels -- Medium-1 30 mins

array

string

## Problem Statement

Given an array of strings `array_str` and a number `n`, find out how many of these strings contain exactly `n` **unique** vowels in them.

### Input

The input to your function is an array of strings, `array_str`, and an integer `n`.

- All the strings contain only lowercase characters.

### Output

The number of strings that contain exactly `n` **unique** vowels

## Test Cases

| Input (string)         | Expected Output (integer) |
| ---------------------- | ------------------------- |
| eiqwa aaabc aheo iou 3 | 3                         |
| aa bhg aeo lia 2       | 1                         |
| anhj berq lopa 1       | 2                         |



Languages Available

Python3

AddPreview

# 79.Countries and States -- Medium-1 20 mins

# Problem Statement

There is an array called `countries` that looks like this:

```javascript
countries = ["India", "USA",..]
```

There is an object called `states`

```javascript
states = {
  "India": [
              {"name": "Karnataka", "population": 200},
              {"name": "Maharashtra", "population": 130},
              {"name": "Goa", "population": 38},
              {"name": "Telangana", "population": 190},
              {"name": "Manipur", "population": 15}
           ],
  "USA": [
            {"name": "Michigan", "population": 120},
            {"name": "Virginia", "population": 48},
            {"name": "Maine", "population": 90},
            {"name": "Texas", "population": 15}
         ],
   ...
}
```

The variables `countries` and `states` are not accessible to you.

An **asynchronous** function `getCountry(countryIndex)` takes an integer as input and returns a Promise that, when resolved, returns the name of a country as a string. If `countryIndex >= countries.length`, the Promise is rejected with "Error"

Another **async** function `getStates(countryName)` takes a country name as input and returns a Promise that, when resolved, returns a list of states.

| Function Call        | On Settling                                                  | Data Type       |
| -------------------- | ------------------------------------------------------------ | --------------- |
| `getCountry(0)`      | Resolves to `"India"`                                        | String          |
| `getCountry(10000)`  | Rejected with `"Error"`                                      | String          |
| `getStates("India")` | Resolves to `[{"name": "Karnataka", "population": 200},...]` | List of objects |

## Task

Given a country index, you are required to return the name of the state with the largest population. If a country with that index doesn't exist, the function must return the string "ind = {index} invalid" where index is the input passed to the function.

## Example

| Input | Expected Output     |
| ----- | ------------------- |
| 0     | Karnataka           |
| 1     | Michigan            |
| 10000 | ind = 10000 invalid |

### Explanation for Input 1 (`0`)

In the list of countries, `India` is the 0th-element. You can see that `Karnataka` has the highest population in this list of Indian states.

### Explanation for Input 2 (`1`)

In the list of countries, `USA` is the 1st-element. You can see that `Michigan` has the highest population in this list of USA states.

# Input & Output

## Input Format

The input is a integer index.

## Output Format

The output must be the name of the most populated state of the country in that list.

# User Task

Your task is to complete the function `solution()`. Do not worry about reading input and printing output. The system does it automatically for you. Just complete the function and return the output.



Languages Available

NodeJS

AddPreview

80.Countries and Capitals -- Medium-2 20 mins

# Problem Statement

There is an array called `countries` that looks like this:

```javascript
countries = ["India", "USA", "countryA", ...]
```

There is an object called `capitals`

```javascript
capitals = {
  "India": "New Delhi", "USA": "Washington DC", "countryA": null
   ...
}
```

If a country doesn't have a capital, its value in the object above is `null`.

There is another object that maps capitals to their populations:

```javascript
const populations = {"New Delhi": 120, "Washington DC": 80}
```

The variables `countries`, `capitals` and `populations` are not accessible to you.

You are given three functions

| Function Name                           | Sync/Async | Returns                    |
| --------------------------------------- | ---------- | -------------------------- |
| `getCountry(countryInd)`                | Sync       | `countries[countryInd]`    |
| `getCapitalFromCountry(countryName)`    | Async      | `capitals[countryName]`    |
| `getPopulationFromCapital(capitalName)` | Sync       | `populations[capitalName]` |

If `countryInd >= countries.length`, `getCountry(countryInd)` returns a null value. If a country doesn't have a capital, `getCapitalFromCountry(countryName)` is rejected with a message "Error".

| Function Call                       | Output                    | Data Type   |
| ----------------------------------- | ------------------------- | ----------- |
| `getCountry(0)`                     | `"India"`                 | String      |
| `getCountry(10000)`                 | `null`                    | Null object |
| `getCapitalFromCountry("India")`    | Resolves to `"New Delhi"` | String      |
| `getCapitalFromCountry("countryA")` | Rejected with `"Error"`   | String      |

## Task

1. Complete the function `solution()`. `solution()` takes the country index as input and returns a string like "India, New Delhi, 120".
2. If the country index is greater than or equal to the length of `countries`, the output must be "No country found at ind = {index}" where index is the input to the function.
3. If the country doesn't have a capital (that is, its capital is null), the output must be "No capital found for country at ind = {index}" where index is the input to the function.

## Example

| Input | Expected Output                         |
| ----- | --------------------------------------- |
| 0     | India, New Delhi, 120                   |
| 1     | USA, Washington DC, 80                  |
| 2     | No capital found for country at ind = 2 |
| 10000 | No country found at ind = 10000         |

### Explanation for Inputs 1 and 2 above (`0` and `1`)

You can clearly see these values from the `countries`, `capitals` and `populations` objects.

### Explanation for Input 3 (`2`)

`countries[2] = "countryA"`. You can see from `capitals` that "countryA" doesn't have a capital

### Explanation for Input 4 (`10000`)

`countries` doesn't have 9999 elements. So, `getCountry()` returns `null`.

# Input & Output

## Input Format

The input is an integer index.

## Output Format

The output must be a string.

# User Task

Your task is to complete the function `solution()`. Do not worry about reading input and printing output. The system does it automatically for you. Just complete the function and return the output.



Languages Available

NodeJS

AddPreview

# 81.Salary Days Off -- Medium-2 20 mins

data analysis

## Datasets

You are working with the employee data of different companies. Each company's dataset contains a list of employee details in the form of a dictionary. For example, one company's dataset may be of the form:

```python
[
    {'id': 1, 'salary': 3000, 'manager': False, 'num_days_off': 8},
    {'id': 2, 'salary': 5000, 'manager': True, 'num_days_off': 10},
    {'id': 3, 'salary': 6000, 'manager': True, 'num_days_off': 14}
]
```

The fields are self-explanatory. `num_days_off` tells you how many days they took off the previous year.

## Problem Statement

Given a dataset, you must calculate 2 values:

- The maximum salary in a given company
- The **total** number of days taken off by all the managers in a company

## Example

If the dataset consisted of only the three records shown above, the maximum salary would be `6000` and the total number of days off would be `24`.

## Requirement

Finish the function shown in the editor alongside. Replace the comment with your code. `dataset` is a list similar to the list shown in the example above.

Your code must set the values for `max_sal` and `total_num_days_off`.

### Output

The output must be a tuple. The first variable must be the maximum salary and the next variable must be the total number of days off.

## Constraints

- Each employee entry will have all these 4 properties
- No value will be `None`

## Sample Inputs

If you click on the `Run Tests` button, your code will be run against the data from `dataset_1`. You can use this to see if your code is working fine. If you are confident that it is working fine, you can then submit the code.

**Note**: You cannot enter custom input for this question



Languages Available

Python3

AddPreview

# 82.Reversing a Linked list -- Hard-1 45 mins

linked list

# Problem Statement

You’re given the pointer to the head node of a linked list. Change the `next` pointers of the nodes so that their order is reversed.

# Input & Output

## Input Format

The first line contains an integer `n`, the number of elements in the linked list. Each of the next `n` lines contains an integer, the `data` values of the elements in the linked list.

## Output Format

The function should return the `head` of the updated list. Which, in turn gets consumed by the driver code which will print the linked list element in the updated order.

# Examples

## Example 1

### Input

```
5
1
2
3
4
5
```

### Output

```
5 4 3 2 1
```

### Explanation

`head` references the list 1 -> 2 -> 3 -> 4 -> 5 -> null

Manipulating the `next` pointers of each node in place and return `head` , now referencing the head of the updated list.

5 -> 4 -> 3 -> 2 -> 1 -> null

## Example 2

### Input

```
2
5
3
```

### Output

```
3 5
```

### Explanation

The reversed version of 5 -> 3 is 3 -> 5

# User Task

Your task is to complete the function `reverseList()` and return the expected answer. You don't need to read the input, just write code within the function block directly.



Languages Available

Java

AddPreview

# 83.Delete Node From Singly Linked List -- Hard-1 45 mins

linked list

# Problem Statement

Given a singly-linked list, delete its `k`th node. You are provided the address of the head of the linked list and the integer `k`. You must return the head of the modified linked list.

# Input & Output

## Input Format

The first line of each test case contains an integer `N` denoting the number of elements of the linked list. Then in the next line are `N` space separated values of the linked list. The third line of each test case contains an integer `k` which denotes the position at which the node needs to be deleted. (We are using 1-based indexing, so `k=1` refers to the first node.)

## Input Constraints

For the number of nodes `N`,

```
1 <= N <= 10000
```

For the integer `k`,

```
1 <= k <= N
```

## Output

The output for each test case will be the space separated value of the returned linked list.

# Examples

## Example 1

### Input

```
4
2 4 5 7
3
```

### Output

```
2 4 7
```

### Explanation

After deleting the node at the 3rd position, the linked list is 2 4 7.

## Example 2

### Input

```
3
1 3 4
3
```

### Output

```
1 3
```

### Explanation

After deleting the node at the 3rd position, the linked list is 1 3.

# User Task

Your task is to complete the method **deleteNode()** which should delete the node at the `k`th position and return the head of the modified linked list. The code has been set up so that you needn't worry about reading the input, converting it to an array, etc.



Languages Available

Java

AddPreview

# 84.Detect Cycle in a Linked List -- Hard-1 45 mins

linked list

# Problem Statement

You are given a linked list of `N` nodes. The task is to check if the linked list has a loop.

# Input & Output

## Input Format

The first line of each test case contains the number of elements in a linked list. The second line shows space-separated nodes of the linked list. The third line shows the index in the linked list to which the last node is connected.

**Note**: Third line will be used only for test cases. It should not be passed as an argument in the function.

## Input Constraints

For the number of nodes `N`

```
1 <= N <= 1000
```

## Output Format

The output for each test case is 1 if it has a loop and 0 otherwise.

## Examples

### Example 1

### Input

```
4
2 5 -4 3
1
```

### Output

```
1
```

### Explanation

Here, the last node (3) points to a node with index number 1 which creates a loop.

### Example 2

### Input

```
2
1 2
0
```

### Output

```
1
```

### Explanation

Here, the last node (2) points to a node with index number 0 which creates a loop.

### Example 3

### Input

```
2
5
-1
```

### Output

```
0
```

### Explanation

Here, the last node (5) points to a node with index number -1 which doesn't exist. So, it doesn't create a loop.

# User Task

The task is to complete the function **detectLoop**(). The function should return whether the linked list is forming any loop. If it is forming a loop, return `true` else return `false`.



Languages Available

Java

AddPreview

# 85.Find Minimum Pages -- Hard-2 45 mins

array

# Problem Statement

There are `n` books and `m` students. The books are arranged in the ascending order of its number of pages. Every student must read some consecutive set of books (at least 1 book per student). Let each such distribution of books amongst the students be denoted by a permutation `i`.

For each such permutation `i`, let `p_i` denote the maximum number of pages that a student has to read. The task is to identify the particular permutation that results in the smallest `p_i`. (Read the example below to understand this better.)

# Input & Output

## Input Format

The first line of each test case contains the number of books `n`. The second line shows an array of `n` space-separated integers, where `ith` integer represents the number of pages in the `ith` book. The third line shows the number of students `m`.

## Input Constraints

- For the number of books `n`

  `1 <= n <= 1000`

- For the number of pages `i` for each book

  `1 <= i <= 1000`

- For the number of students `m`

  `1 <= m <= 1000`

- The books are arranged in ascending order of the number of pages.

## Output Format

The output for each test case will return the minimum number of pages (an integer value). If a valid distribution of the books isn't possible, return `-1`.

# Examples

## Example 1

### Input

```
4
12 34 67 90
2
```

### Output

```
113
```

### Explanation

There are 2 students. We list below all possible permutations of the distribution:

1. [12] and [34, 67, 90]

   Student 1 gets the book with 12 pages, and Student 2 gets the books with 34, 67 and 90 pages.

   Total number of pages for Student 1 = `12`. Total number of pages for Student 2 = 34 + 67 + 90 = `191`

   `p_1` = **max(12, 191)** = 191

2. [12, 34] and [67, 90]

   `p_2` = **max(46, 157)** = 157

3. [12, 34, 67] and [90]

   `p_3` = **max(113, 90)** = 113

Of `p_1`, `p_2` and `p_3`, as `p_3` is the smallest value, we return `p_3`, that is `113`.

## Example 2

### Input

```
3
15 17 20
2
```

### Output

```
32
```

### Explanation

There are 2 students. We list below all possible permutations of the distribution:

1. [15] and [17, 20]

   Student 1 gets the book with 15 pages, and Student 2 gets the books with 17 and 20 pages.

   Total number of pages for Student 1 = `15`. Total number of pages for Student 2 = 17 + 20 = `37`

   `p_1` = **max(15, 37)** = 37

2. [15, 17] and [20]

   `p_2` = **max(32, 20)** = 32

Of `p_1` and `p_2`, `p_2` is the smaller value, so we return `p_2`, that is `32`.

# User Task

Your task is to complete the function **solution()** which takes 2 Integers `n` and `m` and an array as input and returns the expected answer.



Languages Available

Java
