from collections import defaultdict


def helper(a, visited, stack, src):
    visited[src] = stack[src] = True
    for nbr in a[src]:
        if stack[nbr] == True:
            return True
        elif visited[nbr] == False:
            cycle = helper(a, visited, stack, nbr)
            if cycle:
                return True
    stack[src] = False
    return False


class Solution:
    def isCyclic(self, V, adj):
        a = {}
        a = defaultdict(list)
        for i in range(V):
            for ele in adj[i]:
                a[i].append(ele)
        visited = {}
        stack = {}
        visited = defaultdict(lambda: False, visited)
        stack = defaultdict(lambda: False, visited)

        return helper(a, visited, stack, 0)
