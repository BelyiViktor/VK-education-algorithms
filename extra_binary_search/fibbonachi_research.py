# (12:18)-5:56
# M = F(k + 1) - (N + 1), i = F(k) - M, p = F(k - 1), q = F(k - 2)
# i = F(k) - M = N + 1  - F(k - 1)
# i = i - q = F(k) - M - F(k - 2) = F(k - 1) - M, (p, q) = (q, p - q) =
# = (F(k - 2), F(k - 3))


def fibonacci_search(data, needle):
    size = len(data)
    f0 = 0
    f1 = 1
    f2 = f1 + f0

    offset = -1

    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f0 + f1

    while f2 > 1:
        index = min(offset + f0, size - 1)

        if data[index] < needle:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            offset = index
        elif data[index] > needle:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if f1 and (data[size - 1] == needle):
        return size - 1
    return None


lst = [1]
print(fibonacci_search(lst, 6))
