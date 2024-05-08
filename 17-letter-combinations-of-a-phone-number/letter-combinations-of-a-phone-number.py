class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []

        def dfs(combination, i):
            if i >= len(digits):
                res.append(combination)
                return
            for char in phone[digits[i]]:
                dfs(combination+char, i+1)

        dfs("", 0)
        return res