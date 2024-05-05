class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        
        left, right = 0, 2
        while right < len(nums):
            if nums[left] == nums[right]:
                del(nums[right])
            else:
                left += 1
                right += 1
        return len(nums)
        

