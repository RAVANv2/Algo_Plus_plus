from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node = set()


    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        self.node.add(u)
        self.node.add(v)


g = Graph()

g.addEdge()