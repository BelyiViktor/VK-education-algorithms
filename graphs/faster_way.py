from queue import PriorityQueue


class Node:
    def __init__(self, id, content):
        self.id = id
        self.content = content


class Edge:
    def __init__(self, node_id, weight):
        self.node_id = node_id
        self.weight = weight


class Graph:
    def __init__(self):
        self.adj_list = dict()
        self.nodes = dict()

    def add_node(self, node_id, content):
        self.nodes[node_id] = Node(node_id, content)
        self.adj_list[node_id] = []

    def add_edge(self, id1, id2, weight):
        self.adj_list[id1].append(Edge(id2, weight))
        self.adj_list[id2].append(Edge(id1, weight))  # Undirected graph

    def __str__(self):
        return "Nodes is " + str(self.nodes) + '.\n' \
            + "Edges is " + str(self.adj_list) + '.\n'

    def dijkstra(self, startid, endid):
        dist = dict()
        for node in self.nodes.values():
            dist[node.id] = float("+inf")
        dist[startid] = 0
        pq = PriorityQueue()
        pq.put((0, (startid, 0)))
        while not pq.empty():
            node = pq.get()[1][0]

            for edge in self.adj_list[node]:
                if dist[node] + edge.weight < dist[edge.node_id]:
                    dist[edge.node_id] = dist[node] + edge.weight
                    pq.put((dist[edge.node_id], (edge.node_id, dist[edge.node_id])))

        return dist[endid]


edges = int(input())
street = Graph()
for i in range(edges):
    id1, id2, weight = map(int, input().split())
    if id1 not in street.nodes:
        street.add_node(id1 - 1, id1)
    if id2 not in street.nodes:
        street.add_node(id2 - 1, id2)
    street.add_edge(id1 - 1, id2 - 1, weight)

start, end = map(int, input().split())

result = street.dijkstra(start - 1, end - 1)
if result is float('+inf'):
    print("No path found")
else:
    print(result)