class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr_end,curr_far = 0,0
        for i in range(len(nums)-1):
            curr_far = max(curr_far,i+nums[i])
            if i==curr_end:
                ans+=1
                curr_end = curr_far

        return ans
        
        