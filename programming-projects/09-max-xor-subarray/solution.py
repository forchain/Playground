class _TrieNode:
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
