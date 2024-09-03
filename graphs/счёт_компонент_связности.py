visited = set()


def dfs(node, graph):
    global visited
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour, graph)
        return True
    else:
        return False


counter = 0

e = int(input())
graph = dict()
for _ in range(e):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    graph[a].append(b)
    graph[b].append(a)

for v in graph:
    if dfs(v, graph):
        counter += 1

print(counter)