t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    A = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    ans = 0
    ai = 0
    while ai < len(A):
        # a = A[ai]
        if A[ai] < 0:
            ai += 1
            continue
        cumsum = 0
        firstpos = len(A)
        for j in range(ai, len(A)):
            cumsum += A[j]
            if (cumsum >= 0):
                ans += cumsum
                if A[j] >= 0 and j < firstpos and j > ai: #set the starting point of next subarray
                    firstpos = j
            else:
                if firstpos < len(A):
                    ai = firstpos - 1
                break
        ai += 1
    print("Case #{}: {}".format(i, ans))