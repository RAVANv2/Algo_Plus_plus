"""
1. Sort the edges wrt to weights
2. Iterate over every edges and make a edge in MST if cycle is not present
   and add the weight in the cost
"""
from collections import defaultdict
graph = []

def add_edge(u, v, w):
    graph.append([w,u,v])

add_edge(0,1,10)
add_edge(1,2,15)
add_edge(0,2,5)
add_edge(3,1,2)
add_edge(3,2,40)


def find(i, parent):
    if parent[i] == -1:
        return i
    parent[i] = find(parent[i], parent)
    return parent[i]

def union(a, b, parent, rank):
    if rank[a] < rank[b]:
        parent[a] = b
        rank[b] += rank[a]
    else:
        parent[b] = a
        rank[a] += rank[b]
    return parent

def create_MST(graph):
    parent = defaultdict(lambda: -1, {})
    rank = defaultdict(lambda: 1, {})
    cost = 0
    for node in graph:
        s1 = find(node[1], parent)
        s2 = find(node[2], parent)
        if s1 != s2:
            parent = union(node[1], node[2], parent, rank)
            cost += node[0]
    print(parent)
    return cost

sorted_graph = sorted(graph)
print(create_MST(sorted_graph))