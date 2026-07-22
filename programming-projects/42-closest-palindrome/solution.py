def solution(n: str) -> str:
    """返回与 n 数值距离最近且不等于自身的回文数。"""
    value = int(n)
    length = len(n)
    prefix_length = (length + 1) // 2
    prefix = int(n[:prefix_length])
    candidates = {10 ** (length - 1) - 1, 10 ** length + 1}
    for candidate_prefix in (prefix - 1, prefix, prefix + 1):
        if candidate_prefix < 0:
            continue
        left = str(candidate_prefix)
        # 奇数长度不重复中间字符，偶数长度则完整镜像左半边。
        mirrored = left + left[-(2 if length % 2 else 1)::-1]
        candidates.add(int(mirrored))
    candidates.discard(value)
    return str(min(candidates, key=lambda candidate: (abs(candidate - value), candidate)))
