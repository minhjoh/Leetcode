class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(combination: List[int], index: int, current_sum: int):
            if len(combination) == k and current_sum == n:
                res.append(combination[:])
                return
            elif len(combination) > k or current_sum > n:
                return
            for num in range(index + 1, 10):
                dfs(combination + [num], num, current_sum + num)
            
        dfs([], 0, 0)
        return res
