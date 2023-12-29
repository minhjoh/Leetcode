class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums) - 1):
            if i == 1 and nums[i - 1] != nums[i]:
                return nums[0]
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
        return nums[len(nums) - 1]