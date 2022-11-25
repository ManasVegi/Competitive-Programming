List = list
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem == '.':
                    continue
                subbox = ((i // 3) * 3) + (j // 3)
                if elem in rows[i] or elem in cols[j] or elem in subboxes[subbox]:
                    return False
                rows[i].add(elem)
                cols[j].add(elem)
                subboxes[subbox].add(elem)
        return True