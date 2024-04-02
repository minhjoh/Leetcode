class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for x in nums:
            if x < 0:
                count += 1
        i = 0
        if count >= k: #number of -ve numbers is more than k
            for i in range(k):
                nums[i] = -nums[i]
            return(sum(nums))
        else :
            for i in range(count):
                nums[i] = -nums[i]
            k = (k - count) % 2
            nums.sort()
            if k == 1:
                nums[0] = -nums[0]
            return(sum(nums))
        