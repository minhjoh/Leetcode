class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(start, combo, target):
            if target == 0:
                output.append(combo)
            
            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    dfs(i, combo + [candidates[i]], target - candidates[i])
        
        dfs(0, [], target)
        return output