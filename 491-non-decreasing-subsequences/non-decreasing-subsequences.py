class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(arr, index):
            if len(arr) >= 2 and arr not in res:
                res.append(arr[:])  
            for i in range(index, n):
                if not arr:
                    dfs(arr + [nums[i]], i + 1)
                elif nums[i] >= arr[-1]:
                    dfs(arr + [nums[i]], i + 1)
                
        dfs([], 0)
        return res
