"""
We will call a sequence of integers a spike if they first increase (strictly) and then
decrease (also strictly, including the last element of the increasing part). For example
(4,5,7, 6, 3, 2) is a spike, but (1, 1, 5, 4, 3) and (1, 4, 3, 5) are not.
Your are given an array A of N integers. Your task is to calculate the length of the
longest possible spike. Note that you
NOT supposed to find the longest spike as a sub-sequence of A, but rather choose
some numbers from A and reorder them to create the longest spike.
Examples:
1. Given A = [1, 2], your function should return 2, because (1, 2) is already a spike.
2. Given A = [2, 5, 3, 2, 4, 1], your function should return 6, because we can create the
following spike of length 6: (2, 4, 5, 3, 2, 1).
3. Given A = [2, 3, 3, 2, 2, 2, 1], your function should return 4, because we can create the
following spike of length 4: (2, 3, 2, 1) and we cannot create any longer spike. Note that
increasing and decreasing parts should be strictly increasing/decreasing and they
always intersect.
assumptions:
N, A[i] are integers
1 <= N <= 100,000;
1 <= A[i] <= 1,000,000."""
def solution(A):
    A.sort()
    inc, dec = [1] * len(A), [1] * len(A)
    for i in range(1, len(A)):
        dec[i] = dec[i - 1] + 1 if A[i] != A[i - 1] else dec[i - 1]
        inc[len(A) - i - 1] = inc[len(A) - i] + 1 if A[len(A) - i - 1] != A[len(A) - i] else inc[len(A) - i]
    ans = 1
    for i in range(1, len(A)):
        ans = max(dec[i - 1] + inc[i], ans)
    return ans

A1, A2, A3 = [2, 5, 3, 2, 4, 1], [2, 3, 3, 2, 2, 2, 1], [1, 2]
print("solution of A1: %d" % solution(A1))
print("solution of A2: %d" % solution(A2))
print("solution of A3: %d" % solution(A3))