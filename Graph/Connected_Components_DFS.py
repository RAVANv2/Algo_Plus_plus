from collections import defaultdict

def add_edge(graph, u,v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, visited, src):
    visited[src] = True
    print(src, end=' ')
    for nbr in graph[src]:
        if not visited[nbr]:
            dfs(graph, visited, nbr)

def find_components(graph):
    visited = [False for _ in range(len(graph))]
    cnt = 1
    for node in graph:
        if not visited[node]:
            print(f"Component {cnt} --> ", end=' ')
            dfs(graph, visited, node)
            cnt+=1
            print()

graph = defaultdict(list)
add_edge(graph, 0, 1)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 0, 3)
add_edge(graph, 0, 4)
add_edge(graph, 5, 6)
add_edge(graph, 6, 7)
add_edge(graph, 8, 8)

# Find The component of graph
find_components(graph)
