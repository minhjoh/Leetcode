class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        li_range = []
        rangeNum = []
        for i in range(len(nums)):
            if not rangeNum:
                rangeNum.append(nums[i])
            elif nums[i] == rangeNum[-1] + 1:
                rangeNum.append(nums[i])
            else:
                li_range.append(rangeNum)
                rangeNum = [nums[i]]
            if i == len(nums) - 1:
                li_range.append(rangeNum)
        res = []
        for li in li_range:
            if len(li) == 1:
                res.append(str(li[0]))
            else:
                res.append(str(li[0]) + "->" + str(li[-1]))
        return res
 

            

