from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)

def add_edge(u,v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(src, visited, size, cnt):
    size[cnt] += 1
    visited[src] = True
    for node in graph[src]:
        if not visited[node]:
            dfs(node, visited, size, cnt)

def formula(cnt, size, n):
    total = n * (n-1) // 2
    same = 0
    for key, item in size.items():
        same += item * (item - 1) // 2

    return total - same

def count_area(n):
    visited = defaultdict(lambda: False, {})
    cnt = 0
    size = defaultdict(lambda: 0, {})
    for i in range(n):
        for nbr in graph[i]:
            if not visited[nbr]:
                cnt += 1
                dfs(nbr, visited, size, cnt)
    return formula(cnt, size, n)


for _ in range(m):
    u, v = map(int, input().split())
    add_edge(u,v)

print(count_area(n))
