t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    r_s, r_h = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    n = int(input())
    redp = []
    for _ in range(n):
        xr, yr = [int(s) for s in input().split(" ")]
        dist = (xr**2 + yr**2)**0.5
        if (dist) - (r_h + r_s) < 1e-9: #inside
            redp.append(dist)
        # redp.append((xr, yr))
    m = int(input())
    yellowp = []
    for _ in range(m):
        xr, yr = [int(s) for s in input().split(" ")]
        dist = (xr**2 + yr**2)**0.5
        if (dist) - (r_h + r_s) < 1e-9: #inside
            yellowp.append(dist)
    redp.sort()
    yellowp.sort()
    if len(redp) == 0:
        print("Case #{}: {} {}".format(i, 0, len(yellowp)))
    elif len(yellowp) == 0:
        print("Case #{}: {} {}".format(i, len(redp), 0))
    else:
        clr, cly = redp[0], yellowp[0]
        if clr < cly:
            r, score = 0, 0
            while r < len(redp) and redp[r] < cly:
                score += 1
                r += 1
            print("Case #{}: {} {}".format(i, score, 0))
        else:
            y, score = 0, 0
            while y < len(yellowp) and yellowp[y] < clr:
                score += 1
                y += 1
            print("Case #{}: {} {}".format(i, score, 0))
    