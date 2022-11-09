List = list
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        check = {}
        MOD = 10**9 + 7
        for i, n in enumerate(arr):
            check[n] = i
        dp = [1 for _ in range(len(arr))]
        for i in range(1, len(arr)):
            root = arr[i]
            for j in range(i):
                factor = arr[j]
                if root % factor == 0:
                    if (root / factor) in check:
                        dp[i] += (dp[j] * dp[check[root / factor]]) % MOD
        return sum(dp) % MOD