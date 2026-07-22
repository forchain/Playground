# 76. Smallest Subarray (JS)

> 难度与建议用时：Medium-2 45 mins

### Problem Statement

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

### User Task

Your task is to complete the function `minSubarrayLength()` which takes a number of array elements N and an array as input and returns the expected answer. You don't need to read the input as a string, write code within the function block directly.
