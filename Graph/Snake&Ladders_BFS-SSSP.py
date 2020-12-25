from collections import defaultdict

def shortestPath(graph, src, dest):
    dist = [float('inf') for _ in range(len(graph))]
    queue = []
    parent = [0]*(len(graph))

    dist[src] = 0
    queue.append(src)
    parent[src] = src

    while queue:
        node = queue.pop(0)
        for nbr in graph[node]:
            if dist[nbr] == float('inf'):
                dist[nbr] = dist[node] + 1
                queue.append(nbr)
                parent[nbr] = node

    # Printing the shortest path from src to dest
    print(parent)
    temp = dest
    while temp!=src:
        print(f"{temp} <-- ", end=' ')
        temp = parent[temp]
    print(src)
    return dist[dest]


def add_edge(graph, u, v):
    graph[u].append(v)

def add_to_board(graph, board):
    for i in range(37):
        for dice in range(1,7):
            j = i + dice
            j += board[j]

            if j <= 36:
                add_edge(graph, i, j)

    add_edge(graph,36,36)
    return graph

# Board
board = [0 for _ in range(50)]

# Snake and Ladders
board[2] = 13
board[5] = 2
board[9] = 18
board[18] = 11
board[17] = -13
board[20] = -14
board[24] = -8
board[25] = 10
board[32] = -2
board[34] = -22

# Adding Edges to the graph
graph = defaultdict(list)

graph = add_to_board(graph,board)

print(shortestPath(graph, 0, 36))