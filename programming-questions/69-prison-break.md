# 69. Prison Break

> 难度与建议用时：Hard-1 45 mins

array

bit manipulation

## Problem Statement

Imagine you are in a prison with many prison cells. The cells can be locked or unlocked. We represent the cells as an array of `0`'s and `1`'s, where `0` represents an unlocked cell and `1` represents a locked cell. Each cell has exactly 1 prisoner. You are the prisoner in the **leftmost** cell. So, if the configuration is `0 1 0`, it means there are 3 cells: you are in an unlocked cell, the next cell is locked, and the cell after that is also unlocked.

If your cell is unlocked, you can walk down the cells in order and release different prisoners. The cell must be unlocked (`0`) for you to be able to release the prisoner. Once you unlock a cell, all cells will flip from locked to unlocked, and vice-versa. So, if the state is `0 1 0`, it will become `1 0 1`, for example.

Once you release a prisoner, you cannot move back to the previous cell. You can only move forward. Your task is to return the number of prisoners that you can release, `num_release`.

## Input & Output

### Input Format

- The first line is the number of cells
- The second line contains input array elements separated by spaces i.e `0` and `1`.

### Input Constraints

- The array will have at least 1 element
- The array will only have valid integers i.e `0` and `1`

### Output Format

The output must be an integer

### Examples

#### Example 1

##### Input

```
3
1 1 1
```

##### Output

```
0
```

##### Explanation

As the first cell is locked, we can't release any prisoners.

#### Example 2

##### Input

```
7
0 0 1 1 1 0 1
```

### Output

```
4
```

##### Explanation

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

## User Task

Your task is to complete the function `countReleasedPrisoner()`. You don't need to read the input, just write code within the function block directly.
