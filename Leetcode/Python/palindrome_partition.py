List = list
#this solution uses top down dp
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = set()
        for i in range(len(s)):
            start, end = i, i
            while (start >= 0 and end < len(s) and s[start] == s[end]):
                palindromes.add((start, end))
                start -= 1
                end += 1
            start, end = i, i + 1
            while (start >= 0 and end < len(s) and s[start] == s[end]):
                palindromes.add((start, end))
                start -= 1
                end += 1
        history = {}
        def part(l, r):
            if l > r:
                return None
            if (l, r) in history:
                return history[(l, r)]
            if l == r:
                history[(l, r)] = [[s[l]]]
                return [[s[l]]]
            res = []
            if (l, r) in palindromes:
                res.append([s[l:r + 1]])
            for size in range(1, r - l + 2):
                if (l, l + size - 1) in palindromes:
                    p1 = [s[l:l + size]]
                    p2 = part(l + size, r)
                    if p2:
                        for p in p2:
                            res.append(p1 + p)
            history[(l, r)] = res
            return res
        return part(0, len(s) - 1)