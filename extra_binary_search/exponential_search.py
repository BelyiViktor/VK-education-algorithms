from binary_search.binary_recursive_search import binarySearch


def exponentialSearch(data, needle):
    border = 1
    lastElement = len(data) - 1
    while border < lastElement \
            and data[border] < needle:
        border = border * 2
        if data[border] == needle:
            return border
        if border > lastElement:
            border = lastElement
    return binarySearch(data, needle, border / 2, border)