# Задача о Пете и его дипломах:
def binary_search(w, h, n):
    left = max(w, h)
    right = left * n
    while right - left > 1:
        mid = (right + left) // 2
        res = (mid // w) * (mid // h)
        if res < n:
            left = mid
        else:
            right = mid
    return right