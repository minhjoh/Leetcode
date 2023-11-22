class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        rev_num = 0
        if num < 0:
            num = - num
        while num > 0:
            rev_num = rev_num * 10 + num % 10
            num = num // 10
        if x < 0:
            rev_num = -rev_num 
        if rev_num > 2 ** 31 - 1 or rev_num < -2 ** 31:
            return 0
        else:
            return rev_num
