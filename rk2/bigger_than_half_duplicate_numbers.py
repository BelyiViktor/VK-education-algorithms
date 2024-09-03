def h(num):
    return abs(num) % 10000


def solve(table, n):
    for hs in table:
        for elem in hs:
            if elem[1] > n / 2:
                return elem[0]
    return -1


n = int(input())
numbers = [int(num) for num in input().split()]
table = [[] for _ in range(10000)]
for num in numbers:
    hs = h(num)
    exist = False
    for elem in table[hs]:
        if elem[0] == num:
            elem[1] += 1
            exist = True
    if not exist:
        table[hs].append([num, 1])

print(solve(table, n))
