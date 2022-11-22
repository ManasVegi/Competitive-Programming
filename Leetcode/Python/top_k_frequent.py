import heapq
List = list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        pq = []
        for n in freqMap:
            freq = freqMap[n]
            heapq.heappush(pq, (freq, n))
            if len(pq) > k:
                heapq.heappop(pq)
        return list(map(lambda t: t[1], pq))