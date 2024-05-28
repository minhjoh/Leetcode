class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        end = 0
        curCost = 0
        maxLength = 0

        while end < n:
            curCost += abs(ord(s[end]) - ord(t[end]))
            end += 1

            while curCost > maxCost:
                curCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            maxLength = max(maxLength, end - start)

        return maxLength