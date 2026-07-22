def solution(nums: list[int]) -> int:
    """返回拆分元素使序列非递减所需的最少操作数。"""
    operations = 0
    upper_bound = nums[-1]
    for value in reversed(nums[:-1]):
        # 每一份都不超过右侧允许上界时，至少需要 ceil(value/upper_bound) 份。
        parts = (value + upper_bound - 1) // upper_bound
        operations += parts - 1
        # 尽量均分会让最左一份最大，从而给更左侧留下尽可能宽松的上界。
        upper_bound = value // parts
    return operations
