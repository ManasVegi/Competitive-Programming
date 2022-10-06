import heapq
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pq, qMap = [], {}
        intervals.sort(key=lambda x: x[0])
        sQueries = sorted(queries)
        i = 0
        for q in sQueries:
            while i < len(intervals) and intervals[i][0] <= q:
                if q >= intervals[i][0] and q <= intervals[i][1]:
                    heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i]))
                i += 1
            bestCost = -1
            while len(pq) > 0:
                cost, interval = pq[0]
                if q >= interval[0] and q <= interval[1]:
                    bestCost = cost
                    break
                else:
                    heapq.heappop(pq)
            qMap[q] = bestCost

        for i, q in enumerate(queries):
            queries[i] = qMap[q]
        return queries

s = Solution()
intervals = [[4,5],[5,8],[1,9],[8,10],[1,6]]
queries = [7,9,3,9,3]
print(s.minInterval(intervals=intervals, queries=queries))