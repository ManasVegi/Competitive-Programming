import math
#very hard problem due to the care required for the pointers
List = list
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        winlen, start, end = 0, 0, 0
        ans = []
        while end < len(words):
            word = words[end]
            if (maxWidth - winlen - (end - start)) < len(word): #(end - start) is minimum number of spaces to be added in the line
                availableSpace = maxWidth - winlen
                line = ""
                for i in range(end - start - 1):
                    wordSpace = maxWidth - winlen if (end - start) == 1 else math.ceil(availableSpace / (end - start - i - 1))
                    line = ''.join([line, words[start + i],(" " * wordSpace)])
                    availableSpace -= wordSpace
                line = ''.join([line, words[end - 1], " " * availableSpace])
                ans.append(line)
                start = end
                winlen = len(word)
            else:
                winlen += len(word)
            end += 1
        #left justified last line
        if winlen > 0:
            availableSpace = maxWidth - winlen
            line = ""
            for i in range(start, end):
                line = ''.join([line, words[i]])
                if i < (end - 1):
                    line = ''.join([line, " "])
                    availableSpace -= 1
            line = ''.join([line, " " * availableSpace])
            ans.append(line)
        return ans