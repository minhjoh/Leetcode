class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dps = nums[:]
        for i in range(1, len(nums)):
            self.dps[i] = self.dps[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 >= 0:
            return self.dps[right] - self.dps[left-1]
        else:
            return self.dps[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)