def solution(n, arr):
    values = arr[:n]
    for chosen in range(n):
        product = 1
        for i, value in enumerate(values):
            if i != chosen:
                product *= value
        if product == values[chosen]:
            return chosen
    return -1
