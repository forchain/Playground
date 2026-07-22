from math import isqrt

def solution(a, b, c):
    if a == 0:
        raise ValueError("a 必须非零，方程才是二次方程")
    discriminant = b * b - 4 * a * c
    root = isqrt(discriminant)
    if root * root != discriminant:
        raise ValueError("题目保证根为整数")
    first_num, second_num = -b + root, -b - root
    denominator = 2 * a
    if first_num % denominator or second_num % denominator:
        raise ValueError("题目保证根为整数")
    return f"{first_num // denominator} {second_num // denominator}"
