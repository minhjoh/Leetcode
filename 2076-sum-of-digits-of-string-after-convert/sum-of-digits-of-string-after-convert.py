class Solution:
    def getLucky(self, s: str, k: int) -> int:
        stringNum = self.transform(s)
        while k > 0:
            charSum = 0
            for char in stringNum:
                charSum += int(char)
            stringNum = str(charSum)
            k -= 1
        return charSum
    
    def transform(self, s):
        stringNum = ""
        for char in s:
            stringNum += str(ord(char) - ord('a') + 1)
        return stringNum