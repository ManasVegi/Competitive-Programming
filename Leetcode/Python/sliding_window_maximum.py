from collections import deque
List = list
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        dq = deque()
        for i in range(k):
            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        ans = [nums[dq[0]]]
        for i in range(k, len(nums)):
            while len(dq) > 0 and dq[0] <= (i - k):
                dq.popleft()
            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans