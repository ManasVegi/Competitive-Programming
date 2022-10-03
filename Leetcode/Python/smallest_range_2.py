class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        l, h = nums[0] + k, nums[-1] - k
        ans = nums[-1] - nums[0] #worst best case is same op on all
        for i in range(0, len(nums) - 1):
            ans = min(ans, max(h, nums[i] + k) - min(l, nums[i + 1] - k))
        return ans