List = list
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 2:
            return (len(height) - 1) * min(height[0], height[-1])
        left, right, ans = 0, len(height) - 1, 0
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1     
        return ans