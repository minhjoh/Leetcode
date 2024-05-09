class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(arr, index):
            if len(arr) == k:
                res.append(arr)
                return
            for num in range(index+1, n+1):
                dfs(arr + [num], num)
        
        dfs([], 0)
        return res