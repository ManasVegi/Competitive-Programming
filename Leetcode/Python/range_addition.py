class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        arr = [0] * length
        for update in updates:
            start, end, inc = update
            arr[start] += inc
            if end < length - 1:
                arr[end + 1] -= inc
        cumsum = 0
        for i in range(length):
            cumsum += arr[i]
            arr[i] = cumsum
        return arr