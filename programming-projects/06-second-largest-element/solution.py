def solution(n, arr):
    largest = second = None
    for value in arr:
        if largest is None or value > largest:
            if value != largest:
                second, largest = largest, value
        elif value != largest and (second is None or value > second):
            second = value
    return -1 if second is None else second
