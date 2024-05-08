class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, open, close):
            if len(string) == 2 * n:
                if open == close:
                    res.append(string)
                return
            if open < n:
                dfs(string + "(", open + 1, close)
            if open > close:
                dfs(string + ")", open, close + 1)
            
        dfs("", 0, 0)
        return res