class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_num = 0
        num = max(nums)
        for i in range(k):
            sum_num += num
            num += 1
        return sum_num