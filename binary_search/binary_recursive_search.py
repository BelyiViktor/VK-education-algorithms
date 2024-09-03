def binarySearch(data, l, r, needle):
    if l > r:
        return -1
    mid = int((r + l) / 2)
    if data[mid] == needle:
        return mid
    if data[mid] > needle:
        return binarySearch(data, l, mid - 1, needle)
    else:
        return binarySearch(data, mid + 1, r, needle)

print(binarySearch([1, 2, 3, 5, 6], 0, 3, 5))
