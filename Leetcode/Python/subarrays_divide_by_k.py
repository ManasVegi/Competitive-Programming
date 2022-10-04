from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] % k == 0 else 0
        remainderMap = defaultdict(lambda: 0) 
        remainderMap[0] = 1     #need to initialize for the first direct match
        count, cumSum = 0, 0
        for i in range(0, len(nums)):
            cumSum += nums[i]
            rem = cumSum % k
            count += remainderMap[rem]
            remainderMap[rem] += 1
        return count