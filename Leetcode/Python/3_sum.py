List = list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target2sum = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target2sum:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif twoSum < target2sum:
                    l += 1
                else:
                    r -= 1
        return ans