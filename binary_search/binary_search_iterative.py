def binarySearch(data, needle):
    l = 0
    r = len(data)
    if r == 0 or needle < data[0] or needle > data[r - 1]:
        return -1
    while l <= r:
        mid = int((l + r) / 2)
        if needle == data[mid]:
            return mid
        if needle < data[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

print(binarySearch([1, 2, 3, 4, 5], 3))