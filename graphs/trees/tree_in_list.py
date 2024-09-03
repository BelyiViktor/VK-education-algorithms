def left(i):
    return 2 * i + 1


n = int(input())
tree = [int(num) for num in input().split()]

ind_min = 0

while True:
    if left(ind_min) < n:
        ind_min = left(ind_min)
    else:
        break

print(tree[ind_min])
