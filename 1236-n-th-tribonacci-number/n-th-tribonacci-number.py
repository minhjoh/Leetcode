class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a = 0
        b = c = 1
        for i in range(n-2):
            temp = c
            c = a+b+c
            a = b
            b = temp
        return c
            
        