def solution(tree, n, node):
    if 2 * node + 2 < n:
        return solution(tree, n, 2 * node + 2)
    else:
        return tree[node]


n = int(input())
tree = list(map(int, input().split()))
print(solution(tree, n, 0))