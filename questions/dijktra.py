from collections import defaultdict
import heapq

def add_edge(u, v, w, graph):
    graph[u].append([w, v])
    graph[v].append([w, u])
    return graph

def dijktra(graph, src):
    distances = defaultdict(lambda: float("inf"), {})
    distances[src] = 0
    pq = [(0, src)]
    while pq:
        distance, vertex = heapq.heappop(pq)
        if distance > distances[vertex]:
            continue
        for w, nbr in graph[vertex]:
            new_distance = distance + w
            if distances[nbr] > new_distance:
                distances[nbr] = new_distance
                heapq.heappush(pq,(new_distance, nbr))
    return distances

t = int(input())

while t:
    t -= 1
    graph = defaultdict(list)
    n, m = map(int, input().split())
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph = add_edge(u, v, w, graph)
    s = int(input())
    distances = dijktra(graph, s)
    for i in range(1, n):
        if i != s:
            if distances[i] != float("inf"):
                print(distances[i], end=" ")
            else:
                print(-1, end=" ")

    print(distances[n])





