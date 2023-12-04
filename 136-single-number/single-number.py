class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqNum = 0
        for num in nums:
            uniqNum ^= num
        return uniqNum; 