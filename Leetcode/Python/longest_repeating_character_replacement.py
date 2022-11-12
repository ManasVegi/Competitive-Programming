class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winFreq = {s[0]: 1}
        mode = 1
        l, r, ans = 0, 0, 0
        while r < len(s):
            if (r - l - mode + 1) > k:
                winFreq[s[l]] = winFreq.get(s[l]) - 1
                l += 1
            else:
                ans = max(r - l + 1, ans)
                r += 1
                if r < len(s): #edge case handling
                    winFreq[s[r]] = winFreq.get(s[r], 0) + 1
                    mode = max(winFreq[s[r]], mode)
        return ans
