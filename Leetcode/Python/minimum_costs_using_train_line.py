class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        N = len(regular)
        if N == 1:
            return [min(regular[0], expressCost + express[0])]
        rCost, eCost, cost = 0, float('inf'), [0] * N
        for i in range(1, N + 1):
            eCost = express[i - 1] + min(eCost, rCost + expressCost) #needs to be done before modifying rCost
            rCost = regular[i - 1] + (0 if i == 1 else cost[i - 2])
            cost[i - 1] = min(rCost, eCost)
        return cost