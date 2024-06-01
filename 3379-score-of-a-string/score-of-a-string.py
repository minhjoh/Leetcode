class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            sum += abs(int(ord(s[i])) - int(ord(s[i+1])))
        return sum
