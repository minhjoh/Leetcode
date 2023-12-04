class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        else:
            uniqNum = 0
            for num in nums:
                uniqNum ^= num
        return uniqNum; 