from collections import defaultdict

class Solution:
    #with a frequency map for each string and that map as a key for a dict
    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:
        def getFreqMap(string):
            fmap = [0] * 26
            for c in string:
                fmap[ord(c) - ord('a')] += 1
            return tuple(fmap)
        anagrams = defaultdict(list)
        for string in strs:
            fmap = getFreqMap(string)
            anagrams[fmap].append(string)
        ans = []
        for fmap in anagrams:
            ans.append(anagrams[fmap])
        return ans

    #much faster solution (98%) with the sorted string as the key, as anagrams would have the same sorted output
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            anagrams[tuple(sorted(string))].append(string)
        ans = []
        for fmap in anagrams:
            ans.append(anagrams[fmap])
        return ans
