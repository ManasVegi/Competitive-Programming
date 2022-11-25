List = list
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        dp = [[0] * K for _ in range(N - 1)]
        dp.append([costs[N - 1][j] for j in range(K)])
        for i in range(N - 2, -1, -1):
            #if c1 is chosen color for current house
            for c1 in range(K):
                best = float('inf')
                #for possible colors c2 of the house on the right
                for c2 in range(K):
                    if c2 == c1: #cannot paint same colors
                        continue
                    best = min(best, costs[i][c1] + dp[i + 1][c2])
                dp[i][c1] = best
        return min(dp[0])

    #O(nk) solution with O(1) extra space
    def minCostIIOptimal(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        min1, min2 = float('inf'), float('inf')
        idx1 = -1
        for i, c in enumerate(costs[N - 1]):
            if c < min1:
                min2 = min1
                min1 = c
                idx1 = i
            elif c < min2:
                min2 = c
        for i in range(N - 2, -1, -1):
            newmin1, newmin2 = float('inf'), float('inf')
            newidx1 = -1
            for c1 in range(K):
                curr = costs[i][c1]
                if c1 == idx1:
                    curr += min2
                else:
                    curr += min1
                if curr < newmin1:
                    newmin2 = newmin1
                    newmin1 = curr
                    newidx1 = c1
                elif curr < newmin2:
                    newmin2 = curr
            min1, min2, idx1 = newmin1, newmin2, newidx1
        return min1