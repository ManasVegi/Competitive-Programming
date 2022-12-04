class Solution:
    List = list
    def maxProduct(self, nums: List[int]) -> int:
        posProd, negProd = 0, 0
        ans = float('-inf')
        for n in nums:
            if posProd <= 0:
                posProd = 1
            if negProd >= 0:
                negProd = 1
            if n > 0:
                posProd *= n
                negProd *= n
            elif n < 0:
                temp = posProd
                posProd = negProd * n
                negProd = temp * n
            else:
                posProd = 0
                negProd = 0
            ans = max(ans, posProd)
        return ans