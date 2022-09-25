from collections import deque
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
            """
            Do not return anything, modify rooms in-place instead.
            """
            q = deque()
            for i in range(len(rooms)):
                for j in range(len(rooms[0])):
                    if rooms[i][j] == 0:
                        q.append((i, j))
            dist = 1
            while len(q) > 0:
                n = len(q)
                for i in range(n):
                    r, c = q.popleft()
                    if r > 0 and rooms[r - 1][c] == 2147483647:
                        rooms[r - 1][c] = dist
                        q.append((r-1, c))
                    if c > 0 and rooms[r][c - 1] == 2147483647:
                        rooms[r][c - 1] = dist
                        q.append((r, c - 1))
                    if r < len(rooms) - 1 and rooms[r + 1][c] == 2147483647:
                        rooms[r + 1][c] = dist
                        q.append((r + 1, c))
                    if c < len(rooms[0]) - 1 and rooms[r][c + 1] == 2147483647:
                        rooms[r][c + 1] = dist
                        q.append((r, c + 1))
                dist += 1
