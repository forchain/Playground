# 44. Toffees in a Packet

> 难度与建议用时：Hard-1 40 mins

array

sliding window

greedy

## Problem Statement

You are given an array `arr` of positive integers of size `n`. Each value in the array represents the number of toffees in a packet. Each packet can have any number of toffees. For example, if `arr = [2, 3]`, this means that the first packet has 2 toffees and the second has 3 toffees.
There are `x` students. The task is to distribute toffee packets among `x` students such that:

- Each students gets exactly one packet
- The difference between the maximum number of toffees given to a student and the minimum number of toffees given to a student is minimum

## Input & Output

### Input Format

- The first line is an integer `n`, which represents the number of chocolate packets
- The next line is an integer `x`, which represents the number of students
- The next line contains `n` space-separated integer values that represent the number of toffees in each packet

### Input Constraints

```
n >= x > 1
```

### Output Format

An integer representing the difference between the maximum and minimum.

## Examples

### Example 1

#### Input

```
7
3
7 3 2 4 9 12 56
```

#### Output

```
2
```

#### Explanation

Imagine Student 1 got the 2nd packet, Student 2 got the 3rd packet and Student 3 got the 4th packet. So, the three students get 3, 2 and 4 toffees respectively.
The difference between the maximum (4) and minimum (2) number of toffees is 2. For no other distribution will this difference be smaller.

### Example 2

#### Input

```
6
4
6 8 11 21 90 49
```

#### Output

```
15
```

#### Explanation

We have 4 students. Let's say Student 1 got the 1st packet, Student 2 got the 2nd packet, Student 3 got the 3rd packet and Student 4 got the 4th packet. So, the four students get 6, 8, 11 and 21 toffees respectively.
The difference between the maximum (21) and minimum (6) number of toffees is 15. For no other distribution will this difference be smaller.

## User Task

Your task is to complete the function `solution` which takes in two integers `n` and `x`, and the array `arr` as parameters and returns an integer. You don't need to read the input as a string. Just write code within the function block directly.
