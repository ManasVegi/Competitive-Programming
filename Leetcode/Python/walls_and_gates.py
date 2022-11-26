from collections import deque
List = list

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if len(grid)
        INF = 2147483647
        q = deque()
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        dist = 0
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in deltas:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newC < 0 or newR >= len(grid) or newC >= len(grid[0]):
                        continue
                    if grid[newR][newC] == INF:
                        grid[newR][newC] = -1
                        q.append((newR, newC))
            dist += 1