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