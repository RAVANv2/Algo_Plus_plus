from collections import defaultdict

class Solution:
    def bfsOfGraph(self, V, adj):
        visit = {}
        visit = defaultdict(lambda :False, visit)
        ans = []
        visit[0] = True
        q = [0]
        while q:
            node = q.pop(0)
            ans.append(node)
            for nbr in adj[node]:
                if not visit[nbr]:
                    visit[nbr] = True
                    q.append(nbr)
        return ans