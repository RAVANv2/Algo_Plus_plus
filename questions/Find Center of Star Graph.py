import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def aint(): return int(input())


def amap(): return map(int, input().strip().split())


def alist(): return list(map(int, input().strip().split()))


def astr(): return input().strip()


from collections import defaultdict

def make_list(pair, graph):
    graph[pair[0]].append(pair[1])
    graph[pair[1]].append(pair[0])

def findCenter(edges):
    graph = defaultdict(list)
    for i in edges:
        make_list(i, graph)
    for key in graph:
        if len(graph[key]) == len(edges):
            return key

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))
