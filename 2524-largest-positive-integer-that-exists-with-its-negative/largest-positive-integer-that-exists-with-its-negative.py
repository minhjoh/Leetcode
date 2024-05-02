class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        new_set = set(nums)
        length = len(new_set)
        for i in range(length):
            min_num = min(new_set)
            new_set.remove(min_num)
            new_set.add(-min_num)
            if len(new_set) != length:
                return -min_num
        return -1

        
        