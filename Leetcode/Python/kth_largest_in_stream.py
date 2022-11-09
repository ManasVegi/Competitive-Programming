import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        pq = self.pq
        if len(pq) < self.k:
            heapq.heappush(pq, val) #min heap
        else:
            if val > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, val)
        return pq[0]