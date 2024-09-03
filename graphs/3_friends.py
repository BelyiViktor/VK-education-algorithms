def simple_dfs(hero, man, members):
    if members > 3:
        return False
    if hero == man and members == 3:
        return True
    for friend in graph[man]:
        if simple_dfs(hero, friend, members + 1):
            return True


n = int(input())
graph = [n * [] for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for i in range(n):
    if simple_dfs(i, i, 0):
        print("YES")
        break
else:
    print("NO")