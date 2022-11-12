class Solution:
    def minWindow(self, s: str, t: str) -> str:
        winFreq, tFreq = {}, {}
        def addChar(c, freq):
            freq[c] = freq.get(c, 0) + 1
        def removeChar(c, freq):
            if freq[c] == 1:
                freq.pop(c)
            else:
                freq[c] -= 1
        #not commutative equals, tFreq has to be freq2
        def freqsEqual(freq1, freq2):
            for k in freq2:
                if k not in freq1 or freq2[k] > freq1[k]:
                    return False
            return True
        for tc in t:
            addChar(tc, tFreq)
        bestLen, bestL, bestR = float('inf'), -1, -1
        l, r = 0, 0
        while r <= len(s):
            if freqsEqual(winFreq, tFreq):
                if (r - l) < bestLen:
                    bestLen = r - l
                    bestL = l
                    bestR = r
                removeChar(s[l], winFreq)
                l += 1
            else:
                if r < len(s):
                    addChar(s[r], winFreq)
                r += 1

        return "" if bestLen == float('inf') else s[bestL:bestR]