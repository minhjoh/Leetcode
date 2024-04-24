class Solution:
    def tribonacci(self, n: int) -> int:
        li = [[] for _ in range(38)]
        li[0] = 0
        li[1] = 1
        li[2] = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3, 38):
            li[i] = li[i-1] + li[i-2] + li[i-3]
            if n == i:
                return li[n] 
        