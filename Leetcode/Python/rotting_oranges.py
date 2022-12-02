from collections import deque
List = list

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in deltas:
                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= len(grid) or (c + dc) >= len(grid[0]):
                        continue
                    if grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 0 #to ensure same level vertex does not add it back to queue before it is reached
                        q.append((r + dr, c + dc))
            if len(q) > 0:
                minutes += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes 