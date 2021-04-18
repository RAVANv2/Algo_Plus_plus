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

    def is_cycle(self,src,visited,parent):
        visited[src] = True
        for nbr in self.graph[src]:
            if not visited[nbr]:
                cycle = self.is_cycle(nbr,visited,src)
                if cycle:
                    return True
            elif nbr!=parent:
                return True

        return False


    def cycleDetection(self,src,parent):
        visited = {}
        for ele in self.node:
            visited[ele] = False

        return self.is_cycle(src,visited,parent)


g = Graph()

g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)

print(g.cycleDetection(1,-1))