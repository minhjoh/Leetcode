class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = self.merge(nums1, nums2)
        l = len(arr)
        if l % 2 == 0:
            return float((arr[l//2] + arr[l//2 - 1])) / 2
        else:
            return float(arr[l // 2])

    def merge(self, nums1, nums2):
        arr = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

        while j < len(nums2):
            arr.append(nums2[j])
            j += 1
        return arr