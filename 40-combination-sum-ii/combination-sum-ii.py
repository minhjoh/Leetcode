class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                res.append(path)
                return
            elif target < 0:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()
        res = []
        n = len(candidates)
        backtrack(0, [], target)
        return res
