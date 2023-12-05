class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 2

        if n == 1:
            return first

        while (n > 2):
            first, second = second, first + second
            n -= 1
        
        return second 