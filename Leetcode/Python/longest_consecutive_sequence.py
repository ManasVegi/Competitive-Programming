List = list
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fastAccess = set()
        starts = set()
        for n in nums:
            if (n + 1) in starts:
                starts.remove(n + 1)
            if (n - 1) not in fastAccess:
                starts.add(n)
            fastAccess.add(n)
        ans = 0
        for n in starts:
            length = 1
            curr = n
            while (curr + 1) in fastAccess:
                length += 1
                curr += 1
            ans = max(length, ans)
        return ans