class Solution:
    List = list
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        n = len(gas)
        start, end, tank = 0, 0, 0
        while start < n:
            tank += diff[end]
            if tank >= 0 and ((end - start + 1) == n or end == start - 1):
                return start
            if tank < 0:
                if end < start:
                    return -1
                start = end + 1
                tank = 0
            end = (end + 1) % n
        return -1