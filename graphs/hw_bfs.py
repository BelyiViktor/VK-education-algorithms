def bfs(graph, start, end):
    stack = [(start, 0)]
    visited = set()
    while len(stack) != 0:
        cur, deep = stack.pop()
        if cur == end:
            return deep - 1
        if cur not in visited:
            visited.add(cur)
            for child in graph[cur]:
                stack.append((child, deep + 1))
    return "No path found"


e = int(input())
graph = dict()
for i in range(e):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    graph[a].append(b)
    graph[b].append(a)
start, end = map(int, input().split())
print(bfs(graph, start, end))
