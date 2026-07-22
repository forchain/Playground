def longest_white_run(binary: str) -> int:
    total_ones = binary.count('1')
    left = zeros = best = 0
    for right, char in enumerate(binary):
        zeros += char == '0'
        while zeros > 1:
            zeros -= binary[left] == '0'
            left += 1
        # 交换不能创造 1，因此窗口长度还受全串 1 的总数限制。
        best = max(best, min(right - left + 1, total_ones))
    return best
