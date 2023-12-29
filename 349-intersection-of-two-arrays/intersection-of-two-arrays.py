class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = [value for value in nums1 if value in nums2]
        nums = list(dict.fromkeys(nums))
        return nums
