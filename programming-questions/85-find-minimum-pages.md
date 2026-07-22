# 85. Find Minimum Pages

> 难度与建议用时：Hard-2 45 mins

array

## Problem Statement

There are `n` books and `m` students. The books are arranged in the ascending order of its number of pages. Every student must read some consecutive set of books (at least 1 book per student). Let each such distribution of books amongst the students be denoted by a permutation `i`.

For each such permutation `i`, let `p_i` denote the maximum number of pages that a student has to read. The task is to identify the particular permutation that results in the smallest `p_i`. (Read the example below to understand this better.)

## Input & Output

### Input Format

The first line of each test case contains the number of books `n`. The second line shows an array of `n` space-separated integers, where `ith` integer represents the number of pages in the `ith` book. The third line shows the number of students `m`.

### Input Constraints

- For the number of books `n`

  `1 <= n <= 1000`

- For the number of pages `i` for each book

  `1 <= i <= 1000`

- For the number of students `m`

  `1 <= m <= 1000`

- The books are arranged in ascending order of the number of pages.

### Output Format

The output for each test case will return the minimum number of pages (an integer value). If a valid distribution of the books isn't possible, return `-1`.

## Examples

### Example 1

#### Input

```
4
12 34 67 90
2
```

#### Output

```
113
```

#### Explanation

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

### Example 2

#### Input

```
3
15 17 20
2
```

#### Output

```
32
```

#### Explanation

There are 2 students. We list below all possible permutations of the distribution:

1. [15] and [17, 20]

   Student 1 gets the book with 15 pages, and Student 2 gets the books with 17 and 20 pages.

   Total number of pages for Student 1 = `15`. Total number of pages for Student 2 = 17 + 20 = `37`

   `p_1` = **max(15, 37)** = 37

2. [15, 17] and [20]

   `p_2` = **max(32, 20)** = 32

Of `p_1` and `p_2`, `p_2` is the smaller value, so we return `p_2`, that is `32`.

## User Task

Your task is to complete the function **solution()** which takes 2 Integers `n` and `m` and an array as input and returns the expected answer.
