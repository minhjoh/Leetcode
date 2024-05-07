class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])  # Append a copy of the current permutation
                return
            for num in nums:
                if num not in curr:  # Avoid duplicates
                    dfs(curr + [num])  # Pass a new list with the current number added

        dfs([])
        return res