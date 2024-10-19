class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n-1):
            inv=""
            for i in s:
                if i=="1":
                    inv+="0"
                else:
                    inv+="1"
            s+="1"
            s+=inv[::-1]
        return s[k-1]