from collections import defaultdict
import heapq
List = list
#quite slow on leetcode time but time complexity is the same as dijkstra with a pq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMat = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for u, v, w in times:
            adjMat[u][v] = w
        pq = [(0, k)]
        distances = {}
        while len(pq) > 0:
            dist, u = heapq.heappop(pq)
            distances[u] = min(distances.get(u, float('inf')), dist)
            for v in adjMat[u]:
                if (dist + adjMat[u][v]) < distances.get(v, float('inf')):
                    heapq.heappush(pq, (dist + adjMat[u][v], v))
        
        if len(distances) < n:
            return -1
        return max(distances.values())