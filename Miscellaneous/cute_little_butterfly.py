# from collections import defaultdict


# t = int(input()) # read a line with a single integer
# for i in range(1, t + 1):
#     n, e = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
#     energy = {}
#     top, left, bottom, right = float('-inf'), float('inf'), float('inf'), -1
#     for _ in range(n):
#         x, y, c = [int(s) for s in input().split(" ")]
#         top = max(y, top)
#         bottom = min(y, bottom)
#         right, left = max(x, right), min(x, left)
#         energy[(x, y)] = c
#     rows, cols = bottom - top + 1, right - left + 1
#     dpr = defaultdict(lambda: float('-inf'))
#     dpl = defaultdict(lambda: float('-inf'))
#     for c in range(cols):
#         y = bottom + cols
#         for r in range(rows):
#             xr, xl = right - r, left + r
#             cr, cl = energy.get((xr, y), 0), energy.get((xl, y), 0)
#             resr1, resr2 = dpr[(xr, y - 1)], dpr[(xr + 1, y)]
#             resl1, resl2 = dpl[(xl, y - 1)], dpl[(xl - 1, y)]
#             # resr3, resl3 = dpl[(xr, y)] - e, dpr[(xl, y)] - e #change direction
#             dpr[(xr, y)] = max(resr1, resr2) + cr
#             dpl[(xl, y)] = max(resl1, resl2) + cl
#     dp = defaultdict(lambda: float('-inf'))

#     for c in range(cols):
#         y = bottom + cols
#         for r in range(rows):
#             xr, xl = right - r, left + r
#             maxright = max(dpr[(xr, y)], dpl[xr, y] - e)
#             maxleft = max(dpl[(xl, y)], dpr[(xr, y)] - e)
#             dp[()]

#     print("Case #{}: {} {}".format(i, n + m, n * m))



#UNFINISHED ATTEMPT
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, e = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    energy = {}
    top, left, bottom, right = float('-inf'), float('inf'), float('inf'), -1
    for _ in range(n):
        x, y, c = [int(s) for s in input().split(" ")]
        top = max(y, top)
        bottom = min(y, bottom)
        right, left = max(x, right), min(x, left)
        energy[(x, y)] = c
    rows, cols = bottom - top + 1, right - left + 1
    mem = {}
    def dp(x, y, dir):
        if x < 0 or y < 0 or x > right or y < bottom or x < left or y > top:
            return float('-inf')
        if (x, y, dir) in mem:
            return mem[(x, y, dir)]
        mem[(x, y, dir)] = float('-inf')
        res1 = dp(x, y - 1, dir)
        res2 = float('-inf')
        if dir: #right
            res2 = dp(x + 1, y, dir)
        else:
            res2 = dp(x - 1, y, dir)
        res3 = dp(x, y, not dir) - e
        res = max(max(res1, res2) + energy.get((x, y), 0), res3, energy.get((x, y), 0))
        mem[(x, y, dir)] = res
        return res
    ans = dp(left, top, True)
    print(mem)
    print("Case #{}: {}".format(i, ans))