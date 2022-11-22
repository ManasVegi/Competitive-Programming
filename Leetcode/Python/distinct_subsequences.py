def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [[0] * (len(t) + 1) for i in range((len(s) + 1))]
        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, min(i + 1, len(t) + 1)):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] += dp[i - 1][j]
        return dp[len(s)][len(t)]

class Solution:
    #O(n) memory when n is size of t
    def numDistinctBetterMemory(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        prev = [0 for _ in range(N + 1)]
        prev[N] = 1
        for i in range(M - 1, -1, -1):
            dp = [0 for _ in range(N + 1)]
            dp[N] = 1
            for j in range(N - 1, -1, -1):
                dp[j] += prev[j] #dont pick
                if s[i] == t[j]:
                    dp[j] += prev[j + 1]
            prev = dp
        return prev[0]