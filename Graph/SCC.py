from collections import defaultdict

graph = defaultdict(list)


def add_edge(graph,u,v):
    graph[u].append(v)

def dfs(graph,visited,src):
    print(src,end=' ')
    visited[src] = True
    for nbr in graph[src]:
        if not visited[nbr]:
            dfs(graph,visited,nbr)

def dfsToAppend(graph,src,visited,stack):
    visited[src] = True
    for nbr in graph[src]:
        if not visited[nbr]:
            dfsToAppend(graph,nbr,visited,stack)
    stack.append(src)

def reverseGraph(graph):
    g = defaultdict(list)
    for node in graph:
        for nbr in graph[node]:
            add_edge(g,nbr,node)
    return g

def printSCC(graph,src):
    visited = defaultdict(bool)
    stack = []
    dfsToAppend(graph,src,visited,stack)

    # Reverse the graph
    g = reverseGraph(graph)

    # Print SCC
    visited_scc = defaultdict(bool)
    while stack:
        node = stack.pop()
        for nbr in g[node]:
            if not visited_scc[nbr]:
                dfs(g,visited_scc,nbr)
                print("")

add_edge(graph,1,0)
add_edge(graph,0,2)
add_edge(graph,2,1)
add_edge(graph,0,3)
add_edge(graph,3,4)

printSCC(graph,1)

