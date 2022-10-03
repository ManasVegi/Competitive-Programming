class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == target else 0
        bestStart, length = -1,  float('inf')
        start, end, subsum = 0, 1, nums[0]
        while end < len(nums):
            while subsum < target and end < len(nums):
                subsum += nums[end]
                end += 1
            while subsum >= target and start <= end:
                if end - start < length:
                    bestStart, length = start, end - start
                
                subsum -= nums[start]
                start += 1
        return 0 if bestStart == -1 else length