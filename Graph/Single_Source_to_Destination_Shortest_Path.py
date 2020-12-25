from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# Generaic Function for all nodes
def shortestPath(graph, src):
    dist = [float('inf') for _ in range(len(graph))]
    queue = []

    dist[src] = 0
    queue.append(src)

    while queue:
        node = queue.pop(0)
        for nbr in graph[node]:
            if dist[nbr] == float('inf'):
                dist[nbr] = dist[node] + 1
                queue.append(nbr)

    for node in sorted(graph.keys()):
        print(f"Node {node} is at {dist[node]} distance from src")

# Shortest path function from src to dest
def short_SrcToDest(graph, src, dest):
    dist = [float('inf') for _ in range(len(graph))]
    queue = []

    dist[src] = 0
    queue.append(src)

    while queue:
        node = queue.pop(0)
        for nbr in graph[node]:
            if dist[nbr] == float('inf'):
                dist[nbr] = dist[node] + 1
                queue.append(nbr)
    return dist[dest]



add_edge(graph,0,1)
add_edge(graph,0,3)
add_edge(graph,1,2)
add_edge(graph,2,3)
add_edge(graph,3,4)
add_edge(graph,4,5)


shortestPath(graph, 0)
print("*"*40)
print(short_SrcToDest(graph, 0, 5))