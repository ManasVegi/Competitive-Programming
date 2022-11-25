List = list
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestSum = float('inf')
        for i in range(len(nums)):
            target2sum = target - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if abs(target - bestSum) > abs(target2sum - currSum):
                    bestSum = currSum + nums[i]
                if currSum == target2sum:
                    return target
                if currSum < target2sum:
                    l += 1
                else:
                    r -= 1
        return bestSum