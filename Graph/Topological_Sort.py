from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, src, visited, stack):
        visited[src] = True

        for nbr in self.graph[src]:
            if not visited[nbr]:
                self.dfs(nbr, visited, stack)
        stack.append(src)

    def topologicalSort(self):
        visited = [False for i in range(self.V)]
        stack = []

        for idx in range(self.V):
            if not visited[idx]:
                self.dfs(idx, visited, stack)

        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()