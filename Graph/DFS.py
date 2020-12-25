from collections import defaultdict

def add_edge(graph, u,v):
    graph[u].append(v)
    graph[v].append(u)


def dfs_healper(graph, visited, src):
    visited[src] = True
    print(src,end=" ")

    for nbr in graph[src]:
        if not visited[nbr]:
            dfs_healper(graph, visited, nbr)

def dfs(graph, src):
    visited = [False for _ in range(len(graph))]
    dfs_healper(graph, visited, src)

graph = defaultdict(list)
add_edge(graph,0,1)
add_edge(graph,0,3)
add_edge(graph,1,2)
add_edge(graph,2,3)
add_edge(graph,3,4)
add_edge(graph,4,5)
# Calling DFS
dfs(graph, 0)