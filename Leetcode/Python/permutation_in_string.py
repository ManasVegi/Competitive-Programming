class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getFreqMap(s):
            freqMap = {}
            for c in s:
                freqMap[c] = freqMap.get(c, 0) + 1
            return freqMap
        def mapsAreEqual(m1, m2):
            for c in m1:
                if c not in m2 or m2[c] != m1[c]:
                    return False
            for c in m2:
                if c not in m1 or m2[c] != m1[c]:
                    return False
            return True
        map1 = getFreqMap(s1)
        l, r = 0, len(s1) - 1
        map2 = getFreqMap(s2[0:len(s1)])
        while r < len(s2):
            if mapsAreEqual(map1, map2):
                return True
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                map2.pop(s2[l])
            if r < len(s2) - 1:
                map2[s2[r + 1]] = map2.get(s2[r + 1], 0) + 1
            l += 1
            r += 1
        return False