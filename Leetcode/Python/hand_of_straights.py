List = list
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hFreq = {}
        for h in hand:
            hFreq[h] = hFreq.get(h, 0) + 1
        cards = sorted(hFreq.keys())
        for c in cards:
            while hFreq[c] > 0:
                for g in range(1, groupSize):
                    if (c + g) not in hFreq or hFreq[c + g] == 0:
                        return False
                    hFreq[c + g] -= 1
                hFreq[c] -= 1
        for c in cards:
            if hFreq[c] > 0:
                return False
        return True
                    