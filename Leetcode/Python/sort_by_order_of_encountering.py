def sortByEncOrderN(A):
    fMap = {}
    for a in A:
        if a in fMap:
            fMap[a] += 1
        else:
            fMap[a] = 1

    ans = []
    for a in A:
        ans.extend([a] * fMap[a])
        fMap[a] = 0
    return ans
def sortByEncOrderNlogN(A):
    posMap = {}
    for i, a in enumerate(A):
        if a not in posMap:
            posMap[a] = i
    A.sort(key = lambda x:  posMap[x])
    return A
A = [1,3,1,5,1,4,4,7]
print(sortByEncOrderN(A))