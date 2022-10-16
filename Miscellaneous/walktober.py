t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    m, n, p = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    scores = [[0 for _ in range(n)] for _ in range(m)]
    for j in range(m):
        scores[j] = [int(s) for s in input().split(" ")]
    jscores = scores[p - 1]
    steps = 0
    for d in range(n):
        maxsteps, maxIdx = 0, -1
        for part in range(m):
            if part != p and scores[part][d] > maxsteps:
                maxsteps = scores[part][d]
                maxIdx = part
        steps += max(0, maxsteps - jscores[d])
    print("Case #{}: {}".format(i, steps))