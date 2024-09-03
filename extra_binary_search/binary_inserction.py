def binary_search(lst, needle):
    n = len(lst)
    l = 0
    r = n - 1
    m = int((l + r) / 2)
    while r >= l:
        if lst[m] == needle:
            return m
        if lst[m] > needle:
            r = m - 1
        else:
            l = m + 1
        m = int((l + r) / 2)
    return l


_ = input()
lst = [int(x) for x in input().split()]
print(binary_search(lst, int(input())))
