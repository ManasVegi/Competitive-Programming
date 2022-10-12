List = list
#dfs solutin with O(mn) extra space
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(r, c, isHori):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '.':
                return
            board[r][c] = '.'
            if isHori:
                dfs(r, c + 1, isHori)
            else:
                dfs(r + 1, c, isHori)
        battleships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    dfs(i, j, True)
                    board[i][j] = 'X'
                    dfs(i, j, False)
                    battleships += 1
        return battleships

    #O(1) extra space
    def countBattleshipsBetter(self, board: List[List[str]]) -> int:
        battleships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    isOld = (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')
                    if not isOld:
                        battleships += 1
        return battleships