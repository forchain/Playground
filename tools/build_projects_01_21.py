#!/usr/bin/env python3
"""Build standalone projects for questions 1 through 21."""

from pathlib import Path
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "programming-questions"
DEST = ROOT / "programming-projects"

# Each entry contains executable source, test cases, approach, and complexity.
SPECS = {
1:("""def solution(s):
    # split() treats one or more whitespace characters as a separator.
    return max((len(word) for word in s.split()), default=0)
""", [(('The quick brown fox',),5),(('A journey of a thousand miles begins with a single step',),8)], "按空白切分所有单词，并在一次扫描中保留最大长度。", "O(n)", "O(n)"),
2:("""def solution(n):
    # abs removes the sign; converting to text makes every decimal digit explicit.
    return sum(int(ch) for ch in str(abs(n)))
""", [((123,),6),((-2059,),16),((0,),0)], "负号不属于数字，先取绝对值，再逐位累加十进制字符。", "O(d)", "O(d)"),
3:("""from collections import Counter

def solution(s):
    counts = Counter(s)
    # A character contributes only when it occurs exactly once.
    return sum(ord(ch) for ch, count in counts.items() if count == 1)
""", [(('abc',),294),(('abac',),197),(('xyzwx',),362)], "先统计频次，再累加频次恰为 1 的字符的 ASCII 值。", "O(n)", "O(k)"),
4:("""def solution(s):
    vowels = set('aeiouAEIOU')
    # Preserve every non-vowel verbatim, including spaces and punctuation.
    return ''.join(ch for ch in s if ch not in vowels)
""", [(('hello world',),'hll wrld'),(('Programming is fun!',),'Prgrmmng s fn!')], "用元音集合做常数时间成员判断，只过滤元音，其他字符保持原顺序。", "O(n)", "O(n)"),
5:("""def solution(n, arr, k):
    if not arr:
        return []
    k %= len(arr)  # Avoid doing complete, ineffective rotations.
    return arr[-k:] + arr[:-k] if k else arr[:]
""", [((5,[1,2,3,4,5],2),[4,5,1,2,3]),((6,[10,20,30,40,50,60],4),[30,40,50,60,10,20])], "右移 k 位等价于把最后 k 个元素整体放到数组开头；先对长度取模。", "O(n)", "O(n)"),
6:("""def solution(n, arr):
    largest = second = None
    for value in arr:
        if largest is None or value > largest:
            if value != largest:
                second, largest = largest, value
        elif value != largest and (second is None or value > second):
            second = value
    return -1 if second is None else second
""", [((5,[2,3,6,6,5]),5),((3,[10,10,10]),-1),((6,[1,2,3,4,5,4]),4)], "一次遍历维护最大值和严格小于最大值的第二大值，重复最大值不会改变状态。", "O(n)", "O(1)"),
7:("""def solution(n, arr):
    # Values should be exactly 1..n+1 except for one missing value.
    expected = (n + 1) * (n + 2) // 2
    return expected - sum(arr)
""", [((4,[1,2,4,5]),3),((5,[2,3,1,5,6]),4)], "完整序列 1..n+1 的等差数列和减去实际数组和，就是唯一缺失值。", "O(n)", "O(1)"),
8:("""def solution(n, arr, k):
    # Sorting descending makes the 1-based kth element direct to index.
    return sorted(arr, reverse=True)[k - 1]
""", [((6,[3,2,1,5,6,4],2),5),((4,[7,9,3,2],4),2)], "降序排序后，第 k 大元素位于下标 k-1。题意按元素计数，因此重复值也占位置。", "O(n log n)", "O(n)"),
9:("""class _TrieNode:
    def __init__(self):
        self.child = [None, None]

def solution(n, arr):
    root = _TrieNode()
    def insert(value):
        node = root
        for bit in range(31, -1, -1):
            b = (value >> bit) & 1
            if node.child[b] is None:
                node.child[b] = _TrieNode()
            node = node.child[b]
    def best_xor(value):
        node, answer = root, 0
        for bit in range(31, -1, -1):
            b = (value >> bit) & 1
            preferred = b ^ 1
            if node.child[preferred] is not None:
                answer |= 1 << bit
                node = node.child[preferred]
            else:
                node = node.child[b]
        return answer
    prefix = answer = 0
    insert(0)  # Allows a subarray starting at index zero.
    for value in arr:
        prefix ^= value
        answer = max(answer, best_xor(prefix))
        insert(prefix)
    return answer
""", [((4,[1,2,3,4]),7),((5,[8,1,2,12,7]),15)], "子数组异或等于两个前缀异或之异或。二进制 Trie 为当前前缀逐位选择相反比特，得到与旧前缀的最大异或。", "O(nW)，W=32", "O(nW)"),
10:("""def solution(n, arr):
    max_here = min_here = answer = arr[0]
    for value in arr[1:]:
        # A negative value swaps the roles of maximum and minimum products.
        candidates = (value, max_here * value, min_here * value)
        max_here, min_here = max(candidates), min(candidates)
        answer = max(answer, max_here)
    return answer
""", [((5,[2,3,-2,4,-1]),48),((4,[-2,0,-1,3]),3)], "同时维护以当前位置结尾的最大和最小乘积；负数可能把最小负积翻转成最大正积。", "O(n)", "O(1)"),
11:("""def solution(s):
    # A set automatically removes duplicate substrings.
    return len({s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)})
""", [(('abc',),6),(('aaa',),3)], "枚举所有非空区间，把对应子串放入集合去重，最后返回集合大小。", "O(n^3)，包含切片成本", "O(n^3)"),
12:("""def solution(n, arr):
    candidate, balance = None, 0
    for value in arr:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    # Boyer-Moore only yields a candidate, so a second pass must verify it.
    return candidate if arr.count(candidate) > n // 2 else -1
""", [((5,[3,3,4,2,3]),3),((4,[1,2,3,4]),-1),((6,[2,2,1,1,1,2]),-1)], "Boyer-Moore 抵消不同元素后得到唯一可能候选，再统计一次确认其频次严格超过 n/2。", "O(n)", "O(1)"),
13:("""def solution(n, arr):
    left, right, result = 0, n - 1, []
    while left <= right:
        result.append(arr[right]); right -= 1
        if left <= right:
            result.append(arr[left]); left += 1
    return ' '.join(map(str, result))
""", [((6,[1,2,3,4,5,6]),'6 1 5 2 4 3'),((5,[10,20,30,40,50]),'50 10 40 20 30')], "数组已排序，用左右双指针交替取当前最大值和最小值。", "O(n)", "O(n)"),
14:("""def solution(s1, s2):
    if len(s1) != len(s2):
        return -1
    # Search each non-empty left rotation and return its cut length.
    for cut in range(1, len(s1) + 1):
        if s1[cut:] + s1[:cut] == s2:
            return cut
    return -1
""", [(('abcde','deabc'),3),(('hello','lohel'),3),(('abc','cabd'),-1)], "枚举切割长度 cut，比较 s1[cut:]+s1[:cut]。返回的是左移步数。", "O(n^2)", "O(n)"),
15:("""def solution(s):
    best = running = int(s[0])
    for previous, current in zip(s, s[1:]):
        digit = int(current)
        # Continue only while the next digit is strictly smaller.
        running = running + digit if previous > current else digit
        best = max(best, running)
    return best
""", [(('9875',),29),(('1234',),4),(('404',),4)], "扫描连续递减段并维护该段数字和；递减关系断开时从当前数字重新开始。", "O(n)", "O(1)"),
16:("""def solution(s):
    result, start = [], 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[start]:
            count = i - start
            # Follow the written rule: omit the count for a single character.
            result.append(s[start] + (str(count) if count > 1 else ''))
            start = i
    return ''.join(result)
""", [(('aaaabbbcca',),'a4b3c2a'),(('abcccdeeeeffff',),'abc3de4f4')], "游程编码：找到每个连续相同字符段，段长大于 1 才附加数字。测试以明确书面规则为准。", "O(n)", "O(n)"),
17:("""from collections import Counter

def solution(n, arr):
    counts = Counter(arr)
    return sorted(arr, key=lambda value: (-counts[value], value))
""", [((6,[4,5,6,5,4,3]),[4,4,5,5,3,6]),((5,[1,2,2,3,3]),[2,2,3,3,1])], "排序键先使用负频次实现频次降序，再使用元素值实现同频时升序。", "O(n log n)", "O(k)"),
18:("""def solution(s):
    last_seen, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
""", [(('abcabcbb',),3),(('bbbbb',),1),(('pwwkew',),3)], "滑动窗口始终保持无重复；遇到窗口内旧字符时把左边界跳到其上次位置之后。", "O(n)", "O(k)"),
19:("""def solution(s1, s2):
    index = 0
    while index < min(len(s1), len(s2)) and s1[index] == s2[index]:
        index += 1
    return s1[:index]
""", [(('abcd','abcxyz'),'abc'),(('hello','world'),'')], "从首字符同步比较，第一次不同的位置就是公共前缀的结束边界。", "O(min(n,m))", "O(min(n,m))"),
20:("""from collections import defaultdict

def solution(s):
    required = len(set(s)); counts = defaultdict(int)
    formed = left = 0; best = len(s) + 1
    for right, ch in enumerate(s):
        counts[ch] += 1
        if counts[ch] == 1:
            formed += 1
        while formed == required:
            best = min(best, right - left + 1)
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                formed -= 1
            left += 1
    return best
""", [(('abcaacbb',),3),(('aaa',),1),(('abcdef',),6)], "目标字符集合是整串的去重集合。右边界扩张至全部覆盖，再持续收缩左边界以得到最短窗口。", "O(n)", "O(k)"),
21:("""def solution(n, arr):
    if n < 2:
        return n
    up = down = 1
    for previous, current in zip(arr, arr[1:]):
        if current > previous:
            up = down + 1
        elif current < previous:
            down = up + 1
    return max(up, down)
""", [((6,[1,7,4,9,2,5]),6),((7,[1,17,5,10,13,15,10]),5),((5,[10,10,10,10,10]),1)], "up/down 分别记录最后一步上升或下降的最长摆动子序列；新上升只能接在下降状态后，反之亦然。", "O(n)", "O(1)"),
}

TEST_TEMPLATE = '''import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
{methods}

if __name__ == "__main__":
    unittest.main()
'''

def main():
    DEST.mkdir(exist_ok=True)
    for number, (code, cases, approach, time_cost, space_cost) in SPECS.items():
        source = next(SOURCE.glob(f"{number:02d}-*.md"))
        project = DEST / source.stem
        project.mkdir(exist_ok=True)
        problem = source.read_text(encoding="utf-8")
        note = ""
        if number == 5:
            note = "\n> 注意：原 Example 2 的输出与“右移 4 位”矛盾；正确结果为 `30 40 50 60 10 20`，测试采用可复算结果。\n"
        elif number == 14:
            note = "\n> 注意：原 Example 2 将 `hello -> lohel` 标成左移 2 位，实际需要左移 3 位；测试采用可复算结果。\n"
        elif number == 16:
            note = "\n> 注意：原样例对单字符是否添加 `1` 前后矛盾。本工程按 Problem Statement 的明确规则测试。\n"
        readme = problem + f'''\n\n## Python 解法\n\n### 思路\n\n{approach}\n\n### 正确性说明\n\n算法维护的状态始终与上述定义一致，并且按输入顺序处理了所有可能影响答案的元素。每次状态更新都只保留满足题意的候选；处理结束后，返回值因此覆盖全部候选且不会包含非法结果。\n\n### 复杂度\n\n- 时间复杂度：`{time_cost}`\n- 空间复杂度：`{space_cost}`\n{note}\n### 代码与测试\n\n实现见 `solution.py`，题目中的可执行样例见 `test_solution.py`。\n'''
        (project / "README.md").write_text(readme, encoding="utf-8")
        (project / "solution.py").write_text(textwrap.dedent(code), encoding="utf-8")
        methods = []
        for index, (args, expected) in enumerate(cases, 1):
            methods.append(f"    def test_example_{index}(self):\n        self.assertEqual(solution(*{args!r}), {expected!r})")
        (project / "test_solution.py").write_text(TEST_TEMPLATE.format(methods="\n\n".join(methods)), encoding="utf-8")

if __name__ == "__main__":
    main()
