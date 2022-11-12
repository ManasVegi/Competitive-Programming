import heapq
List = list
def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        M, N = len(grid), len(grid[0])
        while len(pq) > 0:
            soFar, r, c = heapq.heappop(pq)
            if grid[r][c] == float('inf'):
                continue
            grid[r][c] = float('inf')
            if r == M - 1 and c == N - 1:
                return soFar
            for dr, dc in deltas:
                if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= M or (c + dc) >= N:
                    continue
                heapq.heappush(pq, (max(soFar, grid[r + dr][c + dc]), r + dr, c + dc))
        return -1