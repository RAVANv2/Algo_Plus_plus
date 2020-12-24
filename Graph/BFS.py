
from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, src):
    queue = []
    queue.append(src)

    visited = [False for _ in range(len(graph.keys()))]
    visited[src] = True

    while queue:
        node = queue.pop(0)
        print(node,end=' ')
        for nbr in graph[node]:
            if not visited[nbr]:
                visited[nbr] = True
                queue.append(nbr)



add_edge(graph,0,1)
add_edge(graph,0,2)
add_edge(graph,1,2)
add_edge(graph,2,3)

bfs(graph,0)

