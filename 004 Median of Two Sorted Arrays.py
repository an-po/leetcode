class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mrg = nums1 + nums2
        mrg.sort()
        if not mrg:
            return None
        if (len(mrg) % 2 == 0):
            return ((float(mrg[len(mrg) // 2 - 1]) + float(mrg[len(mrg) // 2])) / 2)
        else:
            return (mrg[len(mrg) // 2])