class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        length = len(nums)
        for i in range(length):
            min_num = min(nums)
            nums.remove(min_num)
            nums.add(-min_num)
            if len(nums) != length:
                return -min_num
        return -1

        
        