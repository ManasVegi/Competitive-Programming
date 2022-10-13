from collections import deque
class Solution:
    def __init__(self):
        self.letters = [['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l']\
                        , ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    List = list
    #faster on leetcode but slightly more memory
    def letterCombinationsDFS(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        def perm(i):
            d = digits[i]
            if i == len(digits) - 1:
                return self.letters[int(d) - 2].copy()
            nextperm = perm(i + 1)
            ans = []
            for l in self.letters[int(d) - 2]:
                for nl in nextperm:
                    ans.append(''.join([l, nl]))
            return ans
        return perm(0)
    
    def letterCombinationsBacktrack(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        perms = deque()
        for d in self.letters[int(digits[len(digits) - 1]) - 2]:
            perms.append(d)
        for i in range(len(digits) - 2, -1, -1):
            d = digits[i]
            n = len(perms)
            
            for _ in range(n):
                word = perms.popleft()
                for l in self.letters[int(d) - 2]:
                    perms.append(''.join([l, word]))
        
        return perms