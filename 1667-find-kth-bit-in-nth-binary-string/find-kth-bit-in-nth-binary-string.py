class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while n:
            s += "1" + self.invert(s)[::-1]
            n -= 1
        return s[k-1]
        
    def invert(self, num):
        s = ""
        for i in range(len(num)):
            if num[i] == "1":
                s += "0"
            else:
                s += "1"
        return s