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

    def dijkstra(self, startid):
        dist = dict()
        for node in self.nodes:
            dist[node.id] = float("+inf")
        dist[startid] = 0
        pq = PriorityQueue()
        pq.put((0, (startid, 0)))
        while not pq.empty():
            node = pq.get()[0]

            for edge in self.adj_list[node]:
                if dist[node] + edge.weight < dist[edge.node]:
                    dist[edge.node] = dist[node] + edge.weight
                    pq.put((dist[edge.node], (edge.node, dist[edge.node])))

        # Print shortest distances:
        for node in self.nodes:
            print("Distance to node with id ", node.id, " equals ",
                  dist[node.first])

    def bellman_ford(self, startid):
        dist = dict()
        for node in self.nodes:
            dist[node.id] = float('+inf')
        dist[startid] = 0
        for i in range(1, len(self.nodes)):
            for node in self.adj_list:
                for edge in node:
                    if dist[node.id] != float('+inf') and dist[node.id] + edge.weight < dist[edge.node_id]:
                        dist[edge.node_id] = dist[node.first] + edge.weight

        for node in self.adj_list:
            for edge in node:
                if dist[node.id] != float('+inf') and dist[node.id] + edge.weight < dist[edge.node_id]:
                    print("Граф содержит цикл отрицательного веса")
                    return

        for node in self.nodes:
            print(f"Distance to node with id {node.id} equals {dist[node.id]}")

    def floyd_warshall(self):
        v = len(self.nodes)
        dist = [[float('+inf')] * v for i in range(v)]
        for id, edges in enumerate(self.adj_list):
            dist[id][id] = 0
            for edge in edges:
                dist[id][edge.node_id] = edge.weight

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if dist[i][k] != float('+inf') and \
                            dist[k][j] != float('+inf') and \
                            dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(v):
            for j in range(v):
                print(f'dist[{i}][{j}] is ', end='')
                if dist[i][j] == float('+inf'):
                    print('INF')
                else:
                    print(dist[i][j])


