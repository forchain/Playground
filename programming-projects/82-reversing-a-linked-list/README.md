# 82. Reversing a Linked List

## 题目
给定单链表头节点，原地改变 `next` 指针以反转链表，并返回新头。接口 `reverseList(head)`。样例 `1→2→3→4→5` 输出 `5 4 3 2 1`；`5→3` 输出 `3 5`。

## 解析
维护 `previous/current/following`。先保存后继，再令当前节点指向前驱，随后两个游标前进。工程自带最小 `Node` 类型。

## 正确性与复杂度
循环不变式：`previous` 是已处理前缀的完整反转，`current` 指向未处理后缀。每步把一个节点移入反转前缀，结束时全部节点反转且 `previous` 为新头。时间 `O(n)`、空间 `O(1)`。
