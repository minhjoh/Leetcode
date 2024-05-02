class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max = -1
        for num in nums:
            if -num in nums and max < num:
                max = num
        return max
        
        