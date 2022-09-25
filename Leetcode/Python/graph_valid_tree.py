#using union find algo
#leetcode time complexity 92.74%, memory: 90.54%
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) >= n: #without this check, time: 8.8%, memory: 98%
            return False
        #trying with union find
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]] #path compression
                u = parent[u]
            return parent[u]
        def union(u, v):
            rootU, rootV = find(u), find(v)
            if rootU == rootV:
                return False
            if rank[rootU] >= rank[rootV]:
                parent[rootV] = rootU
                rank[rootU] += rank[rootV]
            else:
                parent[rootU] = rootV
                rank[rootV] += rank[rootU]
            return True
        for edge in edges:
            u, v = edge[0], edge[1]
            if not union(u, v):
                return False
        return max(rank) == n