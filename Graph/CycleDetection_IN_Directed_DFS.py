

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node = set()


    def addEdge(self, u,v):
        self.graph[u].append(v)
        self.node.add(u)
        self.node.add(v)

    def cycle_helper(self,node,visited,stack):
        visited[node] = stack[node] = True
        for nbr in self.graph[node]:
            if stack[nbr] == True:
                return True
            elif visited[nbr] == False:
                cycle = self.cycle_helper(nbr,visited,stack)
                if cycle:
                    print(nbr)
                    return True
        stack[node] = False
        return False


    def is_cycle(self,src):
        visited = {}
        stack = {}
        for ele in self.node:
            visited[ele] = stack[ele] = False

        return self.cycle_helper(src,visited,stack)



g = Graph()

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(1,5)
g.addEdge(5,6)
g.addEdge(4,2)

print(g.is_cycle(0))
