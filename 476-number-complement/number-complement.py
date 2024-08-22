class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        thua = 0
        while num > 0:
            bit = num % 2
            if bit == 0:
                n += 2 ** thua
            num //=2
            thua += 1
        return n