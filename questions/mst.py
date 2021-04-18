from collections import defaultdict

def add_edge(u,v,w,graph):
    graph.append([w, u, v])
    return graph

def find(i, parent):
    if parent[i] == -1:
        return i
    return find(parent[i], parent)

def union(a, b, parent, rank):
    if rank[a] > rank[b]:
        parent[b] = a
        rank[a] += rank[b]
    else:
        parent[a] = b
        rank[b] += rank[a]
    return parent

def build_mst(new_graph):
    parent = defaultdict(lambda: -1, {})
    rank = defaultdict(lambda: 1, {})
    cost = 0
    for item in new_graph:
        s1 = find(item[1], parent)
        s2 = find(item[2], parent)
        if s1 != s2:
            parent = union(item[1], item[2], parent, rank)
            cost += item[0]
            print(parent)
    return cost
v, e = map(int, input().split())
graph = []
for _ in range(e):
    u, v, w = map(int, input().split())
    graph = add_edge(u, v, w, graph)

sorted_graph = sorted(graph)
print(sorted_graph)
print(build_mst(sorted_graph))



