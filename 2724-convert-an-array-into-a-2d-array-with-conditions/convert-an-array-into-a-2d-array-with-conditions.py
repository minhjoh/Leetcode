class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = 0
        TwoDArr = []
        while count <= len(nums) - 1:
            li = []
            for i in range(len(nums)):
                if nums[i] in li or nums[i] == 0:
                    continue
                else:
                    li.append(nums[i])
                    nums[i] = 0
                    count += 1
            TwoDArr.append(li)
        return TwoDArr