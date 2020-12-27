from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.node = set()


    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.node.add(u)
        self.node.add(v)

    def topologicalSort(self):
        inorder = {}
        # Initialize all the node with 0 inorder
        for i in self.node:
            inorder[i] = 0

        # Assign inorder to all edges
        for node in self.graph:
            for nbr in self.graph[node]:
                inorder[nbr] += 1

        # Push the element in queue with 0 inorder
        queue = []
        for key in inorder:
            if inorder[key] == 0:
                queue.append(key)

        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for nbr in self.graph[node]:
                inorder[nbr] -= 1
                #  if inorder of that vertex is become 0 that means it has no dependencies
                if inorder[nbr] == 0:
                    queue.append(nbr)



    def printGraph(self):
        for node in self.graph:
            print(f"{node} --> ",end=' ')
            for nbr in self.graph[node]:
                print(nbr,end=' ')
            print()


g = Graph()

g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(4,5)

g.topologicalSort()