def interpolation_search(data, needle):
    left = 0
    right = len(data) - 1
    while data[left] < needle < data[right]:
        if data[left] == data[right]:
            break
        index = left + (right - left) * ((needle - data[left]) // data[right] - data[left])
        if data[index] > needle:
            right = index - 1
        elif data[index] < needle:
            left = index + 1
        else:
            return index

        if data[left] == needle:
            return left
        if data[right] == needle:
            return right
        return -1