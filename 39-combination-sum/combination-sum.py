class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(li, i):
            if sum(li) == target:
                res.append(li)
                return
            elif sum(li) > target:
                return 
            for i in range(i, n):
                backtrack(li + [candidates[i]], i)
            
        res = []
        n = len(candidates)
        backtrack([], 0)
        return res