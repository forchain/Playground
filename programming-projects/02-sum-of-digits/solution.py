def solution(n):
    # abs removes the sign; converting to text makes every decimal digit explicit.
    return sum(int(ch) for ch in str(abs(n)))
