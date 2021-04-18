from collections import defaultdict

graph = defaultdict(list)


def add_edge(u,v):
    graph[u].append(v)
    graph[v].append(u)

def find(i, parent):
    if parent[i] == -1:
        return i
    return find(parent[i], parent)

def union(parent,a,b):
    parent[a] = b
    return parent

def contains_cycle(graph):
    parent = defaultdict(lambda:-1, {})
    for node in graph:
        for nbr in graph[node]:
            s1 = find(nbr, parent)
            s2 = find(node, parent)
            if s1 == s2:
                return True
            parent = union(parent, node, nbr)
    print(parent)
    return False

add_edge(1, 2)
add_edge(2, 3)
add_edge(3, 4)
# add_edge(4, 1)
print(contains_cycle(graph))