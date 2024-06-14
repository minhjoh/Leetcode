class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        steps = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                steps += (nums[i - 1] - nums[i] + 1)
                nums[i] = nums[i - 1] + 1
        
        return steps
            