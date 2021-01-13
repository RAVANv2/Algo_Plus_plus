
# Undirected graph is tree or not.

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.node = set()

    def add_edge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        self.node.add(u)
        self.node.add(v)

    def is_tree(self, src):
        visited = {}
        parent = {}
        queue = []

        for ele in self.node:
            visited[ele] = False
            parent[ele] = ele

        queue.append(src)
        visited[src] = True

        while queue:
            node = queue.pop(0)
            for nbr in self.graph[node]:
                if (visited[nbr] == True) and (parent[node]!= nbr):
                    return False
                elif (not visited[nbr]):
                    parent[nbr] = node
                    visited[nbr] = True
                    queue.append(nbr)
        print(parent)
        return True


g = Graph()
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(3,4)
g.add_edge(2,1)

print(g.is_tree(0))