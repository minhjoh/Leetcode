class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = cur_pos = 0

        while cur_pos <= max_pos and cur_pos < len(nums)-1:
            max_pos = max(max_pos, cur_pos + nums[cur_pos])
            cur_pos += 1

        if max_pos < len(nums) - 1:
            return False
        
        return True
        