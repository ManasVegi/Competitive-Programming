List = list
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m1 = len(nums1) // 2
        m1 = m1 - 1 if len(nums1) % 2 == 0 else m1
        m2 = (len(nums1) + len(nums2)) // 2 - m1 - 2
        while True:
            curr1 = nums1[m1] if m1 >= 0 else float('-inf')
            curr2 = nums2[m2] if m2 >= 0 else float('-inf')
            next1 = nums1[m1 + 1] if m1 < len(nums1) - 1 else float('inf')
            next2 = nums2[m2 + 1] if m2 < len(nums2) - 1 else float('inf')
            if curr1 > next2:
                m1 -= 1
                m2 += 1
            elif curr2 > next1:
                m2 -= 1
                m1 += 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(curr1, curr2) + min(next1, next2)) / 2
                else:
                    return min(next1, next2)