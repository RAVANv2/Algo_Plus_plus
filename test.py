
import heapq

from collections import defaultdict

graph =  defaultdict(list)


def addEdge(u,v,weight):
    graph[u].append([v,weight])
    graph[v].append([u,weight])

def calculate_distance(graph,src):
    distances = {vertex:float("inf") for vertex in graph}
    distances[src] = 0
    pq = [(0,src)]

    while pq:
        curr_distance,curr_vertex = heapq.heappop(pq)
        if curr_distance > distances[curr_vertex]:
            continue
        for nbr,weight in graph[curr_vertex]:
            distance = curr_distance + weight
            if distance < distances[nbr]:

                distances[nbr] = distance
                heapq.heappush(pq,(distance,nbr))
    return distances

def printPath(graph,src,dest,distances):
    visited = defaultdict(bool)



addEdge(0, 1, 4)
addEdge(0, 7, 8)
addEdge(1, 2, 8)
addEdge(1, 7, 11)
addEdge(2, 3, 7)
addEdge(2, 8, 2)
addEdge(2, 5, 4)
addEdge(3, 4, 9)
addEdge(3, 5, 14)
addEdge(4, 5, 10)
addEdge(5, 6, 2)
addEdge(6, 7, 1)
addEdge(6, 8, 6)
addEdge(7, 8, 7)

dist = calculate_distance(graph,0)

print("Vertex  \t Dist from source" )
for vertex, distance in dist.items():
    print(f"{vertex}  \t\t\t\t {distance}")

print(dist)