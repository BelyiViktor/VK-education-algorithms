def ternarySearchRecursive(data, needle, l, r):
    if r >= l:
        mid1 = int(l + (r - l) / 3)
        mid2 = int(r - (r - l) / 3)
        if data[mid1] == needle:
            return mid1
        if data[mid2] == needle:
            return mid2
        if needle < data[mid1]:
            return ternarySearchRecursive(data, needle,
                                 l, mid1 - 1)
        elif needle > data[mid2]:
            return ternarySearchRecursive(data, needle,
                                 mid2 + 1, r)
        else:
            return ternarySearchRecursive(data, needle, mid1 + 1, mid2 - 1)
    return -1


def ternarySearchIterable(data, needle, l, r):
    while r >= l:
        mid1 = int(l + (r - l) / 3)
        mid2 = int(r - (r - l) / 3)

        if data[mid1] == needle:
            return mid1
        if data[mid2] == needle:
            return mid2

        if needle < data[mid1]:
            r = mid1 - 1
        elif needle > data[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1


print(ternarySearchIterable([0, 1, 2], 2, 0, 2))