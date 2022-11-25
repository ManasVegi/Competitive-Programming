List = list
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forw, back = 1, 1
        cum, revcum = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            forw, back = forw * nums[i], back * nums[-i - 1]
            cum[i] = forw
            revcum[-i - 1] = back
        for i in range(len(nums)):
            nums[i] = (1 if i == 0 else cum[i - 1]) * (1 if i == len(nums) - 1 else revcum[i + 1])
        return nums

    def productExceptSelfBetterMemory(self, nums: List[int]) -> List[int]:
        forw = 1
        cum = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            forw = forw * nums[i]
            cum[i] = forw
        back = 1
        for i in range(len(nums) - 1, -1, -1):
            cum[i] = (cum[i - 1] if i > 0 else 1) * back
            back = back * nums[i]
        return cum