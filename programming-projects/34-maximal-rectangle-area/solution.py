def solution(matrix: list[list[int]]) -> int:
    """返回二进制矩阵中全 1 矩形的最大面积。"""
    if not matrix or not matrix[0]:
        return 0
    heights = [0] * len(matrix[0])
    answer = 0
    for row in matrix:
        heights = [height + 1 if value == 1 else 0 for height, value in zip(heights, row)]
        stack = []
        # 末尾哨兵 0 强制结算栈中所有柱子。
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                answer = max(answer, h * (i - left))
            stack.append(i)
    return answer
