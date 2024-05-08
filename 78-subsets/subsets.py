class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr,i):
            if i >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(curr, i+1)
            curr.pop()
            dfs(curr, i+1)

        dfs([],0)
        return res