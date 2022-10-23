#too many edge cases to handle
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if len(p) == 1:
            if p == '*':
                return True
            if len(s) == 1 and (p == '.' or p == s):
                return True
            return False
            
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        end = len(p)
        #need to set the answer as true for any trailing *
        while end >= 0 and p[end - 1] == '*':
            dp[len(s)][end - 2] = True
            end = end - 2
        
        limit = len(p) - 1 if p[-1] == "*" else len(p)
        for i in range(len(s) - 1, -1, -1):
            for j in range(limit - 1, -1, -1):
                res = False
                if j < len(p) - 1 and p[j + 1] == "*":
                    if p[j] == '.' or p[j] == s[i]:
                        res = res or dp[i + 1][j + 2]
                        res = res or dp[i + 1][j]
                    res = res or dp[i][j + 2]
                elif p[j] == '.' or p[j] == s[i]:
                    res = dp[i + 1][j + 1]
                dp[i][j] = res
        return dp[0][0]