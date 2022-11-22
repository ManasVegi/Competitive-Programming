import heapq
List = list
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [] #max heap
        for point in points:
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)
        ans = []
        for dist, point in pq:
            ans.append(point)
        return ans