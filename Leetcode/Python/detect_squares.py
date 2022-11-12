from collections import defaultdict
List = list
class DetectSquares:
    def __init__(self):
        self.x_axis = defaultdict(lambda : defaultdict(lambda: 0))

    def add(self, point: List[int]) -> None:
        x_axis = self.x_axis
        x, y = point
        if x in x_axis:
            x_axis[x][y] = x_axis[x][y] + 1
        else:
            x_axis[x][y] = 1

    def count(self, point: List[int]) -> int:
        x_axis = self.x_axis
        x, y = point
        ans = 0
        if x not in x_axis:
            return 0
        for neigh_y in x_axis[x]:
            if neigh_y == y:
                continue
            a = neigh_y - y
            ans += x_axis[x][neigh_y] *  x_axis[x - a][y] * x_axis[x - a][neigh_y]
            ans += x_axis[x][neigh_y] * x_axis[x + a][y] * x_axis[x + a][neigh_y]
        return ans