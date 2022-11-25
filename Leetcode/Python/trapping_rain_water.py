List = list
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        maxLeft[0], maxRight[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            maxLeft[i] = max(height[i], maxLeft[i - 1])
            maxRight[-i - 1] = max(height[-i - 1], maxRight[-i])
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return ans