class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        def perhelper(i, nums):
            if i >= len(nums):
                return []
            if i == len(nums) - 1:
                return [[nums[i]]]
            A = perhelper(i + 1, nums)
            res = []
            for ordering in A:
                for j in range(len(ordering)):
                    res.append(ordering[0:j] + [nums[i]] + ordering[j:])
                res.append(ordering + [nums[i]])
            return res
        return perhelper(0, nums)