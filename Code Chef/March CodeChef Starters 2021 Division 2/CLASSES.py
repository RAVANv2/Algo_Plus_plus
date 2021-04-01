import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


from collections import defaultdict
import heapq

def addEdge(u,v,weight):
    graph[u].append([v,weight])
    graph[v].append([u,weight])

def minDistance(graph,src):
    distances = defaultdict(lambda :float("inf"))
    distances[src] = 0
    pq = [(0,src)]
    heapq.heapify(pq)
    while pq:
        currDis, currVer = heapq.heappop(pq)
        if currDis > distances[currVer]:
            continue

        for nbr,weight in graph[currVer]:
            dist = currDis + weight
            if dist < distances[nbr]:
                distances[nbr] = dist
                heapq.heappush(pq,(dist,nbr))
    return distances
t = int(input())

while t:
    t -= 1
    n,m,s,k = list(map(int,input().strip().split()))
    graph = defaultdict(list)
    for _ in range(m):
        u,v = list(map(int,input().split()))
        addEdge(u,v,1)
    k_arr = list(map(int,input().split()))

    distances = minDistance(graph,0)
    ans = 0
    dist = []
    for i in k_arr:
        dist.append(distances[i])
    dist = sorted(dist)
    for i in range(k):
        ans += dist[i]
    print(ans*2)
