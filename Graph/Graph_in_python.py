

from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def generate_edge(graph):
    edges = []

    for node in graph:
        for nbr in graph[node]:
            edges.append((node,nbr))

    return edges

def print_graph(graph):
    for node in graph:
        print(node, end=' -> ')
        for nbr in graph[node]:
            print(nbr, end=' ')
        print()



add_edge(graph,0,1)
add_edge(graph,0,2)
add_edge(graph,1,2)
add_edge(graph,2,3)

print("*"*40 + "  Printing All Edges  " + "*"*40)
print(generate_edge(graph))

print("*"*40 + "  Printing Graph  " + "*"*40)
print_graph(graph)