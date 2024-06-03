class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index = 0
        for i in range(len(s)):
            if index >= len(t):
                return 0
            if s[i] == t[index]:
                index += 1
        return len(t[index:])