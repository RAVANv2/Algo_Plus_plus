from collections import deque
from typing import List

path = deque()
path.append(0)
graph = [[1, 2], [3], [3], []]
res = []

def dfs(cur: int, path: List[int], graph: List[List[int]],
        res: List[List[int]]):
    if cur == len(graph) - 1:
        res.append([x for x in path])
        return
    else:
        for i in graph[cur]:
            path.append(i)
            dfs(i, path, graph, res)
            path.pop()

dfs(0, path, graph, res)
print(res)
