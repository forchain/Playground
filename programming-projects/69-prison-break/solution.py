def countReleasedPrisoner(cells):
    if not cells or cells[0] == 1:
        return 0
    released = 0
    flipped = 0
    for cell in cells:
        # 当前实际状态为原状态与翻转奇偶性的异或。
        if cell ^ flipped == 0:
            released += 1
            flipped ^= 1
    return released
