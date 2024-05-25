class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordset = set(wordDict)
        temp, result = [], []

        def helper(start):
            if start == n:
                result.append(" ".join(temp))
            for i in range(start, n):
                if s[start: i+1] in wordset:
                    temp.append(s[start: i+1])

                    helper(i+1)
                    temp.pop()

        helper(0)
        return result

    
                