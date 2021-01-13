from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node = set()


    def addEdge(self,u,v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

        self.node.add(u)
        self.node.add(v)

    def is_cycle(self,stack,visited,src):
        visited[src] = stack[src] = True
        for node in self.graph[src]:
            if stack[node] == True:
                return True
            elif visited[node] == False:
                cycle = self.is_cycle(stack,visited,node)
                if cycle:
                    return True

        stack[src] = False
        return False

    def cycle(self,src):
        stack = {}
        visited = {}

        for ele in self.node:
            stack[ele] = visited[ele] = False

        ans = self.is_cycle(stack, visited, src)
        print(stack)
        return ans



g = Graph()

g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)

print(g.cycle(1))
