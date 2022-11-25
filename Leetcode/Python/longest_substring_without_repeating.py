class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        win = set()
        ans = 0
        while r < len(s):
            while s[r] in win and l < r:
                win.remove(s[l])
                l += 1
            win.add(s[r])
            ans = max(ans, len(win))
            r += 1
        return ans