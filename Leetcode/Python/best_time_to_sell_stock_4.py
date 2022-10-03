class Solution:
    #with optimized memory for dp
    def maxProfit(self, k: int, nums: list[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        buying, selling = [0]*N, [0]*N
        buying[N - 1] = -nums[N - 1]
        selling[N - 1] = nums[N - 1]
        prevBuy = []
        for K in range(1, k + 1):
            for i in reversed(range(N - 1)):
                buying[i] = max(0 if K == 1 else buying[i], buying[i + 1], -nums[i] + (0 if K == 0 else selling[i + 1]))
                selling[i] = max(0 if K == 1 else selling[i], selling[i + 1], nums[i] + (0 if K == 1 else prevBuy[i + 1]))
            prevBuy = list(buying)

        return buying[0]