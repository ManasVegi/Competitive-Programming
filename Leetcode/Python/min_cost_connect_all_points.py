import heapq
class Solution:
    List = list
    #small optimization that doesnt need to calculate every edge
    #done by delaying cost computation to later only if it is not already visied
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = [(0, 0)]
        ans = 0
        visited = set()
        while len(pq) > 0 and len(visited) < len(points):
            dist, idx = heapq.heappop(pq)
            if idx in visited:
                continue
            ans += dist
            for j in range(len(points)):
                if idx == j or j in visited:
                    continue
                heapq.heappush(pq, (abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1]), j))
            visited.add(idx)
        return ans