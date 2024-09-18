def binary_search(data, needle, l, r):
    if l > r:
        return r + 1
    m = int((l + r) / 2)
    if data[m] == needle:
        return m
    if data[m] > needle:
        return binary_search(data, needle, l, m - 1)
    else:
        return binary_search(data, needle, m + 1, r)


def exponential_search(data, needle):
    border = 1
    last_element = len(data) - 1
    while border < last_element and data[border] < needle:
        border = border * 2
        if border > last_element:
            return binary_search(data, needle, int(border / 2), last_element)
        if data[border] == needle:
            return border

    return binary_search(data, needle, int(border / 2), border)


n = int(input())
numbers = [int(num) for num in input().split()]
needle = int(input())

ind = exponential_search(numbers, needle)
print(ind - 1, ind + 1)
