import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.G=  nx.Graph()
        self.G.add_edge('u','v',weight=2)
        self.G.add_edge('u', 'w', weight=5)
        self.G.add_edge('u', 'x', weight=1)
        self.G.add_edge('v', 'x', weight=2)
        self.G.add_edge('v', 'w', weight=3)
        self.G.add_edge('x', 'w', weight=3)
        self.G.add_edge('x', 'y', weight=1)
        self.G.add_edge('y', 'w', weight=1)
        self.G.add_edge('y', 'z', weight=2)
        self.G.add_edge('w', 'z', weight=5)


    def showGraph(self):
        edge_labels = nx.draw_networkx_edge_labels(self.G,pos=nx.spring_layout(self.G))
        nx.draw(self.G, pos=nx.spring_layout(self.G),node_size=300)
        plt.show()

    def shortestPath(self, source,target):
        return nx.shortest_path(self.G,source=source,target=target,weight='weight')

    def shortestPathLength(self,source,target):
        return nx.shortest_path_length(self.G, source=source, target=target, weight='weight')

    def shortestPathEqualEdge(self,source,target):
        return nx.shortest_path(self.G,source=source,target=target)


obj = Graph()
# Graph Visualization
obj.showGraph()

# Shortest Path in graph
print(obj.shortestPath('u','z'))

# Shortest path length
print(obj.shortestPathLength('u','z'))

# Shortest path when graph has equal length
print(obj.shortestPathEqualEdge('u','z'))